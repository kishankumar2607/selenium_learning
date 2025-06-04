from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def music(search_term):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.youtube.com/")

    #Wait and look for search bar
    searchbar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "search_query")))

    #Send text keys
    searchbar.send_keys(search_term + Keys.ENTER)

    #Wait for results
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "video-title")))

    video_elements = driver.find_elements(By.ID, "video-title")

    if len(video_elements) >= 2:
        target = video_elements[1]
    else:
        target = video_elements[0]

    target.click()

    WebDriverWait
    time.sleep(500)
    driver.quit()

if __name__ == "__main__":
    music("Bollywood songs")