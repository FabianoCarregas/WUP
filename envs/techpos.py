from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def run(email, password, url):

    e_mail = (email.get())
    pass_word = (password.get())
    e_url = (url.get())
    driver = webdriver.Firefox()
    driver.get(e_url)

    # logging in
    driver.find_element('xpath', '//*[@id="login-email"]').send_keys(e_mail)
    driver.find_element('xpath', '//*[@id="password"]').send_keys(pass_word)
    driver.find_element('xpath', '//*[@id="form-default"]/button').click()

    # learning
    driver.get(e_url)

    driver.find_element(By.ID, 'courseLabel').click()
    driver.find_element(By.CLASS_NAME, 'header-item-link--degrees').click()
    time.sleep(1)

    #content
    driver.find_element(By.ID, 'contentLabel').click()
    driver.find_element(By.CLASS_NAME, 'header-item-link--alura-mais').click()
    time.sleep(1)

    driver.find_element(By.ID, 'contentLabel').click()
    driver.find_element(By.CLASS_NAME, 'header-item-link--projects').click()
    time.sleep(1)

    #comunity
    driver.find_element('xpath', '/html/body/header[1]/div/nav/div[3]/a').click()
    time.sleep(1)
    driver.find_element('xpath', '/html/body/header[1]/div/nav/div[3]/a').click()

    #news
    driver.find_element('xpath', '/html/body/header[1]/div/nav/div[4]/button').click()
    time.sleep(1)
    driver.find_element('xpath', '/html/body/header[1]/div/nav/div[4]/button').click()
    time.sleep(1)

    #profile
    driver.find_element('xpath', '/html/body/header[1]/div/nav/div[5]/a/span').click()
    driver.find_element(By.CLASS_NAME, 'header-nav-link--profile').click()
    time.sleep(1)

    driver.find_element('xpath', '/html/body/header[1]/div/nav/div[5]/a/span').click()
    driver.find_element(By.CLASS_NAME, 'header-nav-link--profile-edit').click()
    time.sleep(1)

    driver.find_element('xpath', '/html/body/header[1]/div/nav/div[5]/a/span').click()
    driver.find_element(By.CLASS_NAME, 'header-nav-link--purchases').click()
    time.sleep(1)

    # starting course
    action = ActionChains(driver)

    driver.find_element(By.ID, 'courseLabel').click()
    driver.find_element(By.CLASS_NAME, 'header-item-link--degrees').click()
    time.sleep(1)

    driver.find_element(By.CLASS_NAME, 'techpos-card').click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'btn-techpos-continue').click()
    time.sleep(2)
    driver.get('https://pos.alura.tech/course/pos-datascience-modulo1-python-pandas/task/74508')
    time.sleep(2)
    action.send_keys(Keys.SPACE).perform()
    time.sleep(6)

    driver.find_element(By.CLASS_NAME, 'task-actions-button-next').click()
    driver.find_element(By.CLASS_NAME, 'task-actions-button-next').click()
    driver.find_element(By.CLASS_NAME, 'task-actions-button-next').click()
    driver.find_element(By.CLASS_NAME, 'task-actions-button-next').click()
    time.sleep(2)

    # finishing
    driver.get(e_url)