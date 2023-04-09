from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re
import random
import csv 
import json
import schedule    
import time  

driver = None

def open_bot():
    global driver
    # profile = webdriver.FirefoxProfile()
    # profile.set_preference("general.useragent.override", "whatever you want")
    driver = webdriver.Firefox(executable_path="/geckodriver.exe")
    # driver = webdriver.Chrome('/yandexdriver.exe')
    # driver = webdriver.Chrome(executable_path="/chromedriver.exe")
    firefox_options = Options()
    # user_auth_v2:"eyJsb2dnZWRJbiI6dHJ1ZSwiYXV0aCI6eyJ0b2tlbl90eXBlIjoiQmVhcmVyIiwiZXhwaXJlc19pbiI6MTIwOTYwMCwiYWNjZXNzX3Rva2VuIjoiOGQ5MzU5M2RlZmNkMTM2ODZhNGUzZGViZDdkYWUyNTdlZjlmNTU2ZTU1MDdmZDkzZDg1YjAxYjYwYmU5ZGE0ZWU4NmI4Y2YzNmU2ZmI0ZDciLCJyZWZyZXNoX3Rva2VuIjoiYzlmNWRhZjJhMDZlNDEwZmE4Y2Q1ZTlkNDQ4YTQ4MDZhYjEwNWU1YjIxY2ZmMzgzODc5YTU3MmI5MmY4YmQ1NDE0NDdkZWNlZDAzNTAyOWIifSwiaW5mbyI6eyJpZCI6MTAxNjEyLCJmaW8iOiLQnNCw0LrQsNGA0L7QsiDQmtC40YDQuNC70Lsg0JDQvdCw0YLQvtC70YzQtdCy0LjRhyIsImxvZ2luIjoiOTI4Mjc0MjAxMiIsInJvbGUiOiJjYXJyaWVyX293bmVyIiwicm9sZU5hbWUiOiLQn9C10YDQtdCy0L7Qt9GH0LjQuiIsInVzZXJUeXBlIjoiY2FycmllciIsImlzU3RhZmYiOmZhbHNlLCJwZXJtaXNzaW9ucyI6W3siTmFtZSI6ImFjY2Vzc190b19jYXJyaWVyX2NvbXBhbmllcyIsIkRlc2NyaXB0aW9uIjoi0JTQvtGB0YLRg9C/INC6INC60L7QvNC/0LDQvdC40Y/QvCJ9LHsiTmFtZSI6ImNvbXBhbnlfZGlyZWN0b3JfcGVybWlzc2lvbiIsIkRlc2NyaXB0aW9uIjoi0J7RgdC90L7QstC90YvQtSDQv9GA0LDQstCwINC00LjRgNC10LrRgtC+0YDQsCDQutC+0LzQv9Cw0L3QuNC4INC/0LXRgNC10LLQvtC30YfQuNC60LAifSx7Ik5hbWUiOiJjcmVhdGVfYW5kX2VkaXRfZHJpdmVyIiwiRGVzY3JpcHRpb24iOiLQodC+0LfQtNCw0L3QuNC1INC4INGA0LXQtNCw0LrRgtC40YDQvtCy0LDQvdC40LUg0LLQvtC00LjRgtC10LvRjyJ9LHsiTmFtZSI6ImNyZWF0ZV9hbmRfZWRpdF90cmFpbCIsIkRlc2NyaXB0aW9uIjoi0KHQvtC30LTQsNC90LjQtSDQuCDRgNC10LTQsNC60YLQuNGA0L7QstCw0L3QuNC1INC/0YDQuNGG0LXQv9CwIn0seyJOYW1lIjoiY3JlYXRlX2FuZF9lZGl0X3RydWNrIiwiRGVzY3JpcHRpb24iOiLQodC+0LfQtNCw0L3QuNC1INC4INGA0LXQtNCw0LrRgtC40YDQvtCy0LDQvdC40LUg0LDQstGC0L4ifSx7Ik5hbWUiOiJjcmVhdGVfYW5kX2ZpbGxlZF9vcmRlciIsIkRlc2NyaXB0aW9uIjoi0KHQvtC30LTQsNC90LjQtSDQuCDQt9Cw0L/QvtC70L3QtdC90LjQtSDQt9Cw0Y/QstC60LggKNCf0YDQuNC60YDQtdC/0LvQtdC90LjQtSDQstC+0LTQuNGC0LXQu9GPINC4INC00L7QutGD0LzQtdC90YLQvtCyKSJ9LHsiTmFtZSI6ImNyZWF0ZV9jb21wYW55X3BlcnNvbiIsIkRlc2NyaXB0aW9uIjoi0KHQvtC30LTQsNC90LjQtSDQvtGC0LLQtdGC0YHRgtCy0LXQvdC90YvRhSDQv9C10YDQtdCy0L7Qt9GH0LjQutCwIn0seyJOYW1lIjoiY3JlYXRlX2xlZ2FsX2VudGl0eSIsIkRlc2NyaXB0aW9uIjoi0KHQvtC30LTQsNC90LjQtSDRjtGALiDQu9C40YYg0LIg0LrQvtC80L/QsNC90LjQuCDQv9C10YDQtdCy0L7Qt9GH0LjQutCwIn0seyJOYW1lIjoiZGlzcGxheV9kZWxpdmVyaWVzX3dpdGhvdXRfZGVsYXkiLCJEZXNjcmlwdGlvbiI6ItCe0YLQvtCx0YDQsNC20LXQvdC40LUg0YDQtdC50YHQvtCyINCx0LXQtyDQt9Cw0LTQtdGA0LbQutC4In0seyJOYW1lIjoiZHJpdmVyX3Blcm1pc3Npb24iLCJEZXNjcmlwdGlvbiI6ItCf0YDQsNCy0LAg0LTQu9GPINC/0L7Qu9GM0LfQvtCy0LDRgtC10LvRjy3QstC+0LTQuNGC0LXQu9GPIn0seyJOYW1lIjoicmVmdXNlX29yZGVyIiwiRGVzY3JpcHRpb24iOiLQntGC0LzQtdC90LAg0YHQvtCx0YHRgtCy0LXQvdC90YvRhSDQt9Cw0Y/QstC+0LoifSx7Ik5hbWUiOiJyZW1vdmluZ19zcGVjX2Zvcl9hbmFsb2dfb3JkZXJzX293bmVyX29mX2FwcHJvdmVkIiwiRGVzY3JpcHRpb24iOiLQodC90Y/RgtC40LUg0L/RgNC+0LLQtdGA0LrQuCDQvdCwINCw0L3QsNC70L7Qs9C40YfQvdGL0LUg0LfQsNC60LDQt9GLINC+0YIg0YHQvtCx0YHRgtCy0LXQvdC90LjQutCwINC/0YDQuCDRg9GC0LLQtdGA0LbQtNC10L3QuNC4INC30LDRj9Cy0LrQuCJ9LHsiTmFtZSI6InN1YnNjcmliZV90b19mYXZvcml0ZXNfZGlyZWN0aW9ucyIsIkRlc2NyaXB0aW9uIjoi0J/QvtC00L/QuNGB0LrQsCDQvdCwINC40LfQsdGA0LDQvdC90YvQtSDQvdCw0L/RgNCw0LLQu9C10L3QuNGPINGA0LXQudGB0L7QsiJ9LHsiTmFtZSI6InN3aXRjaF90b19kaWZmZXJlbnRfY29tcGFueV90eXBlIiwiRGVzY3JpcHRpb24iOiLQodC80LXQvdC40YLRjCDQuNC90YLQtdGA0YTQtdC50YEg0YEg0L7RgtC/0YDQsNCy0LjRgtC10LvRjyDQvdCwINC/0LXRgNC10LLQvtC30YfQuNC60LAg0Lgg0L7QsdGA0LDRgtC90L4ifSx7Ik5hbWUiOiJ2aWV3X2FncmVlZF9kZWxpdmVyaWVzX2NhcnJpZXIiLCJEZXNjcmlwdGlvbiI6ItCf0YDQvtGB0LzQvtGC0YAg0YHQvtCz0LvQsNGB0L7QstCw0L3QvdGL0YUg0YDQtdC50YHQvtCyINC/0LXRgNC10LLQvtC30YfQuNC60LAgKNCQ0YDRhdC40LIpIn0seyJOYW1lIjoidmlld19ib29rZWRfZGVsaXZlcmllc19jYXJyaWVyIiwiRGVzY3JpcHRpb24iOiLQn9GA0L7RgdC80L7RgtGAINC30LDQsdGA0L7QvdC40YDQvtCy0LDQvdC90YvRhSDRgNC10LnRgdC+0LIg0L/QtdGA0LXQstC+0LfRh9C40LrQsCJ9LHsiTmFtZSI6InZpZXdfY29tcGFueV9wYWdlIiwiRGVzY3JpcHRpb24iOiLQlNC+0YHRgtGD0L8g0L/QtdGA0LXQstC+0LfRh9C40LrQsCDQuiDRgNCw0LfQtNC10LvRgyDQnNC+0Y8g0LrQvtC80L/QsNC90LjRjyJ9LHsiTmFtZSI6InZpZXdfZnJlZV9kZWxpdmVyaWVzX2NhcnJpZXIiLCJEZXNjcmlwdGlvbiI6ItCf0YDQvtGB0LzQvtGC0YAg0YHQstC+0LHQvtC00L3Ri9GFINGA0LXQudGB0L7QsiDQv9C10YDQtdCy0L7Qt9GH0LjQutCwIn1dLCJjb21wYW55Ijp7Im5hbWUiOiLQnNCw0LrQsNGA0L7QsiDQmtC40YDQuNC70Lsg0JDQvdCw0YLQvtC70YzQtdCy0LjRhyIsInR5cGUiOiLQndC+0LLQsNGPINC60L7QvNC/0LDQvdC40Y8ifSwibm90aWZpY2F0aW9uc1NldHRpbmdzIjpbXSwidGVybXNPZlVzZSI6bnVsbCwicHJpdmFjeVBvbGljeSI6bnVsbCwiaXNUZWxlZ3JhbUF0dGFjaGVkIjpmYWxzZSwicnVsZXMiOnsiSXNDYW5Td2l0Y2hUeXBlIjpmYWxzZSwiSXNOZWVkQ3JlYXRlTGVnYWxFbnRpdHkiOnRydWV9LCJjb3VudHJ5Ijp7ImlkIjoxfX19"
    driver.get("https://azur.ru/olginka/o/14236")
    price_lists = driver.find_elements(By.CSS_SELECTOR, '.room-less-prices-table > tbody')
    print(len(price_lists))
    prices = []
    for list in price_lists:
        price = []
        rows = list.find_elements(By.CSS_SELECTOR, 'tr')
        print(len(rows))
        for row in rows:
            # rowTime =  row.find_element(By.CSS_SELECTOR, 'td').get_attribute('innerText') 
            # rowPrice =  row.find_element(By.CSS_SELECTOR, 'strong').get_attribute('innerText') 
            price.append([row.find_element(By.CSS_SELECTOR, 'td').get_attribute('innerText'), row.find_element(By.CSS_SELECTOR, 'strong').get_attribute('innerText')])
        # for tbody in list.find_elements(By.TAG_NAME, 'tbody'):
        prices.append(price)

    print(prices)
    # return prices
    with open("price.txt", "w") as my_file:
        my_file.write(json.dumps(prices))


schedule.every().hour.do(open_bot)

while True:
    schedule.run_pending()
    time.sleep(1)




# def job():    
#     print("I'm working...")    
   
# # schedule.every().day.at("08:00").do(job) 
# schedule.every().minute.at(":17").do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)


# def run_bot():
#     print('входящие данные===')
#     # print(input1.get())
#     print(input2.get())
#     print(input3.get())
#     print(variable.get())
#     print(variableTo.get())
    
#     print('================')
    
#     firefox_options = Options()
#     driver = webdriver.Firefox(executable_path="/geckodriver.exe", options = firefox_options)
#     driver.get("https://svetofore.com/deliveries/dashboard-deliveries")

#     driver.find_element(By.CLASS_NAME, 'head-login__link-login').click()
#     driver.find_element(By.ID, 'normal_login_login').send_keys(input_login.get())
#     sleep(0.5)
