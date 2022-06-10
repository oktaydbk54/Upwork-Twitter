from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



def run_bot(username,password):
    search_value = "#binance"
    
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')

    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options = chrome_options)
    #Page 1 
    url = "https://twitter.com/?logout=1652006058157"

    driver.get(url)
    time.sleep(2)
    print("Page 1 bitti")
    #Page 2
    login_button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div').click()

    time.sleep(2)
    username_button = driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')

    username_button.send_keys(username)

    next_button = driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
    print("Page 2 bitti")
    # Page 3
    time.sleep(2)
    password_button = driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')

    password_button.send_keys(password)

    login_button = driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div').click()
    time.sleep(3)
    print("Page 3 bitti")
    # Page 4
    search_button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input')
    time.sleep(2)
    search_button.send_keys(search_value)
    search_button.send_keys(Keys.ENTER)
    print("Page 4 bitti")
    # Page 5
    time.sleep(2)
    c = 4

    driver.implicitly_wait(5)
    # directing the most latest tweets
    driver.find_element_by_xpath('//*[@id="react-root"]/div/\
    div/div[2]/main/div/div/div/div[1]/div/div[1]/div[2]/\
    nav/div/div[2]/div/div[2]/a').click()

    time.sleep(2)
    while True:
        time.sleep(3)
        comment = driver.find_elements_by_css_selector('.css-18t94o4[data-testid ="reply"]')
        for item in comment:
            try:
                time.sleep(2)
                item.click()
                time.sleep(2)
                value = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
    
                value.send_keys("""Lovely Content ✨
                                Dm on our Instagram Page to get Promoted""")
                time.sleep(2)
                
                save_button = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[2]').click()
                
                c -= 1
                time.sleep(2)
                if c == 0:
                    break
            except:
                pass
            

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        if c == 0:
            break

username = "binandodo"

password = "123456789."

run = run_bot(username,password)