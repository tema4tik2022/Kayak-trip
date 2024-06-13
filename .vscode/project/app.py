from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Обробка даних форми тут (наприклад, збереження в БД або відправка на email)
    return 'Дякуємо за ваше повідомлення!'

if __name__ == '__main__':
    app.run(debug=True)
