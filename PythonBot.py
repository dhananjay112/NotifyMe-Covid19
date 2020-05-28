from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

#for notification
def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:/Users/dhana/OneDrive - Riga Technical University/Py/Dhinchak/coro.ico",
        timeout = 4
    )

#to retrive data from website
def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    try:
        while True:
            #notifyMe("KK", "Let's stop the spread of this virus together")
            myHtmlData = getData("https://www.mohfw.gov.in/")

            soup = BeautifulSoup(myHtmlData, 'html.parser')
            #print(soup.prettify())
            myDataStr = ""
            for tr in soup.find_all('tbody')[0].find_all('tr'):
                myDataStr += tr.get_text()
            myDataStr = myDataStr[1:]
            itemList = myDataStr.split("\n\n")

            states = ['Madhya Pradesh', 'Gujrat', 'Punjab', 'Delhi']
            for item in itemList[0:34]:
                dataList = item.split('\n')
                #print(dataList)
                if dataList[1] in states:
                    nTitle = 'Cases of Covid-19 in India'
                    nText = f"State {dataList[1]}\nConfirmed :{dataList[2]}\nCured & Migrated : {dataList[3]}\nDeaths : {dataList[4]}"
                    notifyMe(nTitle, nText)
                    time.sleep(2)
            time.sleep(20)

    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        pass