import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from WhatsappWebKit.Elements import MessageElement
from WhatsappWebKit import Locators


class Utils(Locators.window):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        super(Utils, self).__init__(self.driver)

    def wait_until_new_message_from_current_chat(self):
        """Waits until a new message is received in the current chat and returns a MessageElement"""
        last_message_id = self.get_loaded_messages()[-1].get_attribute("data-id")
        while True:
            try:
                new_message = self.get_loaded_messages()[-1]
                if last_message_id != new_message.get_attribute("data-id"):
                    return new_message
                else:
                    continue
            except:
                print("Error encountered (0x001)")
                continue

    def wait_for_new_message(self, wait=0):
        """Waits until a new message is received and returns a MessageElement"""
        try:
            last_message_id = self.get_loaded_messages()[-1].get_attribute("data-id")
            last_top_chat_name = self.get_top_chat().get_name()
            while True:
                time.sleep(wait)
                try:
                    new_message = self.get_loaded_messages()[-1]
                    current_chat_name = self.get_top_chat().find_element_by_xpath(
                        ".//span[@class='_1hI5g _1XH7x _1VzZY' and @dir='auto']").get_attribute("title")
                    if last_message_id != new_message.get_attribute("data-id"):
                        return new_message
                    if last_top_chat_name != current_chat_name:
                        self.get_top_chat().click()
                        return self.get_loaded_messages()[-1]
                except:
                    continue
        except:
            print("Unexpected Error! (0x002)")


