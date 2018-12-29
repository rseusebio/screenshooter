import os
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
import pyscreenshot

base_directory = os.path.dirname(os.path.abspath(__file__))
chrome_path = os.path.join(base_directory, 'chromedriver_linux64/chromedriver')

def start_chrome_driver(chrome_path = None)
    if chrome_path  == None:
        raise ValueError("Enter a path to the chrome driver executable.")
    elif type(chrome_path) != str:
        raise TypeError("Enter a string contain the path to the chrome driver executable.")

chrome_options = ChromeOptions()
chrome_options.add_argument('--headless')
driver = Chrome(chrome_path, chrome_options=chrome_options)
driver.fullscreen_window()
driver.get('https://docs.python.org/3/')

big_link_elems = driver.find_elements_by_class_name("bigLink")

a_elem_counter = 0
print(len(big_link_elems))
for elem in big_link_elems:
    if elem.get_property("tagName") == "A":
        a_elem_counter+=1
        inner_text = elem.get_property("innerText")
        if inner_text.find("Python 3.7"):
            print("We found it")
            break
print("a_elem_counter = {0}".format(a_elem_counter))