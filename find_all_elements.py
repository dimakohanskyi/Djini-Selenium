import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from datetime import datetime


load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD_FO_LOG_IN = os.getenv("PASSWORD_FO_LOG_IN")

URL_DJINNI = "https://djinni.co/my/dashboard/"
URL_DOU = "https://dou.ua/"

current_date = datetime.now().date()
weekday = current_date.weekday()

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)


def find_all_elements_for_qa_djinni():
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

        return (salary_start_qa_djinni_without_dollar,
                salary_max_qa_djinni_without_dollar,
                job_amount_djinni_statistic_for_qa,
                responses_amount_djinni_for_qa,
                candidates_amount_djinni_qa)

    except Exception as ex:
        print(ex)


def find_all_elements_for_py_djinni():
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

        return (salary_start_python_djinni_without_dollar,
                salary_max_python_djinni_without_dollar)

    except Exception as ex:
        print(ex)


def find_all_elements_for_qa_dou():
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

        return (sal_start_qa_dou,
                sal_max_qa_dou)

    except Exception as ex:
        print(ex)


def find_all_elements_for_py_dou():
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

        return (python_dev_salary_start_dou,
                python_dev_salary_max_dou)

    except Exception as ex:
        print(ex)




