from behave import fixture, use_fixture
from selenium import webdriver

@fixture
def selenium_browser_chrome(context):
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')

    # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
    context.browser = webdriver.Chrome(chrome_options=chrome_options)
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    # context.browser.quit()

def before_all(context):
    use_fixture(selenium_browser_chrome, context)
    # -- HINT: CLEANUP-FIXTURE is performed after after_all() hook is called.
