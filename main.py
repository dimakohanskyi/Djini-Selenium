import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
PASSWORD_FO_LOG_IN = os.getenv("PASSWORD_FO_LOG_IN")

URL_DJINI = "https://djinni.co/my/dashboard/"
URL_DOU = "https://dou.ua/"

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

## --------------------------------------------------DJINI--------------------------------------------#
try:
    driver.get(URL_DJINI)
    driver.maximize_window()

    email_inp = driver.find_element(By.XPATH, '//*[@id="email"]')
    email_inp.send_keys(MY_EMAIL)

    password_inp = driver.find_element(By.XPATH, '//*[@id="password"]')
    password_inp.send_keys(PASSWORD_FO_LOG_IN)

    button_click = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/form/div[1]/div[3]/button')
    button_click.click()

    statistic_button = driver.find_element(By.XPATH, '/html/body/div[1]/nav/div/div[2]/ul[1]/li[3]/a')
    statistic_button.click()

    qa_manual = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[6]/div/div[1]/div[2]/a[33]')
    qa_manual.click()

    experience_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[6]/div/div[2]/div[2]/a[3]')
    experience_button.click()

    english_level = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[6]/div/div[3]/div[2]/a[4]')
    english_level.click()

    amount_job_prepos = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/div[2]/div[1]/div[1]')
    job = amount_job_prepos.text

    amount_of_responses = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div[1]')
    responses = amount_of_responses.text

    amount_of_candidates = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div[1]')
    candidates = amount_of_candidates.text

    salary = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]')
    sal = salary.text

except Exception as ex:
    print(ex)


###--------------------------------------- DOU-------------------------------------#

try:
    driver.get(URL_DOU)
    driver.maximize_window()

    dou_salary = driver.find_element(By.XPATH, '/html/body/div/header/ul/li[5]/a')
    dou_salary.click()

    drop_down_joblist = driver.find_element(By.XPATH, '//*[@id="dd-position"]/div[1]')
    drop_down_joblist.click()

    qa_dropdown = driver.find_element(By.XPATH, '//*[@id="dd-position"]/div[2]/div[2]/div[2]/div[2]')
    qa_dropdown.click()

    time.sleep(3)
    sal_start = driver.find_element(By.XPATH, '//*[@id="q1"]/div/span[2]').text

    sal_medium = driver.find_element(By.XPATH, '//*[@id="median"]/div/span[2]').text

    salary_from_dou = f"Dou: {sal_start}$-{sal_medium}$\n\n"

except Exception as ex:
    print(ex)

#----------------------------------------------------------------------------------#


SUBJECT = f"Summary of the week(QA Manual)\n\n" \

body_info = f"Job Prepositions: {job},\n\n Responses: {responses},\n\n Candidates: {candidates},\n\n"

salary_from_djini = f"Djini: {sal}"

difference_of_salary = f"General salary statistics: {salary_from_djini} -- {salary_from_dou}"

footer_info = f"You can find this project here 'https://github.com/dimakohanskyi/Djini-Selenium'"

all_info = f"{SUBJECT} {body_info} {difference_of_salary} {footer_info}"

message_bytes = all_info.encode('utf-8')

try:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=all_info
        )
except Exception as ex:
    print(ex)


