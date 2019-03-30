# https://askubuntu.com/questionshttps://www.geeksforgeeks.org/website-blocker-using-python//586677/how-to-disable-network-with-crontab-on-ubuntu-14-04
# https://www.geeksforgeeks.org/website-blocker-using-python/
# Run this script as root
import time
from datetime import datetime as dt

# change hosts path according to your OS
hosts_path = "/etc/hosts"
# localhost's IP
redirect = "127.0.0.1"

# websites That you want to block
website_list =["http://www.cuisinedopamine.com/"]
# i = 0
# while True:
def activate_block():
    # print(i)
    # i += 1
    # time of your work
    if dt(dt.now().year, dt.now().month, dt.now().day,7) < dt.now() \
            < dt(dt.now().year, dt.now().month, dt.now().day,16):
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    # mapping hostnames to your localhost IP address
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)

                    # removing hostnmes from host file
            file.truncate()

        print("Fun hours...")
        time.sleep(5)




activate_block()