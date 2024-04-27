from DiscordUserApi import DiscordApi
import os
import tokenlogin
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()
def main():
    print("""
oooooooooo.   ooooo  .oooooo..o ooooooooooooo   .oooooo.   oooo    oooo 
`888'   `Y8b  `888' d8P'    `Y8 8'   888   `8  d8P'  `Y8b  `888   .8P'  
 888      888  888  Y88bo.           888      888      888  888  d8'    
 888      888  888   `"Y8888o.       888      888      888  88888{      
 888      888  888       `"Y88b      888      888      888  888`88b.    
 888     d88'  888  oo     .d8P      888      `88b    d88'  888  `88b.  
o888bood8P'   o888o 8""88888P'      o888o      `Y8bood8P'  o888o  o888o 

                  Professional Discord Token Manager.
                                                            
Pr0ject Managed by Luminous Team | C0ded by C1ntagr@mABP
Version: 1.1
    """)
    input("Press Enter to Start")
    cls()
    token1 = input("Input User's discord token to control\n~$ ")
    token1 = str(token1)
    cls()
    user = DiscordApi(token=token1)

    print("Logined as {}".format(token1))
    print("Select the menu\n")
    print("1. Dump Information\n2. Join Server\n3. Set typing\n4. Send message\n5. Send mass messages\n6. Set bio\n7. Set custom status\n8. Change Language\n9. Create guilds\n10. Delete guilds\n11. Delete friends\n12. RAID\n13. Bug/Error report\n14. Token Login")
    opt = input("Choose an option\n~$ ")


    if opt == "1":
        user.dump_info()
        cls()
        main()
    elif opt == "2":
        invite = input("Enter Invite Code (example: https://discord.gg/example): ")
        invite = str(invite)
        user.join_server(invite)
        cls()
        main()
    elif opt == "3":
        channelid = input("Enter Channel ID (example: 1008559671285661712): ")
        channelid = str(channelid)
        user.set_typing(channelid, 1)
        cls()
        main()
    elif opt == "4":
        msg = input("Enter Message: ")
        channelid = input("Enter Channel ID: ")
        channelid = str(channelid)
        msg = str(msg)
        user.send_message(msg, channelid)
        cls()
        main()
    elif opt == "5":
        msg = input("Enter Message: ")
        msg = str(msg)
        user.send_mass_messages(msg)
        cls()
        main()
    elif opt == "6":
        bio = input("Enter Bio: ")
        bio = str(bio)
        user.set_bio(bio)
        cls()
        main()
    elif opt == "7":
        status = input("Enter Status: ")
        status = str(status)
        user.set_custom_status(status)
        cls()
        main()
    elif opt == "8":
        print("Language Code: en_US / ko / [Coming Soon]")
        lang = input("Enter Language Code: ")
        lang = str(lang)
        user.change_language(lang)
        cls()
        main()
    elif opt == "9":
        name = input("Enter Server Name: ")
        name = str(name)
        amount = input("Amount: ")
        amount = int(amount)    
        user.create_guilds(name, amount)
        cls()
        main()
    elif opt == "10":
        name = input("Enter Server ID for Exception: ")
        name = str(name)
        user.delete_guilds(name)
        cls()
        main()
    elif opt == "11":
        user.delete_friends()
        cls()
        main()
    elif opt == "12":
        answer = input("This will ABSOLUTLY DESTROYS the account.\nWould you like to continue? [y/n]: ")
        if answer == "y" or "Y":
            user.raid()
            cls()
            main()
        elif answer == "n" or "N":
            cls()
            main()
        else:
            print("Invalid Input")
            cls()
            main()
    elif opt == "13":
        cls()
        input("Contact\nDiscord: CintagramABP#2101\nPress Enter to continue...")
        cls()
        main()
    elif opt == "14":
        cls()
        print("Default chromedriver version: 109\nIf your chrome version is different, please change the file to correct version.")
        print("launching...")
        tokenlogin.TokenLogin(token1)
    else:
        print("Invalid option")
        cls()
        main()

if __name__ == "__main__":
    main()

