from selenium import webdriver
from time import sleep
from pattern.web import URL, extension, cache, plaintext, Newsfeed, DOM

# from secrets import username, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(2)

        # fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        # fb_btn.click()

        # # switch to login popup
        # base_window = self.driver.window_handles[0]
        # self.driver.switch_to_window(self.driver.window_handles[1])

        # email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        # email_in.send_keys(username)

        # pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        # pw_in.send_keys(password)

        # login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        # login_btn.click()

        # self.driver.switch_to_window(base_window)

        # popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        # popup_1.click()

        # popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        # popup_2.click()

    # def like(self):
    #     like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
    #     like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//main/div/div/div/div/div/div[2]/div[2]/button')
        dislike_btn.click()

    def get_persent_data(self):
        info = self.driver.find_element_by_xpath('//main/div/div/div/div/div/div[1]/div[3]/div[3]/button')            
        info.click()
        detail = self.driver.find_element_by_xpath('//main/div/div/div/div/div[1]/div/div[2]/div[1]/div/div[1]')
        name = detail.find_element_by_xpath('div[1]/h1').text
        age = detail.find_element_by_xpath('span').text
        addition_info = self.driver.find_element_by_xpath('//main/div/div/div/div/div[1]/div/div[2]/div[1]/div/div[2]')
        addition_info = [x.text for x in addition_info.find_elements_by_xpath('div/div')]
        description = ''
        try:
            description = self.driver.find_element_by_xpath('//main/div/div/div/div/div[1]/div/div[2]/div[2]')
            description = description.text
        except:
            print("No Description")
        left = self.driver.find_element_by_xpath('//main/div/div/div/div/div/div[2]/div[2]/button')
        right = self.driver.find_element_by_xpath('//main/div/div/div/div/div/div[2]/div[2]/button')


    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = TinderBot()
bot.login()


