from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def check_free_at_kvarnvreten(driver):
    driver.get("https://kvarnvreten.se/")
    assert "Kvarnvreten Fastighet" in driver.title
    elems = driver.find_elements_by_class_name('col-3')
    elems.pop(0)
    for element in elems:
        status = element.find_element_by_tag_name('p')
        if status.text != "Lediga lägenheter: 0":
            print(element.find_element_by_tag_name('a').get_attribute("href"))
            

def main():
    driver = webdriver.Firefox() 
    check_free_at_kvarnvreten(driver)
    driver.close()

if __name__ == "__main__":
    main()