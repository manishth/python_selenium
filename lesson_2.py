"""
Lesson 2: Getting the page source (HTML) of the source.
"""

from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("https://python.org")

html = browser.page_source

print(html)
