import eel
import glob


eel.init('web')


@eel.expose
def say_hello_py():
    mp3_files = glob.glob('web/sounds/*.mp3')
    eel.say_hello_js(mp3_files)

web_app_options = {
    'mode': "chrome-app",
    'port': 8080,
    'chromeFlags': ["--start-fullscreen"]
}

eel.start('main.html', block=True, options=web_app_options)
