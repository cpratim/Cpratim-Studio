from flask import (
    Flask, 
    render_template,
    send_file,
    jsonify,
    request,
)

import gunicorn
from projects import get_projects

from cinematics import (
    load_cines,
    load_file,
    one_block,
)

app = Flask(__name__)

@app.route('/')
def index():
    
    cines = load_cines()
    return render_template('index.html', cines=cines)

@app.route('/projects')
def projects():
    _projects = get_projects()
    return render_template('projects.html', _projects=_projects)

@app.route('/projects_json')
def projects_json():
    return send_file('projects.json')

@app.route('/resource', methods=['GET', 'POST'])
def testing():
    if request.method == 'POST':
        file = request.headers['file']
        return jsonify(load_file(file))

@app.route('/cinematics')
def cinematics():
    code = one_block()
    return jsonify(code)

@app.route('/about')
def about():
    imagedir = '../static/misc'
    images = [
        f'{imagedir}/about{i}.jpg' for i in range(1, 7)
    ]
    return render_template('about.html', images=images)

@app.route('/resume')
def resume():
    return send_file('static/misc/resume.pdf')

if __name__ == '__main__':
    app.run(threaded=True, port=5000)