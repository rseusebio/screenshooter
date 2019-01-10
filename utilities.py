import os
import time
from selenium.webdriver import Chrome, ChromeOptions
import pyscreenshot

base_directory = os.path.dirname(os.path.abspath(__file__))
chrome_path = os.path.join(base_directory, 'chromedriver_linux64/chromedriver')
scrolldown_js = '''
    if ( document.body.scrollHeight - window.scrollY > window.innerHeight ) {
        ((x)=>{
            window.scrollTo(0, window.scrollY + window.innerHeight/x);
            console.log("window scrolled to " + window.scrollY);
        })(1.2);
    }
    else{
        window.alert("It is all over");
    }
'''

def start_chrome_driver(chrome_path = chrome_path, headless = False):
    if chrome_path  == None:
        raise ValueError("Enter a path to the chrome driver executable.")
    elif type(chrome_path) != str:
        raise TypeError("Enter a string containing the path to the chrome driver executable.")
    else:
        try:
            chrome_options = ChromeOptions()
            if headless:
                chrome_options.add_argument('--headless')
            driver = Chrome(chrome_path, chrome_options=chrome_options)
            return driver
        except Exception as err:
            print("An error has occurred")
            raise err

def scroll_down_to_the_bottom(driver, printscreen=False, file_path=None):
    if type(file_path) != str:
        raise TypeError("file_path must be an string")
    else:
        count = 1
        while True:
            try:
                time.sleep(0.2)
                if printscreen:
                    img = pyscreenshot.grab()
                    img.save('{1}{0}.png'.format(count, file_path))
                    count+=1
                driver.execute_script(scrolldown_js)
            except Exception as err:
                alert = driver.switch_to.alert
                alert.accept()
                break
