import logging
from flask import Flask, request, cli
import requests
from datetime import datetime, timedelta

# Вимикаємо системні логи Flask для чистоти консолі
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
cli.show_server_banner = lambda *x: None

app = Flask(__name__)


# Створюємо маршрут для отримання динамічного курсу
@app.route("/currency")
def get_currency_custom():
    # Отримуємо параметр з URL
    param = request.args.get('param')
    base_url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json"

    # Фіксуємо поточну системну дату
    current_date = datetime.now()
    day_label = ""
    target_url = base_url

    if param == 'today':
        # Використовую стандартний URL (НБУ дає курс на завтра 19.11, якщо вже вечір)
        day_label = "сьогодні"

    elif param == 'yesterday':
        # Віднімаємо 1 день від поточної дати
        yesterday_date = current_date - timedelta(days=1)
        # Формуємо дату "вчора" (18.11) і додаємо її в URL запиту
        date_str = yesterday_date.strftime("%Y%m%d")
        target_url = f"{base_url}&date={date_str}"
        day_label = "вчора"
    else:
        return "Error", 400

    try:
        # Виконуємо запит до API НБУ
        response = requests.get(target_url)
        data = response.json()

        if data:
            rate = data[0]['rate']
            ex_date = data[0]['exchangedate']
            # Формуємо відповідь згідно з шаблоном
            return f"Отримані дані на {day_label} {ex_date}, та курс {rate}"
        else:
            return "Дані не знайдено", 404
    except Exception as e:
        return f"Error: {e}", 500


if __name__ == '__main__':
    # Виводимо тільки необхідні посилання для перевірки
    print("Курс на сьогодні (19.11): http://127.0.0.1:8000/currency?param=today")
    print("Курс на вчора (18.11):    http://127.0.0.1:8000/currency?param=yesterday")
    # Запускаємо сервер
    app.run(port=8000)