# Test Case: Login With Valid Credentials

- **ID:** TC-AUTH-001
- **Related Spec:** `tests/e2e/test_login.py::TestLogin::test_tc_auth_001_login_with_valid_credentials`
- **Description:** User should be able to login with valid login credentials

- **Preconditions:**
- Navigate to the login page https://qa-practice.netlify.app/auth_ecommerce 

## Steps 
1. Navigate to the login Page
2. Enter admin@admin.com to the email text field
3. Enter admin123 into the password text field 


## Expected Results
A login success message should be displayed and the user should be navigated to the dashboard
