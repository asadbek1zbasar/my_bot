import telebot
import requests


"""
import sqlite3
connection = sqlite3.connect('data_users', check_same_thread=False)
cursor = connection.cursor()"""


# Your bot token from BotFather
API_TOKEN = '7349597940:AAFr0T76FalIE1-ngu8dNqkIzI-jyAMSLAs'
# OpenWeatherMap API key
bot = telebot.TeleBot(API_TOKEN)


def get_weather(city):
    key = '54d11bec31301dfbb08b0e359a5dbde5'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={key}"
    try:
        info = requests.get(url).json()
        if info['cod'] == 200:
            weather = info['weather'][0]['description']
            temp = info['main']['temp']
            temp_feeling = info['main']['feels_like']
            return f'In {city}, weather is {weather}, temperature {temp}C feels like {temp_feeling}C'
        else:
            return 'please send real city name or try again'
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return f"Error fetching weather data: {e}"


"""def get_info(message):
    name = message.chat.first_name
    id = message.chat.id
    user_name = message.chat.username

    cursor.execute("INSERT INTO user_info (name, user_name, chat_id) VALUES (?, ?, ?)", (name, user_name, id))
    connection.commit()"""



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hello! Send me a city name to get the weather information.")


@bot.message_handler(func=lambda message: True)
def send_weather_info(message):
    bot.reply_to(message, get_weather(message.text) )

bot.infinity_polling()