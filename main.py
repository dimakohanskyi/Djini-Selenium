import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
import sqlite3
from datetime import datetime

# ---------------------------------------------------OPTIONS-----------------------------------------------#

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
PASSWORD_FO_LOG_IN = os.getenv("PASSWORD_FO_LOG_IN")

URL_DJINNI = "https://djinni.co/my/dashboard/"
URL_DOU = "https://dou.ua/"

current_date = datetime.now().date()
weekday = current_date.weekday()

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

# # --------------------------------------------------DJINNI_QA--------------------------------------------#
try:
    driver.get(URL_DJINNI)
    driver.maximize_window()

    email_inp = driver.find_element(By.XPATH, '//*[@id="email"]')
    email_inp.send_keys(MY_EMAIL)

    password_inp = driver.find_element(By.XPATH, '//*[@id="password"]')
    password_inp.send_keys(PASSWORD_FO_LOG_IN)

    button_click = driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div/div/div[2]/form/div[1]/div[3]/button')
    button_click.click()

    statistic_button = driver.find_element(By.XPATH,
                                           '/html/body/div[1]/nav/div/div[2]/ul[1]/li[3]/a')
    statistic_button.click()

    qa_manual = driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div[2]/div/div/div/div/div[6]/div/div[1]/div[2]/a[33]')
    qa_manual.click()

    experience_button = driver.find_element(By.XPATH,
                                            '/html/body/div[1]/div[2]/div/div/div/div/div[6]/div/div[2]/div[2]/a[3]')
    experience_button.click()

    english_level = driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div[2]/div/div/div/div/div[6]/div/div[3]/div[2]/a[4]')
    english_level.click()

    amount_job_preposition = driver.find_element(By.XPATH,
                                                 '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/div[2]/div[1]/div[1]')
    job_amount_djinni_statistic_for_qa = amount_job_preposition.text

    amount_of_responses = driver.find_element(By.XPATH,
                                              '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div[1]')
    responses_amount_djinni_for_qa = amount_of_responses.text

    amount_of_candidates_qa = driver.find_element(By.XPATH,
                                                  '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div[1]')
    candidates_amount_djinni_qa = amount_of_candidates_qa.text

    salary = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]')
    salary_djinni_statistic_qa = salary.text

    divide_sal_qa_djinni = salary_djinni_statistic_qa.split("-")

    salary_start_qa_djinni_with_dollar = divide_sal_qa_djinni[0]
    salary_max_qa_djinni_with_dollar = divide_sal_qa_djinni[1]

    salary_start_qa_djinni_without_dollar = salary_start_qa_djinni_with_dollar.replace('$', '')
    salary_max_qa_djinni_without_dollar = salary_max_qa_djinni_with_dollar.replace('$', '')


except Exception as ex:
    print(ex)

##--------------------------------------------Python Djinni----------------------------------------------#

try:
    driver.get("https://djinni.co/salaries/")

    python_developer_button_djinni = driver.find_element(By.XPATH,
                                                         '/html/body/div[1]/div[2]/div/div/div/div/div[6]/div/div[1]/div[2]/a[32]')
    python_developer_button_djinni.click()

    experience_button_python_djinni = driver.find_element(By.XPATH,
                                                          '/html/body/div[1]/div[2]/div/div/div/div/div[6]/div/div[2]/div[2]/a[3]')
    experience_button_python_djinni.click()

    english_level_python_djinni = driver.find_element(By.XPATH,
                                                      '/html/body/div[1]/div[2]/div/div/div/div/div[6]/div/div[3]/div[2]/a[5]')
    english_level_python_djinni.click()

    salary_for_python_djinni = driver.find_element(By.XPATH,
                                                   '/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[1]').text

    divide_salary_python_djinni = salary_for_python_djinni.split("-")
    salary_start_python_djinni_with_dollar = divide_salary_python_djinni[0]
    salary_max_python_djinni_with_dollar = divide_salary_python_djinni[1]

    salary_start_python_djinni_without_dollar = salary_start_python_djinni_with_dollar.replace('$', '')
    salary_max_python_djinni_without_dollar = salary_max_python_djinni_with_dollar.replace('$', '')

except Exception as ex:
    print(ex)

##--------------------------------------- DOU QA-------------------------------------#

try:
    driver.get(URL_DOU)
    driver.maximize_window()

    dou_salary = driver.find_element(By.XPATH, '/html/body/div/header/ul/li[5]/a')
    dou_salary.click()

    drop_down_joblist = driver.find_element(By.XPATH, '//*[@id="dd-position"]/div[1]')
    drop_down_joblist.click()

    qa_dropdown = driver.find_element(By.XPATH, '//*[@id="dd-position"]/div[2]/div[2]/div[2]/div[2]')
    qa_dropdown.click()

    time.sleep(2)
    sal_start_qa_dou = driver.find_element(By.XPATH, '//*[@id="q1"]/div/span[2]').text

    sal_max_qa_dou = driver.find_element(By.XPATH, '//*[@id="q3"]/div/span[2]').text

except Exception as ex:
    print(ex)

# ------------------------------------------------Python Dou-----------------------------------------------------#

try:
    driver.get("https://jobs.dou.ua/salaries/?period=2023-06&position=Middle%20SE")

    python_developer_button_dou = driver.find_element(By.XPATH, '//*[@id="dws-fl-technology"]/div/div[2]/div[14]')
    python_developer_button_dou.click()

    python_developer_dropdown_dou = driver.find_element(By.XPATH, '//*[@id="dd-position"]/div[1]')
    python_developer_dropdown_dou.click()

    python_dev_option_dropdown = driver.find_element(By.XPATH, '//*[@id="dd-position"]/div[2]/div[1]/div[2]/div[2]')
    python_dev_option_dropdown.click()

    time.sleep(2)
    python_dev_salary_start_dou = driver.find_element(By.XPATH, '//*[@id="q1"]/div/span[2]').text

    python_dev_salary_max_dou = driver.find_element(By.XPATH, '//*[@id="q3"]/div/span[2]').text

except Exception as ex:
    print(ex)

# ----------------------------------------------Creating Databases---------------------------------------#

try:

    db_qa_dou = sqlite3.connect("db/salary_qa_djinni_database.db")
    c = db_qa_dou.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS salary_qa_djinni (
            id INTEGER PRIMARY KEY,
            salary_start_qa INTEGER,
            salary_max_qa INTEGER,
            timestamp DATETIME
    )""")

    c.execute(f"INSERT INTO salary_qa_djinni(salary_start_qa, salary_max_qa, timestamp) VALUES(?, ?, ?)",
              (salary_start_qa_djinni_without_dollar, salary_max_qa_djinni_without_dollar, current_date))

    db_qa_dou.commit()

    db_py_dou = sqlite3.connect("db/salary_python_djinni_database.db")
    c = db_py_dou.cursor()
    c.execute(""" CREATE TABLE IF NOT EXISTS salary_python_djinni (
                id INTEGER PRIMARY KEY,
                salary_start_py INTEGER,
                salary_max_py INTEGER,
                timestamp DATETIME
    )
    """)
    c.execute(f"INSERT INTO salary_python_djinni(salary_start_py, salary_max_py, timestamp) VALUES(?, ?, ?)",
              (salary_start_python_djinni_without_dollar, salary_max_python_djinni_without_dollar, current_date))

    db_py_dou.commit()

    db_qa_dou = sqlite3.connect("db/salary_qa_dou_database.db")
    c = db_qa_dou.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS salary_qa_dou (
            id INTEGER PRIMARY KEY,
            salary_start_qa INTEGER,
            salary_max_qa INTEGER,
            timestamp DATETIME
    )""")

    c.execute(f"INSERT INTO salary_qa_dou(salary_start_qa, salary_max_qa, timestamp) VALUES(?, ?, ?)",
              (sal_start_qa_dou, sal_max_qa_dou, current_date))

    db_qa_dou.commit()

    db_py_dou = sqlite3.connect("db/salary_python_dou_database.db")
    c = db_py_dou.cursor()
    c.execute(""" CREATE TABLE IF NOT EXISTS salary_python_dou (
                id INTEGER PRIMARY KEY,
                salary_start_py INTEGER,
                salary_max_py INTEGER,
                timestamp DATETIME
    )
    """)

    c.execute(f"INSERT INTO salary_python_dou(salary_start_py, salary_max_py, timestamp) VALUES(?, ?, ?)",
              (python_dev_salary_start_dou, python_dev_salary_max_dou, current_date))

    db_py_dou.commit()

except Exception as ex:
    print(ex)

# --------------------------------------------FIND ALL ELEMENTS FROM DATABASE-------------------------------------#

with sqlite3.connect("db/salary_qa_djinni_database.db") as db_qa_dou:
    cursor = db_qa_dou.cursor()

    cursor.execute("SELECT salary_start_qa FROM salary_qa_djinni")
    request_qa_start_djinni = cursor.fetchone()
    msg_qa_start_djinni = request_qa_start_djinni[-1]

    cursor.execute("SELECT salary_max_qa FROM salary_qa_djinni")
    request_qa_max_djinni = cursor.fetchone()
    msg_qa_max_djinni = request_qa_max_djinni[-1]

with sqlite3.connect("db/salary_python_djinni_database.db") as db_py_djinni:
    cursor = db_py_djinni.cursor()

    cursor.execute("SELECT salary_start_py FROM salary_python_djinni")
    request_py_start_djinni = cursor.fetchone()
    msg_py_start_djinni = request_py_start_djinni[-1]

    cursor.execute("SELECT salary_max_py FROM salary_python_djinni")
    request_py_max_djinni = cursor.fetchone()
    msg_py_max_djinni = request_py_max_djinni[-1]

with sqlite3.connect("db/salary_qa_dou_database.db") as db_qa_dou:
    cursor = db_qa_dou.cursor()

    cursor.execute("SELECT salary_start_qa FROM salary_qa_dou")
    request_qa_start_dou = cursor.fetchone()
    msg_qa_start_dou = request_qa_start_dou[-1]

    cursor.execute("SELECT salary_max_qa FROM salary_qa_dou")
    request_qa_max_dou = cursor.fetchone()
    msg_qa_max_dou = request_qa_max_dou[-1]

with sqlite3.connect("db/salary_python_dou_database.db") as db_py_dou:
    cursor = db_py_dou.cursor()

    cursor.execute("SELECT salary_start_py FROM salary_python_dou")
    request_py_start_dou = cursor.fetchone()
    msg_py_start_dou = request_py_start_dou[-1]

    cursor.execute("SELECT salary_max_py FROM salary_python_dou")
    request_py_max_dou = cursor.fetchone()
    msg_py_max_dou = request_py_max_dou[-1]

# # #-------------------------------Create MSG Elements--------------------------------------------------#

SUBJECT = f"Summary of the week(QA Manual / Python Dev)\n\n"

body_job_info = f"Job Prepositions: {job_amount_djinni_statistic_for_qa}"
body_responses_info = f"Responses: {responses_amount_djinni_for_qa}"
body_candidates_info = f"Candidates: {candidates_amount_djinni_qa}"

salary_for_qa_djinni = f"General salary statistics for QA(Djinni): ${msg_qa_start_djinni} -- {msg_qa_max_djinni}"
salary_for_qa_dou = f"General salary statistics for QA(Dou): ${msg_qa_start_dou} -- ${msg_qa_max_dou}"

summary_salary_python_dev_dou = (f"General salary statistics for Python Dev(Dou):"
                                 f" ${msg_py_start_dou} -- ${msg_py_max_dou}")
summary_salary_python_dev_djinni = f"General salary statistics for Python Dev(Djinni): ${msg_py_start_djinni} -- ${msg_py_max_djinni}"

with open("images_result_and_motivation_card/image.jpg", "rb") as image_file:
    image_data = image_file.read()
    image_part = MIMEImage(image_data, name="image.jpg")

# ---------------------------------------------SEND EMAIL ON MONDAYS-------------------------------------#

if weekday == 1:

    message = MIMEMultipart()
    message["From"] = MY_EMAIL
    message["To"] = MY_EMAIL
    message["Subject"] = SUBJECT
    message.attach(image_part)

    # -------------------------------------------------HTML----------------------------------------#

    html_content = f"""
    <html>
    <head>
    
    </head>
    <body style="font-family: Georgia, serif;">
         <p>{body_job_info}</p>
         <p>{body_responses_info}</p>
         <p>{body_candidates_info}</p>
         <p>{salary_for_qa_dou}<br>{salary_for_qa_djinni}</p>
         <p>-------------------------------------------------------------------------------</p>
         <p>{summary_salary_python_dev_dou}<br>{summary_salary_python_dev_djinni}</p>
         <p><a href="https://www.instagram.com/dima_kohanskyi/">&#10071;My Contacts&#10071;</a></p>
         <p><a href="https://github.com/dimakohanskyi/Djini-Selenium">&#10069;Git-Hub&#10069;</a></p>
         <p><a href="https://t.me/dimakohanskyi">&#10071;Telegram Python&#10071;</p>
     </body>
    </html>
    """
    # ----------------------------------------------------------------------------------------------------#

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
