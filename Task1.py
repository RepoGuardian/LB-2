import logging
from flask import Flask, cli

# Вимикаємо зайві системні повідомлення бібліотеки, щоб очистити консоль
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Вимикаємо стандартний банер Flask при запуску
cli.show_server_banner = lambda *x: None

# Ініціалізуємо Flask додаток
app = Flask(__name__)

# Створюємо маршрут для головної сторінки та виводимо повідомлення
@app.route("/")
def task_one_message():
    return "Hello from Flask on port 8000!"

if __name__ == '__main__':
    # Виводимо в консоль посилання для перевірки
    print("Для перевірки перейдіть за посиланням: http://127.0.0.1:8000")
    # Запускаємо веб-сервер на порту 8000
    app.run(port=8000)