from django import forms
from django.core.exceptions import FieldError
from django.utils.functional import cached_property
from wagtail.admin.views.chooser import BrowseView
from wagtail.models import Page


class UserPermsForm(forms.Form):
    user_perms = forms.CharField(required=False)

    class Meta:
        fields = "__all__"


class FilterPageBrowseView(BrowseView):
    def get(self, request, parent_page_id=None):

        self.user_perm = None
        perms_form = UserPermsForm(request.GET)
        if perms_form.is_valid():
            self.user_perm = perms_form.cleaned_data.get(
                "user_perms", None
            )
        return super().get(request, parent_page_id=None)

    @cached_property
    def prepare_filter(self):
        if not self.user_perm:
            return None

        type_filter = {}
        filter_info = self.user_perm.split(",")[0]

        if filter_info.split(":")[0] == "filters_info":
            filter_info = filter_info.split(":")[1]

            for info in filter_info.split(";"):
                type_filter.update({
                    info.split("=")[0]: info.split("=")[1],
                })
            return type_filter

        return None

    def get_object_list(self):
        # Get children of parent page (without streamFields)
        pages = self.parent_page.get_children().defer_streamfields().specific()

        type_filter = self.prepare_filter
        model_name = pages[0].__class__

        if type_filter:
            try:
                pages = model_name.objects.filter(**type_filter)
            except FieldError:
                pages = Page.objects.none()

        if self.i18n_enabled:
            pages = pages.select_related("locale")

        return pages
