from logging import exception
import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import undetected_chromedriver as uc
import json, csv

class My_Chrome():
    def __init__(self, jsondata, csvdata=[], zoho=False):
       
        self.firstName = jsondata["firstName"]
        self.lastName = jsondata["lastName"]
        self.emailEnd = jsondata["emailEnd"]
        self.passw = jsondata["passw"]
        self.email = jsondata["email"]
        self.fullemail = self.email + "@" + self.emailEnd
        self.csvdata = csvdata

        #TODO: turn off the SameSite cookie

        self.browser = uc.Chrome()
        self.browser.delete_all_cookies()
        self.zoho = zoho

    def __del__(self):
        pass

    def saveSuccessfulInfo(self, successList):
        f = open(os.getcwd()+"/emailList.csv", 'w')
        writer = csv.writer(f)
        writer.writerows(successList)
        #tiktok and linked gmail account info
        #tiktok user and password
        #gmail user and password
        f.close()
        return

    def tiktokAccountCreate(self):
        success = False
        iter = 0
        for i in range (len(self.csvdata)):
            self.browser.get("https://www.tiktok.com/signup/phone-or-email/email")
            self.browser.implicitly_wait(10)

            WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located((By.NAME, "email")))
            emailPath = self.browser.find_element(By.NAME, "email")
            emailPath.send_keys(self.email)
            passPath = self.browser.find_element(By.CSS_SELECTOR, "input[type = 'password']")        
            passPath.send_keys(self.passw)
            print("email and password entered.")
            month = WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[2]/div[1]/div')))
            if month:
                self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/form/div[2]/div[1]/div').click()
                self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/form/div[2]/div[1]/ul/li[5]').click()
            
            day = WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/form/div[2]/div[2]/div')))
            if day: 
                self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/form/div[2]/div[2]/div").click()
                self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/form/div[2]/div[2]/ul/li[3]").click()
            
            year = WebDriverWait(self.browser, 20).until(ec.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/form/div[2]/div[3]/div")))
            if year:
                self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/form/div[2]/div[3]/div").click()
                self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/form/div[2]/div[3]/ul/li[40]").click()
                #possibly randomize year
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/form/div[4]/div[5]/button").click()        
        self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/form/div[4]/div[5]/div/input').send_keys(self.getTikTokCode())
        

    #Google Signin
    def googleSignIn(self):
        if self.zoho:
            self.zohoSignIn()
            zohoOTPCode = self.getZohoCode()
                    
            self.browser.switch_to.window(self.browser.window_handles[1])

            self.browser.find_element(By.NAME, 'OTP').send_keys(zohoOTPCode)
            self.browser.find_element(By.ID, 'nextbtn').click()


        self.browser.execute_script("window.open('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin');") 
        #proceed with new tab
        self.browser.switch_to.window(self.browser.window_handles[1])
        
        WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located((By.ID, 'identifierId')))
        gmailUserBox = self.browser.find_element_by_id('identifierId')
        gmailUserBox.send_keys(self.email)

        WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="identifierNext"]/div/button')))
        self.browser.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button').click()
        self.browser.implicitly_wait(10)

        WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located((By.ID, 'identifierId')))
        gmailPasswBox = self.browser.find_element(By.NAME, 'password')
        gmailPasswBox.send_keys(self.passw)

        WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]/div/button')))
        self.browser.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button').click()

        
    #Zoho Signin
    def zohoSignIn(self):
        self.browser.execute_script("window.open('https://accounts.zoho.com/signin?servicename=VirtualOffice&signupurl=https://www.zoho.com/mail/zohomail-pricing.html&serviceurl=https://mail.zoho.com', 'zohoSignIN');")
        #proceed with new tab
        self.browser.switch_to.window('zohoSignIN')

        WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located((By.NAME, 'LOGIN_ID')))
        self.browser.find_element(By.NAME, 'LOGIN_ID').send_keys(self.email)
        self.browser.find_element(By.ID, 'nextbtn').click()   


    #Wait for Google Signin and grab code from email
    def getRecentCode(self):
        self.googleSignIn()
        time.sleep(10)
        self.browser.refresh()
        self.browser.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[8]/div/div[1]/div[3]/div/table/tbody/tr[1]/td[5]/div[2]/span[1]/span").click()

        zohoOTPCode = self.browser.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div[2]/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td/b').text
        print(zohoOTPCode)
        return zohoOTPCode 

    def main(self):
        # self.browser.maximize_window()
        self.tiktokAccountCreate()

if __name__ == "__main__":

    data = open("settings.json", "r+", encoding="utf8")
    jsondata = json.load(data)
    data.close()

    f = open(os.getcwd()+"/emailList.csv", 'w')
    csvdata = f.readlines()

    newChrome = My_Chrome(jsondata, csvdata)
    newChrome.main()

    hangingStall = input("Hanging")