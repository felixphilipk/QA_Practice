# Bug ID: BUG-0004

- **Title:** Email field accepts invalid email values
- **Related Test:** `tests/e2e/test_forms.py::TestForms::tc_forms_0009_test_email_field_invalid_inputs`

## Description
Email  field accepts invalid email values 


## Steps to Reproduce

1. Navigate to `https://qa-practice.netlify.app/bugs-form`.
2. Type test@test to the Email field
## Expected Result

The email field should not accept invalid email formats 

## Actual Result

Email field accepts invalid email formats 


