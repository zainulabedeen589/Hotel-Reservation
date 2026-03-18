from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Load model once (safe load)
try:
    model = joblib.load("models/random_forest.pkl")
except Exception as e:
    print("❌ Model loading failed:", e)
    model = None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500

    try:
        data = request.get_json()

        # ✅ Input validation (important)
        required_fields = [
            "lead_time",
            "market_segment_type",
            "avg_price_per_room",
            "no_of_special_requests",
            "arrival_month",
            "no_of_adults",
            "no_of_week_nights",
            "type_of_meal_plan",
            "room_type_reserved",
            "no_of_weekend_nights",
        ]

        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        # ✅ Convert safely to float
        features = np.array(
            [
                [
                    float(data["lead_time"]),
                    float(data["market_segment_type"]),
                    float(data["avg_price_per_room"]),
                    float(data["no_of_special_requests"]),
                    float(data["arrival_month"]),
                    float(data["no_of_adults"]),
                    float(data["no_of_week_nights"]),
                    float(data["type_of_meal_plan"]),
                    float(data["room_type_reserved"]),
                    float(data["no_of_weekend_nights"]),
                ]
            ]
        )

        prediction = int(model.predict(features)[0])

        return jsonify({"prediction": prediction, "status": "success"})

    except ValueError:
        return jsonify({"error": "Invalid input type"}), 400

    except Exception as e:
        return jsonify({"error": "Prediction failed", "details": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
