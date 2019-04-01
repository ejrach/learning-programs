import time
from datetime import datetime as dt     # creating namespace of "dt"

#hosts_path="/private/etc/hosts"
hosts_temp = "hosts"
redirect="127.0.0.1"
website_list=["gmail.com","www.cnn.com","cnn.com"]

while True:

    # Create a datetime object "dt" of the year, month, day and hours and compare with dt.now()
    # So, for example, if (2018, 04, 01, 8) < (2018, 04, 01, 13) < (2018, 04, 01, 16) then print "working hours"
    # Where, 8 is 8 am, and 16 is 4 pm
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working Hours...")

        # open the file for read and write
        with open(hosts_temp,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    # we will pass, because the website is already in the file
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

    else:
        print("Fun hours...")
     # Delay 5 seconds
    
    time.sleep(5)
