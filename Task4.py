import logging
from flask import Flask, request, jsonify, Response, cli

# Вимикаємо зайві логи
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
cli.show_server_banner = lambda *x: None

app = Flask(__name__)

# Створюємо обробник для перевірки заголовків Content-Type
@app.route('/content-type')
def content_type_handler():
    # Отримуємо значення заголовка із запиту
    c_type = request.headers.get('Content-Type')

    # Перевіряємо тип контенту і повертаємо відповідний формат
    if c_type == 'application/json':
        return jsonify({"message": "Це JSON відповідь"})
    elif c_type == 'application/xml':
        xml_response = "<message>Це XML відповідь</message>"
        return Response(xml_response, mimetype='application/xml')
    else:
        return "Це звичайний текст (Content-Type не задано або інший)"

if __name__ == '__main__':
    # Виводимо посилання для перевірки
    print("Для перевірки перейдіть за посиланням: http://127.0.0.1:8000/content-type")
    # Запускаємо сервер
    app.run(port=8000)