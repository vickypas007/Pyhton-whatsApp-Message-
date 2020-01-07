from selenium import webdriver
from time import sleep
driver =  webdriver.Chrome(executable_path='C:/Users/Vicky/Downloads/chromedriver_win32/chromedriver.exe')
driver.get('https://web.whatsapp.com/')


while True:
    name =input("Enter the name of the user : ")
    filePath =input('Enter the FilePath(Images/Videos) :')

    count =int(input('Enter the count: '))
    input('Enter anything after scanning OR code')
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    for i in range(count):
        attachment_box =driver.find_element_by_xpath('//div[@title = "Attach"]')
        attachment_box.click()


        image_box = driver.find_element_by_xpath(
        '//input[@accept = "image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_box.send_keys(filePath)

        sleep(5)

        send_button =driver.find_element_by_xpath('//span[@data-icon = "send-light"]')
        send_button.click()

