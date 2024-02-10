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
        driver.switch_to.frame("sfmcIframe")
        first = driver.find_element(By.XPATH, '//*[@id="first-name"]')
        last = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        mobile = driver.find_element(By.XPATH, '//*[@id="mobile"]')
        date = driver.find_element(By.XPATH, '//*[@id="date_of_birth_string"]')
        email = driver.find_element(By.XPATH, '//*[@id="email"]')
        state = driver.find_element(By.XPATH, '//*[@id="state"]/option['+line[5]+']')
        gender = driver.find_element(By.XPATH, '//*[@id="'+line[6]+'"]')
        opts = driver.find_element(By.XPATH, '//*[@id="ColgateOralCare'+line[7]+'"]')
        checkbox = driver.find_element(By.XPATH, '//*[@id="confirm"]')

        #send data
        first.send_keys(line[0])
        last.send_keys(line[1])
        mobile.send_keys(line[2])
        date.send_keys(line[3])
        email.send_keys(line[4])
        state.click()
        gender.click()
        opts.click()
        checkbox.click()

        data_delay = float(entry_data_delay.get())
        time.sleep(data_delay)
        submit = driver.find_element(By.XPATH, '//*[@id="frm_col_toothbrush_contest"]/div/div/div/div[3]/div[6]/div/button').click()

        # Check if the error element is present
        error_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="divform"]/div/div/p[3]'))
        )
        time.sleep(2)
        
        global counter
        if error_element:
            print('Data send failed :'+ counter++1)
            return False
        else:
            counter += 1
            print("Data send:", counter)
            newfile = data_file.get()
            with open(f'{newfile}.csv', 'a', newline='') as success_file:
                success_writer = csv.writer(success_file)
                datasuccess = int(1)
                user_data = [line[0], line[1], line[2], line[3], line[4], datasuccess]
                success_writer.writerow(user_data)
            return True

    except NoSuchElementException as e:
        print(f"Element not found: {e}")
        return False
    except TimeoutException as e:
        print(f"Timeout: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def automate_colgate():
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
#                driver.get('https://www.colgate.com/en-in/campaign/win-with-total')
                delay_page = float(entry_delay_page.get())
                time.sleep(delay_page)

                # Scroll
                driver.execute_script("window.scrollTo(0, 1800)")
                delay_scroll1 = float(entry_delay_scroll1.get())
                time.sleep(delay_scroll1)
                
                try:
                    accept_all = driver.find_element(By.XPATH, '//*[@id="truste-consent-button"]')
                    accept_all.click()
                except NoSuchElementException:
                    pass
                
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

    except NoSuchElementException as e:
        print(f"Element not found: {e}")

    except Exception as e:
        print("Error", f"An error occurred: {str(e)}")
    finally:
        driver.quit()

#-------------- GUI -------------------
root = tk.Tk()
root.title('Colgate Automation')
root.geometry('580x400+300+200')

tk.Label(root, text='Colgate form filling automation', font=('Helvetica', 14, 'bold')).grid(row=0, column=1)
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

tk.Label(root, text='Colgate Automation Section: ', font=('Helvetica', 10, 'bold')).grid(row=6, column=1)
tk.Label(root, text='Enter Colgate Tracking Link: ', font=('Helvetica', 10)).grid(row=7, column=0)
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

tk.Button(root, text="Automate Colgate", command=automate_colgate, height=2, width=30, font=('Helvetica', 12, 'bold')).grid(row=14, column=1)
tk.Button(root, text='Close', command=root.destroy).grid(row=15, column=1)
root.mainloop()
