import logging
from flask import Flask, request, cli

# Вимикаємо технічні повідомлення сервера
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
cli.show_server_banner = lambda *x: None

app = Flask(__name__)

# Створюємо маршрут /currency для отримання параметрів
@app.route("/currency")
def get_currency_static():
    # Отримуємо параметр 'key' із запиту
    key = request.args.get('key')
    # Повертаємо статичне значення курсу
    return "USD 41,5"

if __name__ == '__main__':
    # Виводимо готове посилання з параметрами
    print("Для перевірки перейдіть за посиланням: http://127.0.0.1:8000/currency?key=value")
    # Запускаємо сервер
    app.run(port=8000)