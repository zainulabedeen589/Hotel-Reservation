# 🏨 Hotel Booking Cancellation Prediction System

✨ **AI-powered Web Application built with Flask & Machine Learning** ✨
Predict whether a hotel booking will be **cancelled or confirmed** in real-time.

---

## 🚀 Overview

This project is a **Machine Learning-based web application** that predicts the likelihood of a hotel booking being cancelled based on user inputs.

It combines:

* ⚙️ **Flask Backend**
* 🎨 **Modern Interactive Frontend**
* 🤖 **Random Forest ML Model**

The UI includes a **dynamic particle background** and a **glassmorphism card design**, delivering a premium user experience.

---

## 🎯 Features

✅ Real-time prediction using trained ML model
✅ Clean and responsive UI (Tailwind CSS)
✅ Interactive particle background (cursor-based repulsion)
✅ Robust backend with validation & error handling
✅ REST API-based architecture

---

## 🧠 Machine Learning Model

* Algorithm: **Random Forest Classifier**
* Input Features:

  * Lead Time
  * Market Segment Type
  * Average Price per Room
  * Number of Special Requests
  * Arrival Month
  * Number of Adults
  * Week Nights
  * Meal Plan Type
  * Room Type Reserved
  * Weekend Nights

---

## 🏗️ Project Structure

```
Hotel-Booking-Predictor/
│
├── models/
│   └── random_forest.pkl
│
├── templates/
│   └── index.html
│
├── static/ (optional)
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/hotel-booking-predictor.git
cd hotel-booking-predictor
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python app.py
```

---

## 🌐 Usage

1. Open browser:

```
http://127.0.0.1:5000/
```

2. Enter booking details
3. Click **Predict**
4. Get instant result:

   * ✅ Booking Safe
   * ⚠️ Likely Cancelled

---

## 🎨 UI Highlights

* 🌌 Full-screen animated particle background
* 🧊 Glassmorphism card design
* ⚡ Smooth cursor interaction
* 📱 Fully responsive layout

---

## 🔌 API Endpoint

### `POST /predict`

#### Request (JSON):

```json
{
  "lead_time": 50,
  "market_segment_type": 1,
  "avg_price_per_room": 120,
  "no_of_special_requests": 2,
  "arrival_month": 6,
  "no_of_adults": 2,
  "no_of_week_nights": 3,
  "type_of_meal_plan": 1,
  "room_type_reserved": 1,
  "no_of_weekend_nights": 1
}
```

#### Response:

```json
{
  "prediction": 1,
  "status": "success"
}
```

---

## 🛡️ Error Handling

* Missing fields validation
* Invalid data type handling
* Model loading safety
* Structured API responses

---

## 📦 Tech Stack

* **Frontend:** HTML, Tailwind CSS, JavaScript
* **Backend:** Flask (Python)
* **ML:** Scikit-learn
* **Model Storage:** Joblib

---

## 📈 Future Improvements

* 🔥 Add feature encoding pipeline
* 🔥 Deploy on cloud (Render / AWS / GCP)
* 🔥 Add authentication system
* 🔥 Improve model accuracy with feature engineering
* 🔥 Dashboard with analytics

---

## 👨‍💻 Author

**Zainul Abedeen**

---

## ⭐ Support

If you like this project:

👉 Give it a ⭐ on GitHub
👉 Share it with others

---

💡 *Built with passion for AI & Web Development*
