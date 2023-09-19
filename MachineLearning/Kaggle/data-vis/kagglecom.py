



import pandas as pd

data = pd.read_csv('')
test = pd.read_csv('')

def clean(data):
    data = data.drop(['Ticket', 'Cabin', 'Name', 'PassengerId'], axis=1)

    cols = ['SibSp', 'Parch', 'Fare', 'Age']
    for col in cols:
        data[col].fillna(data[col].median(), inplace=True)

    data.Embarked.fillna('U', inplace=True)
    return data

data = clean(data)
test = clean(test)


from sklearn import preprocessing

le = preprocessing.LabelEncoder()

cols = ["Sex", "Embarked"]

for col in cols:
    data[col] = le.fit_transform(data[col])
    test[col] = le.transform(data[col])
    print(le.classes_)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

y = data['Survived']
X = data.drop('Survived', axis=1)

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

clf = LogisticRegression(random_state=0, max_iter=1000).fit(X_train, y_train)

predictions = clf.predict(X_val)
from sklearn.metrics import accuracy_score
accuracy_score(y_val, predictions)

submission_preds = clf.predict(test)

df = pd.DataFrame({"PassengerId": test.values, 'Survived': submission_preds})

df.to_csv("submission.csv", index=False)



