from asyncio.windows_events import NULL
from concurrent.futures import thread
from weakref import proxy
from numpy import empty
from selenium import webdriver
import json
import time


# make 1 gmail account
# automate alias creation on the same email
# save all aliases into json and temporary list
# go to tiktok and loop creation through all aliases, each alias creating a new email

# after successful registration, register gmail account and password + tiktok account and password in 1 json node 

# Functions
def saveSuccessfulInfo():
    #tiktok and linked gmail account info
    #tiktok user and password
    #gmail user and password
    return

def getEmailCode(fullEmail, password): #Go to gmail and save the confirmation code from the most recent email
    return

def createEmailAlias(browser, gmailAddress, passw):
    # use one existing email address
    # create a nickname for the email address
    # save the email in a list

    browser.execute_script("window.open('about:blank', '');")
    browser.switch_to.window(browser.window_handles[1])
    browser.get('https://accounts.google.com/signin/v2/identifier?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

    browser.find_element_by_id("identifierId").send_keys(gmailAddress)
    browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
    browser.implicitly_wait(20)
    #browser.find_element_by_id()
    browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(passw)
    browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()

    browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[4]/div[1]').click()

    emailAlias = ""
    stall = input("Stalling")
    return emailAlias

def tiktokAccountCreate(browser, ):
    return

def main():

    data = open("settings.json", "r+", encoding="utf8")
    jsondata = json.load(data)
    data.close()

    # Import info subject to change
    # Just make variables first, can make dummy information later
    firstName = jsondata["firstName"]
    lastName = jsondata["lastName"]
    emailEnd = jsondata["emailEnd"]
    passw = jsondata["passw"]
    email = jsondata["email"]
    fullemail = email + "@" + emailEnd

    import undetected_chromedriver as uc
    option = uc.ChromeOptions() 
    # option.add_argument("start-maximized")
    # option.add_experimental_option("excludeSwitches", ["enable-automation"])
    # option.add_experimental_option('useAutomationExtension', False)
    browser = uc.Chrome()
    browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    browser.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    print(browser.execute_script("return navigator.userAgent;"))
    browser.get("https://www.tiktok.com/signup/phone-or-email/email")
    browser.implicitly_wait(10)
    
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

    
    #send to tiktok alias
    emailPath.send_keys(createEmailAlias(browser, fullemail, passw))

    #fill in code
    browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/form/div[4]/div[5]/button").click() #send code button
    getEmailCode(fullemail, passw)
    stall = input("Stalling")


if __name__ == "__main__":
    main()