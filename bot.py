from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# URL of the website
url = "https://www.heilbronn.de/rathaus/buergerservice-a-z/inhalt/auslaenderbehoerde.html"

# Create a new instance of the Firefox driver (you can use other drivers like Chrome)
driver = webdriver.Chrome()

try:
    # Open the website

    # Locate the specific link you want to click (replace 'Link Text' with the actual link text)
	driver.get(url)
	link_text = "Termin vereinbaren"
	link_element = WebDriverWait(driver, 10).until(
		EC.element_to_be_clickable((By.LINK_TEXT, link_text))
	)

		# Click on the link
	link_element.click()
	time.sleep(2) 
	# tab_text = "Aufenthaltserlaubnis Familienname Ku - Z"
	# tab_element = WebDriverWait(driver, 10).until(
	# 	EC.presence_of_element_located((By.XPATH, '//*[@id="sg63091"]'))
	# )
	# tab_element.click()
	new_page_handle = driver.window_handles[-1]
	driver.switch_to.window(new_page_handle)
	clickable_elements = driver.find_element(By.CSS_SELECTOR, '#iarrow71555')
	# Print the IDs of clickable elements
	print(clickable_elements.text)
	clickable_elements.click()
	time.sleep(2) 
	clickable_elements = driver.find_element(By.XPATH, '//*[@id="174045"]')
	# Print the IDs of clickable elements
	print(clickable_elements.text)
	clickable_elements.click() 
	time.sleep(2) 
	clickable_elements = driver.find_element(By.XPATH, '//*[@id="bp1"]')
	# Print the IDs of clickable elements
	print(clickable_elements.text)
	clickable_elements.click()
	time.sleep(5) 
		# Add any additional actions you want to perform on the new page here

finally:
    # Close the browser window
    driver.quit()


https://www.browserstack.com/guide/datepicker-in-selenium