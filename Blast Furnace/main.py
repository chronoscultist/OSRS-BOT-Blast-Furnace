from login_function import login
import pyautogui as py
import time

time.sleep(2)


"""
log = login()
# if it detects the osrs login screen image, it will initiate the re-logging process
if py.locateOnScreen("login_screen.png", confidence=0.85):  
    print("Linux supremecy")
    log.login_time()
"""

#reset_mouse_pos = py.locateCenterOnScreen("reset_mouse_position.png", confidence=0.95)
#ini_time = time.time()


     



def timer(i):

    timeri = py.locateCenterOnScreen("timer.png", confidence = 0.55)
    print("TIMER FUNCTION INITIATED")
 
    #This portion checks if we need to pay the foreman, it will initiatiate the paying process if it does
    while timeri == None:
        while True:

            print("TIME TO PAY")

            npc = py.locateCenterOnScreen("npc.png", confidence = 0.6)
            print("NPC FOUND")
            py.click(npc)                      
            time.sleep(1)
            
            if py.locateOnScreen("pay.png", confidence=0.55) !=None:
                print("HERE YA GO, MONEY BOI")
                time.sleep(0.5)
                py.press("1")
                time.sleep(1)
            timeri = py.locateCenterOnScreen("timer.png", confidence = 0.6)
            if timeri !=None:
                print("ARE WE CUMMING!=!=!=!=")
                timeri = None
                smelter(i)
        
                   





def smelter(i):

    
    #this portion executes the smelting process
    print("SMELTER FUNCTION INITIATED")
    print(i)
    print("OMEGA")
   
    if i==2:

        if py.locateCenterOnScreen("collect.png", confidence=0.85) !=None:
            py.moveTo(py.locateCenterOnScreen("collect.png", confidence=0.85))
            time.sleep(0.1)
            py.click()

            while py.locateCenterOnScreen("all.png", confidence=0.95) ==None:
                py.press('space')
                time.sleep(0.5)  
                py.locateCenterOnScreen("all.png", confidence=0.95)

            if py.locateCenterOnScreen("all.png", confidence=0.95) !=None:
                py.moveTo(py.locateCenterOnScreen("all.png", confidence=0.95))
                py.click(py.locateCenterOnScreen("all.png", confidence=0.95))
                time.sleep(1)
                py.press('space')
                time.sleep(0.5)


    bank_reset=py.locateCenterOnScreen("bank_reset.png", confidence = 0.60)
    if bank_reset != None:
        py.moveTo(bank_reset)
        time.sleep(0.5)
        py.click()
        bank = py.locateOnScreen("bank_inv.png", confidence = 0.95)
        #It will wait untill it sees the banking screen.
        
        while bank ==None:
            time.sleep(0.1)
            bank = py.locateOnScreen("bank_inv.png", confidence = 0.9)
        bank=None

        if py.locateCenterOnScreen("deposite_bar.png", confidence=0.85) !=None:
            py.moveTo(py.locateCenterOnScreen("deposite_bar.png", confidence=0.85))
            time.sleep(0.5)
            py.click(py.locateCenterOnScreen("deposite_bar.png", confidence=0.85))
            time.sleep(0.5)
            i=0


        

        while i !=2:
            ore = py.locateCenterOnScreen("ore"+str(i)+".png", confidence = 0.55)
            run = py.locateCenterOnScreen("run.png", confidence = 0.98) 
            if ore != None:
                py.moveTo(ore)
                py.click(ore)
                time.sleep(0.2)
                py.moveTo(py.locateCenterOnScreen("exit_bank.png", confidence =0.94))
                time.sleep(0.1)
                py.click()
            if run != None:
                py.moveTo(run)
                py.click(run)
                time.sleep(0.1)
            
            smelt = py.locateCenterOnScreen("smelt.png", confidence = 0.7)
            timeri = py.locateCenterOnScreen("timer.png", confidence = 0.55)
            if timeri == None:
                print("SOOO, IS THIS WORKING?????????????????")
                timer(i)
            timeri = None

            while smelt !=None:
                py.moveTo(smelt)
                time.sleep(0.1)
                py.click()
                
                while py.locateCenterOnScreen("bag_status.png", confidence = 0.9) == None:
                    time.sleep(1)
                    reset = py.locateCenterOnScreen("reset.png", confidence = 0.95) 
                    if reset !=None:
                        print("you walked all this way?????")
                        reset=None
                        timer(i)
                    py.locateCenterOnScreen("bag_status.png", confidence = 0.9)
                    
                
                i=i+1
                smelt = None
            smelter(i)
        time.sleep(2)


            
timer(0)     
smelter(0)
                          

        