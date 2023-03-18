from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time

chrome_diver = "YOUR PATH TO CHROME DRIVER"

driver = webdriver.Chrome(executable_path= chrome_diver)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

t_end = time.time() + 60 * 5  #time + seconds*minutes
now = datetime.now()
start_time = now.strftime("%H:%M:%S")
time_flag = False

# THE FUNCTION PURCHASE IS TO BE RUN EVERY 5 SECONDS
def purchase():
    money = driver.find_element(By.ID, "money")
    money_collected = money.text.replace(",","")
    active_purchases = driver.find_elements(By.CSS_SELECTOR, "#store div[class=''] b") # LOOK UP THE AVAILABLE UPGRADES
    highest_cost = active_purchases[len(active_purchases)-1].text.split(" - ")[1]
    if int(money_collected) > int(highest_cost.replace(",","")):
        active_purchases[len(active_purchases)-1].click()


while(time.time()<t_end):   
    cookie.click() # KEEP ON CLICKING THE COOKIE
    curr = datetime.now()
    curr_time = curr.strftime("%H:%M:%S")
    diff_time = (datetime.strptime(curr_time,"%H:%M:%S") - datetime.strptime(start_time,"%H:%M:%S")) # USE THIS TO FIND THE SPAN OF 5 SECONDS
    time_past = int(diff_time.total_seconds())
    if(time_past > 0 and time_past % 5 == 0 and time_flag == True):
        time_flag = False
        purchase()
        start_time = curr_time # RESET THE START TIME
    elif(time_past > 0 and time_past % 2 == 0 and time_flag == False):
        time_flag = True

cps = driver.find_element(By.ID, "cps")
final_cps = cps.text.split(" : ")[1]
print(f"You were making {final_cps} cookies per second after 5 minutes")
