import pickle 
import pandas as pd  
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, mean_absolute_percentage_error

df =  pd.read_csv("bdd/processed/madrid_nettoye.csv")

#création d'une colonne pour le prix au m²

df["price_m2"] = (
    df['neighborhood_id']
    .str.extract(r"\(([\d\.]+)\s*€/m2\)")
    .astype(float)
)

#suppréssion des outliers
q1 = df["buy_price"].quantile(0.02)
q99 = df["buy_price"].quantile(0.98)
df = df[(df["buy_price"] >= q1) & (df["buy_price"] <= q99)]

X = df.drop(columns=["title","subtitle",'neighborhood_id',"buy_price","buy_price_by_area","is_buy_price_known","rent_price","is_rent_price_known",'is_exact_address_hidden'])
X = X.dropna()
y = df["buy_price"]
y = y[X.index]  # garder les mêmes index



X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


with open('src/XGBoost.pkl','rb') as f :
   model = pickle.load(f)


y_pred = model.predict(X_test)
y_test_real = y_test  

 

mae = mean_absolute_error(y_test_real, y_pred)
r2 = r2_score(y_test_real, y_pred)
mape = mean_absolute_percentage_error(y_test_real, y_pred)

print(f"XGB MAE  : {mae:,.0f} €")
print(f"XGB R²   : {r2:.3f}")
print(f"XGB MAPE : {mape*100:.2f} %")


