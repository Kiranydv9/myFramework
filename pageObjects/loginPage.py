
class LoginPage:
    textfield_username_id="Email"
    textfield_password_id="Password"
    btn_Login_xpath="//button[contains(text(),'Log in')]"
    linktext_logout_linktext="Logout"


    def __init__(self,driver):
        self.driver=driver
        
    def setUserName(self,username):
        self.driver.find_element_id(self.textfield_username_id).clear()
        self.driver.find_element_id(self.textfield_username_id).sendkeys(username)

    def setPassword(self,password):
        self.driver.find_element_id(self.textfield_password_id).sendkeys(password)

    def setLogin(self,login):
        self.driver.find_element_xpath(self.btn_Login_xpath).click()

    def setLogout(self,logout):
        self.driver.find_element_link_text(self.linktext_logout_linktext).click()

