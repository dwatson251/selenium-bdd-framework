from selenium.webdriver.common.by import By


class Mouse:

    def __init__(self, context, selector):
        self.field = context.navigator.browser.find_element(
            By.CSS_SELECTOR,
            selector
        )

    def click(self):
        self.field.click()
        return
