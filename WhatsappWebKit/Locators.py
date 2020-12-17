from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from WhatsappWebKit import Elements


class window:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def get_top_chat(self):
        """Returns the top chat in the window"""
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(@style,'translateY(0px)') and @class='_1MZWu']")))
        return Elements.ChatElement(element)

    def get_unread_messages_from_current_chat(self):
        """Returns all messages under the 'unread' tag in a chat"""
        loaded_messages = self.get_loaded_messages()
        for message in loaded_messages:
            try:
                if message.get_attribute("class") == "XFAMv focusable-list-item":
                    unread_index = loaded_messages.index(message)
                    return loaded_messages[unread_index + 1:]
            except:
                continue
        return []

    def get_chat_by_name(self, name):
        """Returns the chat element with the specified element"""
        try:
            return Elements.ChatElement(self.driver.find_element_by_xpath("//div[@class='1MZWu'][.//span[@title='{}']]".format(name)))
        except:
            print("Chat by name {} not found!".format(name))

    def get_chats_with_unread_messages(self):
        """Returns chats with unread messages using the green notification icon"""
        chats = []
        for chat in self.driver.find_elements_by_xpath("//div[@class='_1MZWu'][.//span[@class='VOr2j']]"):
            chats.append(Elements.ChatElement(chat))
        return chats

    def get_loaded_messages(self):
        """Returns all loaded messages and tags in the current chat"""
        messages = []
        for message in self.driver.find_elements(By.XPATH, """//*[@id="main"]/div[3]/div/div/div[3]/*"""):
            messages.append(Elements.MessageElement(message))
        return messages
