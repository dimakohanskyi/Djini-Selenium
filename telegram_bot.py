from aiogram import Bot, Dispatcher, executor, types
import logging
import os
from dotenv import load_dotenv
from find_all_data_from_database import (find_data_for_qa_djinni, find_data_for_qa_dou,
                                         find_data_for_py_djinni, find_data_for_py_dou)


load_dotenv()
TOKEN = os.getenv("MY_API_TOKEN_TELEGRAM")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


msg_qa_start_djinni = find_data_for_qa_djinni()[0]
msg_qa_max_djinni = find_data_for_qa_djinni()[1]

msg_qa_start_dou = find_data_for_qa_dou()[0]
msg_qa_max_dou = find_data_for_qa_dou()[1]

msg_py_start_djinni = find_data_for_py_djinni()[0]
msg_py_max_djinni = find_data_for_py_djinni()[1]

msg_py_start_dou = find_data_for_py_dou()[0]
msg_py_max_dou = find_data_for_py_dou()[1]


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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
