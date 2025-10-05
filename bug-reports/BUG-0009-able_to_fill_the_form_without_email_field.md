# Bug ID: BUG-0009

- **Title:** Able to fill the form without filling in the email field
- **Related Test:** `tests/e2e/test_forms.py::TestForms::tc_forms_0014_submit_form_without_email`

## Description
Able to submit the form without filling email field

## Steps to Reproduce
1. Navigate to the forms page 
2. Enter Test to First Name 
3. Leave Last Name empty
4. Enter 2122067090 to Phone number field
5. Select the country Australia 
6. Enter Testing to password field
7. Leave email field empty
7. Click on agree terms and conditions checkbox 
8. Click on the register button

## Expected Result

An error message should be displayed when submitting the form without email field 

## Actual Result

An error message is not displayed and the form is submitted without filling in the email text field 


