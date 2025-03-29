import asyncio
import configparser
from telegram import Bot
from decimal import Decimal, InvalidOperation


# Функция для загрузки конфигурации из INI файла
def load_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config['DEFAULT']


def division(a, b) -> str | None:
    "Функция выполняет операцию деления."
    try:

        result = a / b

    except ZeroDivisionError:
        message = "Ошибка: Деление на ноль!"
        print(message)
        return message

    except Exception as error:
        message = f"Ошибка: {error}"
        print(message)
        return message
    else:
        print(f"Результат деления {a} / {b} = {result}")


# Асинхронная функция для отправки сообщения
async def bot_send_message(message):
    await bot.send_message(chat_id=CHAT_ID, text=message)


async def main():
    print("Для выхода введите 'exit'")
    while True:
        try:
            number1 = input("Введите первое число: ")
            if number1.lower() == "exit":
                print("Пока!")
                break
            number1 = Decimal(number1)

            number2 = input("Введите второе число: ")
            if number2.lower() == "exit":
                print("Пока!")
                break
            number2 = Decimal(number2)

        except InvalidOperation:
            message = "Ошибка: Строка содержит недопустимые символы!"
            print(message)
            await bot_send_message(message)
        else:
            message = division(number1, number2)
            if message is not None:
                await bot_send_message(message)


# Загрузка конфигурации
config = load_config('config.ini')
# Ваш токен бота
TOKEN = config['TOKEN']  # Замените на ваш токен
# Ваш chat_id
CHAT_ID = config['CHAT_ID']  # Замените на ваш chat_id

bot = Bot(token=TOKEN)

if __name__ == '__main__':
    asyncio.run(main())
