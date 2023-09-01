import sqlalchemy
from sqlalchemy import Column, Integer, DateTime, create_engine
from sqlalchemy.orm import sessionmaker


Base = sqlalchemy.orm.declarative_base()


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

    engine = create_engine("sqlite:///db/salary_qa_djinni.db")
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()


class Salary_Qa_Dou(Base):

    __tablename__ = "salary_qa_dou"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    salary_start_dou = Column("salary_start_qa_dou", Integer)
    salary_max_qa_dou = Column("salary_max_qa_dou", Integer)
    timestamp = Column("timestamp", DateTime)

    def __init__(self, salary_start_qa_dou, salary_max_qa_dou, timestamp):
        self.salary_start_qa_dou = salary_start_qa_dou
        self.salary_max_qa_dou = salary_max_qa_dou
        self.timestamp = timestamp


def create_qa_dou_database():

    engine = create_engine("sqlite:///db/salary_qa_dou.db")
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()


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




