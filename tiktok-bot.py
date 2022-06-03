import os
import time
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import undetected_chromedriver as uc
import json, csv

class My_Chrome():
    def __del__(self):
        pass

    def __init__(self, jsondata, csvdata=[], zoho=False):

        self.csvdata = csvdata
        self.firstName = jsondata["firstName"]
        self.lastName = jsondata["lastName"]
        self.email = jsondata["mainEmail"]

        #TODO: turn off the SameSite cookie for lastmx

        self.browser = uc.Chrome()
        self.browser.delete_all_cookies()
        self.zoho = zoho

    def saveSuccessfulInfo(self, successList):
        f = open("../emailList.csv", 'w')
        writer = csv.writer(f)
        writer.writerows(successList)
        #tiktok and linked gmail account info
        #tiktok user and password
        #gmail user and password
        f.close()
        return

    def tiktokAccountCreate(self):
        for i in (0, len(self.csvdata)):
            email = self.csvdata[i]
            #TODO: make random password generation
            # passw = randomPasswordGenerate()

            passw = "Backpack123$" #dummy password
            self.browser.get("https://www.tiktok.com/signup/phone-or-email/email")
            self.browser.implicitly_wait(10)
            time.sleep(2)

            WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located((By.NAME, "email")))
            emailPath = self.browser.find_element(By.NAME, "email")
            emailPath.send_keys(email)
            passPath = self.browser.find_element(By.CSS_SELECTOR, "input[type = 'password']")
            passPath.send_keys(passw)
            root = "root"
            success = False
            m = False
            d = False
            y = False
            print("email and password entered.")
            while success == False: 
                try: 
                    if not m:
                        month = WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Month")]')))
                        print("selecting month")
                        if month:
                            self.browser.find_element(By.XPATH, '//*[contains(text(), "Month")]').click()
                            #Randomize month
                            self.browser.find_element(By.XPATH, '//*[contains(text(), "March")]').click()
                            m = True
                    
                    if not d:
                        day = WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Day")]')))
                        print("selecting day")
                        if day: 
                            self.browser.find_element(By.XPATH, '//*[contains(text(), "Day")]').click()
                            self.browser.find_element(By.XPATH, '//*[text() = "31"]').click()
                            d = True

                    if not y:
                        year = WebDriverWait(self.browser, 20).until(ec.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Year")]')))
                        print("selecting year")
                        if year:
                            self.browser.find_element(By.XPATH, '//*[contains(text(), "Year")]').click()

                            #randomize year selection
                            randomInt = random.randint(1980, 2000)
                            self.browser.find_element(By.XPATH, '//*[contains(text(), ' + str(randomInt) + ')]').click()
                            y = True
                    
                    success = True
                    print("success!")
                except Exception as e: 
                    print("error!")
                    pass
            self.browser.find_element(By.XPATH, '//button[text() = "Send code"]').click()        
            self.browser.find_element(By.XPATH, '//input[starts-with(@placeholder, "Enter 6-digit code")]').send_keys(self.getRecentCode(passw))
            self.browser.find_element(By.CSS_SELECTOR, "button[type = 'submit']").click()

            WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/img')))
            qrCode = self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/img')
            self.browser.get(qrCode)
 
    #Google Signin
    def googleSignIn(self, passw):
        if self.zoho:
            self.zohoSignIn()
            zohoOTPCode = self.getZohoCode()
                    
            self.browser.switch_to.window(self.browser.window_handles[1])

            self.browser.find_element(By.NAME, 'OTP').send_keys(zohoOTPCode)
            self.browser.find_element(By.ID, 'nextbtn').click()

        self.browser.execute_script("window.open('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin');") 
        #proceed with new tab
        self.browser.switch_to.window(self.browser.window_handles[1])
        
        WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located((By.XPATH, '//input[@id="identifierId"]')))
        gmailUserBox = self.browser.find_element(By.XPATH, '//input[@id="identifierId"]')
        gmailUserBox.send_keys(self.email)

        WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable((By.XPATH, '//button[@type = "button"]')))
        time.sleep(1)
        self.browser.find_element(By.XPATH, '//button[@type = "button"]').click()
        time.sleep(1)

        WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located((By.ID, 'identifierId')))
        gmailPasswBox = self.browser.find_element(By.NAME, 'password')
        gmailPasswBox.send_keys(passw)

        WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]/div/button')))
        self.browser.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button').click()
    

    #Zoho Signin
    def zohoSignIn(self, email):
        self.browser.execute_script("window.open('https://accounts.zoho.com/signin?servicename=VirtualOffice&signupurl=https://www.zoho.com/mail/zohomail-pricing.html&serviceurl=https://mail.zoho.com', 'zohoSignIN');")
        #proceed with new tab
        self.browser.switch_to.window('zohoSignIN')

        WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located((By.NAME, 'LOGIN_ID')))
        self.browser.find_element(By.NAME, 'LOGIN_ID').send_keys(email)
        self.browser.find_element(By.ID, 'nextbtn').click()   

    #Wait for Google Signin and grab code from email
    def getRecentCode(self,passw):
        self.googleSignIn(passw)
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
    csvdata = []

    with open(os.getcwd() + '/emailList.csv', mode ='r') as file:
    
        # reading the CSV file
        csvFile = csv.reader(file)

        # displaying the contents of the CSV file
        for row in csvFile:
            csvdata.append(row)
        # print (csvdata)
    newChrome = My_Chrome(jsondata, csvdata)
    newChrome.main()

    hangingStall = input("Hanging")