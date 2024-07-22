from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Create the Flask app object
app = Flask(__name__)

# Load the model
model = pickle.load(open(r"C:\\Users\\farde\\HTML\\asd disorder\\ASD PROEJCT FINAL\\ASD PROEJCT FINAL\\model.pkl", "rb"))

# Define your routes and functions
@app.route('/')
def intro():
    return render_template('intro.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        int_features = [int(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)
        
        output = 'ASD Detected' if prediction[0] == 1 else 'ASD Not Detected'
        
        return render_template('result.html', prediction=output)
    
    except Exception as e:
        return render_template('error.html', error=str(e))

@app.route('/example')
def example_route():
    data = {'key': 'value'}
    return jsonify(data)

# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
