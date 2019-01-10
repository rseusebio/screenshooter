import os
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
import pyscreenshot

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