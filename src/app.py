from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Create uploads folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"
    
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        # Read the CSV
        try:
            df = pd.read_csv(filepath)
            columns = list(df.columns)
            row_count = len(df)
            
            # Simple dummy forecast (just for demonstration)
            # In real version this will use scikit-learn
            forecast_7day = 120
            forecast_30day = 480
            anomaly_score = 0.23
            
            return render_template(
                'results.html',
                filename=file.filename,
                columns=columns,
                row_count=row_count,
                forecast_7day=forecast_7day,
                forecast_30day=forecast_30day,
                anomaly_score=anomaly_score
            )
        except Exception as e:
            return f"Error reading file: {str(e)}"
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)