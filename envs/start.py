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
    driver.find_element('xpath', '/html/body/div[3]/section/section[1]/form/button').click()

    # learning
    driver.get(e_url)

    driver.find_element(By.ID, 'courseLabel').click()
    driver.find_element(By.CLASS_NAME, 'header-nav-link--courses').click()
    time.sleep(1)

    driver.find_element(By.ID, 'courseLabel').click()
    driver.find_element(By.CLASS_NAME, 'header-nav-link--user-guides').click()
    time.sleep(1)

    driver.find_element(By.ID, 'courseLabel').click()
    driver.find_element(By.CLASS_NAME, 'header-nav-link--dashboardAdmin').click()
    time.sleep(1)

    #comunity
    driver.find_element('xpath', '/html/body/header[1]/div/nav/div[2]/a').click()
    driver.find_element(By.CLASS_NAME, 'header-item-link--forum').click()
    time.sleep(1)

    driver.find_element('xpath', '/html/body/header[1]/div/nav/div[2]/a').click()
    driver.find_element(By.CLASS_NAME, 'header-item-link--forum-interactions').click()
    time.sleep(1)

    driver.find_element('xpath', '/html/body/header[1]/div/nav/div[2]/a').click()
    driver.find_element(By.CLASS_NAME, 'header-nav-link--ranking').click()
    time.sleep(1)

    driver.find_element('xpath', '/html/body/header[1]/div/nav/div[2]/a').click()
    driver.find_element(By.CLASS_NAME, 'header-nav-link--public-user-guides').click()
    time.sleep(1)

    #news
    driver.find_element('xpath', '/html/body/header[1]/div/nav/div[3]/button').click()
    time.sleep(1)
    driver.find_element('xpath', '/html/body/header[1]/div/nav/div[3]/button').click()
    time.sleep(1)

    driver.find_element(By.CLASS_NAME, 'pointsGrid-cell--no-score').click()
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

    driver.find_element('xpath', '/html/body/header[1]/div/nav/div[5]/a/span').click()
    driver.find_element(By.CLASS_NAME, 'header-item-link--teams').click()
    time.sleep(1)
    driver.get(e_url)

    # starting course
    action = ActionChains(driver)
    driver.find_element(By.CLASS_NAME, 'headerBusca-icon-svg').click()
    driver.find_element(By.ID, 'headerBusca-campoBusca').send_keys('Cifra de César: Criptografando e decriptografando textos')
    driver.find_element(By.CLASS_NAME, 'headerBusca-submit').click()
    time.sleep(2)
    driver.find_element('xpath', '/html/body/div[4]/div[2]/section/ul/li[1]/a/div/p').click()
    driver.find_element(By.CLASS_NAME, 'course-header-button').click()
    time.sleep(2)
    driver.get('https://cursos.alurastart.com.br/course/criptografia-cesar/task/21223')
    time.sleep(2)
    action.send_keys(Keys.SPACE).perform()
    time.sleep(8)

    driver.find_element(By.CLASS_NAME, 'task-actions-button-next').click()
    driver.find_element(By.CLASS_NAME, 'task-actions-button-next').click()
    driver.find_element(By.CLASS_NAME, 'task-actions-button-next').click()
    driver.find_element(By.CLASS_NAME, 'task-actions-button-next').click()
    driver.find_element(By.CLASS_NAME, 'task-actions-button-next').click()
    time.sleep(2)

    # finishing
    driver.get(e_url)
    driver.find_element(By.CLASS_NAME, 'headerBusca-icon-svg').click()
    driver.find_element(By.ID, 'headerBusca-campoBusca').send_keys('>>>>>>>- ALURA-START WARMED UP SUCCESSFULLY -<<<<<<<  :)')
