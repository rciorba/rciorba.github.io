class Posts(Page):
    url = "{}/wp-admin/post.php".format(config.SITE_URL)
    add_new_btn = Element(link_text="Add New")


posts_page = Posts()
posts_page.goto()
posts_page.add_new_btn.click()
