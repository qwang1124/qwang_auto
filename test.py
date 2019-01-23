import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import allure
from pathlib import Path


class TestCreateexperimentJoe(unittest.TestCase):

    def test6(self):
        driver = testjanelogin()
        driver.get('https://model.arxspan.com/arxlab/bio-experiment.asp?id=31893')
        driver.find_element_by_id('addFile_tab').click()
        fileinput = driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]')
        driver.execute_script(
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
            fileinput)
        path = Path('resources\\~$Xenograft.xls').absolute()
        driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]') \
            .send_keys(str(path))
        time.sleep(2)
        button = driver.find_element_by_css_selector('#resumableBrowserHolder > '
                                                     'section.bottomButtons.buttonAlignedRight > button')
        button.click()
        # check attachment is successful and displayed
        driver.find_element_by_id('attachmentTable_tab').click()
        assert driver.find_element_by_class_name('icons').is_displayed
        driver.find_element_by_css_selector('#submitRow > a:nth-child(1)').click()
        # download the file
        driver.find_element_by_css_selector('#file_p_15668_tr > td.uploadButtons > a:nth-child(2)').click()
        # Make an edit to the file and save it locally and upload again
        driver.find_element_by_class_name('littleButton noLiveEdit').click()
        fileinput = driver.find_element_by_id('file1_90169')
        driver.execute_script(
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
            fileinput)
        path = Path('resources\\~$Xenograft.xls').absolute()
        driver.find_element_by_id('file1_90169').send_keys(str(path))
        button = driver.find_element_by_css_selector('#addFileDiv_90169 > form > '
                                                     'section.bottomButtons.buttonAlignedRight > button')
        button.click()
        assert driver.find_element_by_class_name('icons').is_displayed
        driver.close()


def testjanelogin():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://model.arxspan.com/login.asp')
    # driver.maximize_window()
    driver.find_element_by_id('login-email').send_keys('jane@demo.com')
    driver.find_element_by_id('login-pass').send_keys('carbonCopee')
    driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
    time.sleep(1)
    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text('Model Test Script Company')
    driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
    return driver


