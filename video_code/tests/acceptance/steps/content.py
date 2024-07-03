from behave import *
from selenium.webdriver.common.by import By
from selenium import webdriver

use_step_matcher('re')

@then('There is a title shown on the page')
def step_impl1(context):
    # context.cService = webdriver.ChromeService(
    #     executable_path="C:/Users/ispitkovskyi/PycharmProjects/testing-python-selenium/chromedriver.exe")
    # context.browser = webdriver.Chrome(service=context.cService)

    title_tag = context.browser.find_element(By.TAG_NAME, 'h1')
    assert title_tag.is_displayed()

@step('The title tag has content "(.*)"')  # @step - universal decorator, it works similarly for When, Then, And, Given
def step_impl1(context, label):
    # context.cService = webdriver.ChromeService(
    #     executable_path="C:/Users/ispitkovskyi/PycharmProjects/testing-python-selenium/chromedriver.exe")
    # context.browser = webdriver.Chrome(service=context.cService)
    title_tag = context.browser.find_element(By.TAG_NAME, 'h1')
    title_tag.text == label