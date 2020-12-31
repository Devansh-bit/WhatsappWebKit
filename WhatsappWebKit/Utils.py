import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from WhatsappWebKit import Locators


class Utils(Locators.window):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        super(Utils, self).__init__(self.driver)

    def wait_for_new_message(self, frequency=0):
        """Waits until a new message is received and returns a MessageElement"""
        try:
            last_message_id = self.get_loaded_messages()[-1].get_attribute("data-id")
            last_top_chat_name = self.get_top_chat().get_name()
            while True:
                time.sleep(frequency)
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

    def search_for_chat(self, name_to_search):
        self.driver.find_element_by_xpath("//div[@class='_1awRl copyable-text selectable-text' and @data-tab='3']").send_keys(name_to_search)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, f"//div[@class='_1MZWu'][.//span[@title='{name_to_search}']]")))
        return self.get_chat_by_name(name_to_search)
