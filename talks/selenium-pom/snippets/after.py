from pages.admin import WPAdmin, Posts, NewPost

title = loremipsum.get_sentence()
content = loremipsum.get_paragraph()

wp_admin = WPAdmin(selenium)
wp_admin.left_menu.posts.click()

post_page = Posts(selenium)
post_page.add_new_btn.click()

new_post_page = NewPost(selenium)
new_post_page.title_el.input(title)
new_post_page.raw_text_btn.click()
new_post_page.content.input(content)

post_id = new_post_page.post_id

return title, content, post_id
