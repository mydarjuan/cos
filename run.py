from flask import Flask, jsonify, render_template

from biz import userBiz
from common import dbClient

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('/common/404.html', error), 404


@app.errorhandler(500)
def page_not_found(error):
    return render_template('/common/500.html', error), 500


@app.route('/control-panel/index', methods=['GET'])
def control_panel_index():
    return render_template('/admin/index.html')




@app.route('/', methods=['GET'])
def fornt_index():
    return render_template('/fornt/index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)
