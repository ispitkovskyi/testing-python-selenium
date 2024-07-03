from tests.acceptance.locators.home_page import HomePageLocators
from tests.acceptance.page_model.base_page import BasePage


class HomePage(BasePage):
    @property # this means, that this method can be called WITHOUT specifying (). Example page.url instead of page.url()
    def url(self):
        return super(HomePage, self).url + '/'  # Example of accessing method from a super class

    @property
    def blog_link(self):
        return self.driver.find_element(*HomePageLocators.NAVIGATION_LINK)  # NOTE ASTERISK is needed to de-construct the table, so same as find_element(By.TAG_NAME, 'h1')

