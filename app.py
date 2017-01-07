from flask import Flask, jsonify,render_template

from biz import userBiz
from common import dbClient

app = Flask(__name__)


@app.route('/control-panel/index', methods=['GET'])
def control_panel_index():
    return render_template('/admin/index.html')


@app.route('/', methods=['GET'])
def fornt_index():
    return render_template('/fornt/index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)
