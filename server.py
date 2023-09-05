from flask import Flask, render_template
from find_all_data_from_database import (find_data_for_qa_djinni, find_data_for_qa_dou,
                                         find_data_for_py_djinni, find_data_for_py_dou)
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


app = Flask(__name__)


@app.route('/')
def home_page():
    data_for_web_qa = find_data_for_qa_djinni()[0], find_data_for_qa_djinni()[1]
    data_for_web_qa_d = find_data_for_qa_dou()[0], find_data_for_qa_dou()[1]
    data_for_web_py_djinni = find_data_for_py_djinni()[0], find_data_for_py_djinni()[1]
    data_for_web_py_dou = find_data_for_py_dou()[0], find_data_for_py_dou()[1]
    return render_template('index.html',
                           data_for_web_qa=data_for_web_qa, data_for_web_qa_d=data_for_web_qa_d,
                           data_for_web_py_djinni=data_for_web_py_djinni, data_for_web_py_dou=data_for_web_py_dou)


@app.route('/qasal')
def qasal_page():
    data_for_web_qa = find_data_for_qa_djinni()[0], find_data_for_qa_djinni()[1]
    data_for_web_qa_d = find_data_for_qa_dou()[0], find_data_for_qa_dou()[1]
    return render_template('qa_sal.html', data_for_web_qa=data_for_web_qa,
                           data_for_web_qa_d=data_for_web_qa_d)


@app.route('/pysal')
def pysal_page():
    data_for_web_py_djinni = find_data_for_py_djinni()[0], find_data_for_py_djinni()[1]
    data_for_web_py_dou = find_data_for_py_dou()[0], find_data_for_py_dou()[1]
    return render_template('python_sal.html', data_for_web_py=data_for_web_py_djinni,
                           data_for_web_py_dou=data_for_web_py_dou)


@app.route('/about')
def about_page():
    return render_template('about.html')


if __name__ == ("__main__"):
    app.run(debug=True)
