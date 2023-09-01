from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from load_data_fo_db import Salary_Qa_Djinni, Salary_Qa_Dou, Salary_Python_Dou, Salary_Python_Djinni


def find_data_for_qa_djinni():
     engine = create_engine("sqlite:///db/salary_qa_djinni.db")

     Session = sessionmaker(bind=engine)
     session = Session()

     last_salary_qa_djinni = session.query(Salary_Qa_Djinni).order_by(Salary_Qa_Djinni.timestamp.desc()).first()

     session.close()

     return (last_salary_qa_djinni.salary_start_qa,
             last_salary_qa_djinni.salary_max_qa)


def find_data_for_qa_dou():

    engine = create_engine("sqlite:///db/salary_qa_dou.db")

    Session = sessionmaker(bind=engine)
    session = Session()

    last_salary_start_qa_dou = session.query(Salary_Qa_Dou).order_by(Salary_Qa_Dou.salary_start_dou.desc()).first()
    last_salary_max_qa_dou = session.query(Salary_Qa_Dou).order_by(Salary_Qa_Dou.salary_max_qa_dou.desc()).first()

    session.close()

    return (last_salary_start_qa_dou.salary_start_dou,
            last_salary_max_qa_dou.salary_max_qa_dou)


def find_data_for_py_djinni():

    engine = create_engine("sqlite:///db/salary_py_djinni.db")

    Session = sessionmaker(bind=engine)
    session = Session()

    last_salary_py_djinni = session.query(Salary_Python_Djinni).order_by(Salary_Python_Djinni.timestamp.desc()).first()

    return (last_salary_py_djinni.salary_start_py,
            last_salary_py_djinni.salary_max_py)


def find_data_for_py_dou():

    engine = create_engine("sqlite:///db/salary_py_dou.db")

    Session = sessionmaker(bind=engine)
    session = Session()

    last_salary_py_dou = session.query(Salary_Python_Dou).order_by(Salary_Python_Dou.timestamp.desc()).first()

    return (last_salary_py_dou.salary_start_py,
            last_salary_py_dou.salary_max_py)


