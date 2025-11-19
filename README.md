LB-2 Робота з HTTP протоколом, запитами та публічними API 
Інструменти
Підготовлена та встановлена IDE для розробки на python, наприклад pycharm. 
Postman.
Один з web-фреймворків python (наприклад, flask, bottle) 
Завдання
1. [Easy] Встановити python веб фреймворк та запустити веб сервер на порту 8000. Наприклад:


a. Flask
pip install Flask (встановлення фреймворку)

from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return
   
if __name__ == '__main__':
    app.run(port=8000)
b. Bottle
pip install bottle (встановлення фреймворку)

from bottle import route, run
@route('/')
def hello():
    return

if __name__ == '__main__':
    run(host='localhost', port=8000)

2. [Easy] Написати просту обробку запиту метода GET сервером. На запит повертати строку “Hello World!” 
3. [Easy-Medium] Написати просту обробку запиту метода GET сервером зі шляхом та параметрами в URL, наприклад http://127.0.0.1:8000/currency?today&key=value. Повертати статичне значення курса валют, наприклад “USD - 41,5”.  Для flask отримати параметри запиту за допомогою request.args.get(), для bottle -  request.query()   
4. [Medium] Обробка заголовків запиту. В залежності від значення параметру заголовку “Content-Type” (application/json чи application/xml) повертати json чи xml документ. У разі відсутності - повертати звичайний текст. Для flask отримати заголовки за допомогою request.headers.get, для bottle - request.get_header[]. 

5. [Medium-Hard]  Написати обробку запиту метода GET сервером зі шляхом та параметрами в URL http://127.0.0.1:800/currency?<param>, де допустимі значення param:
today - курс USD, актуальний на сьогодні
yesterday -  курс USD, актуальний на попередній день
Курси валют запитувати динамічно у програмі з офіційного сайту НБУ, згідно API специфікації - https://bank.gov.ua/admin_uploads/article/Instr_API_KURS_VAL_data.pdf 
6. [Hard] Написати обробку методу POST веб-сервером. У тілі повідомлення передавати текстові дані. Зберегти ці дані на сервері:

 a. [Easy] у файл

 b. [Hard2] у sqlite3 базі даних

Посилання
Flask tutorial - https://flask.palletsprojects.com/en/3.0.x/quickstart/ 
Bottle tutorial - https://bottlepy.org/docs/dev/tutorial.html 
