from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

slope = 2
intercept = 10

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get X value from the request
        input_x = float(request.form.get('input_x'))

        # Perform linear regression
        predicted_y = slope * input_x + intercept

        # Return the result as JSON
        return jsonify({'predicted_y': predicted_y})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
