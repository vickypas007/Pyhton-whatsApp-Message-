from selenium import webdriver

driver =  webdriver.Chrome(executable_path='C:/Users/Vicky/Downloads/chromedriver_win32/chromedriver.exe')
driver.get('https://web.whatsapp.com/')


while True:
    name =input("Enter the name of the user : ")
    msg =input('Enter the Message :')
    count =int(input('Enter the count: '))
    input('Enter anything after scanning OR code')
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    msg_box =driver.find_element_by_class_name('_13mgZ')
    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_3M-N-')
        button.click()










