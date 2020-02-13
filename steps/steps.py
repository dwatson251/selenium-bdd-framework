from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@when(u'I type "{text}" in to "{field}"')
def type_in_field(context, field, text):
    field = context.browser.find_element(By.CSS_SELECTOR, f"[name='{field}']")
    field.click()
    field.send_keys(text)


@when(u'I enter incorrect credentials')
def step(context):

    try:
        WebDriverWait(context.browser, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[type='submit']"))
        )
    finally:
        submit = context.browser.find_element(By.CSS_SELECTOR, "[type='submit']")
        type_in_field(context, 'username', 'admin@paylinksolutions.co.uk')
        type_in_field(context, 'password', 'wrong_password')
        submit.click()


@then(u'the title should include "{title}"')
def step(context, brand):
    try:
        WebDriverWait(context.browser, 60).until(
            EC.title_contains(title)
        )
    finally:
        assert EC.title_contains(title)


@then(u'I see "{textToWitness}"')
def step(context, textToWitness):
    WebDriverWait(context.browser, 60).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), textToWitness)
    )
    assert EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), textToWitness)
