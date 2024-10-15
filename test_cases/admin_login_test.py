from selenium import webdriver
from base_page.login_admin_page import Login_Admin_page
from selenium.webdriver.common.by import By

print("Hello")
print(webdriver.__file__)
class Test_01_Admin_login:
    admin_page_url = "https://admin-demo.nopcommerce.com/login"
    username = "admin@userstore.com"
    password = "admin"
    invalid_usernmame = "adminusername@usrstore.com"

    def test_title_verification(self ):
        self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "your store. login"
        if act_title == exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    def test_valid_admin_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_page()
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        act_dashobard_text = self.driver.find_element(By.XPATH,"//div[@class='content-header']/h1").text
        if act_dashobard_text == "Dashboard":
               assert True
               self.driver.close()
        else:
            self.driver.close()
            assert False


    def test_invalid_admin_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_page(self.driver)
        self.admin_lp.enter_username(self.invalid_usernmame)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        error_message = self.driver.find_element(By.XPATH,"//li").text
        if error_message == "No customer account found":
               assert True
               self.driver.close()
        else:
            self.driver.close()
            assert False



