from selenium import webdriver
import time

# CONSTANTS
PROMISED_DOWN = 200
PROMISED_UP = 50
CHROME_DRIVER_PATH = "C:/Users/ccesports2/Development/chromedriver"
TWITTER_USER = "Your twitter"
TWITTER_PASSWORD = " Your password"


# CLASS
class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()
        go_button = self.driver.find_element_by_class_name("start-text")
        go_button.click()
        time.sleep(50)
        self.down = self.driver.find_element_by_class_name("download-speed").text
        self.up = self.driver.find_element_by_class_name("upload-speed").text
        print(self.down)
        print(self.up)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login?lang=en")
        self.driver.maximize_window()
        time.sleep(3)
        username = self.driver.find_element_by_name("session[username_or_email]")
        username.send_keys(TWITTER_USER)
        password = self.driver.find_element_by_name("session[password]")
        password.send_keys(TWITTER_PASSWORD)
        log_in = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
        log_in.click()
        time.sleep(3)
        tweet = self.driver.find_element_by_class_name("public-DraftStyleDefault-block")
        tweet.send_keys(
            f"Hey Xfinity, my internet speed is {self.down} down and {self.up} up, and that's not good enough.")
        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]'
            '/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
        tweet_button.click()


bot = InternetSpeedTwitterBot()

bot.get_internet_speed()

if PROMISED_DOWN > float(bot.down) or PROMISED_UP > float(bot.up):
    bot.tweet_at_provider()
