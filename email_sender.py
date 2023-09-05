import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import os
from datetime import datetime
from find_all_elements import find_all_elements_for_qa_djinni
from find_all_data_from_database import (find_data_for_qa_djinni, find_data_for_qa_dou,
                                         find_data_for_py_djinni, find_data_for_py_dou)

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
PASSWORD_FO_LOG_IN = os.getenv("PASSWORD_FO_LOG_IN")


def email_message_sender():

    current_date = datetime.now().date()
    weekday = current_date.weekday()

    msg_qa_start_djinni = find_data_for_qa_djinni()[0]
    msg_qa_max_djinni = find_data_for_qa_djinni()[1]

    msg_qa_start_dou = find_data_for_qa_dou()[0]
    msg_qa_max_dou = find_data_for_qa_dou()[1]

    msg_py_start_djinni = find_data_for_py_djinni()[0]
    msg_py_max_djinni = find_data_for_py_djinni()[1]

    msg_py_start_dou = find_data_for_py_dou()[0]
    msg_py_max_dou = find_data_for_py_dou()[1]

    job_amount_djinni_statistic_for_qa = responses_amount_djinni_for_qa = candidates_amount_djinni_qa = find_all_elements_for_qa_djinni()

    SUBJECT = f"Summary of the week(QA Manual / Python Dev)\n\n"

    body_job_info = f"Job Prepositions: {job_amount_djinni_statistic_for_qa}"
    body_responses_info = f"Responses: {responses_amount_djinni_for_qa}"
    body_candidates_info = f"Candidates: {candidates_amount_djinni_qa}"

    salary_for_qa_djinni = f"General salary statistics for QA(Djinni): ${msg_qa_start_djinni} -- {msg_qa_max_djinni}"
    salary_for_qa_dou = f"General salary statistics for QA(Dou): ${msg_qa_start_dou} -- ${msg_qa_max_dou}"

    summary_salary_python_dev_dou = (f"General salary statistics for Python Dev(Dou):"
                                     f" ${msg_py_start_dou} -- ${msg_py_max_dou}")
    summary_salary_python_dev_djinni = (f"General salary statistics for Python Dev(Djinni):"
                                        f" ${msg_py_start_djinni} -- ${msg_py_max_djinni}")

    with open("img/image.jpg", "rb") as image_file:
        image_data = image_file.read()
        image_part = MIMEImage(image_data, name="image.jpg")

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
