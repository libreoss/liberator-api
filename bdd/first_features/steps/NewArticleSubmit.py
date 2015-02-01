from behave import given, when, then, register_type
import parse

# FIXME regex patterns aren't working as expected
# \w+ matches only one word, and \w doesn't match one word

@parse.with_pattern(r"\w+")
def parse_word(text):
    return str(text)

@parse.with_pattern(r'\w+')
def parse_string(text):
    return str(text)

register_type(some_word   = parse_word)
register_type(some_string = parse_string)

@given('that Liberator is running')
def step_impl(context):
    pass

@given('{:some_word} homepage is at http://192.168.66.6:{port:d}')
def step_impl(context, word, port):
    context.browser.get('http://192.168.66.6:8000')
    assert "Liberator" in context.browser.title

@given('no access privileges are implemented')
def step_impl(context):
    pass

@given('I load the page for new article submission')
def step_impl(context):
    print("Something!")
    pass

@then('I should see the info "Submit a new article"')
def step_impl(context):
    pass

@then('I should see expected fields')
def step_impl(context):
    for row in context.table:
        pass

@then('I should see "Article script" selection with "Cyrillic" and "Latin"')
def step_impl(context):
    pass

@then('I should see "Submit" button')
def step_impl(context):
    pass

@given('I load the page and fill in some of the fields')
def step_impl(context):
    pass

@when('I click on "Submit" button')
def step_impl(context):
    pass

@then('I should see a message "The data is to be checked and saved"')
def step_impl(context):
    pass
