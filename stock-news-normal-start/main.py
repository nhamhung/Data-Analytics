STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
import requests
import os
AV_key = "IVUC025N58G2KRGK"
news_key = "1e34783b3b774ec5bdea26967ca444f0"
TWILIO_SID = "AC5445f48d0268120d008a52e58253304b"
TWILIO_AUTH = "d75d9155e5daeb5987bf7fbd8fcc831b"
from twilio.rest import Client

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": AV_key
}

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
request = requests.get(STOCK_ENDPOINT, params=parameters)
request.raise_for_status()
request_data = request.json()
daily_stock_prices = [[day, info] for (day, info) in request_data['Time Series (Daily)'].items()]
yesterday_closing_stock_price = float(daily_stock_prices[0][1]['4. close'])

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_closing_stock_price = float(daily_stock_prices[1][1]['4. close'])

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff = yesterday_closing_stock_price - day_before_yesterday_closing_stock_price
up_down = None
if diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_diff = round((diff/day_before_yesterday_closing_stock_price) * 100)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(percent_diff) > 1:
    news_request = requests.get(NEWS_ENDPOINT, params={
        "qInTitle": COMPANY_NAME,
        "apiKey": news_key
    })
    news_request_data = news_request.json()
    articles = news_request_data['articles'][:3]
    formatted_articles = [f"Tesla: {up_down}{percent_diff}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in articles]

    client = Client(TWILIO_SID, TWILIO_AUTH)

    for article in formatted_articles:
        print(article)
        message = client.messages \
            .create(
            body=article,
            from_='+19362373772',
            to='+6591608840'
        )
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.


#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

