from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class Login_page:
    def __init__(self,driver):
        self.driver=driver

    name_loc_by_name="username"
    password_loc_by_name="password"
    submit_loc_by_xpath= "//button[@type='submit']"


    def enter_value_into_username(self,user_name):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.NAME,self.name_loc_by_name)))
        self.driver.find_element(By.NAME,self.name_loc_by_name).click()
        self.driver.find_element(By.NAME,self.name_loc_by_name).clear()
        self.driver.find_element(By.NAME,self.name_loc_by_name).send_keys(user_name)

    def enter_value_into_password(self,password):

        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.NAME,self.password_loc_by_name)))
        self.driver.find_element(By.NAME,self.password_loc_by_name).click()
        self.driver.find_element(By.NAME,self.password_loc_by_name).clear()
        self.driver.find_element(By.NAME,self.password_loc_by_name).send_keys(password)

    def submit_button(self):

        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,self.submit_loc_by_xpath)))
        self.driver.find_element(By.XPATH,self.submit_loc_by_xpath).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,"//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text
        
    


   
            
        

