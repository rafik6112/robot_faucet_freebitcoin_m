from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep 
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import time
import sys 

PATH= "chromedriver.exe"
i =0
def freebitcoin_faucet(addresse_mail, password):
    while True:
        global i
        driver = webdriver.Chrome(PATH)
        driver.get("https://freebitco.in/#")
        driver.implicitly_wait(10) 
######################### function Login #################################
        login = driver.find_element(By.CSS_SELECTOR, 'li.login_menu_button')
        address_mail = driver.find_element(By.ID, 'login_form_btc_address')
        motDePasse = driver.find_element(By.ID, 'login_form_password')
        loginButton = driver.find_element(By.ID, 'login_button')
        login.click()
        noThanks = driver.find_element(By.CSS_SELECTOR, 'div.pushpad_deny_button') ##### alert
        noThanks.click() #### alert
        address_mail.send_keys(addresse_mail)
        motDePasse.send_keys(password)
        loginButton.click()
        try:
            while driver.find_element(By.CSS_SELECTOR, 'span.reward_point_redeem_result'):
                sleep (2)
                loginButton.click()
        except:
            None
############################################################################
        noThanks = driver.find_element(By.CSS_SELECTOR, 'div.pushpad_deny_button')
        noThanks.click()
        try:
            withoutCpatcha=driver.find_element(By.ID, 'play_without_captchas_button')
            Roll=driver.find_element(By.ID, 'free_play_form_button')
            driver.execute_script("arguments[0].scrollIntoView();", withoutCpatcha)
            actions = ActionChains(driver)
            actions.move_to_element(withoutCpatcha).click().perform()
            driver.execute_script("arguments[0].scrollIntoView();", Roll)
            actions1 = ActionChains(driver)
            actions1.move_to_element(Roll).click().perform()
            i+=1
            maintenant = datetime.now()
            l="ce script à été executé avec success la ", i,"eme fois à ", maintenant
            print(l)
            with open('logs.txt', 'a') as f:
                sys.stdout = f
                print("ce script à été executé avec success la ", i,"eme fois à ", maintenant)
                sys.stdout = sys.__stdout__
        except:
            i+=1
            maintenant = datetime.now()
            l="ce script à echouer avec pour le ", i,"essaie fois à ", maintenant
            print(l)
            with open('logs.txt', 'a') as f:
                sys.stdout = f
                print("ce script à été executé avec success la ", i,"eme fois à ", maintenant)
                sys.stdout = sys.__stdout__
        sleep(4)
        driver.quit()
        time.sleep(3650)



freebitcoin_faucet('mrboulmelh@gmail.com', '2hNFTUzW9GKkSTUB')
