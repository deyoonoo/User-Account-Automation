from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import random
import os

data = open("settings.json", "r+", encoding="utf8")
jsondata = json.load(data)
data.close()

# Import info subject to change
# Just make variables first, can make dummy information later
firstName = jsondata["firstName"]
lastName = jsondata["lastName"]
userName = jsondata["userName"] + str(random.randint(10000, 99999))
emailEnd = jsondata["emailEnd"]
passw = jsondata["passw"]
email = jsondata["email"]
emailFull = email + "+" + str(random.randint(10000, 99999)) + "@" + emailEnd

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

def getPhoneCode():
    browser.get("https://freepublicsms.com/page/Fake-Phone-Number-For-Verification")
    browser.implicitly_wait(1)
    fakePhoneTab = browser.current_window_handle

    fake_phone_num = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[1]/div/h2").text()
    return fake_phone_num

def createEmailAccount():
    browser.get("https://accounts.google.com/signup")
    browser.implicitly_wait(1)
    gmailTab = browser.current_window_handle
    try:
        #get the first name textbox
        first_name = browser.find_element_by_id("firstName")
        first_name.send_keys(firstName)

        surname = browser.find_element_by_id("lastName")
        surname.send_keys(lastName)

        username = browser.find_element_by_id("username")
        username.send_keys(userName)
        
        password = browser.find_element_by_id("passwd")
        password.send_keys(passw)

        confirm_password = browser.find_element_by_id("confirm-passwd")
        confirm_password.send_keys(passw)

        next_btn = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
        next_btn.click()       

        phone_number = browser.find_element_by_id("phoneNumberId")
        phone_number.send_keys(getPhoneCode())

        next_btn = browser.find_element_by_xpath('//*[@id="accountDetailsNext"]/div/button')
        next_btn.click()

        if(browser.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[2]/div[2]/div/text()').text() == "That username is taken. Try another."):
            userName = browser.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[2]/div/ul/li[2]/button').text()
            browser.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[2]/div/ul/li[2]/button').click()
            next_btn.click()

    except:
        raise ValueError("Textbox not found")
    return 

def main():
    try:
        #create account
        browser.get("https://www.tiktok.com/signup/phone-or-email/email")
        tiktokTab = browser.current_window_handle

        emailPath = browser.find_element_by_name("email")
        passPath = browser.find_element_by_name("password")

        emailPath.send_keys(emailFull)
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
        createEmailAccount()
        #fill in code
        browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/form/div[4]/div[5]/button").click() #send code button

    except:
        print("Webpage elements have changed.")

    #get code from newly created email account at gmail.com
       


if __name__ == "__main__":
    main()