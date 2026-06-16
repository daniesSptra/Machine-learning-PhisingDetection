import gradio as gr
import pandas as pd
import pickle
import re

from urllib.parse import urlparse

# ==================================
# LOAD MODEL
# ==================================

model = pickle.load(
    open(
        "url_phishing_model.pkl",
        "rb"
    )
)

# ==================================
# FEATURE EXTRACTION
# ==================================

def extract_features(url):

    hostname = urlparse(url).netloc

    digits_url = sum(
        c.isdigit()
        for c in url
    )

    digits_host = sum(
        c.isdigit()
        for c in hostname
    )

    features = {

        'nb_www':
            url.count('www'),

        'ratio_digits_url':
            digits_url / max(len(url),1),

        'ip':
            int(
                bool(
                    re.search(
                        r'\d+\.\d+\.\d+\.\d+',
                        hostname
                    )
                )
            ),

        'nb_qm':
            url.count('?'),

        'length_url':
            len(url),

        'nb_slash':
            url.count('/'),

        'nb_eq':
            url.count('='),

        'length_hostname':
            len(hostname),

        'ratio_digits_host':
            digits_host / max(len(hostname),1),

        'prefix_suffix':
            int('-' in hostname),

        'nb_dots':
            url.count('.'),

        'nb_and':
            url.count('&'),

        'nb_com':
            url.lower().count('.com'),

        'nb_at':
            url.count('@'),

        'nb_subdomains':
            max(
                len(hostname.split('.')) - 2,
                0
            ),

        'https_token':
            int(
                'https' in hostname.lower()
            ),

        'nb_semicolumn':
            url.count(';')
    }

    return pd.DataFrame([features])

# ==================================
# PREDICTION
# ==================================

def predict(url):

    try:

        X = extract_features(url)

        print("="*50)
        print(url)
        print(X)
        print("="*50)

        pred = model.predict(X)[0]

        print("Prediction:", pred)

        if pred == 1:
            return "🚨 PHISHING WEBSITE"

        return "✅ LEGITIMATE WEBSITE"

    except Exception as e:

        return f"Error: {e}"

# ==================================
# GRADIO UI
# ==================================

demo = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(
        label="Masukkan URL",
        placeholder="https://example.com"
    ),
    outputs=gr.Textbox(
        label="Hasil Deteksi"
    ),
    title="Phishing URL Detector",
    description="Deteksi URL Phishing menggunakan Random Forest"
)

demo.launch()