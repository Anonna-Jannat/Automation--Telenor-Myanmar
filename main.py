from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\selenium\chromedriver_win32\chromedriver.exe")
driver.get("https://www.telenor.com.mm/en")
driver.maximize_window()

searchtxtbox = driver.find_element_by_name('search')
print(searchtxtbox.is_displayed())
print(searchtxtbox.is_enabled())
driver.find_element_by_xpath('//*[@id="navigation"]/div[2]/ul[1]/li[1]/a').click()  # Internet


driver.find_element_by_xpath('//*[@id="navigation"]/div[2]/ul[1]/li[2]/a').click()  # International


driver.find_element_by_xpath('//*[@id="navigation"]/div[2]/ul[1]/li[3]/a').click()  # telenor star
driver.find_element_by_xpath('//*[@id="navigation"]/div[2]/ul[1]/li[4]/a').click()  # help


driver.find_element_by_xpath('//*[@id="navigation"]/div[2]/ul[3]/li[1]/a').click()  # packages and plan


driver.find_element_by_xpath('//*[@id="navigation"]/div[2]/ul[3]/li[2]/a').click() # sim and top up


driver.find_element_by_xpath('//*[@id="navigation"]/div[2]/ul[3]/li[3]/a').click()  # Services


driver.find_element_by_xpath('//*[@id="navigation"]/div[2]/ul[3]/li[4]/a').click()  # Gaming and entertainment
driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[1]/a').click()  # personal
driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[2]/a').click()  # Business
driver.find_element_by_xpath('/html/body/header/div[2]/div/div[2]/ul/li[3]/a').click()   # about us
driver.close()
