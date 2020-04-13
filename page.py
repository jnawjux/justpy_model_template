import justpy as jp
import random
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pickle

with open('spam_model.pkl', 'rb') as f:
    model = pickle.load(f)

template = "THHIIIE"


async def predict(self, msg):
    self.div.text = self.value


async def page():
    wp = jp.WebPage()
    wp.head_html = "<link href='https://afeld.github.io/emoji-css/emoji.css' rel='stylesheet'></link>"
    root = jp.Div(a=wp)
    body = jp.Div(
        classes='bg-gray-400 font-sans leading-normal tracking-normal', a=root)
    c2 = jp.Nav(classes='bg-gray-800 p-2 mt-0 w-full', a=body)
    c3 = jp.Div(classes='container mx-auto flex flex-wrap items-center', a=c2)
    c4 = jp.Div(
        classes='flex w-full md:w-1/2 justify-center md:justify-start text-white font-extrabold', a=c3)
    logo_link = jp.A(
        classes='text-white no-underline hover:text-white hover:no-underline', href='#', a=c4)
    logo_cont = jp.Span(classes='flex text-2xl pl-2', a=logo_link)
    logo = jp.I(classes='em em-email my-auto', a=logo_cont)
    title = jp.Div(classes="p-2", text="Spam Detector", a=logo_cont)
    cont_main = jp.Div(
        classes='container mx-auto flex flex-col md:flex-row items-center my-6 md:my-12', a=body)
    cont_left = jp.Div(
        classes='flex flex-col w-full lg:w-1/2 justify-center items-start pt-12 pb-24 px-6', a=cont_main)
    tagline = jp.P(classes='uppercase tracking-loose',
                   a=cont_left, text='Version: 1.0')
    main_title = jp.H1(classes='font-bold text-3xl my-4',
                       a=cont_left, text='Spam Detector')
    description = jp.P(classes='leading-normal mb-4', a=cont_left,
                       text='Keep the bad guys out! Enter the text of your email below and the Spam Detector will tell you how likely it\'s contents is spam:')
    text_in = jp.Textarea(classes='w-full border-2 h-32',
                          placeholder='Please type here', a=cont_left)
    text_in.button = jp.Button(classes='my-4 bg-transparent hover:bg-gray-900 text-gray-900 hover:text-white rounded shadow hover:shadow-lg py-2 px-4 border border-gray-900 hover:border-transparent',
                               a=cont_left, text='See Your Results')
    text_in.div = jp.Div(text='Results: ', a=cont_left)
    cont_right = jp.Div(
        classes='w-full lg:w-1/2 lg:py-6 text-center', a=cont_main)
    mailbox = jp.I(
        classes='text-6xl w-3/5 mx-auto em-svg em-mailbox_with_mail', viewBox='0 0 20 20', a=cont_right)
    footer = jp.Div(classes='bg-white h-1', a=body)
    footer_cont = jp.Div(
        classes='container mx-auto pt-12 md:pt-6 px-6', a=footer)
    footer_text_cont = jp.P(classes='py-4', a=footer_cont)
    love = jp.I(classes='em em-hearts', a=footer_text_cont)
    data = jp.I(classes='em em-bar_chart', a=footer_text_cont)
    science = jp.I(classes='em em-test_tube', a=footer_text_cont)

    return wp


"""@app.route('/predict', methods=['GET', 'POST'])
def predict():
    data = request.json
    prediction = model.predict_proba([data['user_input']])
    return jsonify({'probability': prediction[0][1]})"""


jp.justpy(page)
