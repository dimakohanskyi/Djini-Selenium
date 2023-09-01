from models import create_qa_djinni_database, create_qa_dou_database, create_py_dou_database, create_py_djinni_database
from load_data_fo_db import (load_data_for_qa_djinni_db, load_data_for_qa_dou,
                             load_data_for_py_djinni, load_data_for_py_dou)
from email_sender import email_message_sender


create_qa_djinni_database()
create_qa_dou_database()
create_py_djinni_database()
create_py_dou_database()

load_data_for_qa_djinni_db()
load_data_for_qa_dou()
load_data_for_py_djinni()
load_data_for_py_dou()

email_message_sender()











