import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from find_all_elements import (find_all_elements_for_qa_dou, find_all_elements_for_py_djinni,
                               find_all_elements_for_py_dou, find_all_elements_for_qa_djinni)
from datetime import datetime
from models import Salary_Qa_Djinni, Salary_Qa_Dou, Salary_Python_Dou, Salary_Python_Djinni


Base = sqlalchemy.orm.declarative_base()


def load_data_for_qa_djinni_db():
    engine = create_engine("sqlite:///db/salary_qa_djinni.db", echo=True)


    Session = sessionmaker(bind=engine)
    session = Session()

    current_date = datetime.now().date()

    (job_amount_djinni_statistic_for_qa,
    responses_amount_djinni_for_qa,
    candidates_amount_djinni_qa,
    salary_start_qa_djinni_without_dollar,
    salary_max_qa_djinni_without_dollar) = find_all_elements_for_qa_djinni()


    adding_data_for_qa_djinni = Salary_Qa_Djinni(
        job_amount_djinni_statistic_for_qa,
        responses_amount_djinni_for_qa,
        candidates_amount_djinni_qa,
        salary_start_qa_djinni_without_dollar,
        salary_max_qa_djinni_without_dollar,
        current_date
    )

    session.add(adding_data_for_qa_djinni)
    session.commit()
    session.close()


def load_data_for_qa_dou():

    current_date = datetime.now().date()

    (sal_start_qa_dou, sal_max_qa_dou) = find_all_elements_for_qa_dou()

    engine = create_engine("sqlite:///db/salary_qa_dou.db", echo=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    adding_data_for_qa_dou = Salary_Qa_Dou(sal_start_qa_dou, sal_max_qa_dou, current_date)
    session.add(adding_data_for_qa_dou)
    session.commit()
    session.close()


def load_data_for_py_djinni():

    engine = create_engine("sqlite:///db/salary_py_djinni.db", echo=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    current_date = datetime.now().date()

    (salary_start_python_djinni_without_dollar,
     salary_max_python_djinni_without_dollar) = find_all_elements_for_py_djinni()

    adding_data_for_python_djinni = Salary_Python_Djinni(
        salary_start_python_djinni_without_dollar,
        salary_max_python_djinni_without_dollar,
        current_date)


    session.add(adding_data_for_python_djinni)
    session.commit()
    session.close()


def load_data_for_py_dou():

    current_date = datetime.now().date()

    (python_dev_salary_start_dou, python_dev_salary_max_dou) = find_all_elements_for_py_dou()

    engine = create_engine("sqlite:///db/salary_py_dou.db", echo=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    adding_data_for_python_dou = Salary_Python_Dou(
        python_dev_salary_start_dou,
        python_dev_salary_max_dou,
        current_date
    )

    session.add(adding_data_for_python_dou)
    session.commit()
    session.close()






