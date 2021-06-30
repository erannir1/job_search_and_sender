from selenium import webdriver
from jobs_scraper import JobsScraper
from indeed_job_scrap import message_list
from selenium.webdriver.common.keys import Keys

d = 'chromedriver.exe'
name = input('Enter group/user name:\nexample: Cleantech TAU\n')
msg = message_list

message_head = "Hey guys, here is this week jobs:"
eran_str = "This message sent from Eran Nir using Python"


def send_whatsapp_msg(driver, send_to, message):
    driver = webdriver.Chrome(driver)
    driver.get("https://web.whatsapp.com/")
    driver.maximize_window()

    # name = input("Enter name or group name:")
    # msg = input("Enter message:")
    count = 1

    input("Enter anything after scan QR code:\n")

    user = driver.find_element_by_xpath("//span[@title='{}']".format(send_to))
    user.click()

    msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

    for index in range(count):
        msg_box.send_keys(message_head, "\ue008\ue007")
        for elem in message:
            msg_box.send_keys(elem, "\ue008\ue007")  # Write -> New line
        msg_box.send_keys(eran_str, "\ue008\ue007")
        driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()

    print("Success")


send_whatsapp_msg(driver=d, send_to=name, message=msg)
