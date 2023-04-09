from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re
import random
import csv 

# tkinter
from tkinter import messagebox, StringVar, OptionMenu
from tkinter import ttk

import tkinter as tk
from tkinter.filedialog import Open, SaveAs



xml_path = ''
csv_path = ''
driver = None


def parse(ev):
    if len(csv_path) != 0:
        # parser.main(xml_path, csv_path)
        run_bot()
        # messagebox.showinfo("Success", "Работа бота завершёна")
    else:
        messagebox.showerror("Error", "Укажите путь к csv")




def open_xlsx(ev):
    global csv_path
    csv_path = Open(window, filetypes=[('Excel files', '.csv')]).show()
    open_label['text'] = "Путь к CSV: "+csv_path



def start(ev):
    run_bot()

# def save_btn

window = tk.Tk()
window.geometry('600x400+200+100')
window.title("AXAS svetofore")



# save_label = tk.Label(
#     window, text="Путь к XML:"
# )
from_label =  tk.Label(
    window, text="откуда" 
)
weight_label =  tk.Label(
    window, text="вес" 
)
volume_label =  tk.Label(
    window, text="объем" 
)


open_label = tk.Label(
    window, text="Путь к exel:" 
)

parse_btn = tk.Button(
    window, text='Открыть'
)

search_btn = tk.Button(
    window, text='Старт'
)

save_btn = tk.Button(
    window, text="Указать",
)

login_label =  tk.Label(
    window, text="логин" 
)

password_label =  tk.Label(
    window, text="пароль" 
)
# open_btn = tk.Button(
#     window, text="Изменить"
# )

# open_btn.bind('<Button-1>', open_xlsx)
save_btn.bind('<Button-1>', open_xlsx)
parse_btn.bind('<Button-1>', parse)
search_btn.bind('<Button-1>', start)

input_login = tk.ttk.Entry(driver, textvariable="login")
input_login.insert(0, '9186842677')

# 9282742012
input_password = tk.ttk.Entry()
input_password.insert(0, '1c0gx8')
# 2uvas9
input1 = tk.ttk.Entry()
input2 = tk.ttk.Entry()
input3 = tk.ttk.Entry()


login_label.pack(anchor="s",  pady=1)
input_login.pack( padx=4, pady= 3)

password_label.pack(anchor="n",  pady=(5, 0))
input_password.pack( padx=4, pady= (3, 30))

#select
variable = StringVar(window)
variable.set("откуда") # default value

w = OptionMenu(window, variable,
'Алтайский край',
'Амурская область',
'Башкортостан',
'Брестская область',
'Брянская область',
'Волгоградская область',
'Вологодская область',
'Воронежская область',
'Западно-Казахстанская область',
'Иркутская область',
'Калужская область',
'Кемеровская область',
'Кировская область',
'Костромская область',
'Краснодарский край',
'Красноярский край',
'Курганская область',
'Ленинградская область',
'Минская область',
'Московская область',
'Мурманская область',
'Нижегородская область',
'Новосибирская область',
'Омская область',
'Оренбургская область',
'Пензенская область',
'Пермский край',
'Приморский край',
'Респу́блика Тыва́',
'Республика Карелия',
'Республика Мордовия',
'Республика Татарстан',
'Ростовская область',
'Самарская область',
'Свердловская область',
'Северо-Казахстанская область',
'Ставропольский край',
'Тверская область',
'Томская область',
'Тульская область',
'Туркестанская область',
'Тюменская область',
'Ульяновская область',
'Хабаровский край',
'Ханты-мансийский Ао',
'Челябинская область',
'Ямало-Ненецкий Ао',
'Ярославская область',
)
w.pack()

variableTo = StringVar(window)
variableTo.set("куда") # default value

w_to = OptionMenu(window, variableTo,
'Абайская область',
'Акмолинская область',
'Актюбинская область',
'Алматинская область',
'Алтайский край',
'Амурская область',
'Андижанская область',
'Архангельская область',
'Астана',
'Астраханская область',
'Башкортостан',
'Белгородская народная республика',
'Белгородская область',
'Брестская область',
'Брянская область',
'Витебская область',
'Владимирская область',
'Волгоградская область',
'Вологодская область',
'Воронежская область',
'Восточно-Казахстанская область',
'Гомельская область',
'Гродненская область',
'Дагестан',
'Еврейская автономная область',
'Жамбылская область',
'Жетысуская область',
'Забайкальский край',
'Западно-Казахстанская область',
'Ивановская область',
'Иркутская область',
'Кабардино-Балкарская Республика',
'Калининградская область',
'Калужская область',
'Камчатский край',
'Карагандинская область',
'Карачаево-Черкесская Республика',
'Кемеровская область',
'Кировская область',
'Костанайская область',
'Костромская область',
'Краснодарский край',
'Красноярский край',
'Курганская область',
'Курская область',
'Ленинградская область',
'Липецкая область',
'Магаданская область',
'Мангистауская область',
'Минская область',
'Могилёвская область',
'Московская область',
'Мурманская область',
'Ненецкий автономный округ',
'Нижегородская область',
'Новгородская область',
'Новосибирская область',
'Омская область',
'Оренбургская область',
'Орловская область',
'Павлодарская область',
'Пензенская область',
'Пермский край',
'Приморский край',
'Псковская область',
'Респу́блика Тыва́',
'Республика Адыгея',
'Республика Алтай',
'Республика Бурятия',
'Республика Ингушетия',
'Республика Калмыкия',
'Республика Карелия',
'Республика Коми',
'Республика Марий Эл',
'Республика Мордовия',
'Республика Саха (Якутия)',
'Республика Татарстан',
'Республика Хакасия',
'Ростовская область',
'Рязанская область',
'Самарская область',
'Саратовская область',
'Сахалинская область',
'Свердловская область',
'Северная Осетия — Алания',
'Северо-Казахстанская область',
'Смоленская область',
'Ставропольский край',
'Тамбовская область',
'Тверская область',
'Томская область',
'Тульская область',
'Туркестанская область',
'Тюменская область',
'Удмуртская Республика',
'Улытауская область',
'Ульяновская область',
'Хабаровский край',
'Ханты-мансийский Ао',
'Челябинская область',
'Чеченская Республика',
'Чувашская Республика',
'Шымкент',
'Ямало-Ненецкий Ао',
'Ярославская область',
)
w_to.pack()

# from_label.pack(anchor="n",  pady=5)
# input1.pack( padx=8, pady= 8)



volume_label.pack(anchor="n",  pady=5)
input2.pack( padx=8, pady= 8)

weight_label.pack(anchor="n",  pady=5)
input3.pack( padx=8, pady= 8)

search_btn.pack( padx=8, pady= 8)


# open_label.pack(anchor="n",  pady=5)
# # open_label.grid(column=0, row=0)
# # open_btn.grid(column=1, row=0)
# # save_label.grid(column=0, row=1)

# save_btn.pack(anchor="n")
# parse_btn.pack(anchor="n",  pady=15)
# search_btn.pack(anchor="n",  pady=15)

# driver = webdriver.Chrome('/yandexdriver.exe')
# driver = webdriver.Chrome(executable_path="/chromedriver.exe")
# firefox_options.set_capability("acceptInsecureCerts", True)
# firefox_options.add_argument("--headless")
# driver.execute_script("window.localStorage.setItem('user_auth_v2','eyJsb2dnZWRJbiI6dHJ1ZSwiYXV0aCI6eyJ0b2tlbl90eXBlIjoiQmVhcmVyIiwiZXhwaXJlc19pbiI6MTIwOTYwMCwiYWNjZXNzX3Rva2VuIjoiOGQ5MzU5M2RlZmNkMTM2ODZhNGUzZGViZDdkYWUyNTdlZjlmNTU2ZTU1MDdmZDkzZDg1YjAxYjYwYmU5ZGE0ZWU4NmI4Y2YzNmU2ZmI0ZDciLCJyZWZyZXNoX3Rva2VuIjoiYzlmNWRhZjJhMDZlNDEwZmE4Y2Q1ZTlkNDQ4YTQ4MDZhYjEwNWU1YjIxY2ZmMzgzODc5YTU3MmI5MmY4YmQ1NDE0NDdkZWNlZDAzNTAyOWIifSwiaW5mbyI6eyJpZCI6MTAxNjEyLCJmaW8iOiLQnNCw0LrQsNGA0L7QsiDQmtC40YDQuNC70Lsg0JDQvdCw0YLQvtC70YzQtdCy0LjRhyIsImxvZ2luIjoiOTI4Mjc0MjAxMiIsInJvbGUiOiJjYXJyaWVyX293bmVyIiwicm9sZU5hbWUiOiLQn9C10YDQtdCy0L7Qt9GH0LjQuiIsInVzZXJUeXBlIjoiY2FycmllciIsImlzU3RhZmYiOmZhbHNlLCJwZXJtaXNzaW9ucyI6W3siTmFtZSI6ImFjY2Vzc190b19jYXJyaWVyX2NvbXBhbmllcyIsIkRlc2NyaXB0aW9uIjoi0JTQvtGB0YLRg9C/INC6INC60L7QvNC/0LDQvdC40Y/QvCJ9LHsiTmFtZSI6ImNvbXBhbnlfZGlyZWN0b3JfcGVybWlzc2lvbiIsIkRlc2NyaXB0aW9uIjoi0J7RgdC90L7QstC90YvQtSDQv9GA0LDQstCwINC00LjRgNC10LrRgtC+0YDQsCDQutC+0LzQv9Cw0L3QuNC4INC/0LXRgNC10LLQvtC30YfQuNC60LAifSx7Ik5hbWUiOiJjcmVhdGVfYW5kX2VkaXRfZHJpdmVyIiwiRGVzY3JpcHRpb24iOiLQodC+0LfQtNCw0L3QuNC1INC4INGA0LXQtNCw0LrRgtC40YDQvtCy0LDQvdC40LUg0LLQvtC00LjRgtC10LvRjyJ9LHsiTmFtZSI6ImNyZWF0ZV9hbmRfZWRpdF90cmFpbCIsIkRlc2NyaXB0aW9uIjoi0KHQvtC30LTQsNC90LjQtSDQuCDRgNC10LTQsNC60YLQuNGA0L7QstCw0L3QuNC1INC/0YDQuNGG0LXQv9CwIn0seyJOYW1lIjoiY3JlYXRlX2FuZF9lZGl0X3RydWNrIiwiRGVzY3JpcHRpb24iOiLQodC+0LfQtNCw0L3QuNC1INC4INGA0LXQtNCw0LrRgtC40YDQvtCy0LDQvdC40LUg0LDQstGC0L4ifSx7Ik5hbWUiOiJjcmVhdGVfYW5kX2ZpbGxlZF9vcmRlciIsIkRlc2NyaXB0aW9uIjoi0KHQvtC30LTQsNC90LjQtSDQuCDQt9Cw0L/QvtC70L3QtdC90LjQtSDQt9Cw0Y/QstC60LggKNCf0YDQuNC60YDQtdC/0LvQtdC90LjQtSDQstC+0LTQuNGC0LXQu9GPINC4INC00L7QutGD0LzQtdC90YLQvtCyKSJ9LHsiTmFtZSI6ImNyZWF0ZV9jb21wYW55X3BlcnNvbiIsIkRlc2NyaXB0aW9uIjoi0KHQvtC30LTQsNC90LjQtSDQvtGC0LLQtdGC0YHRgtCy0LXQvdC90YvRhSDQv9C10YDQtdCy0L7Qt9GH0LjQutCwIn0seyJOYW1lIjoiY3JlYXRlX2xlZ2FsX2VudGl0eSIsIkRlc2NyaXB0aW9uIjoi0KHQvtC30LTQsNC90LjQtSDRjtGALiDQu9C40YYg0LIg0LrQvtC80L/QsNC90LjQuCDQv9C10YDQtdCy0L7Qt9GH0LjQutCwIn0seyJOYW1lIjoiZGlzcGxheV9kZWxpdmVyaWVzX3dpdGhvdXRfZGVsYXkiLCJEZXNjcmlwdGlvbiI6ItCe0YLQvtCx0YDQsNC20LXQvdC40LUg0YDQtdC50YHQvtCyINCx0LXQtyDQt9Cw0LTQtdGA0LbQutC4In0seyJOYW1lIjoiZHJpdmVyX3Blcm1pc3Npb24iLCJEZXNjcmlwdGlvbiI6ItCf0YDQsNCy0LAg0LTQu9GPINC/0L7Qu9GM0LfQvtCy0LDRgtC10LvRjy3QstC+0LTQuNGC0LXQu9GPIn0seyJOYW1lIjoicmVmdXNlX29yZGVyIiwiRGVzY3JpcHRpb24iOiLQntGC0LzQtdC90LAg0YHQvtCx0YHRgtCy0LXQvdC90YvRhSDQt9Cw0Y/QstC+0LoifSx7Ik5hbWUiOiJyZW1vdmluZ19zcGVjX2Zvcl9hbmFsb2dfb3JkZXJzX293bmVyX29mX2FwcHJvdmVkIiwiRGVzY3JpcHRpb24iOiLQodC90Y/RgtC40LUg0L/RgNC+0LLQtdGA0LrQuCDQvdCwINCw0L3QsNC70L7Qs9C40YfQvdGL0LUg0LfQsNC60LDQt9GLINC+0YIg0YHQvtCx0YHRgtCy0LXQvdC90LjQutCwINC/0YDQuCDRg9GC0LLQtdGA0LbQtNC10L3QuNC4INC30LDRj9Cy0LrQuCJ9LHsiTmFtZSI6InN1YnNjcmliZV90b19mYXZvcml0ZXNfZGlyZWN0aW9ucyIsIkRlc2NyaXB0aW9uIjoi0J/QvtC00L/QuNGB0LrQsCDQvdCwINC40LfQsdGA0LDQvdC90YvQtSDQvdCw0L/RgNCw0LLQu9C10L3QuNGPINGA0LXQudGB0L7QsiJ9LHsiTmFtZSI6InN3aXRjaF90b19kaWZmZXJlbnRfY29tcGFueV90eXBlIiwiRGVzY3JpcHRpb24iOiLQodC80LXQvdC40YLRjCDQuNC90YLQtdGA0YTQtdC50YEg0YEg0L7RgtC/0YDQsNCy0LjRgtC10LvRjyDQvdCwINC/0LXRgNC10LLQvtC30YfQuNC60LAg0Lgg0L7QsdGA0LDRgtC90L4ifSx7Ik5hbWUiOiJ2aWV3X2FncmVlZF9kZWxpdmVyaWVzX2NhcnJpZXIiLCJEZXNjcmlwdGlvbiI6ItCf0YDQvtGB0LzQvtGC0YAg0YHQvtCz0LvQsNGB0L7QstCw0L3QvdGL0YUg0YDQtdC50YHQvtCyINC/0LXRgNC10LLQvtC30YfQuNC60LAgKNCQ0YDRhdC40LIpIn0seyJOYW1lIjoidmlld19ib29rZWRfZGVsaXZlcmllc19jYXJyaWVyIiwiRGVzY3JpcHRpb24iOiLQn9GA0L7RgdC80L7RgtGAINC30LDQsdGA0L7QvdC40YDQvtCy0LDQvdC90YvRhSDRgNC10LnRgdC+0LIg0L/QtdGA0LXQstC+0LfRh9C40LrQsCJ9LHsiTmFtZSI6InZpZXdfY29tcGFueV9wYWdlIiwiRGVzY3JpcHRpb24iOiLQlNC+0YHRgtGD0L8g0L/QtdGA0LXQstC+0LfRh9C40LrQsCDQuiDRgNCw0LfQtNC10LvRgyDQnNC+0Y8g0LrQvtC80L/QsNC90LjRjyJ9LHsiTmFtZSI6InZpZXdfZnJlZV9kZWxpdmVyaWVzX2NhcnJpZXIiLCJEZXNjcmlwdGlvbiI6ItCf0YDQvtGB0LzQvtGC0YAg0YHQstC+0LHQvtC00L3Ri9GFINGA0LXQudGB0L7QsiDQv9C10YDQtdCy0L7Qt9GH0LjQutCwIn1dLCJjb21wYW55Ijp7Im5hbWUiOiLQnNCw0LrQsNGA0L7QsiDQmtC40YDQuNC70Lsg0JDQvdCw0YLQvtC70YzQtdCy0LjRhyIsInR5cGUiOiLQndC+0LLQsNGPINC60L7QvNC/0LDQvdC40Y8ifSwibm90aWZpY2F0aW9uc1NldHRpbmdzIjpbXSwidGVybXNPZlVzZSI6bnVsbCwicHJpdmFjeVBvbGljeSI6bnVsbCwiaXNUZWxlZ3JhbUF0dGFjaGVkIjpmYWxzZSwicnVsZXMiOnsiSXNDYW5Td2l0Y2hUeXBlIjpmYWxzZSwiSXNOZWVkQ3JlYXRlTGVnYWxFbnRpdHkiOnRydWV9LCJjb3VudHJ5Ijp7ImlkIjoxfX19');")
# driver.execute_script("return localStorage.getItem('user_auth_v2')")


def open_bot():
    global driver
    # profile = webdriver.FirefoxProfile()
    # profile.set_preference("general.useragent.override", "whatever you want")
    driver = webdriver.Firefox(executable_path="/geckodriver.exe")
    # driver = webdriver.Chrome('/yandexdriver.exe')
    # driver = webdriver.Chrome(executable_path="/chromedriver.exe")
    firefox_options = Options()
    # user_auth_v2:"eyJsb2dnZWRJbiI6dHJ1ZSwiYXV0aCI6eyJ0b2tlbl90eXBlIjoiQmVhcmVyIiwiZXhwaXJlc19pbiI6MTIwOTYwMCwiYWNjZXNzX3Rva2VuIjoiOGQ5MzU5M2RlZmNkMTM2ODZhNGUzZGViZDdkYWUyNTdlZjlmNTU2ZTU1MDdmZDkzZDg1YjAxYjYwYmU5ZGE0ZWU4NmI4Y2YzNmU2ZmI0ZDciLCJyZWZyZXNoX3Rva2VuIjoiYzlmNWRhZjJhMDZlNDEwZmE4Y2Q1ZTlkNDQ4YTQ4MDZhYjEwNWU1YjIxY2ZmMzgzODc5YTU3MmI5MmY4YmQ1NDE0NDdkZWNlZDAzNTAyOWIifSwiaW5mbyI6eyJpZCI6MTAxNjEyLCJmaW8iOiLQnNCw0LrQsNGA0L7QsiDQmtC40YDQuNC70Lsg0JDQvdCw0YLQvtC70YzQtdCy0LjRhyIsImxvZ2luIjoiOTI4Mjc0MjAxMiIsInJvbGUiOiJjYXJyaWVyX293bmVyIiwicm9sZU5hbWUiOiLQn9C10YDQtdCy0L7Qt9GH0LjQuiIsInVzZXJUeXBlIjoiY2FycmllciIsImlzU3RhZmYiOmZhbHNlLCJwZXJtaXNzaW9ucyI6W3siTmFtZSI6ImFjY2Vzc190b19jYXJyaWVyX2NvbXBhbmllcyIsIkRlc2NyaXB0aW9uIjoi0JTQvtGB0YLRg9C/INC6INC60L7QvNC/0LDQvdC40Y/QvCJ9LHsiTmFtZSI6ImNvbXBhbnlfZGlyZWN0b3JfcGVybWlzc2lvbiIsIkRlc2NyaXB0aW9uIjoi0J7RgdC90L7QstC90YvQtSDQv9GA0LDQstCwINC00LjRgNC10LrRgtC+0YDQsCDQutC+0LzQv9Cw0L3QuNC4INC/0LXRgNC10LLQvtC30YfQuNC60LAifSx7Ik5hbWUiOiJjcmVhdGVfYW5kX2VkaXRfZHJpdmVyIiwiRGVzY3JpcHRpb24iOiLQodC+0LfQtNCw0L3QuNC1INC4INGA0LXQtNCw0LrRgtC40YDQvtCy0LDQvdC40LUg0LLQvtC00LjRgtC10LvRjyJ9LHsiTmFtZSI6ImNyZWF0ZV9hbmRfZWRpdF90cmFpbCIsIkRlc2NyaXB0aW9uIjoi0KHQvtC30LTQsNC90LjQtSDQuCDRgNC10LTQsNC60YLQuNGA0L7QstCw0L3QuNC1INC/0YDQuNGG0LXQv9CwIn0seyJOYW1lIjoiY3JlYXRlX2FuZF9lZGl0X3RydWNrIiwiRGVzY3JpcHRpb24iOiLQodC+0LfQtNCw0L3QuNC1INC4INGA0LXQtNCw0LrRgtC40YDQvtCy0LDQvdC40LUg0LDQstGC0L4ifSx7Ik5hbWUiOiJjcmVhdGVfYW5kX2ZpbGxlZF9vcmRlciIsIkRlc2NyaXB0aW9uIjoi0KHQvtC30LTQsNC90LjQtSDQuCDQt9Cw0L/QvtC70L3QtdC90LjQtSDQt9Cw0Y/QstC60LggKNCf0YDQuNC60YDQtdC/0LvQtdC90LjQtSDQstC+0LTQuNGC0LXQu9GPINC4INC00L7QutGD0LzQtdC90YLQvtCyKSJ9LHsiTmFtZSI6ImNyZWF0ZV9jb21wYW55X3BlcnNvbiIsIkRlc2NyaXB0aW9uIjoi0KHQvtC30LTQsNC90LjQtSDQvtGC0LLQtdGC0YHRgtCy0LXQvdC90YvRhSDQv9C10YDQtdCy0L7Qt9GH0LjQutCwIn0seyJOYW1lIjoiY3JlYXRlX2xlZ2FsX2VudGl0eSIsIkRlc2NyaXB0aW9uIjoi0KHQvtC30LTQsNC90LjQtSDRjtGALiDQu9C40YYg0LIg0LrQvtC80L/QsNC90LjQuCDQv9C10YDQtdCy0L7Qt9GH0LjQutCwIn0seyJOYW1lIjoiZGlzcGxheV9kZWxpdmVyaWVzX3dpdGhvdXRfZGVsYXkiLCJEZXNjcmlwdGlvbiI6ItCe0YLQvtCx0YDQsNC20LXQvdC40LUg0YDQtdC50YHQvtCyINCx0LXQtyDQt9Cw0LTQtdGA0LbQutC4In0seyJOYW1lIjoiZHJpdmVyX3Blcm1pc3Npb24iLCJEZXNjcmlwdGlvbiI6ItCf0YDQsNCy0LAg0LTQu9GPINC/0L7Qu9GM0LfQvtCy0LDRgtC10LvRjy3QstC+0LTQuNGC0LXQu9GPIn0seyJOYW1lIjoicmVmdXNlX29yZGVyIiwiRGVzY3JpcHRpb24iOiLQntGC0LzQtdC90LAg0YHQvtCx0YHRgtCy0LXQvdC90YvRhSDQt9Cw0Y/QstC+0LoifSx7Ik5hbWUiOiJyZW1vdmluZ19zcGVjX2Zvcl9hbmFsb2dfb3JkZXJzX293bmVyX29mX2FwcHJvdmVkIiwiRGVzY3JpcHRpb24iOiLQodC90Y/RgtC40LUg0L/RgNC+0LLQtdGA0LrQuCDQvdCwINCw0L3QsNC70L7Qs9C40YfQvdGL0LUg0LfQsNC60LDQt9GLINC+0YIg0YHQvtCx0YHRgtCy0LXQvdC90LjQutCwINC/0YDQuCDRg9GC0LLQtdGA0LbQtNC10L3QuNC4INC30LDRj9Cy0LrQuCJ9LHsiTmFtZSI6InN1YnNjcmliZV90b19mYXZvcml0ZXNfZGlyZWN0aW9ucyIsIkRlc2NyaXB0aW9uIjoi0J/QvtC00L/QuNGB0LrQsCDQvdCwINC40LfQsdGA0LDQvdC90YvQtSDQvdCw0L/RgNCw0LLQu9C10L3QuNGPINGA0LXQudGB0L7QsiJ9LHsiTmFtZSI6InN3aXRjaF90b19kaWZmZXJlbnRfY29tcGFueV90eXBlIiwiRGVzY3JpcHRpb24iOiLQodC80LXQvdC40YLRjCDQuNC90YLQtdGA0YTQtdC50YEg0YEg0L7RgtC/0YDQsNCy0LjRgtC10LvRjyDQvdCwINC/0LXRgNC10LLQvtC30YfQuNC60LAg0Lgg0L7QsdGA0LDRgtC90L4ifSx7Ik5hbWUiOiJ2aWV3X2FncmVlZF9kZWxpdmVyaWVzX2NhcnJpZXIiLCJEZXNjcmlwdGlvbiI6ItCf0YDQvtGB0LzQvtGC0YAg0YHQvtCz0LvQsNGB0L7QstCw0L3QvdGL0YUg0YDQtdC50YHQvtCyINC/0LXRgNC10LLQvtC30YfQuNC60LAgKNCQ0YDRhdC40LIpIn0seyJOYW1lIjoidmlld19ib29rZWRfZGVsaXZlcmllc19jYXJyaWVyIiwiRGVzY3JpcHRpb24iOiLQn9GA0L7RgdC80L7RgtGAINC30LDQsdGA0L7QvdC40YDQvtCy0LDQvdC90YvRhSDRgNC10LnRgdC+0LIg0L/QtdGA0LXQstC+0LfRh9C40LrQsCJ9LHsiTmFtZSI6InZpZXdfY29tcGFueV9wYWdlIiwiRGVzY3JpcHRpb24iOiLQlNC+0YHRgtGD0L8g0L/QtdGA0LXQstC+0LfRh9C40LrQsCDQuiDRgNCw0LfQtNC10LvRgyDQnNC+0Y8g0LrQvtC80L/QsNC90LjRjyJ9LHsiTmFtZSI6InZpZXdfZnJlZV9kZWxpdmVyaWVzX2NhcnJpZXIiLCJEZXNjcmlwdGlvbiI6ItCf0YDQvtGB0LzQvtGC0YAg0YHQstC+0LHQvtC00L3Ri9GFINGA0LXQudGB0L7QsiDQv9C10YDQtdCy0L7Qt9GH0LjQutCwIn1dLCJjb21wYW55Ijp7Im5hbWUiOiLQnNCw0LrQsNGA0L7QsiDQmtC40YDQuNC70Lsg0JDQvdCw0YLQvtC70YzQtdCy0LjRhyIsInR5cGUiOiLQndC+0LLQsNGPINC60L7QvNC/0LDQvdC40Y8ifSwibm90aWZpY2F0aW9uc1NldHRpbmdzIjpbXSwidGVybXNPZlVzZSI6bnVsbCwicHJpdmFjeVBvbGljeSI6bnVsbCwiaXNUZWxlZ3JhbUF0dGFjaGVkIjpmYWxzZSwicnVsZXMiOnsiSXNDYW5Td2l0Y2hUeXBlIjpmYWxzZSwiSXNOZWVkQ3JlYXRlTGVnYWxFbnRpdHkiOnRydWV9LCJjb3VudHJ5Ijp7ImlkIjoxfX19"
    driver.get("https://svetofore.com/deliveries/dashboard-deliveries")



def run_bot():
    print('входящие данные===')
    # print(input1.get())
    print(input2.get())
    print(input3.get())
    print(variable.get())
    print(variableTo.get())
    
    print('================')
    
    firefox_options = Options()
    driver = webdriver.Firefox(executable_path="/geckodriver.exe", options = firefox_options)
    driver.get("https://svetofore.com/deliveries/dashboard-deliveries")

    driver.find_element(By.CLASS_NAME, 'head-login__link-login').click()
    driver.find_element(By.ID, 'normal_login_login').send_keys(input_login.get())
    sleep(0.5)
    driver.find_element(By.ID, 'normal_login_password').send_keys(input_password.get())
    sleep(0.5)
    driver.find_element(By.CLASS_NAME, 'login-form-button').click()
    sleep(0.5)
    searching_cross = True
    counter1 = 0
    while searching_cross:
            counter1 += 1
            try:
                driver.find_element(By.CLASS_NAME, 'ant-modal-close').click()
                searching_cross = False
            except:
                if counter1 > 2:
                    searching_cross = False 
                sleep(0.5)
        
    # sleep(9)
    # driver.get("https://svetofore.com/deliveries/list-new")
    # driver.find_element(By.CLASS_NAME, 'ant-modal-close').click()
    sleep(3)
    # select_from = driver.find_elements(By.CLASS_NAME, 'ant-select-show-arrow')
    select_from = driver.find_elements(By.CSS_SELECTOR, '.ant-select.ant-select-enabled')
    print('len of: ', len(select_from))
    searching_select_form = True
    while searching_select_form:
        select_from = driver.find_elements(By.CSS_SELECTOR, '.ant-select.ant-select-enabled')
        if(len(select_from) > 0):
            searching_select_form = False
        sleep(1)
            
    print(len(select_from))
    
    select_from[0].click()
    print(w)
    variantsWrap = driver.find_element(By.CLASS_NAME, 'ant-select-dropdown-menu')
    variants = variantsWrap.find_elements(By.CLASS_NAME, 'ant-select-dropdown-menu-item') 
    for i in variants:
        # print(i.get_attribute('innerText'))
        if(i.get_attribute('innerText') == variable.get()):
            i.click()
    print('=========================')

    select_from[1].click()
    variantsWrapTo = driver.find_elements(By.CLASS_NAME, 'ant-select-dropdown-menu')
    variantsTo = variantsWrapTo[1].find_elements(By.CLASS_NAME, 'ant-select-dropdown-menu-item') 
    for i in variantsTo:
        # print(i.get_attribute('innerText'))
        if(i.get_attribute('innerText') == variableTo.get()):
            i.click()

    

    
    # test_el = driver.find_element(By.CLASS_NAME, "start__btn")
    # # email_form = driver.find_element_by_id("testing_form")
    # print('----')
    # print(test_el.get_attribute('innerHTML'))
    # print()

    # print('click')
    # test_el.click()

    # input_el = driver.find_element(By.CLASS_NAME, "modal__pu_input")

    # input_el.send_keys("SMEDLY.com")
    error_counter = 0
    counter_main_loop = 0
    while True:
        counter_main_loop += 1
        # print(1/0)
        # searching_cross = True
        # counter = 0
        # while searching_cross:
        #     counter += 1
        #     try:
        #         driver.find_element(By.CLASS_NAME, 'ant-modal-close').click()
        #         searching_cross = False
        #     except:
        #         if counter > 1:
        #             searching_cross = False 
        #         sleep(1)
        if counter_main_loop != 1:
            select_from[2].click()
            variantsWrapTo = driver.find_elements(By.CLASS_NAME, 'ant-select-dropdown-menu')
            variantsTo = variantsWrapTo[2].find_elements(By.CLASS_NAME, 'ant-select-dropdown-menu-item')

            if counter_main_loop % 2 == 0: # меняем опцию для поля сортировки каждую новую итерацию
                 text_option = 'Сначала новые'
            else:
                text_option = 'По умолчанию'

            for i in variantsTo:  # находим нужную опцию
                print(i.get_attribute('innerText'))
                if(i.get_attribute('innerText') == text_option):
                    i.click() 



        searching_submit = True
        while searching_submit: # нажимаем на кнопку принять
            try:
                submit = driver.find_element(By.CSS_SELECTOR, '.ant-btn.filters-button.ant-btn-primary.ant-btn-icon-only') 
                print(submit)
                submit.click()
                print('click submit success')
                searching_submit = False
            except:
                print('click submit error')
                sleep(0.5)
        sleep(1)

        
        body = driver.find_element(By.TAG_NAME, "body")
        # driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_UP(Keys.CONTROL, "+"))
        # list =
        
        body.click()
        searchOffers = True
        counterSearchOffers = 0
        el_offers = None
        while searchOffers:
            counterSearchOffers += 1
            if(counterSearchOffers > 100):
                searchOffers = False
            offers_wrap = driver.find_elements(By.CLASS_NAME, "application-block")
            if(len(offers_wrap)<1):
                print('предполагаем пустой список')
                sleep(0.5)
                continue
            # el_cities = driver.find_elements(By.CLASS_NAME, "citi-name")
            
            el_offers = offers_wrap[1].find_elements(By.CLASS_NAME, "ant-spin-nested-loading")
            print('количество рейсов: ', len(el_offers))
            if(len(el_offers) > 0):
                print('дождались рейсов: ', len(el_offers))
                searchOffers = False
            else:
                sleep(0.5)
                continue
            sleep(0.5)
            
        while True:
            infs = None
            request_button = None
            city = None
            try:
                for idx, offer in enumerate(el_offers):
                    infs = offer.find_elements(By.CLASS_NAME, "inf")
                    request_button = offer.find_element(By.CLASS_NAME, "action-button")
                    city = offer.find_element(By.CLASS_NAME, "citi-name").get_attribute("innerText")

                    pattern = r'\d+\.?\d*'
                    # user = '123,3'
                    volume_reg = re.search(pattern, infs[0].get_attribute("innerText"))
                    volume = volume_reg.group(0)

                    weight_reg = re.search(pattern, infs[1].get_attribute("innerText"))
                    weight = weight_reg.group(0)
                    # print(city, volume, weight)
                    # if (float(weight) <= float(input3.get())) and (float(volume) <= float(input2.get())) and (city == input1.get()):
                    if (float(weight) <= float(input3.get())) and (float(volume) <= float(input2.get())):
                        print("Нашел=============================================================================================")
                        request_button.click()
                        sleep(0.5)
                        cross_el = driver.find_element(By.CLASS_NAME, "ant-modal-close")
                        print(cross_el)
                        success_try = False
                        searching_cross = True
                        try:
                            search_finally = True
                            while search_finally:
                                try:
                                    submit_offer = driver.find_elements(By.CSS_SELECTOR, "button.ant-btn.ant-btn-primary")
                                    print(submit_offer)
                                    submit_offer[-1].click()
                                    success_try = True
                                    search_finally = False
                                except:
                                    print('не получилось нажать финальную кнопку')
                                    sleep(1)
                                    
                                
                            
                        except:
                            print('не удалось найти кнопку')
                        if success_try:
                            print('удалось найти кнопку')
                            print(1/0)
                        while searching_cross:
                            try:
                                # driver.find_element(By.CSS_SELECTOR, ' .modal-window .ant-modal-content .ant-modal-close').click()
                                driver.find_elements(By.CSS_SELECTOR, '.modal-window .ant-modal-content .ant-modal-close')[-1].click()
                                print('success click on cross')
                                print(len(driver.find_elements(By.CSS_SELECTOR, ' .modal-window .ant-modal-content .ant-modal-close')))
                                searching_cross = False
                            except:
                                print(len(driver.find_elements(By.CSS_SELECTOR, ' .modal-window .ant-modal-content .ant-modal-close')))
                                print('error click on cross')
                                # driver.find_elements(By.CSS_SELECTOR, '.modal-window .ant-modal-content .ant-modal-close')[-1].click()
                                # searching_cross = False
                                sleep(1)
                break
                
            except: 
                print('споткнулись!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                error_counter += 1
                sleep(1)
        print('end', error_counter, counter_main_loop)
        print('конец итерации')
        # driver.refresh()


    def scrollDown():
        # body.click()
        print('scrollDown')
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()

    def scrollUp():
        try:
            ActionChains(driver).send_keys(Keys.PAGE_UP).perform()
        except():
            print('error page_up')


   
    # driver.close()
    
    # run_bot()


window.mainloop()