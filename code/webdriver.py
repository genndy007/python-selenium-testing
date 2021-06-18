import time
from selenium import webdriver


def check_page_loaded(driver: webdriver.Chrome):
    script_load_checker = 'return document.readyState;'
    complete = 'complete'
    return driver.execute_script(script_load_checker) == complete


url = "https://hotline.ua"

search_line = 'dell xps'
add_text = 'Додати до списку'
compare_text = 'ПОРІВНЯТИ ЦІНИ'

search_box_xpath = '//*[@id="searchbox"]'
search_button_xpath = '//*[@id="doSearch"]'

add_to_list_css = '#page-search > div.cell-fixed-indent.cell-md > div > div:nth-child(1) > div > div.clearfix > div > ul > li:nth-child(1) > div.item-info > ul > li > span > span.crutch-data'
compare_prices_css = '#page-search > div.cell-fixed-indent.cell-md > div > div:nth-child(1) > div > div.clearfix > div > ul > li:nth-child(1) > div.item-price.stick-bottom > div:nth-child(2) > a'

# TEST START

driver = webdriver.Chrome()  # Open browser
driver.get(url)   # Open website

while not check_page_loaded(driver):
    pass

input_box = driver.find_element_by_xpath(search_box_xpath)  # find input box
input_box.send_keys(search_line)     # fill input box

while not check_page_loaded(driver):
    pass

driver.find_element_by_xpath(
    search_button_xpath).click()   # click search button

time.sleep(2)


add_to_list_el = driver.find_element_by_css_selector(add_to_list_css)


print(add_to_list_el.text)
print(add_to_list_el.text == add_text)


compare_prices_el = driver.find_element_by_css_selector(compare_prices_css)

print(compare_prices_el.text.strip())
print(compare_prices_el.text.strip() == compare_text)
