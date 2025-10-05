# Test Case:Invalid inputs in the First Name text field
- **ID:** TC-Forms-0002
- **Related Spec:** `tests/e2e/test_forms.py::TestForms::test_tc_forms_0002_test_invalid_inputs_in_the_first_name_text_field`
- **Description:** The First name text field should not accept alphanumeric characters 

- **Preconditions:**
- Navigate to the login page https://qa-practice.netlify.app/bugs-form

## Steps 
1. Navigate to the forms page 
2. Enter  Test123 into the first name text field


## Expected Results
The First name text field should not accept alphanumeric characters and a error message should be displayed
