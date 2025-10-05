# Bug ID: BUG-0001

- **Title:** First Name Text field accepts alphanumeric characters 
- **Related Test:** `tests/e2e/test_forms.py::TestForms::test_tc_forms_0002_test_invalid_inputs_in_the_first_name_text_field`

## Description
The first name text field is accepting alphanumeric characters 



## Steps to Reproduce

1. Navigate to `https://qa-practice.netlify.app/bugs-form`.
2. Type Test123 to the first name text field

## Expected Result

First name text field should not accept alphanumeric characters 

## Actual Result

First name text field accepts alphanumeric characters 


