from selenium.webdriver.common.by import By

from tests.acceptance.locators.new_post_page import NewPostPageLocators
from tests.acceptance.page_model.base_page import BasePage


class NewPostPage(BasePage):
    @property  # this means, that this method can be called WITHOUT specifying (). Example page.url instead of page.url()
    def url(self):
        return super(NewPostPage, self).url + '/post'  # Example of accessing method from a super class

    @property
    def form(self):
        return self.driver.find_element(*NewPostPageLocators.NEW_POST_FORM)

    @property
    def submit_button(self):
        return self.driver.find_element(*NewPostPageLocators.SUBMIT_BUTTON)

    # Find children of form web element
    def form_field(self, name):
        return self.form.find_element(By.NAME, name)


