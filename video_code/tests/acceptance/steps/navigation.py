from behave import *
from selenium import webdriver

use_step_matcher('re')

@given('I am on the homepage')
def step_impl(context):
    cService = webdriver.ChromeService(executable_path="C:/Users/ispitkovskyi/PycharmProjects/testing-python-selenium/chromedriver.exe")  # the driver is put into the directory with steps. Or you can put it in the PATH and in such case do NOT specify it here
    browser = webdriver.Chrome(service=cService)
    browser.get('http://127.0.0.1:5000')

# @when('I click on the link with id "blog-link"')
