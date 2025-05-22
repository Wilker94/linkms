from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rich')
def rich_page():
    return render_template('rich.html')  # ou "return 'lalala'" se ainda não criou o rich.html

if __name__ == '__main__':
    app.run(debug=True)
