from flask import Flask, render_template, request, jsonify
import jieba
from collections import Counter
import os


app = Flask(__name__)


@app.route('/')
@app.route('/ECharts.html')
def index():
    return render_template('ECharts.html')


@app.route('/addnumber')
def add():
    a = request.args.get('a', 0, type=float)
    b = request.args.get('b', 0, type=float)
    return jsonify(result=a + b)

@app.route('/aaa')
def tb():
    with open('textout4.txt', 'r',encoding='UTF-8') as fr:
        fdata = fr.read()
        print(fdata)
    return jsonify(re = fdata)


if __name__ == '__main__':
    app.run(debug=True)
    '''(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 5000)), debug=True)'''
