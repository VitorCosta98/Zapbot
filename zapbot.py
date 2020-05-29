from selenium import webdriver
import time

# driver = webdriver.Chrome("C:/Users/michael/Downloads/chromedriver_win32/chromedriver.exe")

class whatsAppBot:
    def __init__(self, driver):
        self.mensagem = "Hello, there!"
        self.grupos = ["Secrets"] 
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = driver

    def enviarMensagens(self):
        #GROUPS: <span dir="auto" title="Secrets " class="_1wjpf _3NFp9 _3FXB1">Secrets </span>
        #BOX-TEXT: <div tabindex="-1" class="_1Plpp">
        #BUTTON-SEND: <span data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(15)

        grupo = self.driver.find_element_by_xpath("//span[@title='Secrets ']")
        time.sleep(3)
        grupo.click()
        
        chat_box = self.driver.find_element_by_class_name('_1Plpp')
        time.sleep(3)
        chat_box.click()
        
        while(True):
            chat_box.send_keys(self.mensagem)
            send_button = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(2)
            send_button.click()
            time.sleep(1)

gc = webdriver.Chrome(executable_path=r'./chromedriver')
bot = whatsAppBot(gc)
bot.enviarMensagens()

print("hello, world")