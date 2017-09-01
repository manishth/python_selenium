"""
Lesson 3: Capturing screenshots using selenium.
"""

from selenium import webdriver

browser = webdriver.Firefox()

browser.set_page_load_timeout(30) #It will try to reach the page for 30 secs, it will return an error if it doesn't respond.

browser.get("http://python.org")

browser.maximize_window() # maximize browser's window

browser.implicitly_wait(20) # Wait for 20 seconds

browser.get_screenshot_as_file("python_website.png") # provide the path to where the image will be saved.

browser.quit()