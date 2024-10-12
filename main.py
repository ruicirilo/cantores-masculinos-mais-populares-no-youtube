from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    # Lê o arquivo HTML na raiz do projeto
    with open('index.html', 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/scrape')
def scrape():
    url = "https://kworb.net/youtube/topvideos_male.html"
    response = requests.get(url)
    response.encoding = 'utf-8'  # Forçar a codificação para UTF-8
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontre a tabela
    table = soup.find('table')
    rows = table.find_all('tr')

    # Extraia os dados
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if cols:  # Verifique se a linha não está vazia
            data.append(cols)

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)















