import  time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

Chrome_options=Options()
Chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=Chrome_options)

driver.maximize_window()

driver.get("https://omayo.blogspot.com/")

drp=driver.find_element(By.ID,"drop1")

drpUse=Select(drp)

#drpUse.select_by_index(4)



time.sleep(2)

# drpUse.deselect_by_visible_text('doc 4')

drpUse.select_by_value()

drpUse.select_by_value()

drpUse.select_by_value()

drpUse.select_by_value()

drpUse.select_by_value()
