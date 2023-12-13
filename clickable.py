from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# URL of the website
url = "https://www.qtermin.de/qtermin-stadtheilbronn-abh"

# Create a new instance of the Firefox driver (you can use other drivers like Chrome)
driver = webdriver.Chrome()

try:
    # Open the website
	driver.get(url)
    # Locate the specific link you want to click (replace 'Link Text' with the actual link text)
	time.sleep(2) 
	clickable_elements = driver.find_element(By.CSS_SELECTOR, '#sg71558txt')
	# Print the IDs of clickable elements
	print(clickable_elements.text)
	clickable_elements.click()
	time.sleep(2) 
	
		# Add any additional actions you want to perform on the new page here


#\31 74045
finally:
    # Close the browser window
    driver.quit()


