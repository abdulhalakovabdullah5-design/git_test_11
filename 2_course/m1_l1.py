import requests

 """
404 - Страница не найдена!
403 - Нет доступа
401 - Авторизация
500 - Ошибка сервера
502 -       
200 - Отлично
201 - Успешно сделано
"""
#
# url = "https://bmass.at"
# response = requests.get(url)
# print(response.status_code)
#
# if response.status_code == 200:
#     print(response.text)

url = "https://httpbin.org/post"

data = {
    "foo": "bar",
    "login": "Movsar",
    "password": 123121
}
response = requests.post(url, data=data)
print(response.text)
