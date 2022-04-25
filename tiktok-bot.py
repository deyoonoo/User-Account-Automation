from asyncio.windows_events import NULL
from concurrent.futures import thread
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

browser = webdriver.Chrome(executable_path=os.getcwd() + "/chromedriver")
browser.implicitly_wait(10)
tiktokTab = gmailTab = fakePhoneTab = emailTab = browser.current_window_handle

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
    time.sleep(20)

    browser.find_element_by_id("username").send_keys(userName)
    print("username input")

    browser.find_element_by_id("password").send_keys(passw)
    print("password input")

    browser.find_element_by_id("repeat-password").send_keys(passw)
    browser.find_element_by_class_name('button button-large button-solid-norm w100 mt1-75').click()
    browser.find_element_by_class_name('button button-large button-ghost-norm w100 mt0-5').click()
    browser.switch_to_window(browser.window_handles[0])

    # browser.get("https://account.protonmail.com/signup")
    # userName = jsondata["userName"] + str(random.randint(10000, 99999))

    # browser.implicitly_wait(5)

    # if browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/main/div[2]/div/svg').is_displayed():
    #     browser.implicitly_wait(5)

    # #     browser.implicitly_wait(1)
    # # #get the first name textbox
    # # first_name = browser.find_element_by_id("firstName")
    # # first_name.send_keys(firstName)

    # # surname = browser.find_element_by_id("lastName")
    # # surname.send_keys(lastName)

    # user_name = browser.find_element_by_id("username")
    # user_name.send_keys(userName)
    
    # password = browser.find_element_by_id("password")
    # password.send_keys(passw)

    # confirm_password = browser.find_element_by_id("repeat-password")
    # confirm_password.send_keys(passw)

    # next_btn = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/main/div[2]/form/button")
    # next_btn.click()       

    # while browser.find_element_by_xpath('/html/body/div[1]/label/div[3]/svg').is_displayed():
    #     userName = jsondata["userName"] + str(random.randint(10000, 99999))
    #     user_name.send_keys(userName)
    #     next_btn.click()
    # browser.implicitly_wait(5)

    # browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/main/div[2]/form/button[2]').click()
    # browser.find_element_by_xpath('/html/body/div[4]/dialog/div/div[3]/button[1]').click()
    # browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/main/div[2]/div[2]/div[1]/button').click()
    # browser.find_element_by_id('checkbox').click()

    # browser.implicitly_wait(5)
    # browser.find_element_by_xpath('/html/body/div[4]/dialog/form/div/div/footer/button').click()
    # browser.find_element_by_xpath('/html/body/div[4]/dialog/form/div/div/footer/button').click()

    # return userName + "@protonmail.com"

def randomSleepInterval():
    randomInt = random.randint(range(1,5))
    return randomInt


def main():
    #create account
    browser.get("https://www.tiktok.com/signup/phone-or-email/email")
    tiktokTab = browser.current_window_handle
    emailPath = browser.find_element_by_name("email")
    passPath = browser.find_element_by_name("password")

    passPath.send_keys(passw)
    print("email and password entered.")
    browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/form/div[2]/div[1]/div").click()
    time.sleep(3)
    browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/form/div[2]/div[1]/ul/li[5]").click()
    time.sleep(5)
    browser.find_element_by_xpath("/html/body/div[1]/div").click()
    time.sleep(2)
    browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/form/div[2]/div[2]/div").click()
    time.sleep(7)

    browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/form/div[2]/div[2]/ul/li[5]").click()
    time.sleep(2)

    browser.find_element_by_xpath("/html/body/div[1]/div").click()
    time.sleep(3)

    browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/form/div[2]/div[3]/div").click()
    time.sleep(6)

    browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/form/div[2]/div[3]/ul/li[29]").click() #age
    time.sleep(8)

    browser.find_element_by_xpath("/html/body/div[1]/div").click()
    emailPath.send_keys("zd9393960@gmail.com")

    #fill in code
    browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/form/div[4]/div[5]/button").click() #send code button
    #get code from newly created email account at gmail.com       


if __name__ == "__main__":
    main()