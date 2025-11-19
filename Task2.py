import logging
from flask import Flask, cli

# Вимикаємо системні логи для чистоти виводу
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
cli.show_server_banner = lambda *x: None

# Ініціалізуємо додаток
app = Flask(__name__)

# Створюємо обробку GET запиту на кореневу сторінку
@app.route('/')
def hello_world():
    # Повертаємо рядок "Hello World!"
    return "Hello World!"

if __name__ == '__main__':
    # Виводимо інструкцію з посиланням
    print("Для перевірки перейдіть за посиланням: http://127.0.0.1:8000")
    # Запускаємо сервер
    app.run(port=8000)