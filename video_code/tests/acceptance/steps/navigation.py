from behave import *
from selenium import webdriver

use_step_matcher('re')

@given('I am on the homepage') # - decorator
def step_impl(context):
    context.cService = webdriver.ChromeService(
        executable_path="C:/Users/ispitkovskyi/PycharmProjects/testing-python-selenium/chromedriver.exe")  # the driver is put into the directory with steps. Or you can put it in the PATH and in such case do NOT specify it here
    context.driver = webdriver.Chrome(service=context.cService)
    context.driver.get('http://127.0.0.1:5000')

@given('I am on the blog page') # - decorator
def step_impl(context):
    context.cService = webdriver.ChromeService(
        executable_path="C:/Users/ispitkovskyi/PycharmProjects/testing-python-selenium/chromedriver.exe")  # the driver is put into the directory with steps. Or you can put it in the PATH and in such case do NOT specify it here
    context.driver = webdriver.Chrome(service=context.cService)
    context.driver.get('http://127.0.0.1:5000/blog')

@then('I am on the blog page') # - decorator, it will rename method of the decorated function 'step_impl'
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/blog'
    assert context.driver.current_url == expected_url

@then('I am on the homepage') # - decorator, it will rename method of the decorated function 'step_impl'
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/'
    assert context.driver.current_url == expected_url