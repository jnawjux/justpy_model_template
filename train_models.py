import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pickle

# This model and data for the spam bot courtesy of repo: mileserickson/flask-brython-example/


def load_enron_data(path):
    """Load Enron email data from path into a file."""
    for filename in os.listdir(path):
        row = {
            'filename': filename,
            'content': open(os.path.join(path, filename), 'r', encoding='latin1').read()
        }
        yield row


spam_df = pd.DataFrame(load_enron_data('data/enron/spam/'))
spam_df['is_spam'] = True

ham_df = pd.DataFrame(load_enron_data('data/enron/ham'))
ham_df['is_spam'] = False


email_df = pd.concat([spam_df, ham_df], axis=0)

vec = TfidfVectorizer(stop_words='english')
model = MultinomialNB()

pipeline = Pipeline([
    ('vectorizer', TfidfVectorizer(stop_words='english')),
    ('model', MultinomialNB())
])

pipeline.fit(email_df['content'], email_df['is_spam'])

with open('spam_model.pkl', 'wb') as f:
    pickle.dump(pipeline, f)


# This data courtesy of Kaggle (https://www.kaggle.com/c/titanic/data) hastely made model my own doing

titanic_df = pd.read_csv('data/titanic/train.csv')

titanic_df.drop(columns=['PassengerId', 'Name', 'Ticket',
                         'Cabin', 'SibSp', 'Parch'], inplace=True)
titanic_df['Sex'] = titanic_df['Sex'].map({'female': 1, 'male': 0}).astype(int)
titanic_df['Age'].fillna(titanic_df['Age'].median(), inplace=True)
titanic_df.dropna(inplace=True)
titanic_df['age_group'] = pd.qcut(titanic_df['Age'], 4)
titanic_df['fare_group'] = pd.qcut(titanic_df['Fare'], 4)
titanic_df.drop(columns=['Age', 'Fare'], inplace=True)
age_df = pd.get_dummies(titanic_df['age_group'], prefix="age")
fare_df = pd.get_dummies(titanic_df['fare_group'], prefix="fare")
class_df = pd.get_dummies(titanic_df['Pclass'], prefix="class")
embark_df = pd.get_dummies(titanic_df['Embarked'], prefix="embark")
titanic_df = pd.concat([titanic_df, age_df, fare_df, class_df], axis=1)
titanic_df.drop(columns=['age_group', 'fare_group',
                         'Pclass', 'Embarked'], inplace=True)

"""Columns used for reference: ['Sex', 'age_(0.419, 22.0]', 'age_(22.0, 28.0]',
'age_(28.0, 35.0]', 'age_(35.0, 80.0]', 'fare_(-0.001, 7.896]',
'fare_(7.896, 14.454]', 'fare_(14.454, 31.0]', 'fare_(31.0, 512.329]',
'class_1', 'class_2', 'class_3'] """

X = titanic_df.drop(['Survived'], axis=1)
y = titanic_df['Survived']


log_model = LogisticRegression()
log_model.fit(X, y)

with open('titanic_model.pkl', 'wb') as f:
    pickle.dump(log_model, f)
