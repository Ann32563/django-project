from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Blog Project'
    site_title = 'Blog项目管理后台'
    index_title = 'Home'

custom_site = CustomSite(name='cus_admin')