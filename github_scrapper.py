from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

scrape = input("What page would you like to scrape? :")
cdp = "D:\\chromedriver\\chromedriver.exe" #specify your chrome driver
service = Service(executable_path=cdp)
driver = webdriver.Chrome(service=service)

driver.get(f"{scrape}")
repo = (f"{scrape}")
res = driver.find_elements(By.CLASS_NAME, "repo")

links = []
flink = []


def going_for_raw(second_page):
  # types__StyledButton-sc-ws60qy-0 hHvcfT
    driver.get(second_page)
    # github 'Raw' button class name is "hHvcfT" and may change in the future
    raw = driver.find_element(By.CLASS_NAME, "hHvcfT")
    raw.click()
    html = driver.page_source
    html = f"{html}"
    if "password" in html:
        print("found password " + second_page)
    else:
        print("no such keyword found")


def loop(next_page):
    global a
    driver.get(next_page)
    res2 = driver.find_elements(By.CLASS_NAME, "js-navigation-open")
    for a in res2:
        pass
        print(a.text)

    if "js" in a.text:
        print("------JS file found !!------")
        second_page = f"{next_page}/blob/main/{a.text}"
        print(second_page)
    elif "py" in a.text:
        # then access the second page / click it
        print("------py file found !!------")
        second_page = f"{next_page}/blob/main/{a.text}"
        going_for_raw(second_page)
        print(second_page)
        time.sleep(5)
    else:
        print("---- NO JS or PY files found----")


for i in res:
    links.append(i.text)
print(links)  # print all repository

for l in links:
    next_page = f"{repo}/{l}"
    flink.append(next_page)
    loop(next_page)
print(flink)


# driver.quit()
