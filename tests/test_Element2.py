import time
from datetime import datetime
import chromedriver_autoinstaller
from WhatsappWebKit import Initializer
chromedriver_autoinstaller.install()

driver = Initializer.create_driver("chromedriver.exe", 9922)
window = Initializer.WebDriver(driver)
time.sleep(5)
while len(window.get_chat_by_name("Enter Name of Chat").get_loaded_messages()) < 1:
    continue

window.get_chat_by_name("Enter Name of Chat").get_loaded_messages()[-1].delete()
time.sleep(1)
window.get_chat_by_name("Enter Name of Chat").get_loaded_messages()[-1].reply("Test")


