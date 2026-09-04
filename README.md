# Analisis Optimal Team Composition Mobile Legends

Project Capstone Data Science untuk menganalisis komposisi tim Mobile Legends berdasarkan Role dan Lane menggunakan metode Machine Learning.

## Deskripsi

Project ini bertujuan untuk menganalisis komposisi tim pada Mobile Legends berdasarkan Role dan Lane serta memprediksi peluang kemenangan dari suatu komposisi tim.

Data yang digunakan berasal dari data hero Mobile Legends dan data pertandingan turnamen MPL. Hasil analisis kemudian diimplementasikan ke dalam aplikasi web berbasis Flask yang dapat digunakan sebagai sistem rekomendasi dalam proses Draft Pick.

## Tujuan

- Menganalisis hubungan antara Role dan Lane dalam komposisi tim.
- Mengolah data pertandingan untuk mengetahui performa berbagai komposisi tim.
- Membangun model Machine Learning untuk memprediksi hasil komposisi tim.
- Mengimplementasikan model ke dalam aplikasi web menggunakan Flask.

## Dataset

Dataset yang digunakan dalam project ini meliputi:

- `Hero.csv` — data hero Mobile Legends.
- `New Hero.csv` — data tambahan hero.
- `Data_MPL_Tournament.csv` — data pertandingan turnamen MPL.
- `merged_data.csv` — hasil penggabungan dan pengolahan data.
- `composition_data.csv` — data komposisi tim yang digunakan dalam pemodelan.

## Metodologi

Tahapan pengerjaan project meliputi:

1. Data Collection
2. Data Cleaning
3. Data Preprocessing
4. Exploratory Data Analysis (EDA)
5. Feature Engineering
6. Pembentukan data komposisi tim
7. Model Training
8. Model Evaluation
9. Model Deployment

## Machine Learning

Beberapa algoritma Machine Learning yang diuji dalam project ini antara lain:

- Gaussian Naive Bayes
- Bernoulli Naive Bayes
- Multinomial Naive Bayes
- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- Voting Classifier

Model kemudian dibandingkan berdasarkan beberapa metrik evaluasi seperti:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

Berdasarkan eksperimen pada notebook, beberapa model ensemble dan tree-based menghasilkan performa yang tinggi pada data pengujian.

> Catatan: nilai performa model pada notebook merupakan hasil eksperimen pada skenario pemodelan tertentu dan tidak secara langsung merepresentasikan performa model yang digunakan pada aplikasi Flask.

## Aplikasi Web

Model Machine Learning diimplementasikan menggunakan Flask untuk membuat aplikasi web sederhana yang dapat digunakan untuk melakukan prediksi berdasarkan komposisi tim.

## Teknologi yang Digunakan

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Flask
- Joblib
- Pillow
- Requests
- Jupyter Notebook

## Struktur Project

```text
Capstone Kelompok 4/
├── Capstone.ipynb
├── app.py
├── Hero.csv
├── New Hero.csv
├── Data_MPL_Tournament.csv
├── merged_data.csv
├── composition_data.csv
├── model1.pkl
├── templates/
│   ├── index.html
│   └── results.html
└── static/
    ├── css/
    │   └── style.css
    └── images/
