import tkinter as tk
from tkinter import filedialog, Entry, messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

counter = 0

def automate_data_submission(line, driver):
    try:
        username_input = driver.find_element(By.ID, 'enquire-name')
        email_input = driver.find_element(By.ID, 'enquire-email')
        mobile_input = driver.find_element(By.ID, 'enquire-mobile')
        pincode_input = driver.find_element(By.ID, 'enquire-pincode')

        username_input.send_keys(line[0])
        email_input.send_keys(line[1])
        mobile_input.send_keys(line[2])
        pincode_input.send_keys(line[3])

        remover = driver.execute_script("document.querySelectorAll('button')[0].classList.remove('otpValidate');")
        data_delay = float(entry_data_delay.get())
        time.sleep(data_delay)
        submit = pincode_input.send_keys(Keys.ENTER)

        # Check if the success element is present
        success_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/h2"))
        )
        time.sleep(2)

        if success_element:
            global counter
            counter += 1
            print("Data send:", counter)
            newfile = data_file.get()
            with open(f'{newfile}.csv', 'a', newline='') as success_file:
                success_writer = csv.writer(success_file)
                datasuccess = int(1)
                user_data = [line[0], line[1], line[2], line[3], datasuccess]
                success_writer.writerow(user_data)
            return True
        else:
            print('Data send failed')
            return False

    except NoSuchElementException as e:
        print(f"Element not found: {e}")
        return False
    except TimeoutException as e:
        print(f"Timeout: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def automate_asianpaint():
    global counter
    try:
        url = entry_url.get()
        file_path = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")])

        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)

#        driver.get("http://192.168.8.1/html/home.html")
        driver.get(dongal_url.get())
        driver.maximize_window()

        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)

            for line in csv_reader:
                changeIp = driver.find_element(By.XPATH, dongal_xpath.get())
#                changeIp = driver.find_element(By.XPATH, '//*[@id="mobile_connect_btn"]')
                changeIp.click()
                time.sleep(1)

                driver.execute_script("window.open('', '_blank');")
                driver.switch_to.window(driver.window_handles[-1])
                driver.get(entry_url.get())
#                driver.get('https://www.asianpaints.com/campaign/ap-crm/index.html')
                delay_page = float(entry_delay_page.get())
                time.sleep(delay_page)

                # Scroll
                driver.execute_script("window.scrollTo(0, 1500)")
                delay_scroll1 = float(entry_delay_scroll1.get())
                time.sleep(delay_scroll1)
                driver.execute_script("window.scrollTo(0, 0)")
                delay_scroll2 = float(entry_delay_scroll2.get())
                time.sleep(delay_scroll2)

                success = automate_data_submission(line, driver)

                driver.delete_all_cookies()
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                changeIp.click()

                dongal = dongal_delay.get()
                time.sleep(int(dongal))

                if success:
                    print("data send:", counter)
                else:
                    print('data send fail:')
            print("Automation completed")

    except Exception as e:
        print("Error", f"An error occurred: {str(e)}")
    finally:
        driver.quit()


#------------------- GUI -----------------------
root = tk.Tk()
root.title('AsianPaint Automation')
root.geometry('580x400+300+200')


tk.Label(root, text='AsianPaint form filling automation', font=('Helvetica', 14, 'bold')).grid(row=0, column=1)

tk.Label(root, text='Dongal to change I.P', font=('Helvetica', 10, 'bold')).grid(row=1, column=1)

tk.Label(root, text='Enter Dongal Link :', font=('Helvetica', 10)).grid(row=2, column=0)
dongal_url = Entry(root, width=47)
dongal_url.grid(row=2, column=1)

tk.Label(root, text='Enter Xpath of button :', font=('Helvetica', 10)).grid(row=3, column=0)
dongal_xpath = tk.Entry(root, width=50)
dongal_xpath.grid(row=3, column=1)

tk.Label(root, text='Enter Dongal Delay time :', font=('Helvetica', 10)).grid(row=4, column=0)
dongal_delay = tk.Entry(root, width=10)
dongal_delay.grid(row=4, column=1)

separator = tk.Frame(height=2, bd=1, relief="groove")
separator.grid(row=5, columnspan=2, sticky="ew", pady=5)


tk.Label(root, text='AsianPaint Automation Section: ', font=('Helvetica', 10, 'bold')).grid(row=6, column=1)
tk.Label(root, text='Enter AsianPaint Tracking Link: ', font=('Helvetica', 10)).grid(row=7, column=0)
entry_url = Entry(root, width=50)
entry_url.grid(row=7, column=1)

tk.Label(root, text='Delay After Page Load (seconds) :', font=('Helvetica', 10)).grid(row=8, column=0)
entry_delay_page = tk.Entry(root, width=10)
entry_delay_page.grid(row=8, column=1)

tk.Label(root, text='Delay after 1st Scroll (seconds) :', font=('Helvetica', 10)).grid(row=9, column=0)
entry_delay_scroll1 = tk.Entry(root, width=10)
entry_delay_scroll1.grid(row=9, column=1)

tk.Label(root, text='Delay after 2nd Scroll (seconds) :', font=('Helvetica', 10)).grid(row=10, column=0)
entry_delay_scroll2 = tk.Entry(root, width=10)
entry_delay_scroll2.grid(row=10, column=1)

tk.Label(root, text='Delay for Data submit time (seconds) :', font=('Helvetica', 10)).grid(row=11, column=0)
entry_data_delay = tk.Entry(root, width=10)
entry_data_delay.grid(row=11, column=1)

separator = tk.Frame(height=2, bd=1, relief="groove")
separator.grid(row=12, columnspan=2, sticky="ew", pady=5)

tk.Label(root, text='Enter data send file name:', font=('Helvetica', 10)).grid(row=13, column=0)
data_file = tk.Entry(root, width=35)
data_file.grid(row=13, column=1)

tk.Button(root, text="Automate AsianPaint", command=automate_asianpaint, height=2, width=30, font=('Helvetica', 12, 'bold')).grid(row=14, column=1)

tk.Button(root, text='Close', command=root.destroy).grid(row=15, column=1)
root.mainloop()
