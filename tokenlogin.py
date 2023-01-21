


import requests
from time import sleep
from selenium import webdriver, common

from loginapi import getheaders

def TokenLogin(token):
    j = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token)).json()
    user = j["username"] + "#" + str(j["discriminator"])
    script = """
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"%s"`
            location.reload();
        """ % (token)
    type_ = "chromedriver.exe"

    if type_ == "chromedriver.exe":
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        try:
            driver = webdriver.Chrome(options=opts)
        except common.exceptions.SessionNotCreatedException as e:
            print(e.msg)
            sleep(2)
            print("Press ENTER: ")
            input()
            ()
    
    

    print(f"\n[\x1b[95m>\x1b[95m\x1B[37m] Logging Into: {user}")
    driver.get("https://discordapp.com/login")
    driver.execute_script(script)