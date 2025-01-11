from django.utils.functional import cached_property
from wagtail import blocks


class FilterPageChooserBlock(blocks.PageChooserBlock):
    @cached_property
    def widget(self):
        from .widgets import FilterAdminPageChooser
        custom_args = self.__dict__["_constructor_args"][1]
        filters_info = custom_args.get("filters_info", None)

        return FilterAdminPageChooser(
            target_models=self.target_model,
            can_choose_root=self.can_choose_root,
            user_perms=filters_info,
        )
