from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# 定義網址與對應的頁面
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/variable')
def variable():
    return render_template('variable.html', data={
        'person': {
            'name': '小明',
            'gender': '男'
        },
        'list': ['蘋果', '香蕉', '鳳梨']
    })


@app.route('/api')
def api():
    return render_template('api.html')


#api用
@app.route('/calculate', methods=['POST'])
def postInput():
    # 取得前端傳過來的數值
    insertValues = request.get_json()
    valueA=insertValues['keyA']
    valueB=insertValues['keyB']
    
    result = int(valueA) + int(valueB)

    return jsonify({'result': str(result)})


# 啟動flask
if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
