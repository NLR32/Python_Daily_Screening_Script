

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import subprocess
import pyautogui
import keyboard

# Get Chromedriver
#
browser = webdriver.Chrome('/Users/levirose/chromedriver/chromedriver')

# Pull Up Screening Website
#
browser.implicitly_wait(10);
browser.get('https://visitorscreening.wustl.edu/symptom-screener')

# Find locations for actions
fullNameBar = browser.find_element(By.XPATH, '//*[@id="mat-input-0"]')
emailAdressBar = browser.find_element(By.XPATH, '//*[@id="mat-input-1"]')
dropdown = browser.find_element(By.XPATH,'//*[@id="mat-select-0"]/div/div[1]')
symptomsButton = browser.find_element(By.XPATH, '//*[@id="mat-checkbox-9"]/label/div')
posTest = browser.find_element(By.XPATH, '//*[@id="mat-radio-6"]/label/div[1]')
closeContact = browser.find_element(By.XPATH, '//*[@id="mat-radio-8"]/label/div[1]')
vaxButton = browser.find_element(By.XPATH, '//*[@id="mat-radio-9"]/label/div[1]')
confirmButton = browser.find_element(By.XPATH, '//*[@id="mat-radio-11"]/label/div[1]')
submitButton = browser.find_element(By.XPATH, '/html/body/app-root/app-layout/div/div[3]/app-symptom-screener/div/form/div[5]/div[7]/button')

#
# Fill Out Screening
#

# Enter text
fullNameBar.send_keys('Lev Rose')
emailAdressBar.send_keys('l.l.rose@wustl.edu')

# Dropdown Menu
dropdown.click()
otherVisit = browser.find_element(By.ID, 'mat-option-1')
otherVisit.click()

# Enter Text
campusContact = browser.find_element(By.XPATH, '//*[@id="mat-input-2"]')
campusContact.send_keys('Lev Rose')
symptomsButton.click()

# Select Options For Buttons
posTest.click()
posTest.click()
closeContact.click()
closeContact.click()
vaxButton.click()
vaxButton.click()
confirmButton.click()
confirmButton.click()
submitButton.click()

#
# Take a screenshot and save it
#
time.sleep(2)
screenshot = pyautogui.screenshot(region=(500,500,1500,1500))
screenshot.save("screen.png")
time.sleep(.2)
browser.quit()

#
# Send Screenshot
#

# Open screenshot
time.sleep(1)
FileName = "/Users/levirose/PycharmProjects/WashuScreening/screen.png"
subprocess.call(["open", FileName])
time.sleep(.5)

# Open up Messages
pyautogui.click(134,0)
time.sleep(.1)
pyautogui.click(149,480)
time.sleep(.1)
pyautogui.click(389,648)
time.sleep(1)

# write number and send
keyboard.write("3147537703")
keyboard.press("enter")
pyautogui.click(643,530)





