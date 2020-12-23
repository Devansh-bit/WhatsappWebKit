import threading
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class GoogleMeet():
    def open_meet(self, meet_driver:webdriver.Chrome, meet_link, class_time):
        meet_driver = meet_driver
        meet_driver.execute_script("window.open('');")
        new_handle = meet_driver.window_handles.index(meet_driver.current_window_handle) + 1
        meet_driver.switch_to.window(meet_driver.window_handles[new_handle])
        MyThread(meet_driver, new_handle, class_time).start()
        meet_driver.get(meet_link)
        time.sleep(5)
        element = meet_driver.find_element_by_xpath("//body")
        element.send_keys(Keys.CONTROL, 'd')
        element1 = meet_driver.find_element_by_xpath("//body")
        element1.send_keys(Keys.CONTROL, 'e')
        WebDriverWait(meet_driver, 90).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span")))
        join = meet_driver.find_element_by_xpath(
            '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
        join.click()
    def meet_sign_in(self, meet_driver, email):
        meet_driver.get(
            "https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow")
        WebDriverWait(meet_driver, 90).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='identifierId']")))
        meet_driver.find_element_by_xpath("//*[@id='identifierId']").send_keys(email)
        meet_driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()
        WebDriverWait(meet_driver, 90).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='logo']/img")))

def meet_leave(meet_driver:webdriver.Chrome, handle_id):
    print("leaving")
    meet_driver.switch_to.window(meet_driver.window_handles[handle_id])
    element1 = meet_driver.find_element_by_xpath("//body")
    element1.send_keys(Keys.CONTROL)
    try:
        meet_driver.find_element_by_xpath("//*[@id='ow3']/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div/span").click()
    except:
        print("couldnt exit!")
        pass


class MyThread(threading.Thread):
    def __init__(self, meet_driver:webdriver.Chrome, handle_id, class_time_in_minutes):
        threading.Thread.__init__(self)
        self.meet_driver = meet_driver
        self.handle_id = handle_id
        self.class_time = class_time_in_minutes

    def run(self):
        print("starting new meet thread")
        time_start = datetime.now()
        while True:
            time.sleep(60)
            time_now = datetime.now()
            diff = time_now-time_start
            if diff.seconds >= (self.class_time * 60):
                meet_leave(meet_driver=self.meet_driver, handle_id=self.handle_id)
                return
















