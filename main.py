import keyring
import urllib.request
from dns import resolver
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


def getMyIp():
    return urllib.request.urlopen('https://ident.me').read().decode('utf8')

def updateDNS(dns_map):
    driver = webdriver.Chrome()
    driver.get('https://cp.midominio.do')

    username = 'mojicalewis@gmail.com'

    type_box = Select(driver.find_element(By.ID,'login-role'))
    type_box.select_by_visible_text('Cliente')

    email_box = driver.find_element(By.ID,'login-username')
    email_box.clear()
    email_box.send_keys(username)

    pass_box = driver.find_element(By.ID,'login-password')
    pass_box.clear()
    pass_box.send_keys(keyring.get_password('nic_dns_auto_updater',username))

    #sleep(5)
    print('logging in')
    email_box.send_keys(Keys.RETURN)
    print('logged in')
    #sleep(5)

    driver.get('https://cp.midominio.do/servlet/ListAllOrdersServlet?formaction=listOrders')
    #sleep(5)

    driver.find_element(By.LINK_TEXT,'royaltaste.com.do').click()

    sleep(5)
    driver.find_element(By.CSS_SELECTOR,'div.ul-list-float-block[title="Gestionar DNS"]').click()

    sleep(10)
    driver.switch_to.window(driver.window_handles[1])
    sleep(5)


    for sub_domain in dns_map:
        print(f'updating {sub_domain[0]} to {sub_domain[1]}')
        driver.find_element(By.LINK_TEXT,sub_domain[0]).click()
        driver.find_element(By.CSS_SELECTOR,'input.submit[name="btnModRecord"]').click()


        ip_box = driver.find_element(By.CSS_SELECTOR,'input[name="IPvalue"]')
        ip_box.clear()
        ip_box.send_keys(sub_domain[1])
        driver.find_element(By.CSS_SELECTOR,'input.submit[name="submitform"]').click()
        sleep(5)
        driver.execute_script("window.history.go(-3)")

    sleep(5)
    driver.quit()
    print('done')


def getDomainIP(domain):
    res = resolver.Resolver()
    res.nameservers = ['8.8.8.8']

    return res.resolve(domain)[0].address


if __name__ == "__main__":

    dns_ip = getDomainIP('nextcloud.royaltaste.com.do')
    current_ip = getMyIp()


    print(f'real public ip > {current_ip}')
    print(f'dns map ip > {dns_ip}')

    if current_ip == dns_ip:
        print('DNS record good. DNS won\'t be updated.')
    else:
        print('DNS record bad. Updating DNS.')
        updateDNS([['royaltaste.com.do',current_ip],['nextcloud.royaltaste.com.do',current_ip]])
