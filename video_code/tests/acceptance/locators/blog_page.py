from selenium.webdriver.common.by import By

from tests.acceptance.locators.base_page import BasePageLocators


class BlogPageLocators(BasePageLocators):
    HOME_LINK = By.ID, 'home-link'
    ADD_POST_LINK = By.ID, 'add-post-link'
    POST_SECTION = By.ID, 'posts'
    POST = By.CLASS_NAME, 'post-link'