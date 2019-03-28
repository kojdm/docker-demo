from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_churnbusters():
    chubs = {
        'churnbusters': [
            'Marc',
            'Marvin',
            'Stefano',
            'Aby',
            'Koji',
            'Ivy'
        ]
    }
    return jsonify(chubs)


# Run server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
