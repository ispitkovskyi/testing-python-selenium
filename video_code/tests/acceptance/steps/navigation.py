from behave import *
from selenium import webdriver

from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.home_page import HomePage
from tests.acceptance.page_model.new_post_page import NewPostPage

use_step_matcher('re')

'''
    IMPORTANT: 
    Each method, which is called as 1st in a scenario (line #1 of scenario) must create instance of a chrome driver
    Then, the created instance of the driver is automatically put into the "context" variable and re-used in other methods,
    mapped to all sub-sequent lines in different scenarios (lines #2 or next) will just use instance of driver created by methods called for line #1
'''
@given('I am on the homepage') # - @given is a decorator
def step_impl(context):
    context.cService = webdriver.ChromeService(
        executable_path="C:/Users/ispitkovskyi/PycharmProjects/testing-python-selenium/chromedriver.exe")  # the driver is put into the directory with steps. Or you can put it in the PATH and in such case do NOT specify it here
    context.driver = webdriver.Chrome(service=context.cService)  # FIRST STEP IN SCENARIO - puts driver object into the 'context' variable, which will be passed to other step-methods of this scenario
    page = HomePage(context.driver)
    context.driver.get(page.url)

@given('I am on the blog page') # @given is a - decorator
def step_impl(context):
    context.cService = webdriver.ChromeService(
        executable_path="C:/Users/ispitkovskyi/PycharmProjects/testing-python-selenium/chromedriver.exe")  # the driver is put into the directory with steps. Or you can put it in the PATH and in such case do NOT specify it here
    context.driver = webdriver.Chrome(service=context.cService)   # FIRST STEP IN SCENARIO - puts driver object into the 'context' variable, which will be passed to other step-methods of this scenario
    page = BlogPage(context.driver)
    context.driver.get(page.url)

@then('I am on the blog page') # @then - decorator, it will rename method of the decorated function 'step_impl'
def step_impl(context):
    page = BlogPage(context.driver)
    assert context.driver.current_url == page.url

@then('I am on the homepage') # - decorator, it will rename method of the decorated function 'step_impl'
def step_impl(context):
    page = HomePage(context.driver)
    assert context.driver.current_url == page.url

@given('I am on the new post page') # - decorator
def step_impl(context):
    context.cService = webdriver.ChromeService(
        executable_path="C:/Users/ispitkovskyi/PycharmProjects/testing-python-selenium/chromedriver.exe")  # the driver is put into the directory with steps. Or you can put it in the PATH and in such case do NOT specify it here
    context.driver = webdriver.Chrome(service=context.cService)   # FIRST STEP IN SCENARIO - puts driver object into the 'context' variable, which will be passed to other step-methods of this scenario
    page = NewPostPage(context.driver)
    context.driver.get(page.url)