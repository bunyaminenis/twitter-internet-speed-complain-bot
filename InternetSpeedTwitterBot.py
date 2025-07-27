from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

load_dotenv()

TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
PROMISED_DOWN = 200
PROMISED_UP = 50

class InternetSpeedTwitterBot:

    def __init__(self ,driver_path):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        sleep(2)
        go_button = self.driver.find_element(By.CLASS_NAME, value="start-text")
        go_button.click()

        sleep(60)
        self.down = float(self.driver.find_element(By.CLASS_NAME, value="download-speed").text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, value="upload-speed").text)
        print(self.down)
        print(self.up)

    def tweet_at_provider(self):
        self.driver.get("https://x.com/")

        sleep(2)
        login_button = self.driver.find_element(By.XPATH, value="/html/body/div/div/div/div[2]/main/div/div/div[1]/div/"
                                                                "div/div[3]/div[4]/a/div")
        login_button.click()

        sleep(2)
        username_fill = self.driver.find_element(By.XPATH, value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/"
                                                                 "div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/"
                                                                 "label/div/div[2]/div/input")
        username_fill.send_keys(TWITTER_EMAIL)
        username_fill.send_keys(Keys.ENTER)


        sleep(2)
        password_fill = self.driver.find_element(By.XPATH, value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/"
                                                                 "div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/"
                                                                 "div/label/div/div[2]")
        password_fill.send_keys(TWITTER_PASSWORD)
        password_fill.send_keys(Keys.ENTER)

        sleep(2)
        write_tweet = self.driver.find_element(By)
        write_tweet.send_keys(f"I have been promised for {PROMISED_DOWN}Mbps/ {PROMISED_UP}Mbps, but my current speed is "
                             f"{self.down}Mbps/ {self.up}Mbps")

        send_tweet_button = self.driver.find_element(By)
        send_tweet_button.click()


