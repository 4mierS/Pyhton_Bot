from datetime import date, datetime
import random


def get_date() -> str:
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    return d1


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == "hello":
        return "Hey there!"

    if p_message == "roll":
        return str(random.randint(1, 6))

    if p_message == "!help":
        return "`This is a help message that you can modify.`"
    if p_message == "How are you?":
        return "I am fine, thank you."
    if p_message == "What is your name?":
        return "My name is Amier."
    if p_message == "What is your favorite color?":
        return "My favorite color is red."
    if p_message == "What is your favorite food?":
        return "I love the arabic cuisine."
    if p_message == "How old are you":
        return "I am " + str(calculate_age(date(2001, 6, 16))) + " years old."
    if p_message == "date":
        return get_date()
    if p_message == "Random number":
        return str(random.randint(1, 1000))
    if p_message == "time":
        return datetime.now().strftime("%H:%M:%S")
    if p_message == "help":
        return "`This is a help message`"

    #  return 'Yeah, I don\'t know. Try typing "!help".'
