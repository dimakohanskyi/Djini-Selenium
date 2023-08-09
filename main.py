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

URL = "https://djinni.co/my/dashboard/"

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get(URL)
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


title_info = f"Summary of the week(QA Manual)\n\n" \

body_info = f"Job Prepositions: {job},\n\n Responses: {responses},\n\n Candidates: {candidates},\n\n Salary: {sal}\n\n"

footer_info = f"You can find this project here 'https://github.com/dimakohanskyi'"

all_info = f"{title_info} {body_info} {footer_info}"



message_bytes = all_info.encode('utf-8')

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=all_info
    )


