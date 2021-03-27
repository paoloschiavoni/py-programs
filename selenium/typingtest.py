from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://10fastfingers.com/typing-test/italian")

driver.implicitly_wait(5)
searchbox=driver.find_element_by_xpath('//*[@id="inputfield"]')

while 1:
    parola=driver.find_element_by_class_name('highlight').text
    searchbox.send_keys(parola+' ')
