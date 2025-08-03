import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import pickle

# Load dataset
df = pd.read_csv("mental_health_data.csv")

# Encode categorical variables
le = LabelEncoder()
df['RemoteWork'] = le.fit_transform(df['RemoteWork'])  # Yes=1, No=0
df['CompanySupport'] = le.fit_transform(df['CompanySupport'])
df['StressLevel'] = le.fit_transform(df['StressLevel'])  # Low=1, Medium=2, High=0 (varies)
df['PastHistory'] = le.fit_transform(df['PastHistory'])
df['MentalHealth'] = le.fit_transform(df['MentalHealth'])  # Yes=1, No=0

# Features & target
X = df[['WorkHours', 'RemoteWork', 'CompanySupport', 'StressLevel', 'PastHistory']]
y = df['MentalHealth']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create SVM model
model = SVC(kernel='linear', probability=True)
model.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
