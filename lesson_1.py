"""
Lesson 1: Using Selenium webdriver to checkout search field of python.org website.
"""

from selenium import webdriver # Importing the webdrivers

from selenium.webdriver.common.keys import Keys # Keyboard keys


browser = webdriver.Firefox() # Firefox browser

browser.get("https://python.org") # Opens python.org browser

assert "Python" in browser.title # Assertion check if python is in the browser title or not

elem = browser.find_element_by_name("q") # Search html element with name = "q"

elem.clear() # clears any value in that html element

elem.send_keys("tuple") # Adds the text "tuple" to that html element

elem.send_keys(Keys.ENTER) # press enter

assert "No result found" not in browser.page_source # Checks if the page source has "No result found" in the html source

browser.quit() # Quits the browser