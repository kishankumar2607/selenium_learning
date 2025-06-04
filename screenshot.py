from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def search(search_term):
    driver.get("https://www.duckduckgo.com/")

    #Wait and look for search bar
    searchbar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))

    #Send text keys
    searchbar.send_keys(search_term + Keys.ENTER)

    time.sleep(6)
    driver.save_screenshot("results.png")
    print("Screenshot saved")

    driver.quit()

if __name__ == "__main__":
    search("Bollywood songs")