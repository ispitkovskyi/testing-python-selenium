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

@then('I can see there is a post with title "(.*)" in the posts section')
def step_impl1(context, title):
    page = BlogPage(context.driver)
    posts_with_title = [post for post in page.posts if post.text == title]

    assert len(posts_with_title) > 0

    # NOTE
    # all(...) is a built-in python function, which evaluates to true if ALL elements inside are true
    # there is similar function any(...), which evaluates to true if AT LEAST ONE element inside is true
    assert all([post.is_displayed() for post in posts_with_title])