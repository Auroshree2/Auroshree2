from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import pytest
from pages import login_page
from utilities import datadriven

@pytest.mark.usefixtures('login_cred','log_on_failure')
class Test_login_class:
    @pytest.mark.parametrize('id,password',datadriven.get_data(r"D:\pytest_framework\excelfiles\loginpage.xlsx",'loginPage'))
    def test_tc1(self,id,password):
        login_obj=login_page.Login_page(self.driver)
        login_obj.enter_value_into_username(id)
        login_obj.enter_value_into_password(password)
        login_obj.submit_button()
        act_text='Time at Work'
        # assert act_text==login_obj.submit_button()
      

        time.sleep(3)
        
 


