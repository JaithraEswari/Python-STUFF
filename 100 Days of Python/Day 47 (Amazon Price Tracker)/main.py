import requests
from bs4 import BeautifulSoup
import lxml
from smtplib import SMTP

my_email = 'ejljaithra2002@gmail.com'
my_password = 'xxxxxxxxxxxx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding':'gzip, deflate, br'
}

Url = 'https://www.amazon.in/LG-UltraGearTM-Monitor-Display-Gameplay/dp/B0C8MVVCQN/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=wtRwD&content-id=amzn1.sym.cd312cd6-6969-4220-8ac7-6dc7c0447352%3Aamzn1.symc.ca948091-a64d-450e-86d7-c161ca33337b&pf_rd_p=cd312cd6-6969-4220-8ac7-6dc7c0447352&pf_rd_r=VARBQ8WRFN4E55V392AM&pd_rd_wg=wMbLh&pd_rd_r=ac535447-eb92-4b51-aa8b-9d569b84f337&pd_rd_i=B0C8MVVCQN'

response = requests.get(url=Url, headers=headers)
response.raise_for_status()


soup = BeautifulSoup(response.text, 'lxml')
price = soup.find(name='span', class_='a-price-whole')
splitted = price.text.replace(',', '')
clean_price = int(splitted.replace('.', ''))
print(clean_price)

description = 'LG UltraGear™ Gaming Monitor(27") QHD IPS Display(2560*1440), Smooth Gameplay:165Hz & 1ms, HDR 10, sRGB 99%(Typ.), G-SYNC®, AMD FreeSync™ Premium, Anti-Glare, Height, Pivot, HDMI, DP, HP Out, 27GR75Q now'
encoded_description = description.encode('utf-8')

if clean_price < 25000:
    with SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(my_email, 'ejljaithra2002@gmail.com', f'Subject: Monitor Price Drop!!!!!!\n\n{encoded_description} {clean_price}')
        print(connection)
