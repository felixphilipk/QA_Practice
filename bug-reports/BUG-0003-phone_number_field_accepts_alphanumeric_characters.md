# Bug ID: BUG-0003

- **Title:** Last Name Text field accepts alphanumeric characters 
- **Related Test:** `tests/e2e/test_forms.py::TestForms::tc_forms_0006_test_invalid_inputs_in_the_phone_number_field`

## Description
The phone number field is accepting alphanumeric characters 


## Steps to Reproduce

1. Navigate to `https://qa-practice.netlify.app/bugs-form`.
2. Type 2720344710a to the Phone number text field

## Expected Result

Phone number field should not accept alphanumeric characters 

## Actual Result

Phone number field accepts alphanumeric characters 


