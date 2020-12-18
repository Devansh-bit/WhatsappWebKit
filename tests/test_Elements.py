import re
import time
from WhatsappWebKit import Initializer
import chromedriver_autoinstaller
from datetime import datetime

chromedriver_autoinstaller.install()  # Automatically install chromedriver for the the installed version of chrome

driver = Initializer.create_driver("chromedriver.exe")
window = Initializer.WebDriver(driver)
time.sleep(5)

chat = window.get_top_chat()  # Get top chat in the window and store in 'chat' variable
chat.click()  # Click on the chat to open it
for message in chat.get_loaded_messages():  # Get a list of loaded messages in the chat
    print(message.get_text())  # print text in the message
print(chat.get_name())
time.sleep(2)
###### Wait until certain time ######
day = datetime.now().day
year = datetime.now().year
month = datetime.now().month
time_to_run = datetime(year, month, day, 12, 50)
while (time_to_run - datetime.now()).seconds > 0:
    print((time_to_run - datetime.now()).seconds)
    time.sleep(0.5)
    continue

chat_by_name = window.get_chat_by_name("Basketball+Cricket")  # Create a Chat object from the title of the chat
print(chat_by_name.get_name())  # Print the title of the chat
for message in chat_by_name.get_loaded_messages():  # Get a list of loaded messages in the chat
    print(message.get_text())  # Print each loaded message
chat_by_name.send_message("Chalo sab niklo")  # Send a message to the chat
