from flask import Flask, render_template, request
from joblib import dump, load
from sklearn.preprocessing import LabelEncoder
import numpy as np


app = Flask(__name__)

# Load the model
model = load('D:\CCC\python\old\PY\FlaskWeb\model.joblib')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get input data from the form
        Brand = request.form['Brand']
        Processor_Speed = float(request.form['Processor_Speed'])
        RAM_Size = int(request.form['RAM_Size'])
        Storage_Capacity = int(request.form['Storage_Capacity'])
        Screen_Size = float(request.form['Screen_Size'])
        Weight = float(request.form['Weight'])

        # Perform the prediction using the loaded model
        input_features = [Brand, Processor_Speed, RAM_Size,
                          Storage_Capacity, Screen_Size, Weight]
        print(input_features)

        # 編碼字串型態的資料
        label_encoder = LabelEncoder()
        for idx, value in enumerate(input_features):
            if isinstance(value, str):  # 判斷值是否為字串型態
                input_features[idx] = label_encoder.fit_transform([value])[
                    0]  # 編碼單個字串

        # 將 input_features 轉換為2D陣列
        input_features = np.array(input_features).reshape(1, -1)

        prediction = model.predict(input_features)

        stress_level = prediction[0]

        return render_template('index.html', stress_level=stress_level)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5001)
