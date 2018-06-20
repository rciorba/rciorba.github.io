class LeftMenu(Element):
    posts = Element(link_text="Posts")


class WPAdmin(Page):
    url = "{}/wp-admin/".format(config.SITE_URL)
    left_menu = LeftMenu(id='adminmenu')


admin_page = WPAdmin()
admin_page.left_menu.posts.click()
