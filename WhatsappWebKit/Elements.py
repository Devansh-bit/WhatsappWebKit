from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
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





