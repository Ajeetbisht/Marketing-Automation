'''from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import csv
import unittest
import HtmlTestRunner

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_automationstepbystep(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element(By.NAME, 'q')
        self.send_keys('Automation test case')
#        self.driver.find_element_by_name("btn").click()

    def test_search_automationstepbystep(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element(By.NAME, 'q')
        self.send_keys('random test case').click()
#        self.driver.find_element_by_name("btn").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test Completed")
    
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/vijay Bisht/Desktop/automation'))
'''

    
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import csv
import HtmlTestRunner
from tkinter import filedialog

class TestColgateAutomation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_Challo(self):
        csv_file_path = filedialog.askopenfilename(title="Open CSV File", filetypes=[("CSV files", "*.csv")])

        with open(csv_file_path, 'r') as csv_file: 
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            
            for line in csv_reader:
                self.driver.get("https://eheadway.o18.click/c?o=20963894&m=1871&a=69233")
                self.driver.maximize_window()
                time.sleep(5)

                #close popup
                acceptall = self.driver.find_element(By.XPATH, '//*[@id="truste-consent-button"]').click()

                #scroll
                time.sleep(3)
                self.driver.execute_script("window.scrollTo(0, 1800)")
                time.sleep(3)
                self.driver.execute_script("window.scrollTo(0, 0)")
                time.sleep(3)

                try:
                    self.driver.switch_to.frame("sfmcIframe")
                    first = self.driver.find_element(By.XPATH, '//*[@id="first-name"]')
                    last = self.driver.find_element(By.XPATH, '//*[@id="last-name"]')
                    mobile = self.driver.find_element(By.XPATH, '//*[@id="mobile"]')
                    date = self.driver.find_element(By.XPATH, '//*[@id="date_of_birth_string"]')
                    email = self.driver.find_element(By.XPATH, '//*[@id="email"]')            
                    state = self.driver.find_element(By.XPATH, '//*[@id="state"]/option[' + line[5] + ']') 
                    gender = self.driver.find_element(By.XPATH, '//*[@id="' + line[6] + '"]')
                    opts = self.driver.find_element(By.XPATH, '//*[@id="ColgateOralCare' + line[7] + '"]')
                    checkbox = self.driver.find_element(By.XPATH, '//*[@id="confirm"]')

                    first.send_keys(line[0])
                    last.send_keys(line[1])
                    mobile.send_keys(line[2])
                    date.send_keys(line[3])
                    email.send_keys(line[4])
                    state.click()
                    gender.click()
                    opts.click()
                    checkbox.click()
                    time.sleep(15)
                    submit = self.driver.find_element(By.XPATH, '//*[@id="frm_col_toothbrush_contest"]/div/div/div/div[3]/div[6]/div/button').click()

                    # Your assertion here
                    self.assertTrue(submit)

                except Exception as e:
                    print(e)

                # Wait for the next page to load
                try:
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, '/html/body/div[4]/div/div[2]/div/div[3]/div/div/div/div/div[6]/div[2]/h3')))
                    print("Page successfully loaded after login.")
                    # Additional assertions or actions on the page if needed

                except Exception as e:
                    print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test-reports'))

