from behave import *
from selenium import webdriver

from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.home_page import HomePage

use_step_matcher('re')

@given('I am on the homepage') # - decorator
def step_impl(context):
    context.cService = webdriver.ChromeService(
        executable_path="C:/Users/ispitkovskyi/PycharmProjects/testing-python-selenium/chromedriver.exe")  # the driver is put into the directory with steps. Or you can put it in the PATH and in such case do NOT specify it here
    context.driver = webdriver.Chrome(service=context.cService)
    page = HomePage(context.driver)
    context.driver.get(page.url)

@given('I am on the blog page') # - decorator
def step_impl(context):
    context.cService = webdriver.ChromeService(
        executable_path="C:/Users/ispitkovskyi/PycharmProjects/testing-python-selenium/chromedriver.exe")  # the driver is put into the directory with steps. Or you can put it in the PATH and in such case do NOT specify it here
    context.driver = webdriver.Chrome(service=context.cService)
    page = BlogPage(context.driver)
    context.driver.get(page.url)

@then('I am on the blog page') # - decorator, it will rename method of the decorated function 'step_impl'
def step_impl(context):
    page = BlogPage(context.driver)
    assert context.driver.current_url == page.url

@then('I am on the homepage') # - decorator, it will rename method of the decorated function 'step_impl'
def step_impl(context):
    page = HomePage(context.driver)
    assert context.driver.current_url == page.url