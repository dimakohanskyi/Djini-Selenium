from find_all_elements import (find_all_elements_for_qa_djinni, find_all_elements_for_py_djinni,
                               find_all_elements_for_py_dou, find_all_elements_for_qa_dou)
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Salary_Qa_Djinni(Base):

    __tablename__ = "salary_qa_djinni"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    vacancies = Column("vacancies", Integer)
    responses = Column("responses", Integer)
    candidates = Column("candidates", Integer)
    salary_start_qa = Column("salary_start_qa", Integer)
    salary_max_qa = Column("salary_max_qa", Integer)
    timestamp = Column("timestamp", DateTime)

    def __init__(self, salary_start_qa, salary_max_qa, vacancies, responses, candidates, timestamp):
        self.vacancies = vacancies
        self.responses = responses
        self.candidates = candidates
        self.salary_start_qa = salary_start_qa
        self.salary_max_qa = salary_max_qa
        self.timestamp = timestamp


def create_qa_djinni_database():
    Base = declarative_base()
    engine = create_engine("sqlite:///db/salary_qa_djinni.db")
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()


def load_data_for_qa_djinni():


    Base = declarative_base()
    engine = create_engine("sqlite:///db/salary_qa_djinni.db")
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


class Salary_Qa_Dou(Base):

    __tablename__ = "salary_qa_dou"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    salary_start_qa = Column("salary_start_qa", Integer)
    salary_max_qa = Column("salary_max_qa", Integer)
    timestamp = Column("timestamp", DateTime)

    def __init__(self, salary_start_qa, salary_max_qa, timestamp):
        self.salary_start_qa = salary_start_qa
        self.salary_max_qa = salary_max_qa
        self.timestamp = timestamp


def create_qa_dou_database():
    engine = create_engine("sqlite:///db/salary_qa_dou.db")
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()


def load_data_for_qa_dou():

    current_date = datetime.now().date()

    (sal_start_qa_dou, sal_max_qa_dou) = find_all_elements_for_qa_dou()

    engine = create_engine("sqlite:///db/salary_qa_dou.db")
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    adding_data_for_qa_dou = Salary_Qa_Dou(sal_start_qa_dou, sal_max_qa_dou, current_date)
    session.add(adding_data_for_qa_dou)
    session.commit()


class Salary_Python_Djinni(Base):

    __tablename__ = "salary_python_djinni"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    salary_start_py = Column("salary_start_py", Integer)
    salary_max_py = Column("salary_max_py", Integer)
    timestamp = Column("timestamp", DateTime)

    def __init__(self, salary_start_py, salary_max_py, timestamp):
        self.salary_start_py = salary_start_py
        self.salary_max_py = salary_max_py
        self.timestamp = timestamp


def create_py_djinni_database():
    engine = create_engine("sqlite:///db/salary_py_djinni.db")
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()


def load_data_for_py_djinni():

    engine = create_engine("sqlite:///db/salary_py_djinni.db")
    Base.metadata.create_all(bind=engine)

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


class Salary_Python_Dou(Base):

    __tablename__ = "salary_py_dou"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    salary_start_py = Column("salary_start_py", Integer)
    salary_max_py = Column("salary_max_py", Integer)
    timestamp = Column("timestamp", DateTime)

    def __init__(self, salary_start_py, salary_max_py, timestamp):
        self.salary_start_py = salary_start_py
        self.salary_max_py = salary_max_py
        self.timestamp = timestamp


def create_py_dou_database():
    engine = create_engine("sqlite:///db/salary_py_dou.db")
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()


def load_data_for_py_dou():

    current_date = datetime.now().date()

    (python_dev_salary_start_dou, python_dev_salary_max_dou) = find_all_elements_for_py_dou()

    engine = create_engine("sqlite:///db/salary_py_dou.db")
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    adding_data_for_python_dou = Salary_Python_Dou(
        python_dev_salary_start_dou,
        python_dev_salary_max_dou,
        current_date
    )

    session.add(adding_data_for_python_dou)
    session.commit()
