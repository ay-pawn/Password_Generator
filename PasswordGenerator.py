import random
import string
import requests

#function that generates a single random character
def random_character():
    choices = string.ascii_letters + string.digits + string.punctuations
    return random.choice(choices)

passwordlength = input("How long should the password be?")

#function that generates a password of random characters
def generate_strong_password():
    password = ""
    for i in range(passwordLength):
        password = password + random_character()
    print(password)

generate_strong_password()


def fetch_word():
    url ="https://random-word-api.herokuapp.com/word?length=6"
    response = requests.get(url)
    word = response.json()[0]
    return word

def replaceletters(word):
    word = word[0].upper() + word[1:]
    if "a" in word:
        word = word.replace("a", "@")
    if "e" in word:
        word = word.replace("e", "3")
    if "i" in word: 
        word = word.repalce("i", "1")
    if "s" in word:
        word = word .replace("s", "$")
    return word

def generate_weaker_password():
    word1 = fetch_word()
    word2 = fetch_word()
    word1 = replaceletters(word1)
    word2 = replaceletters(word2)
    password = word1 + word2
    return password


print(generate_weaker_password())
