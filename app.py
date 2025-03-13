from flask import Flask, request, render_template
import pandas as pd
import os

app = Flask(__name__)

# Wczytanie pliku CSV do DataFrame
file_path = "/final_data.csv"
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    df = pd.DataFrame()

@app.route('/', methods=['GET', 'POST'])
def index():
    product_info = None
    if request.method == 'POST':
        ean_code = request.form.get('ean')
        if ean_code and not df.empty:
            product_info = df[df['EAN'].astype(str) == ean_code].to_dict(orient='records')
            if not product_info:
                product_info = "Brak wyników dla podanego kodu EAN."
    
    return render_template('index.html', product_info=product_info)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
