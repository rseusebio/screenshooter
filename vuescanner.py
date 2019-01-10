import os
import time
from selenium.webdriver import Chrome
from utilities import scroll_down_to_the_bottom, start_chrome_driver, chrome_path

def scan_vue_documentation(driver = None):
    global define_function_js, scrolldown_js, show_defined_function
    if type(driver) != Chrome:
        raise TypeError("driver must be a Chrome instance")
    else:
        driver.get('https://vuejs.org/v2/guide/')

if __name__ == '__main__':
    driver = start_chrome_driver(chrome_path, False)
    scan_vue_documentation(driver)
    driver.fullscreen_window()
    # os.mkdir("./vuefiles1/")
    # scroll_down_to_the_bottom(driver, True, './vuefiles1/vue')
    driver.quit()



