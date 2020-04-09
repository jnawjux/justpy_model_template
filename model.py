import justpy as jp


async def my_input(self, msg):
    self.div.text = self.value


def spam_detector():
    wp = jp.WebPage()
    emoji_style = jp.A(href='https://afeld.github.io/emoji-css/emoji.css', classes='invisible', html_tag="link",
                       rel='stylesheet', a=wp)
    container = jp.Div(
        classes='bg-gray-400 font-sans leading-normal tracking-normal mx-auto mt-0', a=wp)
    nav = jp.Nav(
        classes='bg-gray-800 p-2 mt-0 fixed w-full z-10 top-0', a=container)
    nav_cont = jp.Div(
        classes='container mx-auto flex flex-wrap items-center', a=nav)
    title_area = jp.Div(
        classes='flex w-full md:w-1/2 justify-center md:justify-start text-white font-extrabold', a=nav_cont)
    mail = jp.I(classes='flex-initial em em-email', a=title_area)
    title = jp.Div(classes='flex-initial justify-center text-white font-extrabold pl-2',
                   text='Spam Detector', a=title_area)
    main = jp.Div(
        classes="container shadow-lg mx-auto bg-white h-screen", a=container)
    in1 = jp.Div(a=main, classes='m-20 w-2/3 p-2 h-32 text-xl border-2', html_tag='textarea',
                 placeholder='Please type here')
    return wp


jp.justpy(spam_detector)
