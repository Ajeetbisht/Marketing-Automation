from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import csv
import tkinter as tk
from tkinter import filedialog


def import_csv_file():
    csv_file_path = filedialog.askopenfilename(title="Open CSV File", filetypes=[("CSV files", "*.csv")])
    return csv_file_path

def execute_asian_automation(line, url, delay_page, delay_scroll1, data_delay, submit_page):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    time.sleep(delay_page)

    # Close popup
    accept_cookies = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()

    # Scroll
    driver.execute_script("window.scrollTo(0, 1800)")
    time.sleep(delay_scroll1)
    driver.execute_script("window.scrollTo(0, 0)")

    try:
        wait = WebDriverWait(driver, 2)

        #access fields
        username_input = driver.find_element(By.ID, 'enquire-name')
        email_input = driver.find_element(By.ID, 'enquire-email')
        mobile_input = driver.find_element(By.ID, 'enquire-mobile')
        pincode_input = driver.find_element(By.ID, 'enquire-pincode')
        submit_button = driver.find_element(By.CLASS_NAME, 'ctaText')

        #send data
        username_input.send_keys(line[0])
        email_input.send_keys(line[1])
        mobile_input.send_keys(line[2])
        pincode_input.send_keys(line[3])

        remover = driver.execute_script("document.querySelectorAll('button')[1].classList.remove('otpValidate');")
        time.sleep(data_delay)
        submit = pincode_input.send_keys(Keys.ENTER)

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
    data_delay = float(entry_data_delay.get())
    submit_page = float(entry_submit_page.get())

    with open(csv_file_path, 'r') as csv_file: 
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        
        for line in csv_reader:
            execute_asian_automation(line, url, delay_page, delay_scroll1, data_delay, submit_page)


# -------------- GUI -------------------
r = tk.Tk()
r.title('Asianpaint Automation')
r.geometry('500x400+300+200')

tk.Label(r, text='Enter Asianpaint Tracking Link:').grid(row=0, column=0)
entry_url = tk.Entry(r, width=38)
entry_url.grid(row=0, column=1)

tk.Label(r, text='Delay After Page Load (seconds):').grid(row=1, column=0)
entry_delay_page = tk.Entry(r, width=10)
entry_delay_page.grid(row=1, column=1)

tk.Label(r, text='Delay after 1st Scroll (seconds):').grid(row=2, column=0)
entry_delay_scroll1 = tk.Entry(r, width=10)
entry_delay_scroll1.grid(row=2, column=1)

tk.Label(r, text='Delay for Data submit time (seconds):').grid(row=4, column=0)
entry_data_delay = tk.Entry(r, width=10)
entry_data_delay.grid(row=4, column=1)

tk.Label(r, text='Wait Time Post Submit Botton (seconds):').grid(row=5, column=0)
entry_submit_page = tk.Entry(r, width=10)
entry_submit_page.grid(row=5, column=1)

tk.Label(r, text='Upload only CSV file').grid(row=6, column=0)
tk.Button(r, text="Automate Colgate", command=Challo, height=2, width=30).grid(row=7, column=1)

tk.Button(r, text='Close Script', command=r.destroy).grid(row=8, column=1, columnspan=2)
r.mainloop()
