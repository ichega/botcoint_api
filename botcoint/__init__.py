import requests
import json
import time
import addict

BASE_URL = "http://botcoint.ru"

class BotcointAPI:
    def __init__(self):
        self.access_token = ""

    def auth(self, access_token):
        """
        Метод авторизацтии, необходимо указать токен доступа
        :param access_token:
        :return:
        """
        self.access_token = access_token
        self.cookies = {'access_key': access_token}

    def get_unchecked_messages(self):
        """
        Функция возвращает словарь со списком непрочитанных сообщений, операция помечает сообщения прочитанными
        :return:
        """
        try:
            response = requests.get(BASE_URL+"/api/bots/unchecked_events", cookies=self.cookies)
            print('RESPONSE: ', response.text)
            data = json.loads(response.text)
            data = addict.Dict(data)
            # for d in data:
            #     d = addict.Dict(d)
            return data
        except Exception as e:
            return addict.Dict()


    def send_message(self, message):
        """
        Отправка сообщения
        :param message: сообщение
        :return:
        """
        r = requests.post(BASE_URL+"/api/bots/messages", cookies=self.cookies, data=message)