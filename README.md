# Laporan Proyek Machine Learning - Deteksi URL Phishing Menggunakan Random Forest

## Project Overview

Phishing merupakan salah satu bentuk serangan siber yang bertujuan memperoleh informasi sensitif pengguna seperti username, password, maupun data keuangan dengan menyamar sebagai situs web yang sah. Seiring meningkatnya penggunaan internet, jumlah situs phishing terus bertambah sehingga diperlukan sistem deteksi otomatis yang mampu mengidentifikasi URL berbahaya secara cepat dan akurat.

Machine Learning dapat dimanfaatkan untuk mengidentifikasi pola-pola tertentu pada URL dan karakteristik website yang sering digunakan oleh pelaku phishing. Dengan memanfaatkan fitur-fitur tersebut, model dapat membedakan URL phishing dan legitimate.

Pada proyek ini dibangun model klasifikasi menggunakan algoritma Random Forest untuk membedakan URL phishing dan legitimate berdasarkan fitur-fitur yang diekstraksi dari URL dan website.

### Manfaat Proyek

* Membantu mendeteksi URL phishing secara otomatis.
* Mengurangi risiko pengguna mengakses situs berbahaya.
* Mendukung pengembangan sistem keamanan siber berbasis Machine Learning.

Referensi: [PHISING LINK DETECTION](https://jurnal.amikom.ac.id/index.php/intechno/article/view/1562)

---

# Business Understanding

## Problem Statements

1. Bagaimana membangun model Machine Learning yang mampu mengklasifikasikan URL phishing dan legitimate?
2. Fitur apa saja yang paling berpengaruh terhadap status phishing?
3. Seberapa baik performa algoritma Random Forest dalam mendeteksi URL phishing?

## Goals

1. Mengembangkan model klasifikasi URL phishing.
2. Mengidentifikasi fitur-fitur yang memiliki pengaruh besar terhadap status phishing.
3. Mengevaluasi performa model menggunakan metrik klasifikasi.

## Solution Statements

Pendekatan yang digunakan dalam proyek ini meliputi:

* Data Cleaning.
* Feature Engineering menggunakan analisis korelasi Pearson.
* Feature Selection berdasarkan nilai korelasi terhadap target.
* Random Forest Classifier sebagai algoritma klasifikasi.
* Evaluasi menggunakan Accuracy, Precision, Recall, dan F1-Score.

---

# Data Understanding

Dataset yang digunakan merupakan dataset URL phishing yang terdiri dari berbagai fitur karakteristik URL dan website.

## Informasi Dataset

### Ukuran Dataset

```python
"Shape:", df.shape
```

**Shape: (11430, 89)**

### Informasi Dataset

```python
df.info()
```

```text
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 11430 entries, 0 to 11429
Data columns (total 89 columns):
```

| No | Column                     | Non-Null Count | Data Type |
| -- | -------------------------- | -------------- | --------- |
| 0  | url                        | 11430 non-null | object    |
| 1  | length_url                 | 11430 non-null | int64     |
| 2  | length_hostname            | 11430 non-null | int64     |
| 3  | ip                         | 11430 non-null | int64     |
| 4  | nb_dots                    | 11430 non-null | int64     |
| 5  | nb_hyphens                 | 11430 non-null | int64     |
| 6  | nb_at                      | 11430 non-null | int64     |
| 7  | nb_qm                      | 11430 non-null | int64     |
| 8  | nb_and                     | 11430 non-null | int64     |
| 9  | nb_or                      | 11430 non-null | int64     |
| 10 | nb_eq                      | 11430 non-null | int64     |
| 11 | nb_underscore              | 11430 non-null | int64     |
| 12 | nb_tilde                   | 11430 non-null | int64     |
| 13 | nb_percent                 | 11430 non-null | int64     |
| 14 | nb_slash                   | 11430 non-null | int64     |
| 15 | nb_star                    | 11430 non-null | int64     |
| 16 | nb_colon                   | 11430 non-null | int64     |
| 17 | nb_comma                   | 11430 non-null | int64     |
| 18 | nb_semicolumn              | 11430 non-null | int64     |
| 19 | nb_dollar                  | 11430 non-null | int64     |
| 20 | nb_space                   | 11430 non-null | int64     |
| 21 | nb_www                     | 11430 non-null | int64     |
| 22 | nb_com                     | 11430 non-null | int64     |
| 23 | nb_dslash                  | 11430 non-null | int64     |
| 24 | http_in_path               | 11430 non-null | int64     |
| 25 | https_token                | 11430 non-null | int64     |
| 26 | ratio_digits_url           | 11430 non-null | float64   |
| 27 | ratio_digits_host          | 11430 non-null | float64   |
| 28 | punycode                   | 11430 non-null | int64     |
| 29 | port                       | 11430 non-null | int64     |
| 30 | tld_in_path                | 11430 non-null | int64     |
| 31 | tld_in_subdomain           | 11430 non-null | int64     |
| 32 | abnormal_subdomain         | 11430 non-null | int64     |
| 33 | nb_subdomains              | 11430 non-null | int64     |
| 34 | prefix_suffix              | 11430 non-null | int64     |
| 35 | random_domain              | 11430 non-null | int64     |
| 36 | shortening_service         | 11430 non-null | int64     |
| 37 | path_extension             | 11430 non-null | int64     |
| 38 | nb_redirection             | 11430 non-null | int64     |
| 39 | nb_external_redirection    | 11430 non-null | int64     |
| 40 | length_words_raw           | 11430 non-null | int64     |
| 41 | char_repeat                | 11430 non-null | int64     |
| 42 | shortest_words_raw         | 11430 non-null | int64     |
| 43 | shortest_word_host         | 11430 non-null | int64     |
| 44 | shortest_word_path         | 11430 non-null | int64     |
| 45 | longest_words_raw          | 11430 non-null | int64     |
| 46 | longest_word_host          | 11430 non-null | int64     |
| 47 | longest_word_path          | 11430 non-null | int64     |
| 48 | avg_words_raw              | 11430 non-null | float64   |
| 49 | avg_word_host              | 11430 non-null | float64   |
| 50 | avg_word_path              | 11430 non-null | float64   |
| 51 | phish_hints                | 11430 non-null | int64     |
| 52 | domain_in_brand            | 11430 non-null | int64     |
| 53 | brand_in_subdomain         | 11430 non-null | int64     |
| 54 | brand_in_path              | 11430 non-null | int64     |
| 55 | suspecious_tld             | 11430 non-null | int64     |
| 56 | statistical_report         | 11430 non-null | int64     |
| 57 | nb_hyperlinks              | 11430 non-null | int64     |
| 58 | ratio_intHyperlinks        | 11430 non-null | float64   |
| 59 | ratio_extHyperlinks        | 11430 non-null | float64   |
| 60 | ratio_nullHyperlinks       | 11430 non-null | int64     |
| 61 | nb_extCSS                  | 11430 non-null | int64     |
| 62 | ratio_intRedirection       | 11430 non-null | int64     |
| 63 | ratio_extRedirection       | 11430 non-null | float64   |
| 64 | ratio_intErrors            | 11430 non-null | int64     |
| 65 | ratio_extErrors            | 11430 non-null | float64   |
| 66 | login_form                 | 11430 non-null | int64     |
| 67 | external_favicon           | 11430 non-null | int64     |
| 68 | links_in_tags              | 11430 non-null | float64   |
| 69 | submit_email               | 11430 non-null | int64     |
| 70 | ratio_intMedia             | 11430 non-null | float64   |
| 71 | ratio_extMedia             | 11430 non-null | float64   |
| 72 | sfh                        | 11430 non-null | int64     |
| 73 | iframe                     | 11430 non-null | int64     |
| 74 | popup_window               | 11430 non-null | int64     |
| 75 | safe_anchor                | 11430 non-null | float64   |
| 76 | onmouseover                | 11430 non-null | int64     |
| 77 | right_clic                 | 11430 non-null | int64     |
| 78 | empty_title                | 11430 non-null | int64     |
| 79 | domain_in_title            | 11430 non-null | int64     |
| 80 | domain_with_copyright      | 11430 non-null | int64     |
| 81 | whois_registered_domain    | 11430 non-null | int64     |
| 82 | domain_registration_length | 11430 non-null | int64     |
| 83 | domain_age                 | 11430 non-null | int64     |
| 84 | web_traffic                | 11430 non-null | int64     |
| 85 | dns_record                 | 11430 non-null | int64     |
| 86 | google_index               | 11430 non-null | int64     |
| 87 | page_rank                  | 11430 non-null | int64     |
| 88 | status                     | 11430 non-null | object    |


* Total Records: **11,430**
* Total Features: **89**
* Integer Features: **74**
* Float Features: **13**
* Object Features: **2**
* Missing Values: **0**
* Memory Usage: **7.8 MB**


Dataset terdiri dari berbagai fitur numerik yang merepresentasikan karakteristik URL dan website.

## Target Label

| Nilai | Keterangan |
| ----- | ---------- |
| 0     | Legitimate |
| 1     | Phishing   |

---


## Missing Values

Pemeriksaan nilai kosong (missing values) dilakukan untuk memastikan kualitas data sebelum proses preprocessing dan pelatihan model.

```python
df.isnull().sum()
```

### Hasil Pemeriksaan

```text
Total Missing Values : 0
```

### Ringkasan

| Keterangan                | Nilai |
| ------------------------- | ----- |
| Total Kolom               | 89    |
| Total Missing Values      | 0     |
| Persentase Missing Values | 0%    |

### Detail Missing Values per Kolom

| Column          | Missing Values |
| --------------- | -------------- |
| url             | 0              |
| length_url      | 0              |
| length_hostname | 0              |
| ip              | 0              |
| nb_dots         | 0              |
| ...             | ...            |
| web_traffic     | 0              |
| dns_record      | 0              |
| google_index    | 0              |
| page_rank       | 0              |
| status          | 0              |


### Hasil Analisis

Dataset tidak memiliki nilai yang hilang (*missing values*) pada seluruh 89 fitur. Oleh karena itu, tidak diperlukan proses penanganan missing value seperti imputasi atau penghapusan data sebelum tahap preprocessing dan pelatihan model.

---

## Distribusi Label

```python
label_counts = df['status'].value_counts()
print(label_counts)

plt.figure(figsize=(6,4))
sns.countplot(x='status', data=df, palette='Set2')
plt.title('Distribusi Label: Phishing vs Legitimate')
plt.xlabel('Status')
plt.ylabel('Jumlah')
plt.tight_layout()
plt.savefig('label_distribution.png')
plt.show()
```
### Hasil Distribusi
status
legitimate    5715
phishing      5715
Name: count, dtype: int64
/tmp/ipykernel_2533/1605270780.py:6: FutureWarning: 

📷 **Gambar 2. Distribusi Kelas Phishing dan Legitimate**

### Hasil Analisis

Distribusi data menunjukkan bahwa jumlah URL phishing dan legitimate relatif seimbang sehingga tidak diperlukan teknik penanganan data imbalance seperti oversampling maupun undersampling.

---

# Data Preparation

Tahap data preparation dilakukan untuk memastikan kualitas data sebelum digunakan pada proses pemodelan.

## Tipe Data

### Memeriksa tipe data feature

``` Python
print(df.dtypes)
```
### Hasil memeriksa tipe data
length_url         int64
length_hostname    int64
ip                 int64
nb_dots            int64
nb_hyphens         int64
                   ...  
web_traffic        int64
dns_record         int64
google_index       int64
page_rank          int64
status             int64
Length: 88, dtype: object


## Data Cleaning

Menghapus data yang memiliki nilai kosong.

```python
df.dropna(inplace=True)
```

Karena dataset tidak memiliki missing value, jumlah data tidak berubah setelah proses cleaning.

---

## Feature Engineering

Pada tahap ini dilakukan analisis korelasi untuk mengetahui hubungan masing-masing fitur terhadap target `status`.

### Analisis Korelasi

```python
corr_matrix = df.corr()

corr_status = corr_matrix['status'].sort_values(
    ascending=False
)
```

### Hasil Korelasi Tertinggi

| Fitur            | Korelasi |
| ---------------- | -------: |
| google_index     |    0.731 |
| page_rank        |    0.511 |
| nb_www           |    0.443 |
| ratio_digits_url |    0.356 |
| domain_in_title  |    0.343 |
| nb_hyperlinks    |    0.343 |
| phish_hints      |    0.335 |
| domain_age       |    0.332 |
| ip               |    0.322 |

### Visualisasi Korelasi

```python
corr_status.drop('status').sort_values().plot(
    kind='barh'
)
```

📷 **Gambar 3. Korelasi Fitur terhadap Status**

*(Masukkan grafik korelasi fitur terhadap target)*

### Hasil Analisis

Berdasarkan hasil analisis korelasi, fitur `google_index` memiliki korelasi tertinggi terhadap status phishing sebesar 0.731. Selain itu, fitur `page_rank`, `nb_www`, dan `ratio_digits_url` juga menunjukkan hubungan yang cukup kuat terhadap target.

---

## Feature Selection

Pemilihan fitur dilakukan menggunakan threshold korelasi absolut lebih besar dari 0.2.

```python
selected_features = corr_abs[
    corr_abs > 0.2
].index

selected_features = selected_features.drop('status')
```

### Fitur Terpilih

* google_index
* page_rank
* nb_www
* ratio_digits_url
* domain_in_title
* nb_hyperlinks
* phish_hints
* domain_age
* ip
* nb_qm
* length_url
* ratio_intHyperlinks
* nb_slash
* length_hostname
* nb_eq
* ratio_digits_host
* shortest_word_host
* prefix_suffix
* longest_word_path

Jumlah fitur hasil seleksi: **19 fitur**

### Uraian Fitur
| Fitur | Deskripsi |
|---------|---------|
| google_index | Status website terindeks Google |
| page_rank | Nilai PageRank website |
| nb_www | Jumlah kemunculan kata "www" |
| ratio_digits_url | Rasio angka terhadap panjang URL |
| domain_in_title | Kesesuaian domain dengan judul halaman |
| nb_hyperlinks | Jumlah hyperlink pada halaman |
| phish_hints | Indikator karakteristik phishing |
| domain_age | Umur domain |
| ip | Penggunaan alamat IP pada URL |
| nb_qm | Jumlah karakter tanda tanya (?) |
| length_url | Panjang URL |
| ratio_intHyperlinks | Rasio hyperlink internal |
| nb_slash | Jumlah karakter "/" |
| length_hostname | Panjang hostname |
| nb_eq | Jumlah karakter "=" |
| ratio_digits_host | Rasio angka pada hostname |
| shortest_word_host | Panjang kata terpendek pada hostname |
| prefix_suffix | Penggunaan tanda "-" pada domain |
| longest_word_path | Panjang kata terpanjang pada path URL |

### Dataset Akhir

```python
X = df[selected_features]
y = df['status']
```

---

# Modeling

## Pembagian Dataset

Dataset dibagi menjadi data latih dan data uji menggunakan rasio 80:20.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
```

## Algoritma Random Forest

```python
rf = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)
```

### Alasan Pemilihan Algoritma

Random Forest dipilih karena mampu menangani data berdimensi tinggi, mengurangi risiko overfitting, serta menyediakan informasi feature importance yang berguna dalam proses analisis fitur.

## Training Model

```python
rf.fit(X_train, y_train)
```

## Prediksi

```python
y_pred = rf.predict(X_test)
```

---

# Evaluation

Evaluasi dilakukan menggunakan metrik Accuracy, Precision, Recall, dan F1-Score.

## Hasil Evaluasi

| Metrik    |  Nilai |
| --------- | -----: |
| Accuracy  | 95.93% |
| Precision | 95.42% |
| Recall    | 96.50% |
| F1-Score  | 95.95% |

### Interpretasi Hasil

* Accuracy sebesar 95.93% menunjukkan bahwa model mampu mengklasifikasikan URL dengan benar pada sebagian besar data uji.
* Precision sebesar 95.42% menunjukkan bahwa mayoritas URL yang diprediksi sebagai phishing memang benar merupakan phishing.
* Recall sebesar 96.50% menunjukkan bahwa model berhasil mendeteksi sebagian besar URL phishing yang terdapat pada dataset.
* F1-Score sebesar 95.95% menunjukkan keseimbangan yang baik antara precision dan recall.

---

## Classification Report

📷 **Gambar 4. Classification Report**

*(Masukkan screenshot output classification report)*

---

## Confusion Matrix

📷 **Gambar 5. Confusion Matrix**

*(Masukkan gambar confusion matrix dari notebook)*

### Analisis Confusion Matrix

| Actual     | Predicted Legitimate | Predicted Phishing |
| ---------- | -------------------: | -----------------: |
| Legitimate |                 1090 |                 53 |
| Phishing   |                   40 |               1103 |

Model berhasil mengklasifikasikan 1090 URL legitimate dan 1103 URL phishing dengan benar. Terdapat 53 kasus False Positive dan 40 kasus False Negative.

Jumlah False Negative yang relatif rendah menunjukkan bahwa model memiliki kemampuan yang baik dalam mendeteksi URL phishing sehingga cocok digunakan sebagai sistem pendukung deteksi ancaman siber.

---

## Feature Importance

```python
importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': rf.feature_importances_
})
```

📷 **Gambar 6. Feature Importance Random Forest**

*(Masukkan grafik Top 15 Feature Importance)*

### Analisis Feature Importance

Fitur dengan nilai importance tertinggi merupakan fitur yang paling berkontribusi dalam proses klasifikasi URL phishing. Hasil ini memperkuat analisis korelasi yang telah dilakukan pada tahap feature engineering.

---

# Deployment

Tahap deployment dilakukan dengan menyimpan model menggunakan library Pickle sehingga model dapat digunakan kembali tanpa perlu melakukan proses pelatihan ulang.

## Menyimpan Model

```python
import pickle

with open('phishing_model.pkl', 'wb') as file:
    pickle.dump(rf, file)
```

## Memuat Model

```python
with open('phishing_model.pkl', 'rb') as file:
    model = pickle.load(file)
```

## Simulasi Prediksi

```python
sample = X.iloc[[0]]

prediction = model.predict(sample)

print(prediction)
```

Model yang telah disimpan dapat diintegrasikan ke dalam aplikasi web, API, maupun sistem keamanan siber untuk melakukan deteksi URL phishing secara otomatis.

---

# Conclusion

Pada proyek ini berhasil dibangun model klasifikasi URL phishing menggunakan algoritma Random Forest dengan pendekatan CRISP-DM. Tahap feature engineering menunjukkan bahwa fitur seperti `google_index`, `page_rank`, `nb_www`, `ratio_digits_url`, dan `domain_in_title` memiliki hubungan yang cukup kuat terhadap status phishing.

Model Random Forest yang dibangun menggunakan 19 fitur hasil seleksi berhasil memperoleh Accuracy sebesar **95.93%**, Precision sebesar **95.42%**, Recall sebesar **96.50%**, dan F1-Score sebesar **95.95%**.

Berdasarkan hasil evaluasi tersebut dapat disimpulkan bahwa algoritma Random Forest mampu mengklasifikasikan URL phishing dan legitimate secara efektif sehingga berpotensi digunakan sebagai dasar pengembangan sistem deteksi phishing otomatis di masa mendatang.
