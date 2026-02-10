from flask import Flask, request, jsonify , render_template
import pickle
import pandas as pd

app = Flask(__name__)

with open("src/XGBoost.pkl", "rb") as f:
    pipeline = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')
@app.route("/predictPrice", methods=["GET", "POST"])
def predictPrice():
    prediction = None

    if request.method == "POST":
        data = {
            "sq_mt_built": float(request.form["sq_mt_built"]),
            "n_rooms": int(request.form["n_rooms"]),
            "n_bathrooms": float(request.form["n_bathrooms"]),
            "floor": request.form["floor"],
            "is_floor_under": request.form.get("is_floor_under") == "on",
            "house_type_id": request.form["house_type_id"],
            "is_renewal_needed": request.form.get("is_renewal_needed") == "on",
            "is_new_development": request.form.get("is_new_development") == "on",
            "has_lift": request.form.get("has_lift") == "on",
            "is_exterior": request.form.get("is_exterior") == "on",
            "energy_certificate": request.form["energy_certificate"],
            "has_parking": request.form.get("has_parking") == "on",
            "price_m2": float(request.form["price_m2"]),
        }

        df = pd.DataFrame([data])
        prediction = pipeline.predict(df)[0]

    return render_template("predictPrice.html", prediction=prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
