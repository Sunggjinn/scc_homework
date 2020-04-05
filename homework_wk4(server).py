from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def write_order():
# 1. 클라이언트가 준 input_name, input_quantity, input_address, input_phonenum  가져오기.
    name_receive = request.form['name_give']
    quantity_receive = request.form['quantity_give']
    address_receive = request.form['address_give']
    phonenum_receive = request.form['phonenum_give']
# 2. DB에 정보 삽입하기
    doc = {
        'name': name_receive,
        'quantity': quantity_receive,
        'address': address_receive,
        'phonenum': phonenum_receive
        }
    db.orders.insert_one(doc)
# 3. 성공 여부 & 성공 메시지 반환하기
    return jsonify({'r esult': 'success', 'msg': '주문이 성공적으로 작성되었습니다.'})


@app.route('/orders', methods=['GET'])
def read_order():
    #1. DB에서 order 정보 모두 가져오기 - object id 값 빼고
    db.orders.find({}, {'_id': False})

#2. 성공 여부 & 주문 목록 반환하
    return jsonify({'result':'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
