from flask import Flask, render_template, request
import sqlite3
from SQL_scripts import* 
app = Flask(__name__)                             #? Створюємо веб–додаток Flask



@app.route("/")                                   #? Вказуємо url-адресу для виклику функції
def index():
    articles = get_all_articles()
    print(articles)
    return render_template("index.html", articles=articles)          #? html-сторінка, що повертається у браузер

@app.route('/article/<int:article_id>')
def article_page(article_id):
    article = get_article(article_id)
    return render_template('articles_page.html', article=article)

@app.route('/search')
def search():
    query = request.args.get('query', "")
    articles = search_articles(query)
    return render_template('search.html', articles = articles)

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True    #? автоматичне оновлення шаблонів
    app.run(debug=True)                           #? Запускаємо веб-сервер з цього файлу в режимі налагодження

