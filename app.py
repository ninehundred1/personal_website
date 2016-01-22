import sys

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer


DEBUG = True
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'posts'
FLATPAGES_AUTO_RELOAD = True
FLATPAGES_MARKDOWN_EXTENSIONS = ['fenced_code']

app = Flask(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)

app.config.from_object(__name__)


@app.template_filter('date')
def date_filter(s):
    return s.strftime('%B %d, %Y')


@app.template_filter('excerpt')
def excerpt_filter(s):
    paragraphs = s.split('</p>')
    return paragraphs[0]


@app.route('/')
def home():
    if not DEBUG:
        posts = [p for p in flatpages if p.meta['published']]
    else:
        posts = [p for p in flatpages]
    posts.sort(key=lambda item: item['date'], reverse=True)
    latest = posts[0]
    recent = posts[1:4]
    featured = [p for p in posts if p.meta['featured']]
    return render_template('pages/home.html', latest=latest, recent=recent,
                           featured=featured)


@app.route('/about/')
def about():
    return render_template('pages/about.html')


@app.route('/work/')
def work():
    return render_template('pages/work.html')

@app.route('/projects/')
def projects():
    return render_template('pages/projects.html')

@app.route('/resume/')
def welcome():
    return render_template('pages/resume.html')

@app.route('/posts/')
def notes():
    if not DEBUG:
        posts = [p for p in flatpages if p.meta['published']]
    else:
        posts = [p for p in flatpages]
    posts.sort(key=lambda item: item['date'], reverse=True)
    return render_template('pages/posts.html', posts=posts)


@app.route('/posts/<name>/')
def note(name):
    post = flatpages.get_or_404(name)
    return render_template('pages/post.html', post=post)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/page_not_found.html'), 404





if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        DEBUG = False
        freezer.freeze()
    else: #run at http://localhost:8888/
        app.run(host='0.0.0.0', port=8888, debug=True)
