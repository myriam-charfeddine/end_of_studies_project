from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# from global_var import self.feedback


class FirefoxScriptAutomation():
    def __init__(self, driver=""):
        # try:
        self.driver = driver

        #handle tabs
        self.first_tab=""
        self.chat_tab=""
        self.ms_home_tab=""
        self.pts_agile_tab=""

        self.feedback = ""

    def run_pts_with_selenium(self):
        try:
            self.driver.get('https://pts.thinktank.de/executeWelcomRequest.do')
            #get the first tab name
            self.first_tab = self.driver.window_handles[-1]
            self.feedback = "Logged in successfully"
            print("Connected to the PTS")

        except Exception as e:
               print(f"Error while connecting to the PTS: {e}")

    def create_ticket_script(self, short_desc="", long_desc="", effort="", responsible="", product="" , project="" , urgency=""):
            try:
                # self.driver.switch_to.window(self.driver.window_handles[0])
                self.driver.switch_to.window(window_name=self.first_tab)
                self.feedback = ""
                
                WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located((By.ID, "fadein"))
                )
                
                self.driver.find_element(By.ID, "fadein").click()

                WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.ID, "responsibleView"))
                    )
                # self.driver.find_element(By.ID, "responsibleView").send_keys({responsible})

                self.driver.find_element(By.ID, "productView").send_keys({product})

                self.driver.find_element(By.ID, "project").send_keys({project})
                    
                self.driver.find_element(By.ID, "urgencyView").send_keys({urgency})

                self.driver.find_element(By.ID, "shortDescription").send_keys({short_desc})

                self.driver.find_element(By.ID, "longDescription").send_keys({long_desc})

                self.driver.find_element(By.ID, "estimatedEffort").send_keys({str(effort)})

                self.feedback = "Click SAVE to confirm the creation of the new ticket!"
                
            except:
                    try:
                        self.scroll_up()
                        time.sleep(1)

                        WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "#link_img_58713 > img"))
                        )

                        self.driver.find_element(By.CSS_SELECTOR, "#link_img_58713 > img").click()

                        WebDriverWait(self.driver, 5).until(
                                EC.presence_of_element_located((By.ID, "fadein"))
                            )
                        self.driver.find_element(By.ID, "fadein").click()

                        WebDriverWait(self.driver, 5).until(
                                EC.presence_of_element_located((By.ID, "responsibleView"))
                            )
                        self.driver.find_element(By.ID, "responsibleView").send_keys({responsible})

                        self.driver.find_element(By.ID, "productView").send_keys({product})

                        self.driver.find_element(By.ID, "project").send_keys({project})
                            
                        self.driver.find_element(By.ID, "urgencyView").send_keys({urgency})

                            # deadline script needs to be added ****************
                            # self.driver.find_element(By.ID, "deadLine")

                        self.driver.find_element(By.ID, "shortDescription").send_keys({short_desc})

                        self.driver.find_element(By.ID, "longDescription").send_keys({long_desc})

                        self.driver.find_element(By.ID, "estimatedEffort").send_keys({str(effort)})

                        self.feedback = "Click SAVE to confirm the creation of the new ticket!"

                    except Exception as e:
                        print(f"Error while creating a new ticket: {e}")
                        self.feedback="Failed to create a new ticket!"

    def add_comment_script1(self,comment="",effort="", number=""):
            try: 
                if number != "":
                    # self.driver.switch_to.window(self.driver.window_handles[0])
                    self.driver.switch_to.window(window_name=self.first_tab)
                    self.feedback = ""

                    WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.ID, f"colval_{str(number)}_10"))
                    )
                    self.driver.find_element(By.ID, f"colval_{number}_10").click()

                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Add comment"))
                    )
                    self.driver.find_element(By.LINK_TEXT, "Add comment").click()

                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.ID, "comment_"))
                    )
                    self.driver.find_element(By.ID, "comment_").send_keys({comment})

                    self.driver.find_element(By.ID, "effort_").send_keys({str(effort)})

                    self.feedback = f"Validate the add of a new comment to the ticket number {number}"

                else:
                    self.feedback = "Make sure to specify the number of your ticket (the row number not the ID)"
            except:
                  try:
                    self.go_to_my_last_changed_tickets()
                    
                    WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.ID, f"colval_{str(number)}_10"))
                        )
                    self.driver.find_element(By.ID, f"colval_{number}_10").click()

                    WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((By.LINK_TEXT, "Add comment"))
                        )
                    self.driver.find_element(By.LINK_TEXT, "Add comment").click()

                    WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((By.ID, "comment_"))
                        )
                    self.driver.find_element(By.ID, "comment_").send_keys({comment})

                    self.driver.find_element(By.ID, "effort_").send_keys({str(effort)})

                    self.feedback = f"Validate the add of a new comment to the ticket number {number}"
                  except Exception as e:
                    print(f"Error while adding a new comment to the ticket: {e}")
                    self.feedback = "Failed to add comment, try scrolling till your ticket is visible then say your command again"
    
    def add_comment_script(self,comment="",effort="", number=""):
            try: 
                if number != "":
                    if int(number) <= 6:
                        # self.driver.switch_to.window(self.driver.window_handles[0])
                        self.driver.switch_to.window(window_name=self.first_tab)
                        self.feedback = ""

                        WebDriverWait(self.driver, 3).until(
                        EC.presence_of_element_located((By.ID, f"colval_{str(number)}_10"))
                        )
                        self.driver.find_element(By.ID, f"colval_{number}_10").click()

                        WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((By.LINK_TEXT, "Add comment"))
                        )
                        self.driver.find_element(By.LINK_TEXT, "Add comment").click()

                        WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((By.ID, "comment_"))
                        )
                        self.driver.find_element(By.ID, "comment_").send_keys({comment})

                        self.driver.find_element(By.ID, "effort_").send_keys({str(effort)})

                        self.feedback = f"Click SAVE to confirm the add of a new comment to the ticket"

                    else:
                          ticket_not_found = True
                          y = 500
                          while ticket_not_found == True:
                                try:
                                    ActionChains(self.driver).scroll_by_amount(0, y).perform()
                                    WebDriverWait(self.driver, 2).until(
                                        EC.presence_of_element_located((By.ID, f"colval_{number}_10"))
                                        )
                                    self.driver.find_element(By.ID, f"colval_{number}_10").click()

                                    WebDriverWait(self.driver, 10).until(
                                            EC.presence_of_element_located((By.LINK_TEXT, "Add comment"))
                                        )
                                    self.driver.find_element(By.LINK_TEXT, "Add comment").click()
                                    WebDriverWait(self.driver, 10).until(
                                    EC.presence_of_element_located((By.ID, "comment_"))
                                    )
                                    
                                    ticket_not_found = False
                                    self.feedback = f"Click SAVE to confirm the add of a new comment to the ticket"

                                    self.driver.find_element(By.ID, "comment_").send_keys({comment})

                                    self.driver.find_element(By.ID, "effort_").send_keys({str(effort)})
                                    
                                    
                                except:
                                    # y+=300
                                    pass

                else:
                    self.feedback = "Make sure to specify the number of your ticket (the row number not the ID)"
            
            except Exception as e:
                    print(f"Error while adding a new comment to the ticket: {e}")
                    self.feedback = "Failed to add comment, make sure to navigate to the tickets list using the voice command"

    def add_attachment(self, number=""):
            try:
                if number != "":
                # self.driver.switch_to.window(self.driver.window_handles[0])
                    self.driver.switch_to.window(window_name=self.first_tab)
                    self.feedback = ""
                    
                    if int(number) <= 6:
                        WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.ID, f"colval_{str(number)}_9"))
                        )
                        self.driver.find_element(By.ID, f"colval_{number}_9").click()

                        # WebDriverWait(self.driver, 10).until(
                        # EC.presence_of_element_located((By.NAME, "attachmentFile"))
                        # )
                        # self.driver.find_element(By.NAME, "attachmentFile").click()
                        # self.feedback = f"Now select the file you want to attach to the ticket"
                        self.feedback = f"Now select the file you want to attach to the ticket"

                    else:
                        ticket_not_found = True
                        y = 500
                        while ticket_not_found == True:
                            try:
                                ActionChains(self.driver).scroll_by_amount(0, y).perform()
                                WebDriverWait(self.driver, 2).until(
                                EC.presence_of_element_located((By.ID, f"colval_{str(number)}_9"))
                                )
                                self.driver.find_element(By.ID, f"colval_{number}_9").click()

                                # WebDriverWait(self.driver, 10).until(
                                # EC.presence_of_element_located((By.NAME, "attachmentFile"))
                                # )
                                # self.driver.find_element(By.NAME, "attachmentFile").click()
                                ticket_not_found = False
                                self.feedback = f"Now select the file you want to attach to the ticket"
                                
                            
                            except:
                                pass

                else:
                    self.feedback = "Make sure to specify the number of your ticket (the row number not the ID)"

            except Exception as e:
                   print(f"Error while attaching file to the ticket: {e}")
                   self.feedback = "Failed to attach file, make sure to navigate to the tickets list using the voice command"

    def update_ticket(self, number="", short_desc="", long_desc="", estimated_effort="", responsible="", product="" , project="" , urgency="" , deadline="", user_story="", state="", effort="", comment="", answer=""):
            try:
                if number != "":
                    # self.driver.switch_to.window(self.driver.window_handles[0])
                    self.driver.switch_to.window(window_name=self.first_tab)
                    self.feedback = ""
                    
                    if int(number) <= 6:
                        WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.ID, f"colval_{str(number)}_2"))
                        )
                        self.driver.find_element(By.ID, f"colval_{number}_2").click()

                        WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((By.ID, "responsibleView"))
                        )
                        self.driver.find_element(By.ID, "responsibleView").send_keys({responsible})

                        self.driver.find_element(By.ID, "stateView").send_keys({state})

                        self.driver.find_element(By.ID, "productView").send_keys({product})

                        self.driver.find_element(By.ID, "project").send_keys({project})
                        
                        self.driver.find_element(By.ID, "urgencyView").send_keys({urgency})

                        # deadline script will be added later ****************
                        # self.driver.find_element(By.ID, "deadLine")

                        # user_story script will be added later ****************
                        # self.driver.find_element(By.ID, "amount1").send_keys({user_story})

                        self.driver.find_element(By.ID, "shortDescription").send_keys({short_desc})

                        self.driver.find_element(By.ID, "longDescription").send_keys({long_desc})

                        self.driver.find_element(By.ID, "solutionDescription").send_keys({answer})

                        self.driver.find_element(By.ID, "estimatedEffort").send_keys({str(estimated_effort)})

                        self.driver.find_element(By.ID, "comment_").send_keys({comment})

                        self.driver.find_element(By.ID, "effort_").send_keys({str(effort)})

                        self.feedback = "Click SAVE to confirm the updates of the ticket"

                    else:
                        ticket_not_found = True
                        y = 500
                        while ticket_not_found:
                            try:
                                    ActionChains(self.driver).scroll_by_amount(0, y).perform()
                                    WebDriverWait(self.driver, 2).until(
                                    EC.presence_of_element_located((By.ID, f"colval_{str(number)}_2"))
                                    )
                                    self.driver.find_element(By.ID, f"colval_{number}_2").click()

                                    self.feedback = "Click SAVE to confirm the updates of the ticket"
                                    ticket_not_found = False

                                    WebDriverWait(self.driver, 10).until(
                                        EC.presence_of_element_located((By.ID, "responsibleView"))
                                    )
                                    self.driver.find_element(By.ID, "responsibleView").send_keys({responsible})

                                    self.driver.find_element(By.ID, "stateView").send_keys({state})

                                    self.driver.find_element(By.ID, "productView").send_keys({product})

                                    self.driver.find_element(By.ID, "project").send_keys({project})
                                    
                                    self.driver.find_element(By.ID, "urgencyView").send_keys({urgency})

                                    # deadline script will be added later ****************
                                    # self.driver.find_element(By.ID, "deadLine")

                                    # user_story script will be added later ****************
                                    # self.driver.find_element(By.ID, "amount1").send_keys({user_story})

                                    self.driver.find_element(By.ID, "shortDescription").send_keys({short_desc})

                                    self.driver.find_element(By.ID, "longDescription").send_keys({long_desc})

                                    self.driver.find_element(By.ID, "solutionDescription").send_keys({answer})

                                    self.driver.find_element(By.ID, "estimatedEffort").send_keys({str(estimated_effort)})

                                    self.driver.find_element(By.ID, "comment_").send_keys({comment})

                                    self.driver.find_element(By.ID, "effort_").send_keys({str(effort)})

                                    
                            except:
                                    pass
                else:
                    self.feedback = "Make sure to specify the number of your ticket (the row number not the ID)"

            except Exception as e:
                   print(f"Error while updating the ticket: {e}")
                   self.feedback = f"Failed to update the ticket, make sure to navigate to the tickets list using the voice command"

#.....................................................TICKET FIELDS..............................................................

    def set_estimated_effort(self, estimated_effort):
            try:
                # self.driver.switch_to.window(self.driver.window_handles[0])
                self.driver.switch_to.window(window_name=self.first_tab)
                self.feedback = ""

                WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "estimatedEffort"))
                )
                self.driver.find_element(By.ID, "estimatedEffort").send_keys({str(estimated_effort)})

            except:
                self.feedback = "Failed to set the estimated effort!"

    def set_comment(self, comment):
            try:
                # self.driver.switch_to.window(self.driver.window_handles[0])
                self.driver.switch_to.window(window_name=self.first_tab)
                self.feedback = ""

                WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "comment_"))
                )
                self.driver.find_element(By.ID, "comment_").send_keys({comment})

            except:
                self.feedback = "Failed to set the comment!"

    def set_effort(self, effort):
            try:
                # self.driver.switch_to.window(self.driver.window_handles[0])
                self.driver.switch_to.window(window_name=self.first_tab)
                self.feedback = ""

                WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "effort_"))
                )
                self.driver.find_element(By.ID, "effort_").send_keys({str(effort)})

            except:
                self.feedback = "Failed to set the effort!"

    def set_long_description(self, long_desc):
            try:
                # self.driver.switch_to.window(self.driver.window_handles[0])
                self.driver.switch_to.window(window_name=self.first_tab)
                self.feedback = ""

                WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "longDescription"))
                )
                self.driver.find_element(By.ID, "longDescription").send_keys({long_desc})

            except:
                self.feedback = "Failed to set the long description!"

    def set_short_description(self, short_desc):
            try:
                # self.driver.switch_to.window(self.driver.window_handles[0])
                self.driver.switch_to.window(window_name=self.first_tab)
                self.feedback = ""

                WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "shortDescription"))
                )
                self.driver.find_element(By.ID, "shortDescription").send_keys({short_desc})

            except:
                self.feedback = "Failed to set the short description!"

#..........................................................ANSWER...................................................................

    def set_answer(self, number="", answer="", comment="", effort=""):
        try:
            if number != "":
                # self.driver.switch_to.window(self.driver.window_handles[0])
                self.driver.switch_to.window(window_name=self.first_tab)
                self.feedback = ""
                
                if int(number) <= 6:
                    WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.ID, f"colval_{str(number)}_3"))
                    )
                    self.driver.find_element(By.ID, f"colval_{number}_3").click()

                    WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".border-bottom > .Prio")) 
                    )
                    self.driver.find_element(By.CSS_SELECTOR, ".border-bottom > .Prio").click()

                    WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "solutionDescription"))
                    )
                    self.driver.find_element(By.ID, "solutionDescription").send_keys({answer})

                    WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "comment_"))
                    )
                    self.driver.find_element(By.ID, "comment_").send_keys({comment})

                    WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "effort_"))
                    )
                    self.driver.find_element(By.ID, "effort_").send_keys({str(effort)})

                else:
                      ticket_not_found = True
                      y = 500
                      while ticket_not_found:
                        try:
                            ActionChains(self.driver).scroll_by_amount(0, y).perform()
                            WebDriverWait(self.driver, 2).until(
                            EC.presence_of_element_located((By.ID, f"colval_{str(number)}_3"))
                            )
                            self.driver.find_element(By.ID, f"colval_{number}_3").click()

                            WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, ".border-bottom > .Prio")) 
                            )
                            self.driver.find_element(By.CSS_SELECTOR, ".border-bottom > .Prio").click()

                            WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((By.ID, "solutionDescription"))
                            )
                            self.driver.find_element(By.ID, "solutionDescription").send_keys({answer})

                            WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((By.ID, "comment_"))
                            )
                            self.driver.find_element(By.ID, "comment_").send_keys({comment})

                            WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((By.ID, "effort_"))
                            )
                            self.driver.find_element(By.ID, "effort_").send_keys({str(effort)})
                            ticket_not_found = False

                        except:
                            pass
            else:
                self.feedback = "Make sure to specify the number of your ticket (the row number not the ID)"

        except:
                self.feedback = "Failed to set the answer!"
            
    def set_ticket_as_answered(self, number=""):
        try:    
            # self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.switch_to.window(window_name=self.first_tab)
            self.feedback = ""

            if number !="":
                if int(number) <= 6:
                    WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.ID, f"colval_{str(number)}_3"))
                    )
                    self.driver.find_element(By.ID, f"colval_{number}_3").click()

                    WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".Prio > .text_blue > b")) 
                    )
                    self.driver.find_element(By.CSS_SELECTOR, ".Prio > .text_blue > b").click()

                else:
                    ticket_not_found = True
                    y = 500
                    while ticket_not_found:
                                try:
                                    ActionChains(self.driver).scroll_by_amount(0, y).perform() 
                                    WebDriverWait(self.driver, 2).until(
                                    EC.presence_of_element_located((By.ID, f"colval_{str(number)}_3"))
                                    )
                                    self.driver.find_element(By.ID, f"colval_{number}_3").click()

                                    WebDriverWait(self.driver, 10).until(
                                    EC.presence_of_element_located((By.CSS_SELECTOR, ".Prio > .text_blue > b")) 
                                    )
                                    self.driver.find_element(By.CSS_SELECTOR, ".Prio > .text_blue > b").click()
                                    ticket_not_found = False

                                except:
                                    pass

            else:       
                # WebDriverWait(self.driver, 10).until(
                # EC.presence_of_element_located((By.CSS_SELECTOR, ".Prio > .text_blue > b")) 
                # )
                # self.driver.find_element(By.CSS_SELECTOR, ".Prio > .text_blue > b").click() 
                self.feedback = "Make sure to specify the number of your ticket (the row number not the ID)"
        
        except:
                self.feedback = "Failed to set the ticket as answered!"
#............................................OTHERS....................................................

    def discard_changes(self):
                try:
                    # self.driver.switch_to.window(self.driver.window_handles[0])
                    self.driver.switch_to.window(window_name=self.first_tab)
                    self.feedback = ""

                    WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".modal-header > .close"))
                    )
                    self.driver.find_element(By.CSS_SELECTOR, ".modal-header > .close").click() 

            
                except:
                    try:
                        WebDriverWait(self.driver, 3).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, ".modal-header > #close_button_modal"))
                        )
                        self.driver.find_element(By.CSS_SELECTOR, ".modal-header > #close_button_modal").click()

                    except:
                        try:
                            WebDriverWait(self.driver, 3).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, ".modal-headerCell > .close"))
                            )
                            self.driver.find_element(By.CSS_SELECTOR, ".modal-headerCell > .close").click()

                        except:
                            self.feedback = "Failed to discard changes!"
                        

    def go_to_notifications(self): #Newly added and not tested
                try:
                    self.driver.switch_to.window(window_name=self.first_tab)

                    self.scroll_up()
                    time.sleep(1)

                    self.feedback = ""

                    WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.ID, "link_img_58712"))
                    )
                    self.driver.find_element(By.ID, "link_img_58712").click()

                except Exception as e:
                       print(f"Error while going to the notifications: {e}")
                       self.feedback = "Failed to navigate you to the notifications"

    def go_to_my_last_changed_tickets(self): #Works fine
                try:
                    self.driver.switch_to.window(window_name=self.first_tab)

                    self.scroll_up()
                    time.sleep(1)

                    self.feedback = ""

                    WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.ID, "link_img_58713"))
                    )
                    self.driver.find_element(By.ID, "link_img_58713").click()

                except Exception as e:
                       print(f"Error while going to your last changed tickets: {e}")
                       self.feedback = "Failed to navigate you to your last changed tickets"

    def login(self, user_name, password):
                try:
                    self.feedback = ""

                    WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.ID, "UserName"))
                        )
                    self.driver.find_element(By.ID, "UserName").send_keys(user_name)

                    WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.ID, "Password"))
                        )
                    self.driver.find_element(By.ID, "Password").send_keys(password)
                    self.driver.find_element(By.CSS_SELECTOR, ".SubmitInLogin").click()

                    # #get the first tab name
                    # self.first_tab = self.driver.window_handles[-1]
                    # self.feedback = "Logged in successfully"
                
                except Exception as e:
                       print(f"Error logging in: {e}")
                       self.feedback = "Failed to login!"

#.....................................CHAT............................................

    def start_chat(self, number=""):
            try:
                if number != "":
                    self.feedback = ""

                    if int(number) <= 6:
                        WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.ID, f"colval_{str(number)}_11"))
                        )
                        self.driver.find_element(By.ID, f"colval_{number}_11").click()

                        #get the chat tab name
                        self.chat_tab = self.driver.window_handles[1]

                        self.feedback = "Chat started successfully"

                    else:
                        ticket_not_found = True
                        y = 500
                        while ticket_not_found:
                                try:
                                    ActionChains(self.driver).scroll_by_amount(0, y).perform()
                                    WebDriverWait(self.driver, 2).until(
                                    EC.presence_of_element_located((By.ID, f"colval_{str(number)}_11"))
                                    )
                                    self.driver.find_element(By.ID, f"colval_{number}_11").click()

                                    #get the chat tab name
                                    self.chat_tab = self.driver.window_handles[1]

                                    self.feedback = "Chat started successfully"
                                    ticket_not_found = False
                                
                                except:
                                    pass

                else:
                    self.feedback = "Make sure to specify the number of your ticket (the row number not the ID)"

            except Exception as e:
                   print(f"Error starting a new chat for the ticket: {e}")
                   self.feedback = "Failed to satrt a new chat!"

    def write_in_chat(self, message=""):
            try:
                # self.driver.switch_to.window(self.driver.window_handles[-1])
                self.driver.switch_to.window(window_name=self.chat_tab)
                self.feedback = ""

                # original_window = self.driver.current_window_handle
                # print(original_window)
                # self.driver.switch_to.window(self.driver.window_handles[1])

                WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "message"))
                )
                self.driver.find_element(By.ID, "message").send_keys({message})

                # self.driver.switch_to.window(original_window)

                self.feedback = "Successfully wrote in the chat"

            except Exception as e:
                   print(f"Error writing in chat: {e}")
                   self.feedback = "Failed to write in the chat"

    def send_message(self): #not working
            try:
                # self.driver.switch_to.window(self.driver.window_handles[-1]) #!!!!!!!!!!!!
                self.driver.switch_to.window(window_name=self.chat_tab)
                self.feedback = ""

                WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".horizontal-btn-send > .btn yourButton"))
                )
                self.driver.find_element(By.CSS_SELECTOR, ".horizontal-btn-send > .btn yourButton").click()

                self.feedback = "Message sent successfully"

            except Exception as e:
                   print(f"Error sending message in chat: {e}")
                   self.feedback = "Failed to send your message in the chat!"

    def close_chat(self):
                try:
                    # self.driver.switch_to.window(self.driver.window_handles[-1])
                    self.driver.switch_to.window(window_name=self.chat_tab)
                    self.feedback = ""

                    WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.ID, "leave-room"))
                    )
                    self.driver.find_element(By.ID, "leave-room").click()

                    self.feedback = "Chat closed successfully"

                except Exception as e:
                       print(f"Error leaving the chat: {e}")
                       self.feedback = "Failed to leave the chat!"


    def send_file_in_chat(self):  #cant click element (NOT WORKING) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.switch_to.window(window_name=self.chat_tab)
            self.feedback = ""

            WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".footer-btn > .icon-interface"))
            )
            self.driver.find_element(By.CSS_SELECTOR, ".footer-btn > .icon-interface").click() # not working cuz not clickable

    def send_emoji_in_chat(self): #Remove it
            try:
                # self.driver.switch_to.window(self.driver.window_handles[-1])
                self.driver.switch_to.window(window_name=self.chat_tab)
                self.feedback = ""

                WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".footer-btn > .icon-smile"))
                )
                self.driver.find_element(By.CSS_SELECTOR, ".footer-btn > .icon-smile").click()
            except Exception as e:
                   print(f"Error sending emoji in chat: {e}")
                   self.feedback = "Failed to send emoji"

#.....................................MS_HOME........................................................

    def go_to_ms_home(self):
            try:
                self.driver.switch_to.window(window_name=self.first_tab)

                self.scroll_up()
                time.sleep(1)

                self.feedback = ""

                WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "li:nth-child(1) > .PtsIcons img"))
                    )
                self.driver.find_element(By.CSS_SELECTOR,"li:nth-child(1) > .PtsIcons img").click()
                
                #get the ms_home tab name
                self.ms_home_tab = self.driver.window_handles[1]

                self.feedback = "MS HOME opened successfully"

            except Exception as e:
                  print(f"Error going to the MS HOME: {e}")
                  self.feedback = "Failed to naviagate to the MS HOME"

    def add_web_component(self): #Not added yet and not tested
            try:
                self.driver.switch_to.window(window_name=self.ms_home_tab)
                self.feedback = ""

                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.ID, "null"))
                    )
                self.driver.find_element(By.ID, "null").click()

                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".side-panel-container"))
                )
                self.driver.find_element(By.CSS_SELECTOR, ".side-panel-container > agile-pts-journey > .dashboard").click()
                #    self.driver.find_element(By.CSS_SELECTOR, ".side-panel-container > agile-burndown-chart").click()

            except Exception as e:
                  print(f"Error adding a new componenet: {e}")
                  self.feedback = "Failed to add a web component"

#............................................PTS AGILE...............................................................

    def go_to_pts_agile(self): 
            try:
                self.driver.switch_to.window(window_name=self.first_tab)

                self.scroll_up()
                time.sleep(1)

                self.feedback = ""

                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "li:nth-child(5) > .PtsIcons img"))
                )
                self.driver.find_element(By.CSS_SELECTOR,"li:nth-child(5) > .PtsIcons img").click()
            
                #get the ms_home tab name
                self.pts_agile_tab = self.driver.window_handles[1]

                self.feedback = "PTS Agile opened successfully"

            except Exception as e:
                   print(f"Error going to the PTS Agile: {e}")
                   self.feedback = "Failed to navigate to the PTS Agile"

#........................................PAGE INTERACTIONS...............................................................
    def scroll_down(self): #Newly added and NOT tested
            try:
                self.feedback = ""

                y=400
                ActionChains(self.driver).scroll_by_amount(0, y).perform()
            except Exception as e:
                   print(f"Error scrolling down: {e}")
                   self.feedback = "Failed to scroll down"

    def scroll_up(self): #Newly added and NOT tested
            try:
                self.feedback = ""

                y=-300
                ActionChains(self.driver).scroll_by_amount(0, y).perform()
            except Exception as e:
                   print(f"Error scrolling up: {e}")
                   self.feedback = "Failed to scroll up"


    def close_ms_home_tab(self): #Works fine
            try:
                self.feedback = ""

                self.driver.switch_to.window(window_name=self.ms_home_tab)
                self.driver.close() 

                self.feedback = "MS HOME tab closed successfully"

            except Exception as e:
                   print(f"Error closing the MS HOME Tab: {e}")
                   self.feedback = "Failed to close the MS HOME tab"

    def close_browser(self): #Newly added and NOT tested
            try:
                self.feedback = ""

                self.driver.quit()
                self.feedback = "Browser closed successfully"
            except Exception as e:
                   print(f"Error closing the PTS Vocal Command Session: {e}")
                   self.feedback = "Failed to close your browser"

#................................FROM NAVBAR..............................................
    def go_to_my_emails(self):
            try:
                    self.driver.switch_to.window(window_name=self.first_tab)

                    self.scroll_up()
                    time.sleep(1)

                    self.feedback = ""

                    WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.ID, "link_img_58714"))
                    )
                    self.driver.find_element(By.ID, "link_img_58714").click()

            except Exception as e:
                       print(f"Error while going to your last changed tickets: {e}")
                       self.feedback = "Failed to navigate to your emails"

    def go_to_my_timesheet(self):
            try:
                    self.driver.switch_to.window(window_name=self.first_tab)

                    self.scroll_up()
                    time.sleep(1)

                    self.feedback = ""

                    WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.ID, "link_img_10692589"))
                    )
                    self.driver.find_element(By.ID, "link_img_10692589").click()

            except Exception as e:
                       print(f"Error while going to your last changed tickets: {e}")
                       self.feedback = "Failed to navigate to your timesheet"

    def go_to_my_created_tickets(self):
            try:
                    self.driver.switch_to.window(window_name=self.first_tab)

                    self.scroll_up()
                    time.sleep(1)

                    self.feedback = ""

                    WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.ID, "link_img_10690852"))
                    )
                    self.driver.find_element(By.ID, "link_img_10690852").click()

            except Exception as e:
                       print(f"Error while going to your last changed tickets: {e}")
                       self.feedback = "Failed to navigate to your created tickets"

    def go_to_the_system_notifications(self):
            try:
                    self.driver.switch_to.window(window_name=self.first_tab)

                    self.scroll_up()
                    time.sleep(1)

                    self.feedback = ""

                    WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.ID, "link_img_10766808"))
                    )
                    self.driver.find_element(By.ID, "link_img_10766808").click()

            except Exception as e:
                       print(f"Error while going to your last changed tickets: {e}")
                       self.feedback = "Failed to navigate to the system notifications"

    def go_to_my_fist_level_support(self):
            try:
                    self.driver.switch_to.window(window_name=self.first_tab)

                    self.scroll_up()
                    time.sleep(1)

                    self.feedback = ""

                    WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.ID, "link_img_10703614"))
                    )
                    self.driver.find_element(By.ID, "link_img_10703614").click()

            except Exception as e:
                       print(f"Error while going to your last changed tickets: {e}")
                       self.feedback = "Failed to navigate to your 1st level support"

    def go_to_my_chat(self):
            try:
                    self.driver.switch_to.window(window_name=self.first_tab)

                    self.scroll_up()
                    time.sleep(1)

                    self.feedback = ""

                    WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.ID, "link_img_88377"))
                    )
                    self.driver.find_element(By.ID, "link_img_88377").click()

            except Exception as e:
                       print(f"Error while going to your last changed tickets: {e}")
                       self.feedback = "Failed to navigate to your chat!"

#.......................................SEARCH.........................................
    def make_search(self, product="", state="", responsible="", ticket_id="", parent_id="", project="", urgency=""):
            try:
                    self.driver.switch_to.window(window_name=self.first_tab)
                    self.feedback = ""

                    WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.ID, "param1"))
                    )
                    self.driver.find_element(By.ID, "param1").send_keys({product})

                    self.driver.find_element(By.ID, "param2").send_keys({state})
                    self.driver.find_element(By.ID, "param3").send_keys({responsible})
                    self.driver.find_element(By.ID, "param4").send_keys({str(ticket_id)})
                    self.driver.find_element(By.ID, "param5").send_keys({str(parent_id)})
                    self.driver.find_element(By.ID, "param6").send_keys({str(project)})
                    self.driver.find_element(By.ID, "param7").send_keys({urgency})

            except Exception as e:
                       print(f"Error while going to your last changed tickets: {e}")
                       self.feedback = "Search failed!"

    def make_free_search(self, text):
            try:
                self.driver.switch_to.window(window_name=self.first_tab)
                self.feedback = ""

                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.ID, "freeParam"))
                    )
                self.driver.find_element(By.ID, "freeParam").send_keys({text})

            except Exception as e:
                   print(f"Error while making free search: {e}")
                   self.feedback = "Free search failed!"

    def reset_search(self):
            try:
                self.driver.switch_to.window(window_name=self.first_tab)
                self.feedback = ""

                WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Reset"))
                    )
                self.driver.find_element(By.LINK_TEXT, "Reset").click()

            except Exception as e:
                   print(f"Error restting search: {e}")
                   self.feedback = "Error restting search"

    def execute_search(self):
            try:
                self.driver.switch_to.window(window_name=self.first_tab)
                self.feedback = ""

                WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Execute"))
                    )
                self.driver.find_element(By.LINK_TEXT, "Execute").click()

            except Exception as e:
                   print(f"Error executing search: {e}")
                   self.feedback = "Error executing search"

#....................................OTHER FROM NAVBAR..................................
    def go_to_jenkins(self):
           try:
                self.driver.switch_to.window(window_name=self.first_tab)
                self.scroll_up()
                time.sleep(1)

                self.feedback = ""

                WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "li:nth-child(3) > .PtsIcons img"))
                    )
                self.driver.find_element(By.CSS_SELECTOR,"li:nth-child(3) > .PtsIcons img").click()

           except Exception as e:
                print(f"Error taking you to Jenkins: {e}")
                self.feedback = "Error navigating to Jenkins"

    def go_to_gitlab(self):
           try:
                self.driver.switch_to.window(window_name=self.first_tab)
                self.scroll_up()
                time.sleep(1)

                self.feedback = ""

                WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "li:nth-child(7) > .PtsIcons img"))
                    )
                self.driver.find_element(By.CSS_SELECTOR,"li:nth-child(7) > .PtsIcons img").click()

           except Exception as e:
                print(f"Error taking you to Gitlab: {e}")
                self.feedback = "Error navigating to Gitlab"

    def go_to_think_pedia(self):
           try:
                self.driver.switch_to.window(window_name=self.first_tab)
                self.scroll_up()
                time.sleep(1)

                self.feedback = ""

                WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "li:nth-child(2) > .PtsIcons img"))
                    )
                self.driver.find_element(By.CSS_SELECTOR,"li:nth-child(2) > .PtsIcons img").click()

           except Exception as e:
                print(f"Error taking you to Think pedia: {e}")
                self.feedback = "Error navigating to Think pedia"

    def go_to_pts_qa(self):
           try:
                self.driver.switch_to.window(window_name=self.first_tab)
                self.scroll_up()
                time.sleep(1)

                self.feedback = ""

                WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "li:nth-child(4) > .PtsIcons img"))
                    )
                self.driver.find_element(By.CSS_SELECTOR,"li:nth-child(4) > .PtsIcons img").click()

           except Exception as e:
                print(f"Error taking you to PTS-QA: {e}")
                self.feedback = "Error navigating to PTS-QA"

    def go_to_free_search(self):
           try:
                self.driver.switch_to.window(window_name=self.first_tab)
                self.scroll_up()
                time.sleep(1)

                self.feedback = ""

                WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "li:nth-child(3) > .PtsIcons img"))
                    )
                self.driver.find_element(By.CSS_SELECTOR,"li:nth-child(3) > .PtsIcons img").click()

           except Exception as e:
                print(f"Error taking you to Jenkins: {e}")
                self.feedback = "Error navigating to free search!"



            
    
scripts ={
"0" : {
    "params": {
          'short_desc',
          'long_desc' ,
          'estimated_effort',
          'responsible', 
          'product', 
          'project', 
          'urgency', 
          'deadline'
    },
    "function_name":  "create_new_ticket"
    },

"1" : {
    "params": {
          'comment',
          'effort',
          'number'
    },
    "function_name": "add_new_comment"
    },

"2": {
    "params": {
          'number',
          'short_desc', 
          'long_desc', 
          'effort', 
          'responsible', 
          'product', 
          'project', 
          'urgency', 
          'deadline', 
          'user_story', 
          'state', 
          'effort', 
          'comment', 
          'answer'
    },
    "function_name": "update_ticket"
},

"3" : {
    "params": {
          'number'
    },
    "function_name": "add_attachment"
    },

"4" : {
    "params": {
          'number',
          'answer', 
          'comment', 
          'effort'
    },
    "function_name": "set_answer"
    },

"5" : {
    "params": {
          'number'
    },
    "function_name": "set_ticket_as_answered"
    },

"6" : {
    "params": {},
    "function_name": "discard_changes"
    },

"7" : {
    "params": {
          'number'
    },
    "function_name": "start_chat"
    },

"8" : {
    "params": {
          'message'
    },
    "function_name": "write_in_chat"
    },

"9" : {
    "params": {},
    "function_name": "send_message"
    },

"10" : {
    "params": {},
    "function_name": "close_chat"
    },

"11" : {
    "params": {},
    "function_name": "send_file_in_chat"
    },

"12" : {
    "params": {},
    "function_name": "send_emoji_in_chat"
    },

"13" : {
    "params": {
        'effort'
    },
    "function_name": "set_effort"
    },

"14" : {
    "params": {
        'estimated_effort'
    },
    "function_name": "set_estimated_effort"
    },

"15" : {
    "params": {
        'long_desc'
    },
    "function_name": "set_long_description"
    },

"16" : {
    "params": {
        'short_desc'
    },
    "function_name": "set_short_description"
    },

"17" : {
    "params": {
        'comment'
    },
    "function_name": "set_comment"
    },

"18" : {
    "params": {},
    "function_name": "go_to_my_last_changed_tickets"
    },

"19" : {
    "params": {},
    "function_name": "go_to_notifications"
    },

"20" : {
    "params": {},
    "function_name": "go_to_pts_agile"
    },

"21" : {
    "params": {},
    "function_name": "go_to_ms_home"
    }, 

"22" : {
    "params": {},
    "function_name": "add_web_component"
    }, 

"23" : {
    "params": {},
    "function_name": "scroll_down"
    }, 

"24" : {
    "params": {},
    "function_name": "close_ms_home_tab"
    }, 

"25" : {
    "params": {},
    "function_name": "close_browser"
    }, 

"26" : {
    "params": {},
    "function_name": "scroll_up"
    },
}

# firefox = FirefoxScriptAutomation()
# exec("create_ticket_script()")
# create_ticket_script(short_desc='rr',long_desc='ee')