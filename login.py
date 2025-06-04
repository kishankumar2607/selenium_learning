
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def demo_login():
    driver.get("https://the-internet.herokuapp.com/login")

    username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

    passwprd = driver.find_element(By.ID, "password")

    username.send_keys("tomsmith")
    passwprd.send_keys("SuperSecretPassword!")

    login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
    login_button.click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.flash.success")))
    time.sleep(5)

    logout_button = driver.find_element(By.CSS_SELECTOR, "a.button.secondary.radius")
    logout_button.click()

    driver.quit()

if __name__ == "__main__":
    demo_login()