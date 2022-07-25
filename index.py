from flask import Flask
from flask import request

app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/picprocess',methods=["POST"])
def picprocess():
    if 'photo' not in request.files:
        flash('ファイルがありません')
        return 'ファイルがない'
    photo = request.files['photo']
    fileName = photo.filename
    print(fileName)

    picJudgeResult = PicJudge(photo)
    return picJudgeResult + '：ファイル名 ' + fileName

# 画像判定処理　要大観
def PicJudge(photo):
    #ここに処理を記載
    return '判定結果'

app.run(port=8000, debug=True)