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


# Loading data
spam_df = pd.DataFrame(load_enron_data('data/enron/spam/'))
spam_df['is_spam'] = True

ham_df = pd.DataFrame(load_enron_data('data/enron/ham'))
ham_df['is_spam'] = False

# Creating one dataframe
email_df = pd.concat([spam_df, ham_df], axis=0)

# Vectorize text, then run through model
vec = TfidfVectorizer(stop_words='english')
model = MultinomialNB()

pipeline = Pipeline([
    ('vectorizer', TfidfVectorizer(stop_words='english')),
    ('model', MultinomialNB())
])

pipeline.fit(email_df['content'], email_df['is_spam'])

# Pickling spam model pipeline
with open('spam_model.pkl', 'wb') as f:
    pickle.dump(pipeline, f)
