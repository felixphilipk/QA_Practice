# Test Case: Submit form without email
- **ID:** TC-Forms-00014
- **Related Spec:** `tests/e2e/test_forms.py::TestForms::tc_forms_0014_submit_form_without_email`
- **Description:** Should not be able to submit the form without email  field

- **Preconditions:**
- Navigate to the login page https://qa-practice.netlify.app/bugs-form

## Steps 
1. Navigate to the forms page 
2. Enter Test to First Name 
3. Enter Test to Last Name
4. Enter 2122067090 to Phone number field
5. Select the country Australia 
6. Enter Testing to password field
7. Leave Email text field empty 
8. Click on agree terms and conditions checkbox 
9. Click on the register button



## Expected Results
A validation message should be thrown such as the email field is required 