import time
from tkinter import font
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import smtplib
from dotenv import load_dotenv
import os
from email.mime.multipart import MIMEMultipart   ## клас дозволяє прикріпляти до повідомлення текст фото чи html
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


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

    salary_from_djini = f"Djini: {sal}"

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

    sal_max = driver.find_element(By.XPATH, '//*[@id="q3"]/div/span[2]').text

    sal_medium_dou = (int(sal_start) + int(sal_max)) / 2
    salary_from_dou = f"Dou: {sal_medium_dou}$\n\n"

except Exception as ex:
    print(ex)

#-------------------------------MSG Elements--------------------------------------------------#

SUBJECT = f"Summary of the week(QA Manual)\n\n" \

body_job_info = f"Job Prepositions: {job}"
body_responses_info = f"Responses: {responses}"
body_candidates_info = f"Candidates: {candidates}"
difference_of_salary = f"General salary statistics: {salary_from_djini} -- {salary_from_dou}"

with open("image.jpg", "rb") as image_file:
    image_data = image_file.read()
    image_part = MIMEImage(image_data, name="image.jpg")

#---------------------------------------------------------------------------------------------------#

# Create a MIME object
message = MIMEMultipart()
message["From"] = MY_EMAIL
message["To"] = MY_EMAIL
message["Subject"] = SUBJECT
message.attach(image_part)

#----------------------------------------------------------------------------------------------------#
html_content = f"""
<html>
<head>

</head>
<body style="font-family: Georgia, serif;">
    <p>{body_job_info}</p>
    <p>{body_responses_info}</p>
    <p>{body_candidates_info}</p>
    <p>{difference_of_salary}</p>
    <p><a href="https://www.instagram.com/dima_kohanskyi/">&#10071;My Contacts&#10071;</a></p>
    <p><a href="https://github.com/dimakohanskyi/Djini-Selenium">&#10069;Git-Hub&#10069;</a></p>

</body>
</html>
"""
#----------------------------------------------------------------------------------------------------#

html_part = MIMEText(html_content, "html")
message.attach(html_part)

try:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        msg = MIMEMultipart()
        connection.sendmail(MY_EMAIL, MY_EMAIL, message.as_string())

except Exception as ex:
    print(ex)





