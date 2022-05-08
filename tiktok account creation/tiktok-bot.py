from asyncio.windows_events import NULL
from concurrent.futures import thread
import time
from typing import KeysView
from weakref import proxy
from numpy import empty
from selenium import webdriver
import undetected_chromedriver as uc
import json
import google_auth_httplib2


class My_Chrome(uc.Chrome):
    def __del__(self):
        pass

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


    #TODO:

    # - log into domain
    # - make alias
    # - return alias

        emailAlias = ""
        stall = input("Stalling")
        return emailAlias

    def tiktokAccountCreate(browser):
        return

    def main():
        try:
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

            option = uc.ChromeOptions()
            browser = uc.Chrome()
            browser.get("https://www.tiktok.com/signup/phone-or-email/email")
            browser.implicitly_wait(10)
            time.sleep(2)
            
            emailPath = browser.find_element_by_name("email")
            passPath = browser.find_element_by_xpath("//input[@type = 'password']")
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

            #TODO:
            #1. need email address
            #2. log into zoho and create email aliases with Selenium

            browser.execute_script("window.open('https://accounts.zoho.com/signin?servicename=VirtualOffice&signupurl=https://www.zoho.com/mail/zohomail-pricing.html&serviceurl=https://mail.zoho.com');")
            #proceed with new tab
            browser.switch_to.window(browser.window_handles[1])
            browser.implicitly_wait(10)

            browser.find_element_by_name('LOGIN_ID').send_keys(email)
            browser.find_element_by_id('nextbtn').click()
            
            browser.execute_script("window.open('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin');") 
            #proceed with new tab
            browser.switch_to.window(browser.window_handles[2])
            browser.implicitly_wait(10)

            gmailUserBox = browser.find_element_by_id('identifierId')
            gmailUserBox.send_keys(email)        
            browser.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
            browser.implicitly_wait(10)

            gmailPasswBox = browser.find_element_by_name('password')
            gmailPasswBox.send_keys(passw)
            browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()
            browser.implicitly_wait(10)

            time.sleep(10)
            browser.refresh()
            browser.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[8]/div/div[1]/div[3]/div/table/tbody/tr[1]/td[5]/div[2]/span[1]/span").click()

            #TODO: 
            #Find right iframe
            

            zohoOTPCode = browser.find_element_by_xpath('//*[@id=":rk"]/div[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td/b').text
            browser.find_element_by_xpath('//*[@id=":4"]/div[2]/div[1]/div/div[2]/div[3]').click()

            browser.switch_to.window(browser.window_handles[1])

            browser.find_element_by_name('OTP').send_keys(zohoOTPCode)
            browser.find_element_by_id('nextbtn').click()
            browser.implicitly_wait(10)

            # code = browser.find_element_by_xpath()

            #enter email
            #press next
            #skip
            
            # tiktokUser = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/div/div[2]/input').text
            # browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/form/button[1]').click()
            hangingStall = input("Hanging")
        except:
            print("\nbrowser abruptly closed")

    if __name__ == "__main__":
        main()