from behave import *

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.blog_page import BlogPage

use_step_matcher('re')

@then('There is a title shown on the page')
def step_impl1(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()  # No () after .title, because the 'title' function is marked as @property in home_model

@step('The title tag has content "(.*)"')  # @step - universal decorator, it works similarly for When, Then, And, Given
def step_impl1(context, label):
    page = BasePage(context.driver)
    assert page.title.text == label

@then('I can see there is a posts section on the page')
def step_impl1(context):
    page = BlogPage(context.driver)

    assert page.posts_section.is_displayed()