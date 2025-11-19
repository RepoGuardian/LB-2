import logging
import sqlite3
from flask import Flask, request, cli
from datetime import datetime

# Вимикаємо зайві написи в консолі для чистоти виводу
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
cli.show_server_banner = lambda *x: None

# Ініціалізуємо Flask додаток
app = Flask(__name__)

FILE_NAME = "data_log.txt"
DB_NAME = "data.db"


# Ініціалізуємо базу даних (створюємо таблицю при старті, якщо її немає)
def init_db():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS records
                       (
                           id
                           INTEGER
                           PRIMARY
                           KEY
                           AUTOINCREMENT,
                           content
                           TEXT,
                           timestamp
                           TEXT
                       )
                       ''')
        conn.commit()
        conn.close()
    except Exception:
        pass


init_db()


# Створюємо сторінку з формою для відправки POST запиту
@app.route("/", methods=['GET'])
def index():
    return '''
    <html>
        <head><meta charset="utf-8"><title>Завдання 6</title></head>
        <body>
            <h2>Відправка POST запиту</h2>
            <form action="/save-data" method="post">
                <label>Введіть текст для збереження:</label><br>
                <input type="text" name="text_data" style="width: 300px;" required
                       oninvalid="this.setCustomValidity('Будь ласка, заповніть це поле')"
                       oninput="this.setCustomValidity('')">
                <br><br>
                <input type="submit" value="Відправити POST запит">
            </form>
        </body>
    </html>
    '''


# Обробляємо отриманий POST запит і зберігаємо дані
@app.route("/save-data", methods=['POST'])
def save_data():
    if 'text_data' in request.form:
        data = request.form['text_data']
    else:
        data = request.get_data(as_text=True)

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Зберігаємо дані у текстовий файл
    try:
        with open(FILE_NAME, "a", encoding="utf-8") as f:
            f.write(f"[{current_time}] {data}\n")
    except Exception as e:
        return f"Помилка файлу: {e}", 500

    # Зберігаємо дані у базу даних SQLite
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO records (content, timestamp) VALUES (?, ?)", (data, current_time))
        conn.commit()
        conn.close()
    except Exception as e:
        return f"Помилка БД: {e}", 500

    return f'''
        <h3>Успіх!</h3>
        <p>Дані збережено: <b>{data}</b></p>
        <ul>
            <li>Записано у файл: {FILE_NAME}</li>
            <li>Записано у базу даних: {DB_NAME}</li>
        </ul>
        <br>
        <a href="/">Повернутися назад</a>
    '''


if __name__ == '__main__':
    # Виводимо посилання на форму
    print("Для перевірки перейдіть за посиланням: http://127.0.0.1:8000/")
    # Запускаємо сервер
    app.run(port=8000)