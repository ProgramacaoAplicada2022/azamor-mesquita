#python3.7
import undetected_chromedriver as uc
#By = uc.selenium.webdriver.common.by.By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

WebDriverWait = uc.selenium.webdriver.support.ui.WebDriverWait
EC = uc.selenium.webdriver.support.expected_conditions

opts = uc.selenium.webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = uc.Chrome(chrome_options=opts)

code="""def google_signin(email, password):
    driver.get("https://google.com")

    #d=driver.find_element(By.XPATH, "//a[contains(., 'https://accounts.google.com')]")
    login_button=driver.find_element(By.XPATH, "//a[contains(@href, 'https://accounts.google.com')]")
    login_button.click()

    input_email=driver.find_element(By.XPATH, "//input[contains(@type, 'email')]")
    input_email.send_keys(email)

    button_next=driver.find_element(By.XPATH, "//button[contains(., 'Avançar')]")
    button_next.click()

    password_xpath = "//input[contains(@type, 'password')]"
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, password_xpath)))
    WebDriverWait(driver, 5)

    input_password=driver.find_element(By.XPATH, password_xpath)
    input_password.click()
    input_password.send_keys(password)

    button_next=driver.find_element(By.XPATH, "//button[contains(., 'Avançar')]")
    button_next.click()
"""
exec(code)

email = "prog.aplic.bubble@gmail.com"
password = "Um2345678"

google_signin(email, password)

driver.get("https://bubble.io/login?mode=login")



el_xpath = "//div[contains(@class, 'clickable-element')]"
WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, el_xpath)))
el=driver.find_element(By.XPATH, el_xpath)
el.click()

el_xpath = '//div[contains(@data-email, "' + email + '")]'
WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, el_xpath)))
el=driver.find_element(By.XPATH, el_xpath)
el.click()


div = driver.find_element(By.XPATH, "//a[contains(@href, 'apptestpee')]")