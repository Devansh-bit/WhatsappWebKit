import time
from datetime import datetime

import chromedriver_autoinstaller

from WhatsappWebKit import Initializer

chromedriver_autoinstaller.install()  # Automatically install chromedriver for the the installed version of chrome

driver = Initializer.create_driver("chromedriver.exe", 9922)
window = Initializer.WebDriver(driver)
time.sleep(5)

chat = window.get_top_chat()  # Get top chat in the window and store in 'chat' variable
chat.click()  # Click on the chat to open it
for message in chat.get_loaded_messages():  # Get a list of loaded messages in the chat
    print(message.get_chat().get_name())
time.sleep(2)
###### Wait until certain time ######
def wait():
    day = datetime.now().day
    year = datetime.now().year
    month = datetime.now().month
    time_to_run = datetime(year, month, day, 12, 50)
    while (time_to_run - datetime.now()).seconds > 0:
        print((time_to_run - datetime.now()).seconds)
        time.sleep(0.5)
        continue

for loaded_chat in window.get_loaded_chats():
    if "y" in input("Should I send a message to {}".format(loaded_chat.get_name())):
        loaded_chat.send_message("test")

chat_by_name = window.get_chat_by_name("Basketball+Cricket")  # Create a Chat object from the title of the chat
print(chat_by_name.get_name())  # Print the title of the chat
for message in chat_by_name.get_loaded_messages():  # Get a list of loaded messages in the chat
    print(message.get_text())  # Print each loaded message
chat_by_name.send_message("Chalo sab niklo")  # Send a message to the chat
