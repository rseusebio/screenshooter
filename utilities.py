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

def scroll_down_to_the_bottom(driver, printscreen=False, file_name='file'):
    count = 1
    while True:
        try:
            driver.execute_script(scrolldown_js)
            time.sleep(0.2)
            if printscreen:
                img = pyscreenshot.grab()
                img.save('{1}{0}.png'.format(count, file_name))
                count+=1
        except Exception as err:
            alert = driver.switch_to.alert
            alert.accept()
            break

    # driver.execute_script('''console.log('done')''')
    # actions = ActionChains(driver)
    # actions.key_down(Keys.ENTER)
    # actions.perform()
#
# if __name__ == "__main__":
#     driver = start_chrome_driver(chrome_path)
#     scan_vue_documentation(driver)
#     count = 1
#     while True:
#         try:
#             scrolldown(driver, count)
#             count+=1
#         except Exception as err:
#             print(err)
#             print("------------")
#             for prop in dir(err):
#                 print(prop)
#             print("-------------")
#             break
#     print("We breaked")
#     time.sleep(2)
#     alert = driver.switch_to.alert
#     alert.accept()
#     time.sleep(1)
#     print("done :)")
#     driver.get("http://google.com")
#     actions = ActionChains(driver)
#     actions.key_down(Keys.ENTER)
#     actions.key_up(Keys.ENTER)
#     actions.perform()
#     print("And it is done.")
#     time.sleep(3)
#     driver.quit()
#     print("The end!...")

