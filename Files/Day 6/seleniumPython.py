from selenium import webdriver

browser=webdriver.Chrome("/Users/macdonald/Developer/Python/Selenium/drivers/chromedriver")
# the path for Chrome webdriver changes based on where the file is located.
browser.get("http://www.facebook.com")
#.get loads the web page in the browser object

browser.set_page_load_timeout(30)
# set_page_load_timeout(secs) is used sets the amount of time the program waits for 
# the browser to lead a web page before throwing an error!

print("Opening "+browser.title)

browser.get_screenshot_as_file("/Users/macdonald/Developer/Python/Selenium/ScreenShots/Facebook.png")
# saves a screenshot in the given path

browser.implicitly_wait(20)
#sends a timeout to implicitly wait for an element to be found

browser.find_element_by_id("email").send_keys("anyusername")
browser.find_element_by_id("pass").send_keys("correspondingpassword")
# findelementbyid is used to get the ID of the widget from the browser. sendkeys sends
# data to be filled in that particular location.

browser.find_element_by_id("loginbutton").click()

browser.get_screenshot_as_file("/Users/macdonald/Developer/Python/Selenium/ScreenShots/AfterLogin.png")

print("ScreenShot Captured!")
browser.quit()