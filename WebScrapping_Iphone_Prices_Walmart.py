# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 10:20:10 2023

@author: Malith Jayasinghe
"""

from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs
import pandas as pd
import random

url = "https://www.walmart.com/browse/cell-phones/apple-iphone/1105910_7551331_1127173?povid=GlobalNav_rWeb_Electronics_CellPhones_iPhone"

#Header through the postman
headers = {
  'authority': 'www.walmart.com',
  'accept': 'application/json',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/json',
  'cookie': 'AID=wmlspartner%3D0%3Areflectorid%3D0000000000000000000000%3Alastupd%3D1678087466499; auth=MTAyOTYyMDE4kj7lnc9cbUotzKXvOQin%2BYJ1rXiTHKugufO1B8cDlvsyYDg1%2Fq6MWCy4WZ53EYJprBU09srRd6NGMA5nLsyPwXCJuHwzjxaJ4evgMb2ULzXp%2Baur0uxTV2mLMqRs8w8s767wuZloTfhm7Wk2KcjygpySosImygUk1x1iKsdnk49xGIQA%2BqlQmBp3DsHownsLXjCcp5HLRN6DFPcfhgF%2BG0YVm0ngHOJTLFkQpjZFc9AUMk70P8glgOEpLOprhDfMDCcb9mgycy9jtT1uIyOBHQNTOrot%2FxhbgW8FFQHm3XY89OtMDIwAC%2FZui46nkIpsEGc%2BzNZFGOrBbdZqLvU3c8ZYoQxj3YwN6oVMIXW4lMrXFVcCoWXx%2BioiH9MKKd%2FWKh6D9w6SZvLXAN9J4XHpSkjyrOXbKKhH072NS%2FW0j%2FU%3D; ACID=df24ae0a-20a5-4d34-99dc-d7e7dc2c3bde; hasACID=true; locDataV3=eyJpc0RlZmF1bHRlZCI6dHJ1ZSwiaXNFeHBsaWNpdCI6ZmFsc2UsImludGVudCI6IlNISVBQSU5HIiwicGlja3VwIjpbeyJidUlkIjoiMCIsIm5vZGVJZCI6IjMwODEiLCJkaXNwbGF5TmFtZSI6IlNhY3JhbWVudG8gU3VwZXJjZW50ZXIiLCJub2RlVHlwZSI6IlNUT1JFIiwiYWRkcmVzcyI6eyJwb3N0YWxDb2RlIjoiOTU4MjkiLCJhZGRyZXNzTGluZTEiOiI4OTE1IEdlcmJlciBSb2FkIiwiY2l0eSI6IlNhY3JhbWVudG8iLCJzdGF0ZSI6IkNBIiwiY291bnRyeSI6IlVTIiwicG9zdGFsQ29kZTkiOiI5NTgyOS0wMDAwIn0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjozOC40ODI2NzcsImxvbmdpdHVkZSI6LTEyMS4zNjkwMjZ9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJodWJOb2RlSWQiOiIzMDgxIiwic3RvcmVIcnMiOiIwNjowMC0yMzowMCIsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIlBJQ0tVUF9JTlNUT1JFIiwiUElDS1VQX0NVUkJTSURFIl0sInN0b3JlU2VsZWN0aW9uVHlwZSI6IkRFRkFVTFRFRCJ9XSwic2hpcHBpbmdBZGRyZXNzIjp7ImxhdGl0dWRlIjozOC40ODI2NzcsImxvbmdpdHVkZSI6LTEyMS4zNjkwMjYsInBvc3RhbENvZGUiOiI5NTgyOSIsImNpdHkiOiJTYWNyYW1lbnRvIiwic3RhdGUiOiJDQSIsImNvdW50cnlDb2RlIjoiVVMiLCJsb2NhdGlvbkFjY3VyYWN5IjoibG93IiwiZ2lmdEFkZHJlc3MiOmZhbHNlfSwiYXNzb3J0bWVudCI6eyJub2RlSWQiOiIzMDgxIiwiZGlzcGxheU5hbWUiOiJTYWNyYW1lbnRvIFN1cGVyY2VudGVyIiwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOltdLCJpbnRlbnQiOiJQSUNLVVAiLCJzY2hlZHVsZUVuYWJsZWQiOmZhbHNlfSwiZGVsaXZlcnkiOnsiYnVJZCI6IjAiLCJub2RlSWQiOiIzMDgxIiwiZGlzcGxheU5hbWUiOiJTYWNyYW1lbnRvIFN1cGVyY2VudGVyIiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6Ijk1ODI5IiwiYWRkcmVzc0xpbmUxIjoiODkxNSBHZXJiZXIgUm9hZCIsImNpdHkiOiJTYWNyYW1lbnRvIiwic3RhdGUiOiJDQSIsImNvdW50cnkiOiJVUyIsInBvc3RhbENvZGU5IjoiOTU4MjktMDAwMCJ9LCJnZW9Qb2ludCI6eyJsYXRpdHVkZSI6MzguNDgyNjc3LCJsb25naXR1ZGUiOi0xMjEuMzY5MDI2fSwiaXNHbGFzc0VuYWJsZWQiOnRydWUsInNjaGVkdWxlZEVuYWJsZWQiOnRydWUsInVuU2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwiYWNjZXNzUG9pbnRzIjpbeyJhY2Nlc3NUeXBlIjoiREVMSVZFUllfQUREUkVTUyJ9XSwiaHViTm9kZUlkIjoiMzA4MSIsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIkRFTElWRVJZX0FERFJFU1MiXSwic3RvcmVTZWxlY3Rpb25UeXBlIjoiREVGQVVMVEVEIn0sImluc3RvcmUiOmZhbHNlLCJyZWZyZXNoQXQiOjE2NzgwODc3NjY1NjIsInZhbGlkYXRlS2V5IjoicHJvZDp2MjpkZjI0YWUwYS0yMGE1LTRkMzQtOTlkYy1kN2U3ZGMyYzNiZGUifQ%3D%3D; assortmentStoreId=3081; hasLocData=1; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsInN0b3JlSW50ZW50IjoiUElDS1VQIiwibWVyZ2VGbGFnIjpmYWxzZSwiaXNEZWZhdWx0ZWQiOnRydWUsInN0b3JlU2VsZWN0aW9uVHlwZSI6IkRFRkFVTFRFRCIsInBpY2t1cCI6eyJub2RlSWQiOiIzMDgxIiwidGltZXN0YW1wIjoxNjc4MDg3NDY2NTYwfSwic2hpcHBpbmdBZGRyZXNzIjp7InRpbWVzdGFtcCI6MTY3ODA4NzQ2NjU2MCwidHlwZSI6InBhcnRpYWwtbG9jYXRpb24iLCJnaWZ0QWRkcmVzcyI6ZmFsc2UsInBvc3RhbENvZGUiOiI5NTgyOSIsImNpdHkiOiJTYWNyYW1lbnRvIiwic3RhdGUiOiJDQSIsImRlbGl2ZXJ5U3RvcmVMaXN0IjpbeyJub2RlSWQiOiIzMDgxIiwidHlwZSI6IkRFTElWRVJZIiwic3RvcmVTZWxlY3Rpb25UeXBlIjoiREVGQVVMVEVEIn1dfSwicG9zdGFsQ29kZSI6eyJ0aW1lc3RhbXAiOjE2NzgwODc0NjY1NjAsImJhc2UiOiI5NTgyOSJ9LCJtcCI6W10sInZhbGlkYXRlS2V5IjoicHJvZDp2MjpkZjI0YWUwYS0yMGE1LTRkMzQtOTlkYy1kN2U3ZGMyYzNiZGUifQ%3D%3D; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; TB_SFOU-100=; vtc=dzAI-KpAR2j67BpLSrGOeQ; bstc=dzAI-KpAR2j67BpLSrGOeQ; mobileweb=0; xpth=x-o-mart%2BB2C~x-o-mverified%2Bfalse; xpa=0dn-S|14us3|2OL6S|6N-qW|A5Ih6|BgpxY|Ce2NS|D8jju|Eq7vl|FOCoj|FVa_h|FvI0t|Ho3eT|IIcmL|IM26Z|RFZpx|Tgis7|VMEdu|YUOnt|YnYws|c8tN_|coocN|dOaut|dj4QZ|kNvPV|qybp-|rwcby|uGOHl|uPVFl|wW-8A|xStsO; exp-ck=0dn-S12OL6S1A5Ih61BgpxY1Ce2NS1D8jju1Eq7vl1FvI0t1Ho3eT1IIcmL1IM26Z3RFZpx1Tgis71VMEdu1YnYws2coocN1dOaut1kNvPV2qybp-1xStsO1; _pxhd=ae8bd7a7e97ab64ba14b7f1ce613f0d0ee2e3e9afe60bf1e558a16dc8f33f103:ece93e90-bbef-11ed-b236-52564e477a54; xptwj=rq:e0be397e9ca569348fc0:aBzifVhBsZK5K4dQiKe1uwktz9RweO9m1UWEvYI54Qp4B7Pu5Cdj2OyVFRxTLM/YnjTQodWR9a1JPGr2cm5p5q44Dj/Fq/uJa1+/sMx/nRA4evBRo60a9MqnWf8x7Ow=; akavpau_p2=1678088067~id=430c60a3e4b92bae05ce13be8f2f7482; ak_bmsc=21245A9BA887CD8009E32983EF111739~000000000000000000000000000000~YAAQM1RLaJIJyrWGAQAAybXOtROI2MCysenGTdhJtpbHeuX8gZ6nzpenZ559mKY59qQLGIhUqwSeDQodQgSSdSni4JRWAWXHcGV+MV9Yus/UTsUphqj0PM6yHxInA8V+GHSOK1fXr9ktcYwbjh9ehPVUwtbtSenA+EJG388YTBJZ1tiZm9l4D0X3gFLLSA7eCgDY2OHb883x/9weOQ3SHP40RaAyp2F4N+wYdoFInHm3B/w7s8CQUojz71Zm6bCP8tZCudpU9oBzjclGxzpyy5t9NcFQ/1/ltpJZw52cnhf9bs+akRuvyYUs1oPHoZUN22QnmX79bXyHfvASVqPZvz5i79bAxBWdWwHnjXvx1eK0OkQFhdNM1qQDWvKURTSyZEIEl/l2Tix16d2zBtXgdRSDL9H37z74fkrZ8s3IXiBF7MuYLmJqcNBUKZkd+zYDD8o+iDOP/u8TEcm3YKGZD01lZFhOxfsci9JJZ1bn5cwHcg==; TBV=7; _astc=fe6064fe9ae3a4f2d2773bbad3f3efb3; adblocked=false; pxcts=eeba8ea2-bbef-11ed-b6fb-4a71566b7370; _pxvid=ece93e90-bbef-11ed-b236-52564e477a54; _pxff_cfp=1; xptc=assortmentStoreId%2B3081; _px3=d01740ae459b72428fb822bf4cf081c98b16dec5fc7f79ea3a06e3bfd422f5f3:7EmsYHrk9ZM7DK39svtoQ5ZvOwhwhjvkwMBWdexvYb/Ur/tBtaeZjFcB25cbqplB2OlB60H6EWtijt/4X7mp/w==:1000:2mbMU4o6XdQe/SNnwvwftsToUJvClIC+1Z5tf+PgJ3bZ/327MX9OMDM+QCyqEGdksSWOMaG8U0gu0p90MABudRzcY2ii1RlcyyTMtUOGr6YEg+I7ivGk7q6B+iiTlKx3/6WPuTI0CtdgGOPRWkVpATBPj/HdvoR2/PRjcCnJDavumIto+Gx/vBuMtPj1NFHOrMBlvJWcDdtV8CUxZ7iUJQ==; _pxde=b3a4cf35be13540c870cbf18fc38aeb1e49a87c4bc6a7b8a4049e3f17aa0a213:eyJ0aW1lc3RhbXAiOjE2NzgwODc0Nzk4MDd9; xpm=1%2B1678087470%2BdzAI-KpAR2j67BpLSrGOeQ~%2B0; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1678087487000@firstcreate:1678087466499"; xptwg=4220775243:1A1227348642690:42BA1B5:B3D9FD86:499DD9BE:3FFA160C:; TS012768cf=01b895dea4413c739c700e74f033450da6cef0a5ed77e688d76203bc16f077ae5cb96633304d6f5dd002dec643104c010b8649ff41; TS01a90220=01b895dea4413c739c700e74f033450da6cef0a5ed77e688d76203bc16f077ae5cb96633304d6f5dd002dec643104c010b8649ff41; TS2a5e0c5c027=082e3f18deab2000674f2e2e8e2a8511e821eb2ff982f566b2dcd3f0acfe024022f7756813dbeb27083388e9761130004709e2c4b94e3523aa5d1914e9d8d79441eee9cdcbfdb87c657e85c1fbe3912f980109edafe0508103e69e28a3daf2d0; bm_sv=2C213E1D686796587237E23153E2061B~YAAQM1RLaFcLyrWGAQAAZgHPtRMFF1Tq/M4f1yiXuptvH6SPyo8e3ew+qdrl9OjAplKGOVast2wGVvQp0W3zYimZcyM7I6b6WdwZe9YRu6ME0j2eadGlRPT2ruU7jMfXM7jNUIT2Pl2zjnzsz1LF4tnwY43J6J0W/i7B5GT0IaIZ6Xtu8dVSBViuZaeQmlzzxlaov9DBNy4tDdbcJD1RCurC8rsWFhuJQWfatOQ0BPJNJ95icyUEMo+XyQPk04vI6A==~1',
  'device_profile_ref_id': 'U9QxwYLFWfu4r0GYt-w0lRjiOZW2eNYcknWZ',
  'referer': 'https://www.walmart.com/browse/cell-phones/apple-iphone/1105910_7551331_1127173?povid=GlobalNav_rWeb_Electronics_CellPhones_iPhone&page=2&affinityOverride=default',
  'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'traceparent': '00-0fa86a42744e7cb9c2f6dec3c65840f1-6b44b4901032d4bf-00',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
  'wm_mp': 'true',
  'wm_page_url': 'https://www.walmart.com/browse/cell-phones/apple-iphone/1105910_7551331_1127173?povid=GlobalNav_rWeb_Electronics_CellPhones_iPhone&page=2&affinityOverride=default',
  'wm_qos.correlation_id': 'O-CrK8_oT7-BrXMYjaI9iH4kTFK2MNDdLhLD',
  'x-apollo-operation-name': 'Browse',
  'x-enable-server-timing': '1',
  'x-latency-trace': '1',
  'x-o-bu': 'WALMART-US',
  'x-o-ccm': 'server',
  'x-o-correlation-id': 'O-CrK8_oT7-BrXMYjaI9iH4kTFK2MNDdLhLD',
  'x-o-gql-query': 'query Browse',
  'x-o-mart': 'B2C',
  'x-o-platform': 'rweb',
  'x-o-platform-version': 'main-1.51.0-1f10f1-0302T0622',
  'x-o-segment': 'oaoh'
}

options = webdriver.ChromeOptions()
options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36')

#Min and Max timers generate random sleep timer
min_sleep = 7
max_sleep = 10
sleep_time = random.randint(min_sleep, max_sleep)


# set the base URL and create a list of all the page URLs
base_url = r"https://www.walmart.com/browse/cell-phones/apple-iphone/1105910_7551331_1127173?povid=GlobalNav_rWeb_Electronics_CellPhones_iPhone&action=Create&rm=true&page="
page_num = 25
page_urls = [base_url + str(i) for i in range(1, page_num)]

# loop through all the page URLs and extract the required information
iphone_models = []
iphone_prices = []
#iphone_ratings = []

for url in page_urls:
    driver = webdriver.Chrome(executable_path = r"D:\Campus\3rd years\Second Sem\Statistics in Practice\Guest Lecture on Web Scrapping\Assigment\chromedriver.exe", chrome_options = options)
    # wait for the page to load
    time.sleep(sleep_time)
    # open the page in the browser
    response = driver.get(url)
    html = driver.page_source
    bsobj = bs(html,'lxml')
    
    # get all the product elements on the current page
    model = bsobj.findAll('span',{'class':"w_V_DM"})
    price = bsobj.findAll('div',{'data-automation-id':"product-price"})
    #rating = bsobj.findAll('div.flex items-center mt2',{'class':"w_iUH7"})
    
    for model,price in zip(model, price):
        iphone_models.append(model.span.text.strip())
        iphone_prices.append(price.div.text.strip())
        #iphone_ratings.append(rating.span.text.strip())
    print("Scrapping Done"+url) 
    driver.quit() 
    #Driver had to close before go to the next page since I couldn't able to bypass walmart captcha. Dynamic proxies will do the job but It's a paid option.
    
    time.sleep(sleep_time) 
    #Human verification can still be poped-up since we are using the same IP-addressess. This can interupt the data extraction. Therefore It's good to have a vpn service and change the location manually after every 3/4 pages. 



# save the extracted information to an Excel file
save_path = r"D:\Campus\3rd years\Second Sem\Statistics in Practice\Guest Lecture on Web Scrapping\Assigment\iphone_prices.xlsx"

df = pd.DataFrame({'Iphone_Model':iphone_models,'Price':iphone_prices})
df.to_excel(save_path)




















