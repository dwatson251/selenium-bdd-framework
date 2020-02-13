from selenium.webdriver.common.by import By
from framework.form_interaction.field_input import FieldInput


class Form:

    def __init__(self, context, form_selector='', profile='{}'):
        """
        Defines a "form" on the application, and provides methods for handling data within them.

        :param context:
        :param form_selector: A selector for the form itself
        :param profile: A user profile to use when filling out the form data
        """
        self.context = context
        self.form_selector = form_selector
        self.profile = profile

        self.context.navigator.wait_for_element((By.CSS_SELECTOR, form_selector))

        self.form = self.context.navigator.browser.find_element(By.CSS_SELECTOR, form_selector)

    def fill(self, data):
        """
        Automates the process of filling out the form, based on the specified profile

        :param data:
        :return:
        """

        for field, value in self.profile[data].items():
            field_selector = "[ng-reflect-name='{field}'], [name='{field}'], [formcontrolname='{field}']"\
                .format(field=field)

            field_input = FieldInput(self.context, self.form_selector + " " + field_selector)
            field_input.input(value)
        return

    def submit(self):
        """
        Finds the submit element from within the form and clicks it, in order to submit the form.

        :return:
        """
        self.context.navigator.wait_for_element((By.CSS_SELECTOR, self.form_selector + " [type='submit']"))
        submit = self.form.find_element(By.CSS_SELECTOR, "[type='submit']")
        submit.click()
        return
