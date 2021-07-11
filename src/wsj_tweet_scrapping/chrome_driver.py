# works with Microsoft Edge and it's driver
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from bs4 import BeautifulSoup


def open_driver(executable_driver_path: str):
    """
    Open and return driver.
    
    Note : Path to chrome driver should be set correctly.
    """
    executable_driver_path = r"C:\\Users\\user\\Downloads\\Softwares\\chromedriver_win32\\chromedriver.exe"
    return webdriver.Chrome(executable_driver_path)


def load_url(driver: WebDriver,
             url : str,
             verbose : bool: False):
    """
    Load URL using driver.
    
    Parameters
    ----------
    driver : selenium.chrome.webdriver.
    
    url : str.
    
    verbose : boolean, default=False
        if True, print function log.
    """
    if verbose >= 5: print("Loading page")
    try:
        driver.get(url) # loading page
    except Exception as e:
        print(f"Failed loading page for url : {url}, exception : {e}")
        
        
def get_driver_page_source(driver : WebDriver):
    """Extract page source and return BeautifulSoup object."""
    return BeautifulSoup(driver.page_source, "lxml")
