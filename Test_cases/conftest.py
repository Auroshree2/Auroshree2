import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import allure
from utilities import ReadConfiguraiton

from allure_commons.types import AttachmentType

@pytest.fixture()
def login_cred(request):
    config_driver=ReadConfiguraiton.read_configuration('basic info','browser')
    global driver
    if config_driver=='chrome':
        driver=webdriver.Chrome()
    elif config_driver=='edge':
        driver=webdriver.Edge()
    elif config_driver=='firefox':
        driver=webdriver.Firefox()
    elif config_driver=='safari':
        driver=webdriver.Safari()
    url=ReadConfiguraiton.read_configuration('basic info','url')
    driver.get(url)
    driver.maximize_window()
    request.cls.driver=driver # in the test cse file we have created class so we have to use this
    yield
    driver.quit()

# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):    
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
#     return rep

# @pytest.fixture()
# def log_on_failure(request):
#     item = request.node
#     if item.rep_call.failed:
#     # if hasattr(request.node, "result"):
#     # if request.node is not None and hasattr(request.node, "rep_call") and request.node.rep_call.failed:
  
#         allure.attach(driver.get_screenshot_as_png(),name='failed',attachment_type=AttachmentType.PNG)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture()
def log_on_failure(request):
    item = request.node
    if hasattr(item, "rep_call") and item.rep_call.failed:
        # Attach screenshot if the test failed
        allure.attach(driver.get_screenshot_as_png(), name='failed', attachment_type=AttachmentType.PNG)


