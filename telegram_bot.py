from aiogram import Bot, Dispatcher, executor, types
import logging
import os
from dotenv import load_dotenv
import sqlite3

load_dotenv()
TOKEN = os.getenv("MY_API_TOKEN_TELEGRAM")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Hi!📌\nYou can discover salary statistics for QA Engineers and Python Developers by clicking:🔻🔻🔻\n"
        "\n📈/salary_qa_djinni📈 \n📈/salary_qa_dou📈"
        "\n📈/salary_py_djinni📈 \n📈/salary_py_dou📈")


@dp.message_handler(commands=['salary_qa_djinni'])
async def salary_qa_djinni(message: types.Message):
    await message.reply(
        f"General salary statistics for QA(DJINNI)💸: 💰{msg_qa_start_djinni} -- 💰{msg_qa_max_djinni}")


@dp.message_handler(commands=['salary_qa_dou'])
async def salary_qa_dou(message: types.Message):
    await message.reply(
        f"General salary statistics for QA(DOU)💸: 💰{msg_qa_start_dou} -- 💰{msg_qa_max_dou}")


@dp.message_handler(commands=['salary_py_djinni'])
async def salary_py_djinni(message: types.Message):
    await message.reply(
        f"General salary statistics for Python Developer(DJINNI)💸: 💰{msg_py_start_djinni} -- 💰{msg_py_max_djinni}"
    )


@dp.message_handler(commands=['salary_py_dou'])
async def salary_py_dou(message: types.Message):
    await message.reply(
        f"General salary statistics for Python Developer(DOU)💸: 💰{msg_py_start_dou} -- 💰{msg_py_max_dou}"
    )


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("The list of my commands🆘🆘🆘: \n/start \n/help \n ❕/salary_qa_djinni❕ \n ❕/salary_qa_dou❕"
                        " \n ❕/salary_py_djinni❕ \n ❕/salary_py_dou❕")


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

    cursor.execute("SELECT salary_start_py FROM salary_python_dou order by timestamp DESC limit 1")
    request_py_start_dou = cursor.fetchone()
    msg_py_start_dou = request_py_start_dou[0]

    cursor.execute("SELECT salary_max_py FROM salary_python_dou")
    request_py_max_dou = cursor.fetchone()
    msg_py_max_dou = request_py_max_dou[-1]


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
