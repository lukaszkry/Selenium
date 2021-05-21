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
        self.item = 'mirror shard'
        self.currency_type = 'Exalted Orb'
        self.currency_threshold = 13

# Function checking if there are any offers cheaper than set threshold
    def check(self):
        self.driver.get('https://www.pathofexile.com/trade/search/Ultimatum')
        time.sleep(5)    # try WebdriverWait method is not working for some reason (element is located but I can't interact with it)
        text_field = self.driver.find_element_by_class_name('multiselect__input')
        text_field.send_keys(self.item)
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
        for x in price:
            print(x.text)
        data = [price[0].text, price[9].text, price[12].text]
        self.driver.quit()
        return data

    def compare(self, data):
        if data[2].lower() == self.currency_type.lower():
            if float(data[1]) <= self.currency_threshold:
                print(f'Buy {data[0]} for {float(data[0])*float(data[1])} {data[2]}')
            else:
                print("Too expensive!")
        else:
            print('Wrong currency type!')

    def execute(self):
        data = self.check()
        print(data)
        self.compare(data)


a = Price()
a.execute()
