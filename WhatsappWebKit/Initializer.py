from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from WhatsappWebKit import GoogleMeet
from WhatsappWebKit import Utils


def create_driver(path_to_chromedriver, port:int = None):
    """Create the driver used for whatsapp web with preset options.
       If the chromedriver.exe is in Path, put "chromedriver.exe" in path_to_chromedriver
       Use the port to interact with pre-opened Chrome window"""
    opt = Options()
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")
    # Pass the argument 1 to allow and 2 to block
    if port is None:
        opt.add_experimental_option("prefs", { \
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 1,
            "profile.default_content_setting_values.notifications": 1
        })
    else:
        opt.add_experimental_option("debuggerAddress", "localhost:{}".format(port))
    driver = webdriver.Chrome(path_to_chromedriver, chrome_options=opt)
    return driver
def create_meet_driver(path_to_chromedriver):
    """Creates a driver specifically for the GoogleMeet module"""
    opt = Options()
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")
    # Pass the argument 1 to allow and 2 to block
    opt.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 2
    })
    driver = webdriver.Chrome(executable_path=path_to_chromedriver, chrome_options=opt)
    return driver
class WebDriver(Utils.Utils, GoogleMeet.GoogleMeet):
    """This is the main class to be manipulated.
       Create a driver object using Initializer.create_driver() and pass the object"""
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.driver = driver
        self.driver.get("https://web.whatsapp.com")
        WebDriverWait(self.driver, 90).until(EC.visibility_of_element_located((By.XPATH, """//*[@id="side"]/div[1]/div/label/div/div[2]""")))






