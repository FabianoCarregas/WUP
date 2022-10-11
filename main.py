import tkinter as tk
from functools import partial

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# os.system("gnome-terminal -e 'printf testando cmd'")

# logging in
def log_in(email, password, url):
    e_mail = (email.get())
    pass_word = (password.get())
    e_url = (url.get())
    driver = webdriver.Firefox()
    driver.get(e_url)

    driver.find_element('xpath', '/html/body/div/div[2]/button[3]').click()
    driver.find_element('xpath', '//*[@id="details-button"]').click()
    time.sleep(2)
    driver.find_element('xpath', '//*[@id="login-email"]').send_keys(e_mail)
    driver.find_element('xpath', '//*[@id="password"]').send_keys(pass_word)
    driver.find_element('xpath', '/html/body/div[3]/section/section[1]/form/div[1]/button').click()

    action = ActionChains(driver)
    driver.find_element(By.CLASS_NAME, 'headerBusca-icon-svg').click()
    driver.find_element(By.ID, 'headerBusca-campoBusca').send_keys('Certificação Java SE 7 Programmer I')
    driver.find_element(By.CLASS_NAME, 'headerBusca-submit').click()
    time.sleep(2)
    driver.find_element('xpath', '/html/body/div[4]/div[2]/section/ul/li[1]/a/div/p').click()
    driver.find_element(By.CLASS_NAME, 'course-header-button').click()
    time.sleep(2)
    action.send_keys(Keys.SPACE).perform()
    time.sleep(8)

    driver.find_element(By.CLASS_NAME, 'task-actions-button-next').click()
    driver.find_element(By.CLASS_NAME, 'task-actions-button-next').click()
    driver.find_element(By.CLASS_NAME, 'task-actions-button-next').click()
    driver.find_element(By.CLASS_NAME, 'task-actions-button-next').click()
    driver.find_element(By.CLASS_NAME, 'task-actions-button-next').click()
    time.sleep(2)

    # learning
    driver.get(e_url)

    driver.find_element(By.ID, 'courseLabel').click()
    driver.find_element(By.CLASS_NAME, 'header-nav-link--courses').click()
    time.sleep(1)

    driver.find_element(By.ID, 'courseLabel').click()
    driver.find_element(By.CLASS_NAME, 'header-nav-link--user-guides').click()
    time.sleep(1)

    driver.find_element(By.ID, 'courseLabel').click()
    driver.find_element(By.CLASS_NAME, 'header-nav-link--company-guides').click()
    time.sleep(1)

    #content
    driver.find_element(By.ID, 'contentLabel').click()
    driver.find_element(By.CLASS_NAME, 'header-item-link--gnarusflix').click()
    driver.execute_script("window.scrollTo(0,6000)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,0)")
    time.sleep(1)

    driver.find_element(By.ID, 'contentLabel').click()
    driver.find_element(By.CLASS_NAME, 'header-item-link--alura-mais').click()
    driver.execute_script("window.scrollTo(0,6000)")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,0)")
    time.sleep(1)

    driver.find_element(By.ID, 'contentLabel').click()
    driver.find_element(By.CLASS_NAME, 'header-item-link--degrees').click()
    time.sleep(1)

    driver.find_element(By.ID, 'contentLabel').click()
    driver.find_element(By.CLASS_NAME, 'header-item-link--immersions').click()
    time.sleep(1)

    driver.find_element(By.ID, 'contentLabel').click()
    driver.find_element(By.CLASS_NAME, 'header-item-link--cases').click()
    time.sleep(1)

    driver.find_element(By.ID, 'contentLabel').click()
    driver.find_element(By.CLASS_NAME, 'header-item-link--projects').click()
    time.sleep(1)

    driver.find_element(By.ID, 'contentLabel').click()
    driver.find_element(By.CLASS_NAME, 'header-item-link--podcasts').click()
    time.sleep(1)

    driver.find_element(By.ID, 'contentLabel').click()
    driver.find_element(By.CLASS_NAME, 'header-item-link--recommendations').click()
    time.sleep(1)

    #comunity
    driver.find_element('xpath', '/html/body/header[1]/div/nav/div[3]/a').click()
    driver.find_element(By.CLASS_NAME, 'header-item-link--forum').click()
    time.sleep(1)

    driver.find_element('xpath', '/html/body/header[1]/div/nav/div[3]/a').click()
    driver.find_element(By.CLASS_NAME, 'header-item-link--forum-interactions').click()
    time.sleep(1)

    driver.find_element('xpath', '/html/body/header[1]/div/nav/div[3]/a').click()
    driver.find_element(By.CLASS_NAME, 'header-nav-link--ranking').click()
    time.sleep(1)

    driver.find_element('xpath', '/html/body/header[1]/div/nav/div[3]/a').click()
    driver.find_element(By.CLASS_NAME, 'header-nav-link--public-user-guides').click()
    time.sleep(1)

    #news
    driver.find_element('xpath', '/html/body/header[1]/div/nav/div[4]/button').click()
    time.sleep(1)
    driver.find_element('xpath', '/html/body/header[1]/div/nav/div[5]/a/div[2]/div[18]').click()
    time.sleep(1)

    #profile
    driver.find_element('xpath', '/html/body/header[1]/div/nav/div[6]/a/span').click()
    driver.find_element(By.CLASS_NAME, 'header-nav-link--profile').click()
    time.sleep(1)

    driver.find_element('xpath', '/html/body/header[1]/div/nav/div[6]/a/span').click()
    driver.find_element(By.CLASS_NAME, 'header-nav-link--profile-edit').click()
    time.sleep(1)

    driver.find_element('xpath', '/html/body/header[1]/div/nav/div[6]/a/span').click()
    driver.find_element(By.CLASS_NAME, 'header-nav-link--purchases').click()
    time.sleep(1)

    driver.find_element('xpath', '/html/body/header[1]/div/nav/div[6]/a/span').click()
    driver.find_element(By.CLASS_NAME, 'header-item-link--vitrinedev').click()
    return

window = tk.Tk()
window.title('WUG')
window.geometry("390x165")

var_email = tk.StringVar()
var_password = tk.StringVar()
var_url = tk.StringVar()

tk.Label(window, text='Warm up Gnarus').grid(column=1, row=0)

tk.Label(window, text='-url-').grid(column=0, row=1)
url = tk.Entry(window, textvariable=var_url, width=35).grid(column=1, row=1)

tk.Label(window, text='Email').grid(column=0, row=2)
email = tk.Entry(window, textvariable=var_email, width=35).grid(column=1, row=2)

tk.Label(window, text='Key').grid(column=0, row=3)
password = tk.Entry(window, textvariable=var_password, show='*', width=35).grid(column=1, row=3)
tk.Checkbutton(window, text='save').grid(column=0, row=4)

log_in = partial(log_in, var_email, var_password, var_url)
tk.Button(window, text='$-START-$', command=log_in).grid(column=1, row=5)

window.mainloop()