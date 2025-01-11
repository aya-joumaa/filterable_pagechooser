from wagtail.admin.widgets import AdminPageChooser


class FilterAdminPageChooser(AdminPageChooser):
    chooser_modal_url_name = "filter_wagtail_admin_choose_page"
