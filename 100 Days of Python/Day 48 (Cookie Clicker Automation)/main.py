from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from threading import Timer


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

action = ActionChains(driver)

cookie = driver.find_element(By.ID, 'cookie')
money = driver.find_elements(By.ID, 'money')

def buy_upgrade():
        b_cursor = driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b').text
        b_grandma = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]/b').text.replace(',', '')
        b_factory = driver.find_element(By.XPATH, '//*[@id="buyFactory"]/b').text.replace(',', '')
        b_mine = driver.find_element(By.XPATH, '//*[@id="buyMine"]/b').text.replace(',', '')
        b_shipment = driver.find_element(By.XPATH, '//*[@id="buyShipment"]/b').text.replace(',', '')
        b_alchemy = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]/b').text.replace(',', '')
        b_portal = driver.find_element(By.XPATH, '//*[@id="buyPortal"]/b').text.replace(',', '')
        b_time_machine = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]/b').text.replace(',', '')
        b_elder = driver.find_element(By.XPATH, '//*[@id="buyElder Pledge"]/b').text.replace(',', '')
        result = (b_cursor + ' ' + b_grandma + ' ' + b_factory+ ' ' + b_mine+ ' ' + b_shipment+ ' ' + b_alchemy+ ' ' + b_portal+ ' ' + b_time_machine+ ' ' + b_elder)
        godlike = [i for i in result.split(' ') if i.isnumeric()]
        for j in money:
            cookie_currency = j.text
            for x in godlike:
                if cookie_currency >= x:
                    if godlike.index(x) == 0:
                        cursor = driver.find_element(By.ID, 'buyCursor')
                        action.click(cursor)
                        action.perform()
                    elif godlike.index(x) == 1:
                        grandma = driver.find_element(By.ID, 'buyGrandma')
                        action.click(grandma)
                        action.perform()
                    elif godlike.index(x) == 2:
                        factory = driver.find_element(By.ID, 'buyFactory')
                        action.click(factory)
                        action.perform()
                    elif godlike.index(x) == 3:
                        mine = driver.find_element(By.ID, 'buyMine')
                        action.click(mine)
                        action.perform()
                    elif godlike.index(x) == 4:
                        shipment = driver.find_element(By.ID, 'buyShipment')
                        action.click(shipment)
                        action.perform()
                    elif godlike.index(x) == 5:
                        alchemy_lab = driver.find_element(By.ID, 'buyAlchemy lab') 
                        action.click(alchemy_lab)
                        action.perform()
                    elif godlike.index(x) == 6:
                        portal = driver.find_element(By.ID, 'buyPortal')
                        action.click(portal)
                        action.perform()
                    else:
                        time_machine = driver.find_element(By.ID, 'buyTime machine')
                        action.click(time_machine)
                        action.perform()
                    break

def stop_time():
    global is_on
    is_on = False
    global timer_is_on
    timer_is_on = False
    for i in money:
        print(f'cookies/second: {i.text}')
    driver.quit()


timer = 0
Timer(300, stop_time).start()
is_on = True
while is_on:
    action = ActionChains(driver)
    action.click(cookie)
    action.perform()
    timer += 1
    if timer % 5 == 0:
        buy_upgrade()