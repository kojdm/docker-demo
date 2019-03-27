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
        ]
    }
    return jsonify(chubs)


# Run server
if __name__ == '__main__':
    app.run(debug=True)
