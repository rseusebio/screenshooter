import os
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
import pyscreenshot

base_directory = os.path.dirname(os.path.abspath(__file__))
chrome_path = os.path.join(base_directory, 'chromedriver_linux64/chromedriver')

def start_chrome_driver(chrome_path = None):
    if chrome_path  == None:
        raise ValueError("Enter a path to the chrome driver executable.")
    elif type(chrome_path) != str:
        raise TypeError("Enter a string contain the path to the chrome driver executable.")
    else:
        try:
            chrome_options = ChromeOptions()
            # chrome_options.add_argument('--headless')
            driver = Chrome(chrome_path, chrome_options=chrome_options)
            return driver
        except Exception as err:
            print("An error has occurred")
            raise err

def start_python_doc_scan(driver=None):
    if type(driver) != Chrome:
        raise TypeError("The driver must be an Chrome class instance.")
    else:
        # driver.fullscreen_window()
        driver.get('https://docs.python.org/3/')
        big_link_elems = driver.find_elements_by_class_name("biglink")
        a_elem_counter = 0
        print("elems found: {0}".format(len(big_link_elems)))
        for elem in big_link_elems:
            if elem.get_property("tagName") == "A":
                a_elem_counter+=1
                inner_text = elem.get_property("innerText")
                if inner_text.find("Python 3.7"):
                    return elem
        print("a_elem_counter = {0}".format(a_elem_counter))

def screenshot_all_the_pages(driver, start_link):
    if type(driver) != Chrome and type(start_link) != object:
        raise TypeError()
    else:
        start_link.click()
        img = pyscreenshot.grab()
        img.save(os.path.join(base_directory, 'test.jpg'))
        a_elems = driver.find_element_by_tag_name('')

if __name__ == "__main__":
    driver = start_chrome_driver(chrome_path)
    start_link  = start_python_doc_scan(driver)
    screenshot_all_the_pages(driver, start_link)
    driver.quit()