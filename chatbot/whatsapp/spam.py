from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
print('scan qr code')
input()

contatto=str(input('contatto: '))
#adesso devo trovare il contatto, dalla pagina html del sito
search_box=driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")
search_box.send_keys(contatto)
search_box.send_keys(Keys.ENTER)

for i in range(300):
    msg_box=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
    msg_box.send_keys('f')
    msg_box.send_keys(Keys.ENTER)
driver.quit()
