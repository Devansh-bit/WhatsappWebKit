import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


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

    def __get_loaded_messages(self):
        """Returns all loaded messages and tags in the current chat"""
        messages = []
        for message in self.chat.find_elements(By.XPATH, """//*[@id="main"]/div[3]/div/div/div[3]/*"""):
            messages.append(MessageElement(message))
        return messages
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
        loaded_messages = self.__get_loaded_messages()
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

    def wait_until_new_message(self):
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

    def get_chat(self):
        """Returns a chat element from the message element"""
        name = self.message.find_element_by_xpath(".//ancestor::div[@class='i5ly3 _2l_Ww']").find_element_by_xpath(".//span[@class='_1hI5g _1XH7x _1VzZY']").text
        chat: ChatElement = ChatElement(self.message.find_element_by_xpath("//div[@class='_1MZWu'][.//span[@title='{}']]".format(name)))
        return chat

    def delete(self, everyone=False):
        """Deletes the message passed.
           use everyone=True for deleting messages for everyone"""
        self.message.click()
        self.message.send_keys(Keys.ARROW_RIGHT)
        self.message.find_element_by_xpath("//div[@title='Delete message']").click()
        try:
            self.message.find_element_by_xpath('//div[@class="_30EVj gMRg5"]').click()
        except:
            if not everyone:
                self.message.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[3]/div/div[1]/div').click()
            else:
                self.message.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[3]/div/div[3]/div').click()

    def reply(self, text=None):
        """Adds reply of the passed message to the input box.
           If text is given, sends the the message with provided text"""
        self.message.click()
        self.message.send_keys(Keys.ARROW_RIGHT)
        try:
            self.message.find_element_by_xpath("//div[@title='Reply']").click()
        except NoSuchElementException:
            raise Exception("Message has been been deleted")
        if text is not None:
            self.get_chat().send_message(text)






