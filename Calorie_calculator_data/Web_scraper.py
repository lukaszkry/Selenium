from selenium import webdriver
import pandas as pd

PATH = 'msedgedriver.exe'

driver = webdriver.Edge(PATH)

product_list = []
product = []
counter = 0
page = 1

while page < 138:

    driver.get(f'https://kalkulatorkalorii.net/tabela-kalorii/{page}')

    table = driver.find_element_by_class_name('tab-content')
    products = table.find_elements_by_tag_name('td')

    for item in products:
        if counter < 5:
            product.append(item.text)
            counter = counter + 1
        else:
            product_list.append(product)
            product = []
            counter = 0

    page += 1

driver.quit()

df = pd.DataFrame(product_list, columns=['Name', 'Calories', 'Protein', 'Carbs', 'Fat'])

# 'cleanups'
df = df.apply(lambda x: x.str.replace(',', '.') if x.name != 'Name' else x)
df[['Calories', 'Protein', 'Carbs', 'Fat']] = df[['Calories', 'Protein', 'Carbs', 'Fat']].astype(float)

# export data to csv file
df.to_csv(r'calorie_base.csv', index=False)
