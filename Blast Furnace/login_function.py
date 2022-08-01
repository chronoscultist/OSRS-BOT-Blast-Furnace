import pyautogui as py
import time

class login:

    def login_time(self):
        password = "deadhead11"


        if py.locateOnScreen('log_screen.JPG', confidence=0.90):
            log_in_location = py.locateOnScreen("existing_user.PNG", confidence=0.95)
            log_in_location = py.moveTo(log_in_location)
            py.click(log_in_location)
            py.typewrite(password, interval=0.1)
            py.press('enter')
            time.sleep(10)
            if py.locateOnScreen("click_here_to_enter.JPG", confidence=0.90):
                enter_here = py.locateOnScreen("click_here_to_enter.JPG", confidence=0.90)
                enter_here = py.moveTo(enter_here)
                py.click(enter_here)
                time.sleep(4)

            elif py.locateOnScreen("error_wrong.JPG", confidence=0.95):
                exit

            elif py.locateOnScreen("already_logged.JPG", confidence=0.9):
                time.sleep(600)

        elif py.locateOnScreen('dc_screen.JPG', confidence=0.90):
            ok_location = py.locateOnScreen("dc_ok.JPG", confidence=0.90)
            ok_location = py.moveTo(ok_location)
            py.click(ok_location)
            time.sleep(1)

        elif py.locateOnScreen("login_password.JPG", confidence=0.90):
                enter_here = py.locateCenterOnScreen("enter_password.JPG", confidence=0.80)
                enter_here = py.moveTo(enter_here)
                py.click(enter_here)
                py.typewrite(password, interval=0.1)
                py.press('enter')
                time.sleep(10)
                if py.locateOnScreen("click_here_to_enter.JPG", confidence=0.90):
                    enter_here = py.locateOnScreen("click_here_to_enter.JPG", confidence=0.90)
                    enter_here = py.moveTo(enter_here)
                    py.click(enter_here)
















