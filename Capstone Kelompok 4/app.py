import pandas as pd
from joblib import load
from flask import Flask, render_template, request
from sklearn.preprocessing import LabelEncoder
import ast

app = Flask(__name__)

# Memuat model Naive Bayes yang sudah dilatih
model = load('model1.pkl')

# Memuat DataFrame merged_df dan composition_df
merged_df = pd.read_csv('merged_data.csv')
composition_df = pd.read_csv('composition_data.csv')

# Memastikan 'Composition' dalam composition_df adalah list dari role
composition_df['Composition'] = composition_df['Composition'].apply(ast.literal_eval)

# Membuat LabelEncoder untuk role
label_encoder = LabelEncoder()
merged_df['Encoded Role'] = label_encoder.fit_transform(merged_df['Role'])

# Daftar hero yang valid
Hero = merged_df['Hero'].tolist()

# Fungsi untuk mendapatkan role dari hero
def get_hero_role(hero_name):
    hero_row = merged_df[merged_df['Hero'].str.lower() == hero_name.lower()]
    if not hero_row.empty:
        return hero_row['Role'].values[0]
    else:
        return None

# Fungsi untuk memprediksi pemenang berdasarkan komposisi tim
def predict_winner(team1_composition, team2_composition, composition_df, model):
    # Memastikan label yang ada sudah terdaftar di encoder
    team1_composition_encoded = []
    for role in team1_composition:
        if role in label_encoder.classes_:  # Memeriksa apakah role ada di dalam classes LabelEncoder
            team1_composition_encoded.append(label_encoder.transform([role])[0])
        else:
            # Jika tidak ada, beri nilai default atau abaikan
            team1_composition_encoded.append(-1)  # Misalnya, beri nilai -1 untuk role yang tidak dikenal
    
    team2_composition_encoded = []
    for role in team2_composition:
        if role in label_encoder.classes_:
            team2_composition_encoded.append(label_encoder.transform([role])[0])
        else:
            team2_composition_encoded.append(-1)  # Nilai default untuk role yang tidak dikenal

    # Mencari komposisi yang cocok untuk masing-masing tim
    matching_compositions1 = composition_df[
        composition_df['Composition'].apply(lambda comp: all(role in comp for role in team1_composition))
    ]
    matching_compositions2 = composition_df[
        composition_df['Composition'].apply(lambda comp: all(role in comp for role in team2_composition))
    ]

    # Jika salah satu tim tidak memiliki komposisi yang cocok, langsung dianggap kalah
    if matching_compositions1.empty:
        return "Team 2 menang, Team 1 kalah (komposisi tidak cocok)"
    elif matching_compositions2.empty:
        return "Team 1 menang, Team 2 kalah (komposisi tidak cocok)"
    
    # Menyiapkan data untuk prediksi
    team1_data_for_prediction = matching_compositions1[['Match', 'T1 Picks', 'T2 Picks']]
    team2_data_for_prediction = matching_compositions2[['Match', 'T1 Picks', 'T2 Picks']]

    # Melakukan prediksi probabilitas kemenangan
    team1_win_probability = model.predict_proba(team1_data_for_prediction)[:, 1].mean()
    team2_win_probability = model.predict_proba(team2_data_for_prediction)[:, 1].mean()

    # Menentukan pemenang berdasarkan probabilitas kemenangan
    if team1_win_probability > team2_win_probability:
        return "Team 1"
    elif team2_win_probability > team1_win_probability:
        return "Team 2"
    else:
        return "Draw"

@app.route('/')
def index():
    return render_template('index.html', heroes=Hero)

@app.route('/predict', methods=['POST'])
def predict():
    # Mendapatkan data dari form
    team1_data = {
        'Exp': request.form['team1_exp'],
        'Jungle': request.form['team1_jungle'],
        'Mid': request.form['team1_mid'],
        'Gold': request.form['team1_gold'],
        'Roam': request.form['team1_roam']
    }

    team2_data = {
        'Exp': request.form['team2_exp'],
        'Jungle': request.form['team2_jungle'],
        'Mid': request.form['team2_mid'],
        'Gold': request.form['team2_gold'],
        'Roam': request.form['team2_roam']
    }

    # Membuat list untuk komposisi tim berdasarkan role
    team1_composition = [get_hero_role(hero) for hero in team1_data.values()]
    team2_composition = [get_hero_role(hero) for hero in team2_data.values()]

    # Prediksi pemenang
    result = predict_winner(team1_composition, team2_composition, composition_df, model)

    # Menampilkan hasil
    return render_template('results.html', team1=team1_data, team2=team2_data, result=result)

if __name__ == '__main__':
    app.run(debug=True)
