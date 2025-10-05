# Test Case: Submit form without password
- **ID:** TC-Forms-00015
- **Related Spec:** `tests/e2e/test_forms.py::TestForms::tc_forms_0015_submit_form_without_password`
- **Description:** Should not be able to submit the form without password

- **Preconditions:**
- Navigate to the login page https://qa-practice.netlify.app/bugs-form

## Steps 
1. Navigate to the forms page 
2. Enter Test to First Name 
3. Enter Test to Last Name
4. Enter 2122067090 to Phone number field
5. Select the country Australia 
6. Leave password field empty
7. Leave Email text field empty 
8. Click on agree terms and conditions checkbox 
9. Click on the register button


## Expected Results
An error message should be displayed that the password field is required 