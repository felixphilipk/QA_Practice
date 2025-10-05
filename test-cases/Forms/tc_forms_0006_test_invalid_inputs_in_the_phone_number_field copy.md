# Test Case: Invalid inputs in the phone number field
- **ID:** TC-Forms-0006
- **Related Spec:** `tests/e2e/test_forms.py::TestForms::test_tc_forms_0006_test_invalid_inputs_in_the_phone_number_field`
- **Description:** The phone number field should not accept alphanumeric characters 

- **Preconditions:**
- Navigate to the login page https://qa-practice.netlify.app/bugs-form

## Steps 
1. Navigate to the forms page 
2. Enter 2720344710a into the phone number field


## Expected Results
The phone number field does not accepts alphanumeric characters
