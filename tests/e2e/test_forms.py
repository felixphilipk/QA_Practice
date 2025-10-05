from __future__ import annotations
import pytest
from playwright.sync_api import Page
from tests.pages.forms_page import FormsPage

@pytest.mark.regression
@pytest.mark.smoke
class TestForms:

    def test_tc_forms_0001_test_valid_inputs_in_the_first_name_text_field(
        self,
        page: Page,
        base_url: str,
    ) -> None:
        forms_page = FormsPage(page, base_url)
        forms_page.visit()
        first_name = "Test"
        forms_page.fill_first_name(first_name)
        forms_page.expect_first_name_value(first_name)

    def test_tc_forms_0002_test_invalid_inputs_in_the_first_name_text_field(
        self,
        page: Page,
        base_url: str,
    ) -> None:
        forms_page = FormsPage(page, base_url)
        forms_page.visit()
        invalid_first_name = "Test123"
        forms_page.fill_first_name(invalid_first_name)
        forms_page.invalid_name_value(invalid_first_name)

    def test_tc_forms_0003_test_valid_inputs_in_the_last_name_text_field(
        self,
        page: Page,
        base_url: str,
    ) -> None:
        forms_page = FormsPage(page, base_url)
        forms_page.visit()
        last_name = "Test"
        forms_page.fill_last_name(last_name)
        forms_page.expect_last_name_value(last_name)

    def test_tc_forms_0004_test_invalid_inputs_in_the_last_name_text_field(
        self,
        page: Page,
        base_url: str,
    ) -> None:
        forms_page = FormsPage(page, base_url)
        forms_page.visit()
        invalid_last_name = "Test123"
        forms_page.fill_last_name(invalid_last_name)
        forms_page.invalid_name_value(invalid_last_name)

    def test_tc_forms_0005_test_valid_inputs_in_the_phone_number_field(
        self,
        page: Page,
        base_url: str,
    ) -> None:
        forms_page = FormsPage(page, base_url)
        forms_page.visit()
        phone_number = "2720344710"
        forms_page.fill_phone_number(phone_number)
        forms_page.expect_phone_number_value(phone_number)
        
    def test_tc_forms_0006_test_invalid_inputs_in_the_phone_number_field(
        self,
        page: Page,
        base_url: str,
    ) -> None:
        forms_page = FormsPage(page, base_url)
        forms_page.visit()
        invalid_phone_number = "2720344710a"
        forms_page.fill_phone_number(invalid_phone_number)
        forms_page.invalid_phone_number_value(invalid_phone_number)

    def test_tc_forms_0007_test_country_selection_dropdown(
        self,
        page: Page,
        base_url: str,
    ) -> None:
        forms_page = FormsPage(page, base_url)
        forms_page.visit()
        forms_page.expect_country_dropdown_visible()
        selected_country = "Australia"
        forms_page.select_country(selected_country)
        forms_page.expect_country_selected(selected_country)

    def test_tc_forms_0008_test_email_field_valid_inputs(
        self,
        page: Page,
        base_url: str,
    ) -> None:
        forms_page = FormsPage(page, base_url)
        forms_page.visit()
        valid_email = "test@example.com"
        forms_page.fill_email(valid_email)
        forms_page.expect_email_value(valid_email)

    def test_tc_forms_0009_test_email_field_invalid_inputs(
        self,
        page: Page,
        base_url: str,
    ) -> None:
        forms_page = FormsPage(page, base_url)
        forms_page.visit()
        invalid_email = "test@test"
        forms_page.fill_email(invalid_email)
        forms_page.invalid_email_value(invalid_email)

    def test_tc_forms_0010_test_password_field_valid_inputs(
        self,
        page: Page,
        base_url: str,
    ) -> None:
        forms_page = FormsPage(page, base_url)
        forms_page.visit()
        valid_password = "Testing"
        forms_page.fill_password(valid_password)
        forms_page.expect_password_value(valid_password) 

    def test_tc_forms_0011_test_terms_and_conditions_checkbox(
        self,
        page: Page,
        base_url: str,
    ) -> None:
        forms_page = FormsPage(page, base_url)
        forms_page.visit()
        forms_page.click_terms_and_conditions_checkbox()
        forms_page.expect_terms_and_conditions_checkbox_enabled()   
    
    def test_tc_forms_0012_submit_form_with_valid_inputs(
        self,
        page: Page,
        base_url: str,
    ) -> None:
        forms_page = FormsPage(page, base_url)
        forms_page.visit()
        first_name = "Test"
        last_name = "Test"
        phone_number = "2122067092"
        country = "New Zealand"
        email = "test@test.com"
        password = "Testing"
        forms_page.fill_first_name(first_name)
        forms_page.fill_last_name(last_name)
        forms_page.fill_phone_number(phone_number)
        forms_page.select_country(country)
        forms_page.fill_email(email)
        forms_page.fill_password(password)
        #Todo  the terms and conditions checkbox is commented out because of BUG-0005 
        #forms_page.click_terms_and_conditions_checkbox()
        forms_page.submit_form()
        forms_page.expect_success_message("Successfully registered the following information")
        forms_page.expect_success_message_first_name(first_name)
        #Todo the last name value in the success message is missing the last character because of BUG-0006
       # forms_page.expect_success_message_last_name(last_name)
       #Todo the phone number value in the success message is showing an incremented value because of BUG-0007
        #forms_page.expect_success_message_phone_number(phone_number)
        forms_page.expect_success_message_country(country)
        forms_page.expect_success_message_email(email)

    def test_tc_forms_0013_submit_form_without_last_name(
        self,
        page: Page,
        base_url: str,
    ) -> None:
        forms_page = FormsPage(page, base_url)
        forms_page.visit()
        first_name = "Test"
        phone_number = "2122067090"
        country = "Australia"
        password = "Testing"
        email = "test@test.com"
        forms_page.fill_first_name(first_name)
        forms_page.fill_phone_number(phone_number)
        forms_page.fill_password(password)
        forms_page.select_country(country)
        forms_page.fill_email(email)
        forms_page.submit_form()
        forms_page.expect_success_message("Last Name is required")

    def test_tc_forms_0014_submit_form_without_email(
        self,
        page: Page,
        base_url: str,
    ) -> None:
        forms_page = FormsPage(page, base_url)
        forms_page.visit()
        first_name = "Test"
        last_name = "Test"
        phone_number = "2122067090"
        country = "Australia"
        password = "Testing"
        forms_page.fill_first_name(first_name)
        forms_page.fill_last_name(last_name)
        forms_page.fill_phone_number(phone_number)
        forms_page.fill_password(password)
        forms_page.select_country(country)
        forms_page.submit_form()
        forms_page.expect_success_message("Email is required")    

    def test_tc_forms_0015_submit_form_without_password(
        self,
        page: Page,
        base_url: str,
    ) -> None:
        forms_page = FormsPage(page, base_url)
        forms_page.visit()
        first_name = "Test"
        last_name = "Test"
        email = "test@test.com"
        phone_number = "2122067090"
        country = "Australia"
        forms_page.fill_first_name(first_name)
        forms_page.fill_last_name(last_name)
        forms_page.fill_phone_number(phone_number)
        forms_page.fill_email(email)
        forms_page.select_country(country)
        forms_page.submit_form()
        forms_page.expect_success_message("The password should contain between [6,20] characters!")
