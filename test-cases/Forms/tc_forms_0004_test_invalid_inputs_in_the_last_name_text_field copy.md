# Test Case: Valid inputs in the Last Name text field
- **ID:** TC-Forms-0004
- **Related Spec:** `tests/e2e/test_forms.py::TestForms::test_tc_forms_0004_test_invalid_inputs_in_the_last_name_text_field`
- **Description:** The last name text field should not accept alphanumeric characters 

- **Preconditions:**
- Navigate to the login page https://qa-practice.netlify.app/bugs-form

## Steps 
1. Navigate to the forms page 
2. Enter Test123 into the last name text field


## Expected Results
The last name text field should not accept alphanumeric characters 
