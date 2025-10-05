# Test Case: Submit form without filling the last name 
- **ID:** TC-Forms-00013
- **Related Spec:** `tests/e2e/test_forms.py::TestForms::tc_forms_0013_submit_form_without_last_name`
- **Description:** Test should not be able to submit form without filling in the last name 

- **Preconditions:**
- Navigate to the login page https://qa-practice.netlify.app/bugs-form

## Steps 
1. Navigate to the forms page 
2. Enter Test to First Name 
3. Leave last name empty
4. Enter 2122067090 to Phone number field
5. Select the country Australia 
6. Enter Testing to password field
7. Enter test@test.com email field
8. Click on agree terms and conditions checkbox 
9. Click on the register button



## Expected Results
A validation message should be shown that last name is required