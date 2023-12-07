from urllib import response
import requests
import datetime as dt
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

my_email = 'ejljaithra2002@gmail.com'
my_password = 'ddwz nsmp kjid amqi'

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
#?q=Tesla Inc&from=2023-12-05&sortBy=popularity&apiKey=0444a288e01d46ac91ca9747248617b0

previous_date = dt.date.today() - dt.timedelta(days=1)
day_before_yesterday = previous_date - dt.timedelta(days=1)

news_param = {
    "q": COMPANY_NAME,
    "from": f"{previous_date}",
    "sortBy": "popularity",
    "apiKey": "0444a288e01d46ac91ca9747248617b0"
}

stock_param = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": "K703EWMPW1943V47"
    
}

response = requests.get(STOCK_ENDPOINT, stock_param)
response.raise_for_status()
stock_data = response.json()
previous_day = stock_data['Time Series (Daily)'][f'{previous_date}']['4. close']
day_before_yesterday = stock_data['Time Series (Daily)'][f'{day_before_yesterday}']['4. close']
print(previous_day)

positive_difference = (float(day_before_yesterday) - float(previous_day)) * -1

five_percent_change = float(positive_difference) * 0.05

if float(positive_difference)> 2:
    
    news_response = requests.get(NEWS_ENDPOINT, news_param)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data['articles']
    slices_articles = articles[0:3]
    
    titles = [article['title'] for article in slices_articles]
    descriptions = [article['description'] for article in slices_articles]

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        for title, description in zip(titles, descriptions):
            connection.sendmail(my_email, 'ejljaithra2002@gmail.com' , f'Subject: {titles}\n\n{descriptions}')


