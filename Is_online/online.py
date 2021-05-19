from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class IsOnline:

    def __init__(self):
        PATH = 'msedgedriver.exe'
        self.driver = webdriver.Edge(PATH)

    # Function check if character exist, if exist function will return name of the server on which the character is
    def if_exist(self, nick):
        # Find entry field, input nick, click button
        self.driver.get('https://www.tibia.com/community/?subtopic=characters')
        border = self.driver.find_element_by_class_name('Border_3')
        submit = border.find_elements_by_tag_name('input')
        submit[0].send_keys(nick)
        submit[1].click()

        # If character exist function returns server's name, timeout == character does not exist
        try:
            table = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.TAG_NAME, 'table'))
            )
            columns = table.find_elements_by_tag_name('td')
            if columns[13].text == 'World:':
                server = columns[14].text
            else:
                server = columns[16].text
        except:
            server = None

        return server

    def is_playing(self, server):
        players_online = []
        self.driver.get(f'https://www.tibia.com/community/?subtopic=worlds&world={server}')
        table = self.driver.find_element_by_class_name('Table2')
        players = table.find_elements_by_tag_name('a')
        for player in players:
            players_online.append(player.text)
        return players_online

    def checking(self, nick):
        server = self.if_exist(nick)
        if server is None:
            result = nick + ' does not exist'
        else:
            player_list = self.is_playing(server)
            if nick in player_list:
                result = nick + ' is online'
            else:
                result = nick + ' is offline'
        self.driver.quit()
        return result

