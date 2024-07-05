from behave import *
from selenium.webdriver.common.by import By

from tests.acceptance.page_model.base_page import BasePage

use_step_matcher('re')

@when('I click on the "(.*)" link')
def step_impl1(context, link_text): # link variable is extracted by the user_step_matcher from the @when expression part "(.*)"
    page = BasePage(context.driver)
    links = page.navigation
    matching_links = [l for l in links if l.text == link_text]

    if len(matching_links) > 0:
        matching_links[0].click()
    else:
        raise RuntimeError()