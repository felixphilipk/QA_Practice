# Bug ID: BUG-0008

- **Title:** Able to fill the form without filling mandatory name fields 
- **Related Test:** `tests/e2e/test_forms.py::TestForms::tc_forms_0013_submit_form_without_last_names`

## Description
Able to submit the form without filling mandatory name field 

## Steps to Reproduce
1. Navigate to the forms page 
2. Enter Test to First Name 
3. Leave Last Name empty
4. Enter 2122067090 to Phone number field
5. Select the country Australia 
6. Enter Testing to password field
7. Click on agree terms and conditions checkbox 
8. Click on the register button

## Expected Result

The form should not be submitted without filling the mandatory fields 

## Actual Result

Able to submit the form without filling the last name field 


