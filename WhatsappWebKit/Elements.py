import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChatElement(WebElement):
    def __init__(self, chat: WebElement):
        """A WebElement that contains a whatsapp web chat"""
        super().__init__(chat.parent, chat.id)
        if not chat.get_attribute("class") == "_1MZWu":
            raise TypeError("Element is not a chat")
        self.chat = chat

    def get_name(self):
        """Returns the name of the chat"""
        if type(self.chat) == WebElement:
            return self.chat.find_element_by_xpath(".//span[@dir='auto']").text

    def get_loaded_messages(self):
        """Returns all loaded messages and tags in the current chat"""
        self.chat.click()
        messages = []
        for message in self.chat.find_elements(By.XPATH, """//*[@id="main"]/div[3]/div/div/div[3]/*"""):
            messages.append(MessageElement(message))
        return messages

    def get_unread_messages(self):
        """Gets unread messages from the chat"""
        self.chat.click()
        loaded_messages = self.get_loaded_messages()
        for message in loaded_messages:
            try:
                if message.get_attribute("class") == "XFAMv focusable-list-item":
                    unread_index = loaded_messages.index(message)
                    return loaded_messages[unread_index + 1:]
            except:
                continue
        return []

    def send_message(self, message:str):
        """Sends the given message to the chat"""
        self.chat.click()
        text_box = self.chat.find_element_by_xpath("//div[@class='_1awRl copyable-text selectable-text' and @data-tab='6']")
        text_box.click()
        text_box.send_keys(message)
        time.sleep(0.1)
        send_button = self.chat.find_element_by_xpath("//button[@class='_2Ujuu']")
        send_button.click()
        #except NoSuchElementException:
        #    print("Couldn't send message!")



class MessageElement(WebElement):
    """A WebElement that contains a whatsapp web message"""
    def __init__(self, message: WebElement):
        super().__init__(message.parent, message.id)
        self.message = message

    def get_text(self):
        """Converts message/list of message object(s) to text.
                   Returns message_deleted if the message was deleted or did not contain text"""
        if type(self.message) == WebElement:
            try:
                return self.message.find_element(By.XPATH,
                                            ".//span[@class='_1VzZY selectable-text invisible-space copyable-text']/span").text
            except NoSuchElementException:
                return "message_deleted"






