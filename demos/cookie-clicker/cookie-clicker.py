import pyautogui

def locate_cookie():
    loc = None
    while loc == None:
        loc = pyautogui.locateCenterOnScreen('rsrc/bigcookie.png')
    return loc

def click_cookie(loc, ntimes):
    x,y = loc
    pyautogui.moveTo(x,y)
    for _ in range(ntimes):
        pyautogui.click()

def round():

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

