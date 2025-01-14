import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from random import randint

from data import WEBSITE_LIST


USERS_USER_AGENT_DICT = {
        "firefox":r"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0",
        "edge":r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35",
        "chrome":r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"            
                        }

def create_chrome_driver(ublock:bool, headless:bool=True):
    ublock_path = os.getcwd()+"\\uBlock.crx"
    chrome_driver_path = os.getcwd()+"\\chrome\\chromedriver.exe"

    user_agent = USERS_USER_AGENT_DICT["chrome"]
    chrome_options = webdriver.ChromeOptions()
    if headless:chrome_options.add_argument("--headless")
    chrome_options.add_argument(f"user-agent={user_agent}")
    if ublock:
        chrome_options.add_extension(ublock_path)

    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    return driver

def create_firefox_driver(ublock:bool, headless:bool=True):
    ublock_path = os.getcwd()+"\\uBlock.xpi"
    firefox_driver_path = os.getcwd() + "\\ff\\geckodriver.exe"
    user_agent = USERS_USER_AGENT_DICT["firefox"]
    firefox_options = webdriver.FirefoxOptions()
    if headless:firefox_options.add_argument("--headless")
    firefox_options.add_argument(f"user-agent={user_agent}")
    if ublock:
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.add_extension(ublock_path)

    driver = webdriver.Firefox(executable_path=firefox_driver_path, options=firefox_options, firefox_profile=firefox_profile)
    return driver

def create_edge_driver(ublock:bool, headless:bool=True):
    ublock_path = os.getcwd()+"\\uBlock.crx"
    edge_driver_path = os.getcwd() + "\\edge\\msedgedriver.exe"
    user_agent = USERS_USER_AGENT_DICT['edge']
    edge_options = webdriver.EdgeOptions()
    if headless:edge_options.add_argument("--headless")
    edge_options.add_argument(f"user-agent={user_agent}")
    if ublock:
        edge_options.add_extension(ublock_path)
    driver = webdriver.Edge(executable_path=edge_driver_path, options=edge_options)
    return driver

def test_struct(website_url:str):
    website_data = WEBSITE_LIST.get(website_url)
    print(website_data.keys())
    main_menu = website_data.get("main_menu")
    if main_menu: print("MAIN MENU:",main_menu)
    specifics = website_data.get("specifics")
    if specifics:print("EXTRA DATA:", specifics)
    print("\nAll starting endpoints")
    endpoints = website_data.get("endpoints")
    for x in endpoints.keys():
        print(str(endpoints[x]).split(";"))

    sub_endpoints = website_data.get("sub-endpoints")
    for x in sub_endpoints.keys():
        print(sub_endpoints[x])
        print("xpaths")
        for y in sub_endpoints[x].keys():
            print(str(sub_endpoints[x][y]).split(";"))

    pass

# def test_xpath_list(website_url:str, xpath_list:list, driver):
#     driver.get(website_url)
#     time.sleep(3)
#     count = 0
#     for x_path in xpath_list:
#         print(count)
#         count+=1
#         input()
#         element = driver.find_element("xpath", x_path)
#         element.click()
#         time.sleep(2)

# def s_find_element(driver, type_find, identificaiton):
#     try:
#         return driver.find_element(type_find, identificaiton)
#     except:
#         return None

def retry_3times_relies_prev_multiple(driver, website_url, last_type_find, last_css, next_type_find, next_css):
    elements = None
    count = 0
    while elements == None and count < 3:
        count+=1
        try:
            #element = driver.find_elements(next_type_find, next_css)
            elements = better_find_element(driver,  website_url, next_css, next_type_find)
            return elements
        except: #attempt to refresh
            driver.refresh()
            #last_el = driver.find_elements(last_type_find, last_css)
            last_el = better_find_element(driver, website_url, last_css, last_type_find, False)
            last_el.click()
            time.sleep(2)
            #elements = driver.find_elements(next_type_find, next_css)
            elements = better_find_element(driver, website_url, next_css, next_type_find, True)
            return elements

def retry_3times_relies_prev_single(driver, website_url, last_type_find, last_css, next_type_find, next_css):
    element = None
    count = 0
    while element == None and count < 3:
        count+=1
        try:
            #element = driver.find_element(next_type_find, next_css)
            element = better_find_element(driver,  website_url, next_css, next_type_find)
            return element
        except: #attempt to refresh
            try:
                driver.refresh()
                time.sleep(2)
                #last_el = driver.find_element(last_type_find, last_css)
                last_el = better_find_element(driver, website_url, last_css, last_type_find, False)
                last_el.click()
                time.sleep(2)
                element = better_find_element(driver, website_url, next_css, next_type_find, False)
                #element = driver.find_element(next_type_find, next_css)
                return element
            except:
                pass

def better_find_element(driver, url, css, type_find, pural:bool=False):
    # if "p_" in type_find:
    #     pural = True
    # try: 
    #     if type_find[:1] == "p_":
    #         type_find = type_find.split("p_")
    # except:
    #     pass
    if pural:
        elements = driver.find_elements(type_find, css)
        return elements
    elif type_find == "direct-link":
        driver.get(url+"/"+css)
        return
    else:
        element = driver.find_element(type_find, css)
        return element

def test_ss_list(website_url:str, ss_list:list, driver):
    driver.get(website_url)
    time.sleep(5)
    #input()
    count = 0
    refresh_mem =[]
    for csss in ss_list:
        type_find, css = str(csss).split(";")
        #special = None
        special_list = [None]
        done_special = False
        try:
            special, type_find = type_find.split(":")
            special_list = special.split["~"]
        except:
            pass
        print(count)
        count+=1
        #input()
        print(type_find)
        if special: # specific indexed result
            if "refresh_sens" in special_list:
                refresh_mem.append((type_find, css))
            #if special[:3] == "ind_":
            if any("ind_" in string for string in special_list):
                done_special=True
                try:
                    #elements = driver.find_elements(type_find, css)
                    elements = better_find_element(driver, website_url, css, type_find, True)
                except:
                    if "relies_prev" in special_list:#check if in a state that requires to run last command
                        last_type_find, last_css = refresh_mem.pop()
                        elements = retry_3times_relies_prev_multiple(driver, website_url, last_type_find, last_css, type_find, css)
                    #elements = driver.find_elements(type_find, css)
                ind = int(special.split("ind_"))
                print(ind)
                element = elements[ind]
            if "rand_ind" in special_list: #randomly index result
                done_special=True
                try:
                    #elements = driver.find_elements(type_find, css)
                    elements = better_find_element(driver, website_url, css, type_find, pural=True)
                except:
                    if "relies_prev" in special_list:#check if in a state that requires to run last command
                        last_type_find, last_css = refresh_mem.pop()
                        elements = retry_3times_relies_prev_multiple(driver, website_url, last_type_find, last_css, type_find, css)

                rand_ind = randint(1,len(elements))-1
                element = elements[rand_ind]
        if not done_special:
            try:
                #element = driver.find_element(type_find, css)
                element = better_find_element(driver, website_url, css, type_find)
            except Exception as e: #attempt to refresh
                print(e)
                if "relies_prev" in special_list: #check if in a state that requires to run last command
                    last_type_find, last_css = refresh_mem.pop()
                    element = retry_3times_relies_prev_single(driver, website_url, last_type_find, last_css, type_find, css)
                    
        try:
            if type_find != "direct-link": 
                element.click()
        except:
            print("FAILED TO GET ELEMENT AFTER RETRIES")
            break
        time.sleep(2)
    input("OUT")

if __name__ == "__main__":
    #c_driver = create_edge_driver(ublock=True, headless=False)
    #c_driver = create_chrome_driver(ublock=True, headless=False)
    website_to_test = "https://www.youtube.com/"
    seleniumsselector_list = ["rand_ind:css selector;ytd-rich-item-renderer"] # "refresh_sens:id;guide-icon", "relies_prev:partial link text;Trending",
    #seleniumsselector_list = ["direct-link;signin", "partial link text;Create account"]
    #test_ss_list(website_to_test, seleniumsselector_list, c_driver)
    test_struct("https://www.youtube.com/")
    pass