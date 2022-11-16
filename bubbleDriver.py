#python3.7
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

WebDriverWait = uc.selenium.webdriver.support.ui.WebDriverWait
EC = uc.selenium.webdriver.support.expected_conditions

opts = uc.selenium.webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = uc.Chrome(chrome_options=opts)

def google_signin(email, password):
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

def bubbleLogin(email):
    driver.get("https://bubble.io/login?mode=login")
    
    el_xpath = "//div[contains(@class, 'clickable-element')]"
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, el_xpath)))
    el=driver.find_element(By.XPATH, el_xpath)
    el.click()
    
    el_xpath = '//div[contains(@data-email, "' + email + '")]'
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, el_xpath)))
    el=driver.find_element(By.XPATH, el_xpath)
    el.click()
    
    #div = driver.find_element(By.XPATH, "//a[contains(@href, 'apptestpee')]")

def bypass_bubble_trial():
    class_name = "btn-cancel"
    
    WebDriverWait(driver, 15000).until(EC.element_to_be_clickable((By.CLASS_NAME, class_name)))
    cancel_button = driver.find_element(By.CLASS_NAME, class_name)
    cancel_button.click()


def create_type(field_name):
    #go to data type page if not in it
    in_data_type_tab = driver.current_url.find("subtab=Data+Types") > -1
    if not in_data_type_tab:
        driver.get("https://bubble.io/page?name=index&id=apptestpee&tab=tabs-3&subtab=Data+Types&type_id=asfg")
        bypass_bubble_trial()

    #close trial popup if necessary
    class_name = "btn-cancel"
    if len(driver.find_elements(By.CLASS_NAME, class_name)) > 0:
        bypass_bubble_trial()

    div_xpath = "//div[contains(@class, 'green-box')]"
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, div_xpath)))
    div = driver.find_element(By.XPATH, div_xpath)
    
    new_type_input = div.find_elements(By.XPATH, "//input[contains(@class, 'bubble-ui')]")[1]
    new_type_input.send_keys(field_name)

    button_create = div.find_elements(By.XPATH, "//div[contains(., 'Create')]")[12]
    button_create.click()

email = "prog.aplic.bubble@gmail.com"
password = "Um2345678"

#google_signin(email, password)