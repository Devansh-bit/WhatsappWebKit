import re
import time
from WhatsappWebKit import Initializer
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
#from datetime import datetime
#day = datetime.now().day
#year = datetime.now().year
#month = datetime.now().month
#time_to_run = datetime(year, month, day, 7, 0)
#delta_time = time_to_run - datetime.now()
#time_to_sleep = delta_time.seconds
#print(time_to_sleep/3600, " hours")


driver = Initializer.create_driver("chromedriver.exe")
window = Initializer.WebDriver(driver)

time.sleep(5)
window.get_top_chat().click()
