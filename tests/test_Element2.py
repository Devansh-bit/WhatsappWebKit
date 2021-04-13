import time
import chromedriver_autoinstaller
from WhatsappWebKit import Initializer

chromedriver_autoinstaller.install()

driver = Initializer.create_driver("chromedriver.exe", port=6942)
window = Initializer.WebDriver(driver)
time.sleep(5)
chat = window.search_for_chat("bruh")
chat.click()
time.sleep(2)
messages = chat.get_loaded_messages()
for message in chat.get_loaded_messages():
    print(message.get_text())
