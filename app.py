# This is a sample Python script.
import json
from flask import Flask, render_template
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from Publications import Publications

app = Flask(__name__)

def get_publications_data():
    publications = Publications()
    publications.fetch_publications_data()
    with open('data.json', 'r') as json_file:
        publications.data = json.load(json_file)
    return publications.data

def generate_word_cloud(titles):
    text = ' '.join(titles)
    wordcloud = WordCloud(width=800, height=400).generate(text)
    plt.figure(figsize=(15, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('static/word_cloud.png')

@app.route('/')
def index():
    data = get_publications_data()
    titles = [item['title'] for item in data]
    generate_word_cloud(titles)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(threaded=True)
