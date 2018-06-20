title = loremipsum.get_sentence()
content = loremipsum.get_paragraph()

selenium.find_element_by_xpath("//li[@id='menu-posts']/a/div[3]").click()
selenium.find_element_by_css_selector("a.page-title-action").click()
selenium.find_element_by_id("content-html").click()

selenium.find_element_by_id("title").clear()
selenium.find_element_by_id("title").send_keys(title)
selenium.find_element_by_id("content").clear()
selenium.find_element_by_id("content").send_keys(content)

post_id = selenium.find_element_by_id('post_ID').get_attribute('value')

return title, content, post_id
