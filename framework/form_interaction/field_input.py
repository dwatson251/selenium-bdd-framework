"""
Defines a "field" within the application and provides methods for interacting with various types of field types.

A field is defined by a string selector.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class FieldInput:

    def __init__(self, context, field_selector=''):
        """
        Performs the task of "selecting" the field by the specified "name"

        Different field types are selected in different types, and for that reason requires
        identification of that fields type, which is also stored in this class.

        :param context:
        :param name: The name of the field
        """
        self.context = context

        context.navigator.browser.execute_script("document.querySelector('{field_selector}').scrollIntoView();"
                                                 .format(field_selector=field_selector.replace("'", "\\'")))

        self.field = context.navigator.browser.find_element(
            By.CSS_SELECTOR,
            field_selector
        )

        self.field_type = self.field.get_attribute("type")

        if self.field_type in ['radio', 'checkbox']:
            self.field_augment = self.field.find_element(
                By.XPATH,
                ".."
            )

        if self.field_type not in ['radio', 'checkbox']:
            context.navigator.wait_for_element((By.CSS_SELECTOR, field_selector))

        if self.field.tag_name in ['select']:
            self.field_type = 'select'

        return

    def set_value(self, value):
        """
        If all normal methods of setting a value fail, this method provides a way of setting a value on a field by means
        of injected JavaScript.

        :param value:
        :return:
        """

        self.context.navigator.browser.execute_script(
            "arguments[0].setAttribute(arguments[1], arguments[2]);",
            self.field,
            "value",
            value
        )

        return

    def input(self, value):
        """
        Based on the field type, performs an appropriate input method.

        :param value:
        :return:
        """
        if self.field_type in ['text', 'password', 'tel', 'number']:
            return self.input_text(value.format(timestamp=self.context.timestamp))

        if self.field_type in ['select']:
            return self.input_select(value)

        if self.field_type in ['radio', 'checkbox']:
            return self.input_check(value)

        return

    def input_text(self, text):
        """
        Focuses the field and sends keys to it based on the specified text

        :param text: Text that you want entered in the field
        :return:
        """

        self.field.click()
        self.field.send_keys(text)
        return

    def input_select(self, value):
        """
        Operates a dropdown/ select field

        :param value: Attempts to find an option in the select field matching the specified value
        :return:
        """

        select_wrapper = Select(self.field)
        select_wrapper.select_by_visible_text(value)
        return

    def input_check(self, value):
        """
        Checks an input field, either of a checkbox or radio type.

        :param value: A boolean value that defines the value you want the checkbox/ radio to be
        :return:
        """

        if self.field.is_selected() != value:
            try:
                self.field_augment.click()
            finally:
                return
        return
