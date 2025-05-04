import requests
import sys
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText


def eml(l,name,url):

    title = 'My title'
    msg_content = (f"Name: {name} \n Url: {url}")
    message = MIMEText(msg_content, 'html')

    message['From'] = 'Reminder <sender@server>'
    message['To'] = 'Receiver Name <receiver@server>'
    message['Cc'] = 'Receiver2 Name <receiver2@server>'
    message['Subject'] = 'New Product Arived'

    msg_full = message.as_string()

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login("newproductremind@gmail.com","sbis28330")
    
    server.sendmail('newproductremind@gmail.com',l,
                    msg_full)



name=[]
Url=[]
price=[]
day=[]
base_url = "https://sg.carousell.com"
def sc(query):
    url="https://www.carousell.sg/search/"+query+"?addRecent=true&searchId=bH-4y9&sort_by=3"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup=BeautifulSoup(plain_text,"html5lib")
    for i in soup.find_all("a"):
        s=str(i.get("href"))
        if s.startswith("/p/"):
            w=(i.find_all("img"))[-1].get("alt")
            #print(w)
            Url.append(base_url+s)
            
            name.append(w)
            nxt=i.find_all("p")
            for o in nxt:
                o1=str(o.string)
                #print(o1)
                if o1.startswith("S$"):
                    #print(o1)
                    price.append(o1)
            #print(i.find_all("p"))
        if s.startswith("/u/"):
            for n in i.find_all("p"):
                o2=str(n.string)
                if o2.endswith("ago"):
                    day.append(o2)
    return name,price,day,Url

#print(price)
def crawl(query, min_price, max_price):
    min = int(min_price)
    max = int(max_price)
    d=0
    while d<len(day):
        a=day[d].split(" ")
        try:
            if ((int(price[d][2:])>=min)and(int(price[d][2:]))<=max):
                try:
                        file=open(query,"r")
                        li=file.readlines()
                        if (a[1]!="days") or (a[1]!="months") or (a[1]!="month"):
                            if (name[d]+"\n") not in li:
                                print(f"Name: {name[d]}\n Day: {day[d]}\n Price: {price[d]}\n Url: {Url[d]}")
                                l="manikchandrabiswas72@gmail.com"
                                eml(l,name[d],Url[d])
                                fi=open(query,"a")
                                fi.write(name+"\n")
                                fi.close()
                        file.close()
                except:
                    file=open(query,"a+")
                    file.write(name[d]+"\n")
                    file.close()
        except:
            pass
        d=d+1
#print(len(name

if __name__ == '__main__':

    print(" { - - WELCOME - - } ")
    print("\n")
    if(len(sys.argv) < 2):
        pass

    query = sys.argv[1]
    #print(query)
    if(len(sys.argv) == 2):
        name,price,day,Url=sc(query)
        crawl(query, 0, sys.maxsize)
    else:
        name,price,day,Url=sc(query)
        crawl(query, sys.argv[2], sys.argv[3])
