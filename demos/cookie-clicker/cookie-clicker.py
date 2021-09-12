# Cookie clicker auto-clicker
# Works for the classic version here: https://orteil.dashnet.org/experiments/cookie/

import pyautogui

def locate_cookie():

    """
    Returns the locations of the Big Cookie
    Does not return until the cookie is found
    """

    loc = None
    while loc == None:
        loc = pyautogui.locateCenterOnScreen('rsrc/bigcookie.png')
    return loc

def click_cookie(loc, ntimes):

    """
    Moves mouse to `loc` and clicks `ntimes`
    """

    x,y = loc
    pyautogui.moveTo(x,y)
    for _ in range(ntimes):
        pyautogui.click()

def round():

    """
    Does 1 round. 
    Returns `Yes` if user wants to continue
    Returns `No` otherwise.
    """

    loc = locate_cookie()

    pyautogui.alert(
        title = "Found cookie!", 
        text = str(loc))

    while True:

        number_of_times = pyautogui.prompt(
            title = "Continue?",
            text = "Click how many times?")

        if not number_of_times.isdigit():
            pyautogui.alert(
                title = "Error!", 
                text = "Input isn't an integer!")
            continue

        break

    number_of_times = int(number_of_times)
    click_cookie(loc, number_of_times)

    reply = pyautogui.confirm(
        title = "Done!",
        text = "Another round?",
        buttons = ["Yes", "No"])

    return reply

while True:
    reply = round()
    if reply == "No":
        break

