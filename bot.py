from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup


def open_website(driver, url):
    driver.get(url)

def click_link_and_switch_window(driver, link_text):
    link_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, link_text))
    )
    link_element.click()
    time.sleep(2)  # Wait for the new window to open

    new_page_handle = driver.window_handles[-1]
    driver.switch_to.window(new_page_handle)

def click_element(driver, by, selector):
    clickable_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((by, selector))
    )
    clickable_element.click()
    time.sleep(2)  # Adjust the sleep time as needed

def find_selected_month(driver):
    month_element = driver.find_element(By.XPATH, '//*[@id="divDP"]/div/div/div/select')
    html_snippet_month = month_element.get_attribute("outerHTML")
    soup = BeautifulSoup(html_snippet_month, 'html.parser')
    return soup.find('option', {'selected': 'selected'}).text

def find_selected_day(driver):
    day_element = driver.find_element(By.XPATH, '//*[@id="divDP"]/div/table/tbody')
    html_snippet_day = day_element.get_attribute("outerHTML")
    soup = BeautifulSoup(html_snippet_day, 'html.parser')
    return soup.find('td', class_='ui-datepicker-days-cell-over dayA ui-datepicker-current-day').text

def find_selected_time(driver):
    time_element = driver.find_element(By.CSS_SELECTOR, '#slot1')
    html_snippet_time = time_element.get_attribute("outerHTML")
    soup = BeautifulSoup(html_snippet_time, 'html.parser')
    return soup.find('span').text

def main():
    closest_appointment = {}
    url = "https://www.heilbronn.de/rathaus/buergerservice-a-z/inhalt/auslaenderbehoerde.html"
    driver = webdriver.Chrome()

    try:
        open_website(driver, url)
        click_link_and_switch_window(driver, "Termin vereinbaren")
        click_element(driver, By.CSS_SELECTOR, '#iarrow71555')
        click_element(driver, By.XPATH, '//*[@id="174045"]')
        click_element(driver, By.XPATH, '//*[@id="bp1"]')

        # find the given month on the page
        closest_appointment['month'] = find_selected_month(driver)
        print("Selected Month:", closest_appointment['month'])

        # find given day
        closest_appointment['day'] = find_selected_day(driver)
        print("Selected day:", closest_appointment['day'])

        # find given slot
        closest_appointment['time'] = find_selected_time(driver)
        print("Selected time:", closest_appointment['time'])

    finally:
        # Close the browser window
        driver.quit()
		
if __name__ == "__main__":
    main()
