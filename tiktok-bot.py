from asyncio.windows_events import NULL
from concurrent.futures import thread
from weakref import proxy
from numpy import empty
from selenium import webdriver
import json
import random
import os
import time



data = open("settings.json", "r+", encoding="utf8")
jsondata = json.load(data)
data.close()

# Import info subject to change
# Just make variables first, can make dummy information later
firstName = jsondata["firstName"]
lastName = jsondata["lastName"]
userName = ""
emailEnd = jsondata["emailEnd"]
passw = jsondata["passw"]
email = jsondata["email"]

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome(options=options, executable_path=os.getcwd() + "/chromedriver")
browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
browser.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
print(browser.execute_script("return navigator.userAgent;"))

# Functions
def saveSuccessfulInfo():
    #tiktok and linked gmail account info
    #tiktok user and password
    #gmail user and password
    return

def getEmailCode(): #Go to gmail and save the confirmation code from the most recent email
    return

def createEmailAlias():
    # use one existing email address
    # create a nickname for the email address

    fullEmail = ""
    browser.execute_script("window.open('about:blank', '');")
    browser.switch_to.window(browser.window_handles[1])
    browser.get('https://account.protonmail.com/signup')
    time.sleep(10)

    browser.find_element_by_id("username").send_keys(userName)
    print("username input")

    browser.find_element_by_id("password").send_keys(passw)
    print("password input")

    browser.find_element_by_id("repeat-password").send_keys(passw)
    browser.find_element_by_class_name('button button-large button-solid-norm w100 mt1-75').click()
    browser.find_element_by_class_name('button button-large button-ghost-norm w100 mt0-5').click()
    browser.switch_to_window(browser.window_handles[0])


def main():
    #create account
    browser.get("https://www.tiktok.com/signup/phone-or-email/email")
    tiktokTab = browser.current_window_handle
    emailPath = browser.find_element_by_name("email")
    passPath = browser.find_element_by_name("password")

    passPath.send_keys(passw)
    print("email and password entered.")
    browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/form/div[2]/div[1]/div").click()
    browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/form/div[2]/div[1]/ul/li[5]").click()
    browser.find_element_by_xpath("/html/body/div[1]/div").click()
    browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/form/div[2]/div[2]/div").click()
    browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/form/div[2]/div[2]/ul/li[5]").click()
    browser.find_element_by_xpath("/html/body/div[1]/div").click()
    browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/form/div[2]/div[3]/div").click()
    browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/form/div[2]/div[3]/ul/li[29]").click() #age
    browser.find_element_by_xpath("/html/body/div[1]/div").click()
    emailPath.send_keys()

    #fill in code
    browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/form/div[4]/div[5]/button").click() #send code button
    #get code from newly created email account at gmail.com       


if __name__ == "__main__":
    main()