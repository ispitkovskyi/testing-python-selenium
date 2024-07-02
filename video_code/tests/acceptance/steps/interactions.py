from behave import *
from selenium.webdriver.common.by import By

use_step_matcher('re')

@when('I click on the link with id "(.*)"')
def step_impl1(context, link_id): # link_id variable is extracted by the user_step_matcher from the @when expression part "(.*)"
    link = context.browser.find_element(by=By.ID, value=link_id)
    link.click()