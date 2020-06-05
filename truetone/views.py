import os
from truetone import app
from truetone.models import content
from truetone.models import content_metadata
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
    entries = content_metadata.ContentMetadata.build(f'{cwd}/content').metadata
    return render_template('index.html', entries=entries)


@app.route('/<slug>')
def from_markdown(slug):
    cwd = os.path.dirname(os.path.realpath(__file__))
    file_path = f'{cwd}/content/{slug}.md'
    if path.exists(file_path):
        raw_html = content.Content.build(file_path).html
        return render_template('markdown.html', raw_html=raw_html)
    else:
        abort(404)
