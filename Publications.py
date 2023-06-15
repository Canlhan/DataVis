# publications.py

import json
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class Publications:
    def __init__(self):
        self.publication_data = []
        self.driver = self.setup_driver()
        self.years={}
    def setup_driver(self):
        chrome_options = Options()

        return webdriver.Chrome(options=chrome_options)
    def fetch_publications_data(self):

        # Use Selenium to fetch data from your website
          # Assuming you have Chrome webdriver installed
        self.driver.get('http://boracanbula.com.tr')  # Go to your personal website
        # Perform necessary actions to navigate to the Publications tab and fetch the data
        time.sleep(3)
        publicaitons=self.driver.find_element(By.CSS_SELECTOR,('[href="#articles"]'))
        publicaitons.click()


        articles=self.driver.find_element(By.XPATH,"//*[@id='articles']")
        articles_ul=articles.find_elements(By.TAG_NAME,"ul")
        for ar in articles_ul:
            title=ar.find_element(By.TAG_NAME,"a").text
            spans=ar.find_elements(By.TAG_NAME,"span")
            authors=spans[0].text.split(",")
            year=spans[1].text.split(",")[2]
            if year not in self.years:
                self.years[year] = 1
            else:
                self.years[year] += 1



            self.publication_data.append({'title':title,'year':year,'authors':authors})

        # Example: Fetching publication data and storing in self.data




    def get_years_dict(self):

        return self.years

    def save_data_to_json(self):
        # Save the fetched data to a JSON file
        with open('data.json', 'w') as json_file:
            print("sdfsd")
            json.dump(self.publication_data, json_file)


# app.py

if __name__=="__main__":
    pub=Publications()
    pub.fetch_publications_data()
    pub.save_data_to_json()