'''from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import csv

def Challo():
    csv_file_path = filedialog.askopenfilename(title="Open CSV File", filetypes=[("CSV files", "*.csv")])

    with open(csv_file_path, 'r')as csv_file: 
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        
        for line in csv_reader:
            driver=webdriver.Chrome()
#            url = 'https://www.colgate.com/en-in/campaign/win-with-total'
            url = "https://eheadway.o18.click/c?o=20963894&m=1871&a=69233"
            driver.get(url)
            driver.maximize_window()
            time.sleep(5)

            #close popup
            acceptall= driver.find_element(By.XPATH, '//*[@id="truste-consent-button"]').click()

            #scroll
            time.sleep(3)
            driver.execute_script("window.scrollTo(0, 1800)")
            time.sleep(3)
            driver.execute_script("window.scrollTo(0, 0)")
            time.sleep(3)

            try:
                driver.switch_to.frame("sfmcIframe")
                first = driver.find_element(By.XPATH, '//*[@id="first-name"]')
                last = driver.find_element(By.XPATH, '//*[@id="last-name"]')
                mobile = driver.find_element(By.XPATH, '//*[@id="mobile"]')
                date = driver.find_element(By.XPATH, '//*[@id="date_of_birth_string"]')
                email = driver.find_element(By.XPATH, '//*[@id="email"]')            
                state = driver.find_element(By.XPATH, '//*[@id="state"]/option['+line[5]+']') 
                gender = driver.find_element(By.XPATH, '//*[@id="female"]')
                gender = driver.find_element(By.XPATH, '//*[@id="'+line[6]+'"]')
                opts = driver.find_element(By.XPATH, '//*[@id="ColgateOralCare'+line[7]+'"]')
                checkbox = driver.find_element(By.XPATH, '//*[@id="confirm"]')

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
                submit = driver.find_element(By.XPATH, '//*[@id="frm_col_toothbrush_contest"]/div/div/div/div[3]/div[6]/div/button').click()
                time.sleep(20)
                if submit == True:
                    print("response submited thankyou")        
                else:
                    print("not submited")
                    
        
                #    searchbox.send_keys(Keys.ENTER)
            except Exception as e:
                print(e)
                

            # Wait for the next page to load (adjust the timeout as needed)
            try:
                # Wait until a certain element is present on the page (replace 'element_id' with the actual element ID)
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, '/html/body/div[4]/div/div[2]/div/div[3]/div/div/div/div/div[6]/div[2]/h3')))
                print("Page successfully loaded after login.")
                
                # Now you can perform additional ations on the page

            except Exception as e:
                print(f"An error occurred: {str(e)}")

            finally:
                driver.quit()
                print("browser quits")


#---------------  GUI  ------------------

import tkinter as tk
from tkinter import *
from tkinter import filedialog

r=tk.Tk()
r.title('Colgate Automation')
r.geometry('500x400+300+200')

tk.Label(r, text='Upload only CSV file').grid(row=0, column=0)
tk.Button(r, text = "Automate Colgate", command =Challo, height=2, width=40).grid(row=20, column=70) 

tk.Button(r, text='Close', command=r.destroy).grid(row=450, column=80)
r.mainloop()
'''




#------------- Production Ready -----------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import tkinter as tk
from tkinter import filedialog


def import_csv_file():
    csv_file_path = filedialog.askopenfilename(title="Open CSV File", filetypes=[("CSV files", "*.csv")])
    return csv_file_path

def execute_colgate_automation(line, url, delay_page, delay_scroll1, delay_scroll2, data_delay, submit_page):
    driver = webdriver.Chrome()
    driver.get(url)

#    url = 'https://www.colgate.com/en-in/campaign/win-with-total'
#    url = "https://eheadway.o18.click/c?o=20963894&m=1871&a=69233"
    driver.maximize_window()
    time.sleep(delay_page)

    # Close popup
    accept_all = driver.find_element(By.XPATH, '//*[@id="truste-consent-button"]').click()

    # Scroll
    driver.execute_script("window.scrollTo(0, 1800)")
    time.sleep(delay_scroll1)
    driver.execute_script("window.scrollTo(0, 0)")
    time.sleep(delay_scroll2)

    try:
        driver.switch_to.frame("sfmcIframe")
        wait = WebDriverWait(driver, 2)

        first = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]')))
        last = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="last-name"]')))
        mobile = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mobile"]')))
        date = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="date_of_birth_string"]')))
        email = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email"]')))
        state = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="state"]/option[' + line[5] + ']')))
        gender = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="' + line[6] + '"]')))
        opts = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ColgateOralCare' + line[7] + '"]')))
        checkbox = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="confirm"]')))

        first.send_keys(line[0])
        last.send_keys(line[1])
        mobile.send_keys(line[2])
        date.send_keys(line[3])
        email.send_keys(line[4])
        state.click()
        gender.click()
        opts.click()
        checkbox.click()

        time.sleep(data_delay)
        submit = driver.find_element(By.XPATH, '//*[@id="frm_col_toothbrush_contest"]/div/div/div/div[3]/div[6]/div/button').click()
        time.sleep(submit_page)
        
        if submit:
            print("Response submitted, thank you!")
        else:
            print("Not submitted")
    except Exception as e:
        print(e)

    finally:
        driver.quit()
        print("Browser quits")

def Challo():
    csv_file_path = import_csv_file()
    url = entry_url.get()
    delay_page = float(entry_delay_page.get())
    delay_scroll1 = float(entry_delay_scroll1.get())
    delay_scroll2 = float(entry_delay_scroll2.get())
    data_delay = float(entry_data_delay.get())
    submit_page = float(entry_submit_page.get())

    with open(csv_file_path, 'r') as csv_file: 
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        
        for line in csv_reader:
            execute_colgate_automation(line, url, delay_page, delay_scroll1, delay_scroll2, data_delay, submit_page)

# -------------- GUI -------------------
r = tk.Tk()
r.title('Colgate Automation')
r.geometry('500x400+300+200')

tk.Label(r, text='Enter Colgate Tracking Link:').grid(row=0, column=0)
entry_url = tk.Entry(r, width=40)
entry_url.grid(row=0, column=1)

tk.Label(r, text='Delay After Page Load (seconds):').grid(row=1, column=0)
entry_delay_page = tk.Entry(r, width=10)
entry_delay_page.grid(row=1, column=1)

tk.Label(r, text='Delay after 1st Scroll (seconds):').grid(row=2, column=0)
entry_delay_scroll1 = tk.Entry(r, width=10)
entry_delay_scroll1.grid(row=2, column=1)

tk.Label(r, text='Delay after 2nd Scroll (seconds):').grid(row=3, column=0)
entry_delay_scroll2 = tk.Entry(r, width=10)
entry_delay_scroll2.grid(row=3, column=1)

tk.Label(r, text='Delay for Data submit time (seconds):').grid(row=4, column=0)
entry_data_delay = tk.Entry(r, width=10)
entry_data_delay.grid(row=4, column=1)

tk.Label(r, text='Wait Time Post Submit Botton (seconds):').grid(row=5, column=0)
entry_submit_page = tk.Entry(r, width=10)
entry_submit_page.grid(row=5, column=1)

tk.Label(r, text='Upload only CSV file').grid(row=6, column=0)
tk.Button(r, text="Automate Colgate", command=Challo, height=2, width=40).grid(row=7, column=0)

tk.Button(r, text='Close Script', command=r.destroy).grid(row=8, column=1, columnspan=2)
r.mainloop()






'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import csv
import tkinter as tk
from tkinter import filedialog
import HtmlTestRunner

class ColgateAutomationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_colgate_automation(self):
        csv_file_path = self.import_csv_file()
        
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            
            for line in csv_reader:
                self.execute_colgate_automation(line)

    def import_csv_file(self):
        csv_file_path = filedialog.askopenfilename(title="Open CSV File", filetypes=[("CSV files", "*.csv")])
        return csv_file_path

    def execute_colgate_automation(self, line):
        url = "https://eheadway.o18.click/c?o=20963894&m=1871&a=69233"
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(5)

        # Close popup
        accept_all = self.driver.find_element(By.XPATH, '//*[@id="truste-consent-button"]').click()

        # Scroll
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
            gender = self.driver.find_element(By.XPATH, '//*[@id="female"]')
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
            time.sleep(20)
            
            if submit:
                print("Response submitted, thank you!")
            else:
                print("Not submitted")

        except Exception as e:
            print(e)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test-reports'))
'''
