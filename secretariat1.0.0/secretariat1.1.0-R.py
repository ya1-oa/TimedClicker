from cryptography.fernet import Fernet # apache or BSD
from selenium import webdriver # apache 
from selenium.webdriver.common.by import By   # apache 
from selenium.webdriver.chrome.service import Service  # apache
from selenium.webdriver.support.ui import WebDriverWait  # apache
from selenium.webdriver.support import expected_conditions as EC  # apache
from selenium.webdriver.chrome.options import Options  # apache
#and chrome driver license
from subprocess import CREATE_NO_WINDOW #standard library
from selenium.common.exceptions import NoSuchElementException  # apache
from selenium.common.exceptions import ElementNotSelectableException  # apache
from selenium.common.exceptions import ElementNotVisibleException  # apache
from selenium.common.exceptions import TimeoutException  # apache
import threading # standard library
import tkinter as tk # standard library 
import tkinter.ttk as ttk # standard library
import sys, time, os #standard library
from twisted.internet import reactor # MIT 
from twisted.internet.task import LoopingCall # MIT 
import subprocess # standard library
import ctypes # MIT 
from PIL import ImageTk,Image # HPND License
#nuitka for packaging and distribution is apache

users_UUID = '3259A1A8-6119-0000-0000-000000000000'

y = str(subprocess.check_output('wmic csproduct get UUID'))
fp = y.find("\\n")+2
yid = y[fp:-15]



#c = b"""

x = yid == users_UUID 

class element_has_ctr(object):
  def __init__(self, loc, css):
    self.loc = loc
    self.css = css

  def __call__(self, driver):
    element = driver.find_element(*self.loc)
    if self.css in element.get_attribute("class"):
        return True
    else:
        return False

class TimedClicker():
 
    def __init__(self):
        def load(file: str) -> str:
            return os.path.join(os.path.dirname(__file__), file)
        self.options = Options()   
        self.options.add_argument("--start-maximized")
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.service = Service(load("driver/chromedriver.exe"))# add if drop down is X set driver to X for multiple browsers
        self.service.creationflags = CREATE_NO_WINDOW

        self.stop = False
        self.driver_on = False
        self.reactor_on = False
        self.do_levels = False
    
    def start_driver(self):
        self.driver = webdriver.Chrome(service=self.service, options=self.options, )# add if statements to start different browsers based on X
        self.driver_on = True
    
    def is_Start(self):
            global log
            log.set("Starting")
            self.start_driver()
            self.findSite("https://cotps.com/#/pages/login/login?originSource=transaction") #/html/body/uni-app/uni-tabbar/div[1]/div[3]/div/div[2]
            self.wait_Ctr()
            self.findSite("https://cotps.com/#/pages/transaction/transaction")
            self.sLogic()
       
    def findSite(self, site_):
        try:
            self.driver.get(site_)    
        except:
            log.set("Page failed to load.") 
            sys.exit()

    def no_Levels(self):
        self.do_levels = False

    def yes_Levels(self):
        self.do_levels = True

    def wait_click_x(self, xpath_, button):
        try:
            wait = WebDriverWait(self.driver, 300)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_)))
            element.click()
            log.set("Clicked " + button)
        except TimeoutException:
            log.set("Timed out finding " + button + " restart")
            sys.exit()

    def does_Exist(self, xp):
        try:
            self.driver.find_element(By.XPATH, (xp))
        except NoSuchElementException:
            return False
        return True

    def wait_Ctr(self):
        try:
            wait = WebDriverWait(self.driver, 300)
            wait.until(element_has_ctr((By.XPATH, '/html/body'), "uni-body pages-userCenter-userCenter"))
        except TimeoutException:
            log.set("Timed out finding User Center, restart")
            sys.exit()

            
    def wait_Lst(self):
        
        try:
            wait = WebDriverWait(self.driver, 10, poll_frequency=2)
            lst = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//uni-view[@class='itemList list']")))
            
            if not lst:
                return False
            else:
                return True
        except TimeoutException:
            log.set("Timed out finding List")
            pass
      
    def wait_Check(self):
        try:
            wait = WebDriverWait(self.driver, 15)
            wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//uni-toast[@data-duration='1500']")))
        except TimeoutException:
            log.set("Timed out finding Check, restart")
            sys.exit()
 
    
    def wait_Btn(self, css, button):
        try:
            wait = WebDriverWait(self.driver, 300)
            btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css)))
            btn.click()
        except TimeoutException:
            log.set("Timed out finding " + button + " restart")
            sys.exit()
        log.set("Clicked " + button)


    def sLogic(self):
        def secretariat_brain():
            if self.stop == True:
                sys.exit()
            try:
                wait = WebDriverWait(self.driver, 300)
                balance = wait.until(EC.visibility_of_all_elements_located((By.XPATH , "//uni-view[@class='division-num' and text()!='']")))
                transaction = float(balance[0].text)
                wallet_num = float(balance[1].text)
                wallet = 5.0 
                W_over5 = wallet_num > wallet 
                T_over0 = transaction > 0.0 
                log.set("Wallet: $" + str(wallet_num) + " Transaction: $" + str(transaction))
            except TimeoutException:
                log.set("Timed out finding assets, restart")
                sys.exit()
  
            if W_over5 == False and T_over0 == False and self.stop == False:
                log.set("Close and run after Funding your account")
                sys.exit()

            if W_over5 == False and T_over0 == True and self.stop == False:
                for i in range(7800,0,-1):
                    if self.stop == False:
                        hours, remainder = divmod(i, 3600)
                        mins, secs = divmod(remainder, 60)
                        timeformat = "{:02d}:{:02d}:{:02d}".format(hours, mins, secs)
                        log.set(timeformat)
                        time.sleep(1)
                    else:
                        log.set("Timer terminated, restart")
                        break
                        
                
                
                while True and self.stop == False:
                    log.set("Evaluating if Transaction is still Zero")

                    try:
                        log.set("Refreshing")
                        self.driver.refresh()
                    except:
                        log.set("Page failed to load.")
                        sys.exit()
                    
                    try:
                        wait = WebDriverWait(self.driver, 300)
                        balance = wait.until(EC.visibility_of_all_elements_located((By.XPATH , "//uni-view[@class='division-num' and text()!='']")))
                        transactionC = float(balance[0].text)
                        t_bool = transactionC > 0.0 
                        log.set("Transaction has $" + str(transactionC))
                    except TimeoutException:
                        log.set("Timed out finding transaction, restart")
                        sys.exit()

                    if t_bool == False and self.stop == False:
                        log.set("Exiting timer")
                        time.sleep(1)
                        break
                    if t_bool == True and self.stop == False:
                        for i in range(60,0,-1):
                            if self.stop == False:
                                hours, remainder = divmod(i, 3600)
                                mins, secs = divmod(remainder, 60)
                                timeformat = "{:02d}:{:02d}:{:02d}".format(hours, mins, secs)
                                log.set(timeformat)
                                time.sleep(1)
                            else:
                                log.set("Timer terminated restart")
                                break

            if W_over5 == True and T_over0 == False and self.stop == False:
                log.set("Preparing to Trade.")
                # if user has set levels button to ON
                if self.do_levels == True:
                    log.set("Checking for Levels")
                    wait = WebDriverWait(self.driver, 300)
                    try:
                        self.driver.get("https://cotps.com/#/pages/userCenter/myTeam")
                    except:
                        log.set("Page failed to load.")

                    if self.wait_Lst():
                        try:
                            res1 = wait.until(EC.visibility_of_all_elements_located((By.XPATH , "//uni-view[@class='card-num' and text()!='']")))   
                            residual1 = float(res1[1].text)
                            resBool1 = residual1 > 0.0
                            log.set("Residual Income has $" + str(residual1))
                        except TimeoutException:
                            log.set("Timed out finding assets, restart")
                            sys.exit()
                        if resBool1 == True:
                            log.set("Getting lvl 1!")
                            self.wait_click_x("/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view/uni-button", "Lvl 1 Recieve") 
                            log.set("Successful lvl 1!")
                            self.wait_Check()
                            time.sleep(1)
                    else:
                        log.set("No residual income found")
                        pass  

                    self.wait_click_x("/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[2]", "Lvl 2 Tab") # click lvl 2 button  
                    if self.wait_Lst():
                        try:
                            res2 = wait.until(EC.visibility_of_all_elements_located((By.XPATH , "//uni-view[@class='card-num' and text()!='']"))) 
                            residual2 = float(res2[1].text)
                            resBool2 = residual2 > 0.0
                            log.set("Residual Income has $" + str(residual2))
                        except TimeoutException:
                            log.set("Timed out finding assets, restart")
                            sys.exit()
                        
                        if resBool2 == True: 
                            log.set("Getting lvl 2")
                            self.wait_click_x("/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view/uni-button", "Lvl 2 Recieve") # click lvl 2 recieve
                            log.set("Succesful lvl 2!")
                            self.wait_Check()
                            time.sleep(1)
                
                    self.wait_click_x("/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[3]", "Lvl 3 Tab") # click lvl 3 button
                    if self.wait_Lst():
                        try:
                            res3 = wait.until(EC.visibility_of_all_elements_located((By.XPATH , "//uni-view[@class='card-num' and text()!='']")))
                            residual3 = float(res3[1].text)
                            resBool3 = residual3 > 0.0
                            log.set("Residual Income has $" + str(residual3))
                        except TimeoutException:
                            log.set("Timed out finding assets, restart")
                            sys.exit()
                        if resBool3 == True:
                            log.set("Getting lvl 3")
                            self.wait_click_x("/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view/uni-button", "Lvl 3 Recieve") # click lvl 3 recieve 
                            log.set("Successful lvl 3!")
                            self.wait_Check()
                            time.sleep(1)
                    else:
                        log.set("No residual income found") 

                    infinite_present = self.does_Exist("/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[4]")
                    if infinite_present == True:
                        self.wait_click_x("/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[4]", "Infinite Tab") # click infinite butto
                        if self.wait_Lst():
                            try:                            
                                res4 = wait.until(EC.visibility_of_all_elements_located((By.XPATH , "//uni-view[@class='card-num' and text()!='']")))          
                                residual4 = float(res4[1].text)
                                resBool4 = residual4 > 0.0
                                log.set("Residual Income has $" + str(residual4))
                            except TimeoutException:
                                log.set("Timed out finding assets, restart")
                                sys.exit()
                            if resBool4 == True:
                                log.set("Getting infinite!")
                                self.wait_click_x("/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view/uni-button", "Infinite Recieve") # click infinite recieve
                                log.set("Successful infinite!")
                                self.wait_Check()
                                time.sleep(1)
                                self.findSite("https://cotps.com/#/pages/transaction/transaction")  
                        else:
                            log.set("No residual income found")
                    else:
                        log.set("Infinite Level not found")
                        self.findSite("https://cotps.com/#/pages/transaction/transaction")
                        log.set("Loading Transaction Page")   

                while True and self.stop == False:
                    wait = WebDriverWait(self.driver, 300, poll_frequency=1)
                    try:
                        balance1 = wait.until(EC.visibility_of_all_elements_located((By.XPATH , "//uni-view[@class='division-num' and text()!='']")))
                        walletA = float(balance1[1].text)
                        walBool1 = walletA > 5.0
                        log.set("Wallet has " + "$" + str(walletA))
                    except TimeoutException:
                        log.set("Timed out finding assets, restart")
                        sys.exit()
                    if walBool1 == False and self.stop == False:
                        break
                    
                    self.wait_Btn(".orderBtn", "Order Button")
                    #self.wait_click_x("//uni-button[@class='orderBtn']", "Competition Button")
                    self.wait_Btn(".buttons > uni-button:nth-child(2)", "Sell Button")
                    self.wait_click_x("/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[8]/uni-view/uni-view/uni-button", "Confirm Button")
                    self.driver.refresh()

                    try:
                        balance4 = wait.until(EC.visibility_of_all_elements_located((By.XPATH , "//uni-view[@class='division-num' and text()!='']")))
                        walletD = float(balance4[1].text)
                        walBool4 = walletD > 5.0
                        log.set("Wallet has " + "$" + str(walletD))
                    except TimeoutException:
                        log.set("Timed out finding assets, restart")
                        sys.exit()
                    if walBool4 == False and self.stop == False:
                        log.set("Wallet is empty leaving loop")
                        break  
            

            if W_over5 == True and T_over0 == True and self.stop == False:
                log.set("Money is transferring back")
                
                while True and self.stop == False:
                    log.set("Refreshing")
                    try:
                        self.driver.refresh()
                    except:
                        log.set("Page failed to load.")
                        sys.exit()
                    try:
                        wait = WebDriverWait(self.driver, 300)
                        balance = wait.until(EC.visibility_of_all_elements_located((By.XPATH , "//uni-view[@class='division-num' and text()!='']")))
                        transaction2 = float(balance[0].text)
                        t_bool = transaction2 > 0
                        log.set("Transaction has " + str(transaction2))
                    except TimeoutException:
                        log.set("Timed out finding assets, restart")
                        sys.exit()       
                    if t_bool == False and self.stop == False: 
                        break

                    if t_bool == True and self.stop == False:
                        for i in range(60,0,-1):
                            if self.stop == False:
                                hours, remainder = divmod(i, 3600)
                                mins, secs = divmod(remainder, 60)
                                timeformat = "{:02d}:{:02d}:{:02d}".format(hours, mins, secs)
                                log.set(timeformat)
                                time.sleep(1)
                            else:
                                log.set("Timer terminated, restart")
                                break
            
        
        sl = LoopingCall(secretariat_brain)
        sl.start(1)
        reactor.run(installSignalHandlers=False)
        

if x == True:
    bot = TimedClicker()          

class Secretariat():

    def __init__(self):
        self.run()

    def callback(self):
        self.root.destroy()

    def change_button(self):
        if self.start_btn['text'] == "Launch":
            self.start_btn.configure(text="Shutdown")
            self.sc = threading.Thread(target=bot.is_Start, daemon=True).start()
            
        else:
            self.start_btn.configure(text="Launch")
            bot.stop = True
            self.callback()
            bot.driver.quit()
            
            

    def change_levels(self):
        if self.levels_btn['text'] == "Levels Off":
            self.levels_btn.configure(text="Levels On")
            bot.yes_Levels()
        else:
            self.levels_btn.configure(text="Levels Off")
            bot.no_Levels()

    def run(self):

        def load(file: str) -> str:
            return os.path.join(os.path.dirname(__file__), file)

        self.root = tk.Tk()
        self.root.geometry('500x300+500+500')
        self.root.iconbitmap(load("icon/sec.ico"))
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.title('$ecretariat')
        self.root.resizable(height = 0, width = 0)
        global log 
        log=tk.StringVar()
        self.root.tk.call("source", load("sunvalley/sun-valley.tcl"))
        self.root.tk.call("set_theme", "dark")  

        label = ttk.Label(self.root, textvariable=log, font=("Fixedsys", 16))
        log.set("Press start to begin earning")
        label.place(x=130,y=120)
        
        img= Image.open(load("icon/secretariat4.png"))
        resized = img.resize((40,40))
        img_r = ImageTk.PhotoImage(resized)
        logo = ttk.Label(self.root, image=img_r)
        logo.image = img_r
        logo.place(x=9, y=10)

        style = ttk.Style()
        style.configure('Accent.TButton', width=15)
        self.start_btn = ttk.Button(self.root, text="Launch", style="Accent.TButton", command=self.change_button)
        self.start_btn.place(x=100 ,y=220)
        self.levels_btn = ttk.Checkbutton(self.root, text="Levels Off", command=self.change_levels)
        self.levels_btn.place(x=300, y=220)

        self.root.mainloop()

        bot.stop = True    
        if bot.driver_on == True:
            bot.driver.quit()
        sys.exit()
    

if x == True:
    instance = Secretariat()

if x == False:
    ctypes.windll.user32.MessageBoxW(None, "Cannot function on this Machine", "Invalid Machine", 0)
    os._exit(0)
"""
key = Fernet.generate_key()
e_t = Fernet(key)
e_m = e_t.encrypt(c)

d_m = e_t.decrypt(e_m)

exec(d_m)