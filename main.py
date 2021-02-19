import smtplib
import ssl
import time
import timer
import yagmail
import requests
from bs4 import BeautifulSoup

#the program below will send you an email if there is at least one new ad on olx based on your search list defined below

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = 'senderemail' #complete with your email
password = 'sender_password' #pass
receiver_email = 'destinationemail' #complete with receiver email

done = False

def sendEmail(title, newer):
    print('email sent')
    print(title)
    print(newer)
    print("----------------")
    yag = yagmail.SMTP(sender_email, password) # easy email
    yag.send(receiver_email, subject=title + ", new:" + str(newer))

    # Create a secure SSL context #alternative email solution
    # context = ssl.create_default_context()
    # message = """\
    # Subject: {0}, {1} newer
    #
    # This message is sent from Python.""".format(title, newer)
    # # Try to log in to server and send email
    # try:
    #     server = smtplib.SMTP(smtp_server, port)
    #     server.ehlo()  # Can be omitted
    #     server.starttls(context=context)  # Secure the connection
    #     server.ehlo()  # Can be omitted
    #     server.login(sender_email, password)
    #     server.sendmail(sender_email, receiver_email, message)
    # except Exception as e:
    #     # Print any error messages to stdout
    #     print(e)
    # finally:
    #     server.quit()
    #
    # pass
    def search(self):
        global numToCheck
        self.resNumber = '0'
        page = requests.get(self.urlToSearch)
        soup = BeautifulSoup(page.content, 'html.parser')
        line = soup.find_all('h2')
        if len(line) > 2:
            line = line[2]
            line = list(str(line)[9:22])
        else:
            line = list(str(line)[30:43])

        for i in line:
            if i.isdigit():
                self.resNumber += i
        if int(self.resNumber) != self.prevResults:
            # print(int(self.resNumber))

            if self.prevResults!=0 and self.prevResults < int(self.resNumber):
                print("prevRes = " + str(self.prevResults))
                print("currentRes = " + self.resNumber)

                sendEmail(self.urlToSearch.split('/')[4][2:], int(self.resNumber) - self.prevResults, self.urlToSearch)
            self.prevResults = int(self.resNumber)
            # print("works")
            # print(numToCheck)
          

        else:
            # print("works2")
            # print(self.urlToSearch.split('/')[4][2:])
            # print(self.prevResults)
            # print(int(self.resNumber))
            # print("-----")
          

            pass



all = ['https://www.olx.ro/oferte/q-rig-minare',
       'https://www.olx.ro/oferte/q-rig-minat',
       'https://www.olx.ro/oferte/q-mining-rig',
       'https://www.olx.ro/oferte/q-r9-390/?search%5Bfilter_float_price%3Afrom%5D=300&search%5Bfilter_float_price%3Ato%5D=1200',
       'https://www.olx.ro/oferte/q-rx-580/?search%5Bfilter_float_price%3Afrom%5D=300&search%5Bfilter_float_price%3Ato%5D=1200',
       'https://www.olx.ro/oferte/q-rx-480/?search%5Bfilter_float_price%3Afrom%5D=300&search%5Bfilter_float_price%3Ato%5D=1200',
       'https://www.olx.ro/oferte/q-5700-xt/?search%5Bfilter_float_price%3Afrom%5D=300&search%5Bfilter_float_price%3Ato%5D=2500',
       'https://www.olx.ro/vama/q-1151/?currency=RON&search%5Bfilter_float_price%3Ato%5D=300&search%5Bdist%5D=15',
       'https://www.olx.ro/oferte/q-rx-470/?search%5Bfilter_float_price%3Afrom%5D=300&search%5Bfilter_float_price%3Ato%5D=1200']
searchList = []
for index, url in enumerate(all):
    # print(index)
    # print(url)
    searchList.append(Search(url))

import threading
# while True:
def repeat():
    for obj in searchList:
        # done = False
        # if numToCheck == 0:
            # numToCheck += 1
        obj.search()
    threading.Timer(5.0, repeat).start()
repeat()
