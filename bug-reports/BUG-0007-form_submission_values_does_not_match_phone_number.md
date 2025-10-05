# Bug ID: BUG-0007

- **Title:** Phone number value does not match after submitting the form 
- **Related Test:** `tests/e2e/test_forms.py::TestForms::tc_forms_0012_submit_form_with_valid_inputs`

## Description
After submitting the form the phone number value does not match the value inputted before form submission

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

The form should be submitted and all the values entered in the form should be present in the success message. The phone number value expected is 2122067090

## Actual Result

The 1 is being added to the last digit of the phone number in the success message the phone number in the success message is 2122067091


