"""
The code is generated using the News API. One can generate his own API key from the link -  https://newsapi.org/
The program is divided based on different url. The API key give access to 2 different url and there is different documentation for both the url.
URL_1 = https://newsapi.org/v2/top-headlines and URL_2 = https://newsapi.org/v2/everything
Before making any changes in the parameter section of the code, make sure you read documentation. Insert the API key in the 'apiKey' section and use the code. 
Comment if you found any suggestion or have any error in the file. 
"""
import requests
# import time


url_1 = 'https://newsapi.org/v2/top-headlines'
url_2 = 'https://newsapi.org/v2/everything'
key = 'Generate your API using https://newsapi.org/'

def source_news(k): #News based on the particular source. 
    print(f'You will be provided with the top headlines of the day using NewsAPI from {k}.')
    # time.sleep(2) #You can introduce the sleep module to make it more presentable and readable. 
    url = url_1
    param = {
        'sources' : k,
        'sortBy' : 'top',
        'apiKey' : key
    }

    req = requests.get(url, param)
    open_news_headline = req.json()

    for i in open_news_headline['articles']:
        print(i['title'])
        # time.sleep(2) # This will give a delay of 2 sec before giving the next news. 

def category_news(a): # Based on the user keyword. Get top news. 
    print(f'You will be provide with the news of the day using NewsAPI for a particular keword: {a}.')
    # time.sleep(2)
    url = url_2
    param = {
        'q': a,
        'sortBy' : 'top',
        'apiKey' : key
    }

    req = requests.get(url, param)
    open_news_headline = req.json()

    for i in open_news_headline['articles']:
        print(i['title'])
        # time.sleep(2)

def country_news(b): # Enter the country code to know the news belonging to particular country.
    print(f'You will be provide the top headlines of the day using NewsAPI for country: {b}.')
    # time.sleep(2)
    url = url_1
    param = {
        'country': b,
        'sortBy' : 'top',
        'apiKey' : key
    }

    req = requests.get(url, param)
    open_news_headline = req.json()

    for i in open_news_headline['articles']:
        print(i['title'])
        # time.sleep(2)

def domain_news(c): # Based on the specific domain get news.   
    print(f'You will provide you the news of the day using NewsAPI from a specific domain: {c}.')
    # time.sleep(2)
    url = url_2
    param = {
        'domains': c,
        'sortBy' : 'top',
        'apiKey' : key
    }

    req = requests.get(url, param)
    open_news_headline = req.json()

    for i in open_news_headline['articles']:
        print(i['title'])
        # time.sleep(2)

def language_news(d): # Get news based on the language. 
    print(f'You will be provide with the top headlines of the day using NewsAPI for language: {d}')
    # time.sleep(2)
    url = url_1
    param = {
        'language': d,
        'sortBy' : 'top',
        'apiKey' : key
    }

    req = requests.get(url, param)
    open_news_headline = req.json()

    for i in open_news_headline['articles']:
        print(i['title'])
        # time.sleep(2)

def category_time_news(e,f,g): # Get news on the time period and the intrest you are looking for. 
    print(f'You will be provide with the news of the day using NewsAPI for specific category: {e}, and time period starting from: {f} and ending at: {g}.')
    # time.sleep(2)
    url = url_2
    param = {
        'q' : e,
        'from': f,
        'to' : g,
        'apiKey' : key
    }
    
    req = requests.get(url, param)
    open_news_headline = req.json()
    # print(open_news_headline)

    for i in open_news_headline['articles']:
        print(i['title'])
        # time.sleep(2)

print('Welcome! Please go along the options in order to reciceve the news.')
print('What type of news you wish to see: \n1. Based on news sources - such as BBC News, ABC News, etc. \n2. Based on the Keyword auch as apple, sony, village, pollution, etc. \n3. Based on the Country such as India - in, USA - us, etc. \n4. Based on particular domain such as engadget.com, etc. \n5. Based on time language such as english - en, arbic -ar, etc. \n6. Based on Keyword and time from such as sony from 2024-02-02 to 2024-02-26, etc. \n7. Done with the news')

while(True):
    k = input('Enter the number based on the menu: ')
    keyword = int(k)
    if keyword == 1:
        usr_inpt = input('Enter the news source from which you want to recieve the headlines: ')
        source_news(usr_inpt)
    elif keyword == 2:
        fltr_wrd = input('Enter the word you want news for: ')
        category_news(fltr_wrd)
    elif keyword == 3:
        cntry_code = input('Entry the code of the country you wish to listen the news: ')
        country_news(cntry_code)
        print('You can try from different country code as well - ae, ar, at, au, be, bg, br, ca, ch, cn, co, cu, cz, de, eg, fr, gb, gr, hk, hu, id, ie, il, in, it, jp, kr, lt, lv, ma, mx, my, ng, nl, no, nz, ph, pl, pt, ro, rs, ru, sa, se, sg, si, sk, th, tr, tw, ua, us, ve, za.')
    elif keyword == 4:
        domn = input('Entry the domain from which you would like to get the headlines: ')
        domain_news(domn)
    elif keyword == 5:
        lang_news = input('Enter the language you wish to obtain the news from: ')
        language_news(lang_news)
        print('You can try for different languages as well - ar, de, en, es, fr, he, it, nl, no, pt, ru, se, ud, zh.')
    elif keyword == 6:
        print('Enter format is keyword, YYYY-MM-DDT00:00:00, YYYY-MM-DDT00:00:00')
        catgry_fltr = input('Enter the filter word:  ')
        from_fltr = input('Starting Date: ')
        to_fltr = input('End Date: ')
        category_time_news(catgry_fltr,from_fltr,to_fltr)
    else:
        print('Thank you. Hope you found the required news.')
        break
