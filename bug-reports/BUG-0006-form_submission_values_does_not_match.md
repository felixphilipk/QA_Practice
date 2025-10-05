# Bug ID: BUG-0006

- **Title:** Last Name value does not match after submitting the form 
- **Related Test:** `tests/e2e/test_forms.py::TestForms::tc_forms_0012_submit_form_with_valid_inputs`

## Description
After submitting the form the last name value does not match the value inputted before form submission

## Steps to Reproduce
1. Navigate to the forms page 
2. Enter Test to First Name 
3. Enter Test to Last Name
4. Enter 2122067090 to Phone number field
5. Select the country Australia 
6. Enter Testing to password field
7. Click on agree terms and conditions checkbox 
8. Click on the register button

## Expected Result

The form should be submitted and all the values entered in the form should be present in the success message the value expected is 'Last Name: Test'

## Actual Result

The last character in the last name value is not being displayed in the success message after the form submission the value displayed is "Last Name: Tes"


