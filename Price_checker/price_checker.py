from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Price:

    def __init__(self):
        path = 'msedgedriver.exe'
        self.driver = webdriver.Edge(path)
        self.item = 'exalted orb'
        self.currency_type = 'Exalted Orb'
        self.buy_threshold = '13'
        self.sell_threshold = '14'

# Function checking if there are any offers cheaper than set threshold
    def check(self, item):
        self.driver.get('https://www.pathofexile.com/trade/search/Ultimatum')
        time.sleep(5)    # try WebdriverWait method is not working for some reason (element is located but I can't interact with it)
        text_field = self.driver.find_element_by_class_name('multiselect__input')
        text_field.send_keys(item)
        text_field.send_keys(Keys.RETURN)
        search_button = self.driver.find_element_by_class_name('controls')
        button = search_button.find_element_by_tag_name('span')
        button.click()

        try:
            table = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'resultset'))
            )
        except:
            print('nie dziala')
        time.sleep(5)
        rows = table.find_element_by_class_name('row')
        price = rows.find_elements_by_tag_name('span')
        if price[0].text == '':   # data = [amount, item price, currency type, item type]
            data = [1, price[-8].text, price[-5].text, price[1].text]
        else:
            data = [price[0].text, price[-8].text, price[-5].text, price[2].text]
        return data

    def compare(self, data, buy, sell):
        if buy == '':
            pass
        elif float(data[1]) <= float(buy):
            print(f'Buy {data[0]} {data[3]} for {float(data[0])*float(data[1])} {data[2]}')
        elif sell == '':
            pass
        elif float(data[1]) >= float(sell):
            print(f'Sell {data[0]} {data[3]} for {float(data[0])*float(data[1])} {data[2]}')

    def finish(self):
        self.driver.quit()

    def sleep(self, refesh_rate):
        time.sleep(refesh_rate)

    def execute(self):
        data = self.check(self.item)
        self.compare(data, self.buy_threshold, self.sell_threshold)
        self.finish()

if __name__ == '__main__':
    check = Price()
