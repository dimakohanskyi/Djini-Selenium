from create_database import (create_qa_dou_database, create_qa_djinni_database,
                             create_py_dou_database, create_py_djinni_database)

from create_database import (load_data_for_qa_dou, load_data_for_qa_djinni,
                             load_data_for_py_djinni, load_data_for_py_dou)


create_qa_djinni_database()
load_data_for_qa_djinni()

create_qa_dou_database()
load_data_for_qa_dou()

create_py_djinni_database()
load_data_for_py_djinni()

create_py_dou_database()
load_data_for_py_dou()







