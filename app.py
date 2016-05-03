# coding: utf-8

import os
from flask import Flask, request, render_template


app = Flask(__name__)


tasks = []

for i in range(10):
    tasks.append({
        'id': i,
        'name': 'task %d' % i,
        'done': False,
    })


@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        id = request.form.get('id')
        for task in tasks:
            if task['id'] == int(id):
                task['done'] = True
                break
    return render_template('homepage.html', tasks=tasks)


def main():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)


if __name__ == '__main__':
    main()