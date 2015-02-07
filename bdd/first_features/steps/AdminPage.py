from behave import *

@given(u'the homepage is at http://localhost:8000')
def step_impl(context):
        raise NotImplementedError(u'STEP: Given the homepage is at http://localhost:8000')

@given(u'I load the homepage')
def step_impl(context):
        raise NotImplementedError(u'STEP: Given I load the homepage')

@then(u'I should see the links "Show all articles" and "Create an article"')
def step_impl(context):
        raise NotImplementedError(u'STEP: Then I should see the links "Show all articles" and "Create an article"')

@given(u'I am on the homepage')
def step_impl(context):
        raise NotImplementedError(u'STEP: Given I am on the homepage')

@when(u'I click on Show all articles shown on the page')
def step_impl(context):
        raise NotImplementedError(u'STEP: When I click on Show all articles shown on the page')

@then(u'I should see article_show_all or content loading.')
def step_impl(context):
        raise NotImplementedError(u'STEP: Then I should see article_show_all or content loading.')

@when(u'I click on Create an article shown on the page')
def step_impl(context):
        raise NotImplementedError(u'STEP: When I click on Create an article shown on the page')

@then(u'I should see article_create_new or content loading.')
def step_impl(context):
        raise NotImplementedError(u'STEP: Then I should see article_create_new or content loading.')

