from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class window:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def get_top_chat(self):
        """waits for 20 seconds and locates presence of top chat then returns chat element"""
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@style,'translateY(0px)') and @class='_1MZWu']")))
        return element


    def get_unread_messages_from_current_chat(self):
        loaded_messages = self.get_loaded_messages()
        for message in loaded_messages:
            try:
                if message.get_attribute("class") == "XFAMv focusable-list-item":
                    unread_index = loaded_messages.index(message)
                    return loaded_messages[unread_index+1:]
            except:
                continue
        return []

    def get_chat_by_name(self, name):
        try:
            return self.driver.find_element_by_xpath("//div[@class='1MZWu'][.//span[@title='{}']]".format(name))
        except:
            print("Chat by name {} not found!".format(name))

    def get_chats_with_unread_messages(self):
        return self.driver.find_elements_by_xpath("//div[@class='_1MZWu'][.//span[@class='VOr2j']]")

    def get_loaded_messages(self):
        return self.driver.find_elements(By.XPATH, """//*[@id="main"]/div[3]/div/div/div[3]/*""")









