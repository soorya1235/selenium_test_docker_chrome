from selenium.webdriver.common.by import By
from selenium import webdriver

import time

print("Test Execution Started")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Remote(
command_executor='http://localhost:4444/wd/hub',
options=options
)
#maximize the window size
driver.maximize_window()
time.sleep(5)
#navigate to browserstack.com
driver.get("https://www.browserstack.com/")
time.sleep(5)
msg = driver.current_url
print(msg)
#click on the Get started for free button
#driver.find_element_by_link_text("Get started free").click()
driver.find_element(By.LINK_TEXT,"Get started free").click()
time.sleep(5)
#close the browser
driver.close()
driver.quit()
print("Test Execution Successfully Completed!")