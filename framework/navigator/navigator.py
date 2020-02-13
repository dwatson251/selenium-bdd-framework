from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Navigator(object):
    __TIMEOUT = 30

    def __init__(self, browser):
        """
        Class performs various navigation tasks that the selenium tests may require.

        :param browser:
        """
        
        super(Navigator, self).__init__()
        self.web_driver_wait = WebDriverWait(browser, Navigator.__TIMEOUT)
        self.browser = browser
        return

    def open(self, url):
        """
        Opens the web browser at a specific page

        :param url:
        :return:
        """

        self.browser.get(url)
        return

    def wait_for_clickable(self, locator):
        """
        Given a locator tuple, waits for the element to be clickable before proceeding

        :param locator:
        :return:
        """

        return self.web_driver_wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element(self, locator):
        """
        Given a locator tuple, waits for an element to be visible before proceeding

        :param locator:
        :return:
        """

        return self.web_driver_wait.until(EC.visibility_of_element_located(locator))

    def wait_for_elements(self, locator):
        """
        Given a locator tuple, waits for all elements matching that tuple before proceeding.

        :param locator:
        :return:
        """

        return self.web_driver_wait.until(EC.presence_of_all_elements_located(locator))
