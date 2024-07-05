from tests.acceptance.locators.base_page import BasePageLocators
from tests.acceptance.locators.home_page import HomePageLocators
class BasePage:

    #CONSTRUCTOR (will be executed for any instance of a child-class (like in Java)
    def __init__(self, driver):
        self.driver = driver

    @property # this means, that this method can be called WITHOUT specifying (). Example page.url instead of page.url()
    def url(self):
        return 'http://127.0.0.1:5000'

    @property  # this means, that this method can be called WITHOUT specifying (). Example page.title instead of page.title()
    def title(self):
        return self.driver.find_element(*HomePageLocators.TITLE)  # NOTE ASTERISK is needed to de-construct the table, so same as find_element(By.TAG_NAME, 'h1')

    @property
    def navigation(self):
        return self.driver.find_elements(*BasePageLocators.NAV_LINKS)