from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# دالة لتوليد جدول الضرب
def generate_table(number, limit):
    table = []
    for i in range(1, limit + 1):
        table.append({"multiplier": i,"result": number * i})
    return table

# Endpoint رئيسي
@app.route('/multiplication', methods=['GET'])
def multiplication():
    # قراءة القيم من الـ query string (مثلاً: /multiplication?number=5&limit=10)
    number = request.args.get('number', type=int)
    limit = request.args.get('limit', type=int, default=10)  # limit افتراضي = 10

    if number is None:
        return jsonify({"error": "Please provide a number parameter"}), 400

    result = generate_table(number, limit)
    return jsonify({
        "number": number,
        "limit": limit,
        "table": result
    })

if __name__ == '__main__':
    app.run(debug=True)
