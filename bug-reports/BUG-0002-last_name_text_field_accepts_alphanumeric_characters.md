# Bug ID: BUG-0002

- **Title:** Last Name Text field accepts alphanumeric characters 
- **Related Test:** `tests/e2e/test_forms.py::TestForms::tc_forms_0004_test_invalid_inputs_in_the_last_name_text_field`

## Description
The Last name text field is accepting alphanumeric characters 


## Steps to Reproduce

1. Navigate to `https://qa-practice.netlify.app/bugs-form`.
2. Type Test123 to the Last name text field

## Expected Result

Last name text field should not accept alphanumeric characters 

## Actual Result

Last name text field accepts alphanumeric characters 


