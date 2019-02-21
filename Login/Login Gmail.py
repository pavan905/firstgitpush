from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")

driver.maximize_window()

driver.find_element_by_id("email").send_keys("pavan905@gmail.com")
driver.find_element_by_id("pass").send_keys("Mp3@mylyf!")

driver.find_element_by_id("loginbutton").click()
#driver.find_element_by_css_selector("body").click()



