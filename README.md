# Symptom-based Disease Prediction System

A machine learning–based web application that predicts possible diseases based on user-selected symptoms.

This project was originally developed as part of my undergraduate final year project. The deployed version focuses on the core prediction pipeline to provide a clean and maintainable demonstration of the system.

---

## 🚀 Features

- Symptom-based disease prediction using a trained ML model
- Top 3 predicted diseases with confidence scores
- Clean and responsive web interface (Bootstrap 5)
- Stateless design (no database or authentication required)
- Real-time prediction using Django backend

---

## 🧠 How It Works

1. The user selects symptoms from a predefined list
2. The system converts symptoms into a binary feature vector
3. The trained machine learning model processes the input
4. The model outputs:
   - Predicted disease
   - Confidence score
   - Top 3 likely diseases

---

## ⚙️ Tech Stack

- **Backend:** Django
- **Frontend:** HTML, Bootstrap 5
- **Machine Learning:** scikit-learn
- **Model Loading:** joblib
- **Deployment:** Docker (Railway)

---

## ⚠️ Disclaimer

This application is intended for **educational and demonstration purposes only**.

The predictions are based on a machine learning model and should **not be considered medical advice or diagnosis**. Always consult a qualified healthcare professional.

## 💡 Design Decisions

- Removed authentication and database layers to focus on the core ML pipeline
- Implemented a stateless architecture for simplicity and reliability
- Separated model loading logic from views for clean design
- Preserved original feature encoding to ensure model correctness






