import justpy as jp

def hello_world():
    wp = jp.WebPage()
    root = jp.Div(a=wp)
    c1 = jp.A(href='https://unpkg.com/tailwindcss/dist/tailwind.min.css', rel='stylesheet', a=root)
    c2 = jp.A(href='https://afeld.github.io/emoji-css/emoji.css', rel='stylesheet', a=root)
    c3 = jp.Div(classes='bg-gray-400 font-sans leading-normal tracking-normal', a=root)
    c4 = jp.Nav(classes='bg-gray-800 p-2 mt-0 fixed w-full z-10 top-0', a=c3)
    c5 = jp.Div(classes='container mx-auto flex flex-wrap items-center', a=c4)
    c6 = jp.Div(classes='flex w-full md:w-1/2 justify-center md:justify-start text-white font-extrabold', a=c5)
    c7 = jp.A(classes='text-white no-underline hover:text-white hover:no-underline', href='#', a=c6)
    c8 = jp.Span(classes='text-2xl pl-2', a=c7)
    c9 = jp.I(classes='em em-email', a=c8, text='Spam Detector')
    c10 = jp.Div(classes='flex w-full pt-2 content-center justify-between md:w-1/2 md:justify-end', a=c5)
    c11 = jp.Div(classes='container shadow-lg mx-auto bg-white mt-24 md:mt-16 h-screen', a=c3)

    return wp

jp.justpy(hello_world)