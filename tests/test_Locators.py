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
meet_driver = Initializer.create_meet_driver("chromedriver.exe")
window.meet_sign_in(meet_driver, "your_email_here@host.com")

time.sleep(5)
window.get_top_chat().click()
#print("going to sleep for {} seconds".format(time_to_sleep))
#time.sleep(time_to_sleep)
print("Waking up! Starting main thread")
while True:
    driver.execute_script("window.focus();")
    message = window.wait_for_new_message()
    text = window.get_text_from_message(message)
    print(text)
    if "https://meet.google.com/" in text:
        window.open_meet(meet_driver, (re.search("(?P<url>https?://[^\s]+)", text).group("url")), class_time=40)



