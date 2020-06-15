import os
from truetone import app
from truetone.models.content.content import Content
from truetone.models.content.metadata import ContentMetadata
from flask import render_template
from flask import send_from_directory
from flask import abort
import os.path
from os import path


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/')
def index():
    cwd = os.path.dirname(os.path.realpath(__file__))
    entries = ContentMetadata.build(f'{cwd}/content').metadata
    return render_template('index.html', entries=entries)


@app.route('/<slug>')
def from_markdown(slug):
    cwd = os.path.dirname(os.path.realpath(__file__))
    file_path = f'{cwd}/content/{slug}.md'
    if path.exists(file_path):
        content = Content.build(file_path)
        return render_template('markdown.html',
                               raw_html=content.html,
                               title=content.metadata["title"])
    else:
        abort(404)
