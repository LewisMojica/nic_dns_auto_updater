from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://cp.midominio.do')


type_box = Select(driver.find_element(By.ID,'login-role'))
type_box.select_by_visible_text('Cliente')

email_box = driver.find_element(By.ID,'login-username')
email_box.clear()
email_box.send_keys('mojicalewis@gmail.com')

pass_box = driver.find_element(By.ID,'login-password')
pass_box.clear()
pass_box.send_keys('TMH0@viB1JXT3')

#sleep(5)
email_box.send_keys(Keys.RETURN)
#sleep(5)

driver.get('https://cp.midominio.do/servlet/ListAllOrdersServlet?formaction=listOrders')
#sleep(5)

driver.find_element(By.LINK_TEXT,'royaltaste.com.do').click()
sleep(5)

driver.find_element(By.CSS_SELECTOR,'div.className[title="Gestionar DNS"]').click()

sleep(5)

driver.close()