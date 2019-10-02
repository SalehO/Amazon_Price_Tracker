import requests
import smtplib
from bs4 import BeautifulSoup
import time
URL = 'https://www.amazon.com/Zero-Tolerance-0393GLCF-Hinderer/dp/B07PDJB4NF?pf_rd_p=0fc3f2c4-3ed5-4d11-9995-8d7c82394713&pd_rd_wg=jBCi1&pf_rd_r=EG2FXTY6WKCCFYZKJ9Y9&ref_=pd_gw_cr_simh&pd_rd_w=VDEYC&pd_rd_r=6311b83e-84d2-4543-bc3b-9420b5f7b2f5'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}


def checker(url_param, eml):
    #set email to the email provided
    em_add = eml
    #open url
    page = requests.get(url_param, headers=headers)

    #parse url
    soup = BeautifulSoup(page.content,'lxml')

    title = soup.find(id="productTitle").get_text() #get the title text only and strip spaces
    price = soup.find(id="priceblock_ourprice").get_text().strip()
    price=price.replace("$","")#remove $ from price string

    
   
   
    float_price = float(price) #convert price from string to float for comparrasion reasons

    print("The product is: \n"+ "   "+title.strip())
    print("The price is:")
    print("   "+ str(float_price))
    old_price = get_price(soup);
    i =0;
    while(True):
        if(float_price < float_price):
            ret_string = "The product: \n   {}\n Current Price is:\n   {}\n\n".format(title.strip(),str(float_price))
            send_email(ret_string , em_add)
        print("checked: "+ str(i))
        i = i+1
        time.sleep(60)


def send_email(title_price, em):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo() # establish connection
    server.starttls()
    server.ehlo()

    server.login('price.drop.tracker@gmail.com','oduofmqwsgmlwhym')

    subject= "Amazon Price Drop!"
    body = '{} Check the amazon link https://www.amazon.com/Zero-Tolerance-0393GLCF-Hinderer/dp/B07PDJB4NF?pf_rd_p=0fc3f2c4-3ed5-4d11-9995-8d7c82394713&pd_rd_wg=jBCi1&pf_rd_r=EG2FXTY6WKCCFYZKJ9Y9&ref_=pd_gw_cr_simh&pd_rd_w=VDEYC&pd_rd_r=6311b83e-84d2-4543-bc3b-9420b5f7b2f5'.format(title_price)

    message = f"Subject: {subject}\n\n{body}"
    server.sendmail('price.drop.tracker@gmail.com', em ,message) ## Replace ramohamidoo@gmail.com with your OWN email

    print("Email has been sent")

    server.quit()

def user_input():
    g = input("Enter the URL: ")
    e = input("Enter your email address: ")
    checker(g, e)

# checker()

def get_price(sp):
    # title = sp.find(id="productTitle").get_text() #get the title text only and strip spaces
    price = sp.find(id="priceblock_ourprice").get_text().strip()
    price=price.replace("$","")#remove $ from price string
    float_price = float(price) 
    return float_price

    
   
   
    float_price = float(price)


user_input()
