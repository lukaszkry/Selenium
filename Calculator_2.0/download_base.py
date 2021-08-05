# Download product base from https://www.fitatu.com/catalog/pl
from selenium import webdriver
import pandas as pd

class Getdata:

    def __init__(self):
        path = 'msedgedriver.exe'
        self.driver = webdriver.Edge(path)
        self.df = pd.read_csv("calorie_base.csv")
        self.temp = []

    def get_data(self, link):
        self.driver.get(link)
        name = self.driver.find_element_by_tag_name('strong')
        table = self.driver.find_element_by_class_name('product-page__informations')
        rows = table.find_elements_by_tag_name('span')

        self.temp.append({
            'Nazwa': name.text,
            'Wartość energetyczna': rows[1].text,
            'Białka': rows[3].text,
            'Zwierzęce': rows[5].text,
            'Roślinne': rows[7].text,
            'Tłuszcze': rows[9].text,
            'Nasycone': rows[11].text,
            'Jednonienasycone': rows[13].text,
            'Wielonienasycone': rows[15].text,
            'Węglowodany': rows[17].text,
            'Węglowodany netto': rows[19].text,
            'Cukry': rows[21].text,
            'Cholesterol': rows[23].text,
            'Błonnik': rows[25].text
        })

        data = pd.DataFrame(self.temp)
        data = data.apply(lambda x: x.str.replace('b.d.', '0') if x.name != 'Name' else x)
        data[['Wartość energetyczna', 'Białka', 'Zwierzęce', 'Roślinne', 'Tłuszcze', 'Nasycone', 'Jednonienasycone', 'Wielonienasycone', 'Węglowodany', 'Węglowodany netto', 'Cukry', 'Cholesterol', 'Błonnik']] = data[[ 'Wartość energetyczna', 'Białka', 'Zwierzęce', 'Roślinne', 'Tłuszcze', 'Nasycone', 'Jednonienasycone', 'Wielonienasycone', 'Węglowodany', 'Węglowodany netto', 'Cukry', 'Cholesterol', 'Błonnik']].astype(float)
        self.df = self.df.append(data, ignore_index=True)
        self.df.to_csv(r'calorie_base.csv', index=False)

    def finish(self):
        self.driver.quit()

if __name__ == '__main__':
    scrapper = Getdata()

scrapper.get_data('https://www.fitatu.com/catalog/pl/bataty--24777027')
scrapper.finish()
