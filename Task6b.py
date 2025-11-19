import logging
import sqlite3
from flask import Flask, request, cli
from datetime import datetime

# Вимикаємо системні повідомлення для чистого виводу
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
cli.show_server_banner = lambda *x: None

app = Flask(__name__)

DB_NAME = "my_database.db"


# Створюємо таблицю в базі даних, якщо вона не існує
def init_db():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS messages
                       (
                           id
                           INTEGER
                           PRIMARY
                           KEY
                           AUTOINCREMENT,
                           content
                           TEXT,
                           created_at
                           TEXT
                       )
                       ''')
        conn.commit()
        conn.close()
    except Exception:
        pass


init_db()


# Створюємо HTML форму для введення даних
@app.route("/", methods=['GET'])
def index():
    return '''
    <html>
        <head><meta charset="utf-8"><title>Завдання 6b</title></head>
        <body>
            <h2>Збереження в SQLite</h2>
            <form action="/save-db" method="post">
                <label>Введіть повідомлення:</label><br>
                <input type="text" name="text_data" style="width: 300px;" required
                       oninvalid="this.setCustomValidity('Будь ласка, заповніть це поле')"
                       oninput="this.setCustomValidity('')">
                <br><br>
                <input type="submit" value="Зберегти в БД">
            </form>
        </body>
    </html>
    '''


# Обробляємо POST запит і виконуємо запис в БД
@app.route("/save-db", methods=['POST'])
def save_to_db():
    if 'text_data' in request.form:
        data = request.form['text_data']
    else:
        data = request.get_data(as_text=True)

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        # Виконуємо SQL запит на вставку даних
        cursor.execute("INSERT INTO messages (content, created_at) VALUES (?, ?)", (data, current_time))
        conn.commit()
        conn.close()

        return f'''
            <h3>Успішно збережено в БД!</h3>
            <p>Текст: <b>{data}</b></p>
            <p>Час: {current_time}</p>
            <a href="/">Назад</a>
        '''
    except Exception as e:
        return f"Помилка: {e}", 500


if __name__ == '__main__':
    # Виводимо фінальне посилання в консоль
    print("Перейдіть за посиланням: http://127.0.0.1:8000/")
    # Запускаємо сервер
    app.run(port=8000)