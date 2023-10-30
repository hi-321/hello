import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

file_name = input("Enter the dataset file name (e.g. 'data.csv'): ")
data = pd.read_csv("")

if 'id' in data.columns:
    data.drop(columns='id', inplace=True)
for column in data.columns:
    if data[column].dtype == 'float64' or data[column].dtype == 'int64':
        data[column].fillna(data[column].median(), inplace=True)
    else:
        data[column].fillna(data[column].mode()[0], inplace=True)

data = pd.get_dummies(data=data, drop_first=True)
X = data.iloc[:, :-1]
Y = data.iloc[:, -1]

test_train = float(input("Enter the test_train percentage (e.g. 0.4): "))
criterion = input("Enter the criterion for the Random Forest Classifier (e.g. 'gini' or 'entropy'): ")
n_estimators = int(input("Enter the number of decision trees for the Random Forest Classifier: "))

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_train, random_state=42, stratify=Y)
model = RandomForestClassifier(n_estimators=n_estimators, bootstrap=True, max_samples=0.5, criterion=criterion)
model.fit(X_train, Y_train)
pred = model.predict(X_test)

print('Accuracy is ', accuracy_score(Y_test, pred)*100, end='\n\n')
cm = confusion_matrix(Y_test, pred)
print(cm)