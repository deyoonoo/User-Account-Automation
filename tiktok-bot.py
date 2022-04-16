from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
import random
import os

data = open("settings.json", "r+", encoding="utf8")
jsondata = json.load(data)
data.close()

# Import info subject to change
# Just make variables first, can make dummy information later
# firstName = jsondata["firstName"]
firstName = "David"
lastName = jsondata["firstName"]
userName = jsondata["userName"] + str(random.randint(1, 99999))
emailEnd = jsondata["emailEnd"]
passw = jsondata["passw"]
email = jsondata["email"]
emailFull = email + "+" + str(random.randint(1, 99999)) + "@" + emailEnd
browser = webdriver.Chrome(executable_path=os.getcwd() + "/chromedriver")
browser.implicitly_wait(10)

# Functions
# def getGmail():
#     import gmailReader as gr
#     print("getMail")
#     code = gr.getmail()
#     codePath = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/form/div[4]/div[5]/div/input')
#     if not (codePath.get_property("value") == code):
#         try:
#             codePath.clear()
#         except:
#             print("Deletion could not be performed")
#         codePath.send_keys(code)
#         Register()
#     else:
#         if browser.current_url is None:
#             exit()
#         else:
#             getGmail()


# def Register():
#     global emailFull, passw
#     try:
#         browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/form/div[4]/button').click()
#         time.sleep(1)
#         result = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/form/div[4]/div[6]/div')
#         print("1")

#         if result.get_attribute("innerHTML") == "Incorrect code":
#             time.sleep(1)
#             getGmail()
#         elif result.get_attribute("innerHTML") == "Verification failed. Please click Resend and try again.":
#             print("Verification failed. Please click Resend and try again.")
#             time.sleep(1)
#             Register()
#             print("2")
#         elif result.get_attribute("innerHTML") == "Verification failed. Please click Resend and try again.":
#             print("YOUR IP BLOCKED!")
#             print("3")
#         else:
#             try:
#                 skipPath = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/form/button[2]")
#                 print("The account has been created, the mails are deleted and the new account is transferred")
#                 skipPath.click()

#                 import gmailReader as gr
#                 gr.deletemail()
#                 browser.quit()
#             except:
#                 print("no account opened")
#             print("5")
#     except:
#         try:
#             print(browser.current_url)
#         except:
#             import bot
#             exit()
#         try:
#             skipPath = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/form/button[2]")
#             print("The account has been created, the mails are deleted and the new account is transferred")
#             skipPath.click()
#             successReg(emailFull, passw)
#             import gmailReader as gr
#             gr.deletemail()
#             browser.quit()
#             import os, sys
#             os.startfile(__file__)
#             sys.exit()
#         except:
#             if (browser.current_url == "https://www.tiktok.com/login/download-app"):
#                 successReg(emailFull, passw)
#                 import gmailReader as gr
#                 gr.deletemail()
#                 browser.quit()
#                 import os, sys
#                 os.startfile(__file__)
#                 sys.exit()
#             print("You did not enter the code, try again")
#             time.sleep(1)
#             Register()
#             print("6")


# def successReg(email, password):
#     veri = open("users.txt", "a")
#     veri.write(email + ":" + password + "\n")

def getGmailCode():
    try:
        tiktokTab = browser.current_window_handle
        browser.delete_all_cookies()
        
        #Fill in account creation pages
        browser.execute_script('''window.open("https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp","_blank");''')
        gmailTab = browser.current_window_handle

        print('Gmail Page is open successfully.')
        browser.manage().timeouts().implicitlyWait(5)
        browser.find_element_by_xpath("//*[@id='firstName']").send_keys(firstName)
        print ('Enter First Name')
        browser.find_element_by_id('lastName').send_keys(lastName)
        print ('Enter Last Name')
        userNameBox = browser.find_element_by_id('username')
        userNameBox.send_keys(userName)
        userNameBox.send_keys(Keys.Tab)
        
        #if username is taken
        if(browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[2]/div[2]/div/text") == "That username is taken. Try another."):
            browser.find_element_by_xpath("1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[2]/div/ul/li[2]/button").click()

        
        print ('enter username')
        browser.find_element_by_name('Passwd').send_keys(passw)
        print ('Password Enter Successfully')

        browser.switch_to_window(tiktokTab)
        browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/form/div[4]/div[5]/button").click() #send code button
        browser.switch_to_window(gmailTab)
        return 0
    except:
        return 1


def main():
    try:
        browser.get("https://www.tiktok.com/signup/phone-or-email/email")
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
    except:
        print("Webpage elements have changed.")

    #get code from newly created email account at gmail.com
    code = getGmailCode()
    print(code)


if __name__ == "__main__":
    main()