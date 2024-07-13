from tests.acceptance.locators.blog_page import BlogPageLocators
from tests.acceptance.page_model.base_page import BasePage


class BlogPage(BasePage):
    @property # this means, that this method can be called WITHOUT specifying (). Example page.url instead of page.url()
    def url(self):
        return super(BlogPage, self).url + '/blog'  # Example of accessing method from a super class

    @property
    def home_link(self):
        return self.driver.find_element(*BlogPageLocators.HOME_LINK)  # NOTE ASTERISK is needed to de-construct the table, so same as find_element(By.TAG_NAME, 'h1')
    
    @property
    def add_post_link(self):
        return self.driver.find_element(*BlogPageLocators.ADD_POST_LINK)

    @property
    def posts_section(self):
        return self.driver.find_element(*BlogPageLocators.POST_SECTION)

    @property
    def posts(self):
        return self.driver.find_elements(*BlogPageLocators.POST)