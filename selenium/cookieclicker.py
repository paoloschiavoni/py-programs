from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://orteil.dashnet.org/cookieclicker/')

cookie=driver.find_element_by_id('bigCookie')
cookie_count=driver.find_element_by_id('cookies')
driver.implicitly_wait(10)

items=[driver.find_element_by_id('productPrice'+str(i)) for i in range(1, -1, -1)]#va da 1 a 0 andando al contrario
contatore=-1#degli item

actions=ActionChains(driver)
actions.click(cookie)
for i in range(2000):
    actions.perform()
    count=int(cookie_count.text.split(' ')[0].replace(" ", ""))
    for item in items:
        value=int(item.text.replace(",", ""))
        if value<=count:
            newaction=ActionChains(driver)
            newaction.move_to_element(item)
            newaction.click()
            newaction.perform()
