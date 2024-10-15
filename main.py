from test_cases.admin_login_test import Test_01_Admin_login

def main():
    x = Test_01_Admin_login()
    # x.test_title_verification()
    # x.test_valid_admin_login()
    x.test_invalid_admin_login()
    # x.test_valid_admin_login()
    # x.test_invalid_admin_login()

    

if __name__ == "__main__":
    main()                