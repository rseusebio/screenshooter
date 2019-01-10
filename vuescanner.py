import os
import time
from selenium.webdriver import Chrome
from utilities import scroll_down_to_the_bottom, start_chrome_driver, chrome_path

# Some Global Variables
main_vue_folder = "./vue_get_started/"
page_folder_name = "vuepage"

def scan_vue_documentation(driver = None):
    global define_function_js, scrolldown_js, show_defined_function
    if type(driver) != Chrome:
        raise TypeError("driver must be a Chrome instance")
    else:
        driver.get('https://vuejs.org/v2/guide/')

def find_next_link(driver = None):
    if type(driver) != Chrome:
        raise TypeError("driver must be a Chrome instance")
    else:
        try:
            guide_links = driver.find_elements_by_class_name("guide-links")
            print("length of guide_links = {0}".format(len(guide_links)))
            guide_link = guide_links[0]
            print("guide_link = {0}".format(guide_link))
            children = guide_link.get_property("children")
            print("length of children = {0}".format(len(children)))
            next_link = children[1]
            print("next_link = {0}".format(next_link))
            return next_link
        except Exception as err:
            print(err)
            return None

def scan_single_page(number):
    if type(number) == int:
        folder_path = os.path.join(main_vue_folder, page_folder_name + "{0}/".format(number))
        file_path = os.path.join(folder_path, "vue")
        print("folder_path = {0} and file_path = {1}".format(folder_path, file_path))
        os.mkdir(folder_path)
        scroll_down_to_the_bottom(driver, True, file_path)
    else:
        raise TypeError("number param must be an integer.")

if __name__ == '__main__':
    driver = start_chrome_driver(chrome_path, False)
    scan_vue_documentation(driver)
    driver.fullscreen_window()
    os.mkdir(main_vue_folder)

    count = 1
    scan_single_page(count)
    next_link = find_next_link(driver)

    while next_link != None:
        count += 1
        next_link.click()
        time.sleep(0.5)
        scan_single_page(count)
        next_link = find_next_link(driver)
    driver.quit()



