from .base_page import BasePage

class MainPage(BasePage):

    def go_to_autocomplite(self):
        autocomplite_link = self.browser.find_element_by_css_selector('li:nth-child(5) > a')
        autocomplite_link.click()

    def go_to_buttons(self):
        buttons_link = self.browser.find_element_by_css_selector('li:nth-child(6) > a')
        buttons_link.click()

    def go_to_checkbox(self):
        checkbox_link = self.browser.find_element_by_css_selector('li:nth-child(7) > a')
        checkbox_link.click()

    def go_to_datepicker(self):
        datepicker_link = self.browser.find_element_by_css_selector('li:nth-child(8) > a')
        datepicker_link.click()

    def go_to_drag_and_drop(self):
        drag_and_drop_link = self.browser.find_element_by_css_selector('li:nth-child(9) > a')
        drag_and_drop_link.click()

    def go_to_dropdown(self):
        dropdown_link = self.browser.find_element_by_css_selector('li:nth-child(10) > a')
        dropdown_link.click()

    def go_to_enabled_and_disabled_elements(self):
        enable_and_disabled_link = self.browser.find_element_by_css_selector('li:nth-child(11) > a')
        enable_and_disabled_link.click()

    def go_to_file_upload(self):
        file_upload_link = self.browser.find_element_by_css_selector('li:nth-child(12) > a')
        file_upload_link.click()

    def go_to_key_and_mouse_press(self):
        key_and_mouse_link = self.browser.find_element_by_css_selector('li:nth-child(13) > a')
        key_and_mouse_link.click()

    def go_to_modal(self):
        modal_link = self.browser.find_element_by_css_selector('li:nth-child(14) > a')
        modal_link.click()

    def go_to_page_scroll(self):
        page_scroll_link = self.browser.find_element_by_css_selector('li:nth-child(15) > a')
        page_scroll_link.click()

    def go_to_radio_button(self):
        radio_button_link = self.browser.find_element_by_css_selector('li:nth-child(16) > a')
        radio_button_link.click()

    def go_to_switch_window(self):
        switch_window_link = self.browser.find_element_by_css_selector('li:nth-child(17) > a')
        switch_window_link.click()

    def go_to_complete_web_form(self):
        complete_web_form_link = self.browser.find_element_by_css_selector('li:nth-child(18) > a')
        complete_web_form_link.click()
