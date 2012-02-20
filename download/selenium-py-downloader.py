import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

fp = webdriver.FirefoxProfile() # Workaround of download problem in firefox

fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir", os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

browser = webdriver.Firefox(firefox_profile=fp) # Get local session of firefox
browser.get("http://jon-jacky.github.com/uw_python/winter_2012/index.html") # Load page
assert "Internet Programming in Python" in browser.title
time.sleep(10.0) # Let the page load, will be added to the API
py_links = browser.find_elements_by_partial_link_text(".py") # Return list of .py links
for py in py_links:
    py.click() # Download .py links
try:
    browser.find_element_by_xpath("//a[contains(@href,'.py')]")
except NoSuchElementException:
    assert 0, "can't find python files to download"
browser.close() # Close browser
