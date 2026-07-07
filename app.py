# -*- coding: utf-8 -*-
# 球速けいそくアプリ(シンプル版)
# 教科書の第2章〜第6章を全部やると、このファイルになります

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# トップページを表示する
@app.route("/")
def index():
    return render_template("index.html")


# ブラウザから距離と時間を受け取って、球速を計算して返す
@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    distance = float(data["distance"])   # 距離 [m]
    time_sec = float(data["time"])       # 時間 [秒]

    speed_ms = distance / time_sec       # 速さ [m/秒] = 距離 ÷ 時間
    speed_kmh = speed_ms * 3.6           # ×3.6 で時速 [km/h] になる

    message = judge(speed_kmh)

    return jsonify({
        "speed_kmh": round(speed_kmh, 1),
        "message": message
    })


# 球速に合わせてコメントを決める関数
def judge(speed_kmh):
    if speed_kmh < 60:
        return "いいね！少年野球で通用するスピード！"
    elif speed_kmh < 80:
        return "すごい！少年野球のエース級！"
    elif speed_kmh < 100:
        return "中学生トップクラスの速球！"
    elif speed_kmh < 140:
        return "高校生レベルの本格派！"
    else:
        return "プロ級！？(押しまちがいかもよ)"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, use_reloader=False)
