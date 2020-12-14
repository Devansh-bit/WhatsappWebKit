import sys

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from WhatsappWebKit import Locators
from selenium import webdriver
import time


class Utils(Locators.window):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        super(Utils, self).__init__(self.driver)

    def get_text_from_message(self, message):
        """Converts message/list of message object(s) to text
           Returns message_deleted if the message was deleted or did not contain text"""

        if type(message) == WebElement:
            try:
                return message.find_element(By.XPATH,
                                            ".//span[@class='_1VzZY selectable-text invisible-space copyable-text']/span").text
            except NoSuchElementException:
                return "message_deleted"
        elif type(message) == list:
            msg_list = []
            for msg in message:
                try:
                    msg_list.append(msg.find_element(By.XPATH,
                                                     ".//span[@class='_1VzZY selectable-text invisible-space copyable-text']/span").text)
                except NoSuchElementException:
                    msg_list.append("message_deleted")
            return msg_list
        else:
            return None

    def wait_until_new_message_from_current_chat(self):
        last_message_id = self.get_loaded_messages()[-1].get_attribute("data-id")
        while True:
            try:
                new_message = self.get_loaded_messages()[-1]
                if last_message_id != new_message.get_attribute("data-id"):
                    return new_message
                else:
                    continue
            except:
                print("An unexpected error occured! (ele_stale)")
                continue

    def wait_for_new_message(self):
        """Might not function as expected if the window is being manually interacted with. To be fixed soon."""
        try:
            last_message_id = self.get_loaded_messages()[-1].get_attribute("data-id")
            last_top_chat_name = self.get_top_chat().find_element_by_xpath(
                ".//span[@class='_1hI5g _1XH7x _1VzZY' and @dir='auto']").get_attribute("title")
            while True:
                time.sleep(0.1)
                try:
                    new_message = self.get_loaded_messages()[-1]
                    current_chat_name = self.get_top_chat().find_element_by_xpath(
                        ".//span[@class='_1hI5g _1XH7x _1VzZY' and @dir='auto']").get_attribute("title")
                    if last_message_id != new_message.get_attribute("data-id"):
                        return new_message
                    if last_top_chat_name != current_chat_name:
                        self.get_top_chat().click()
                        return self.get_loaded_messages()[-1]

                    # try:
                    # self.driver.find_element_by_xpath("""//span[@class="VOr2j"]""").click()
                    # except NoSuchElementException:
                    # continue
                    # return self.get_unread_messages_from_current_chat()[0]

                except:
                    continue
        except:
            print("Unexpected Error! (Ex0987)")
            sys.exit()
