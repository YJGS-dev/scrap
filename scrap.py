from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests


def getHTMLParser(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup

def getDriver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.headless = True

    chrome_options.add_experimental_option("prefs", prefs)
    myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return myDriver

def getTiendasJumboHTML(url, browser, interval = 0):
    browser.get(url)
    time.sleep(interval or 1)
    inner_height = getInnerHeightWebSite(browser)
    scrollbar_height = getScrollbarHeightWebSite(browser)
    loop = round(scrollbar_height / inner_height)
    for i in range(0, loop):
        browser.execute_script(f"window.scrollBy(0, {inner_height});")
        time.sleep(interval or 1)
    html = browser.page_source
    return html

def getHostWebSite(browser):
    host_site = browser.execute_script("return window.location.origin;")
    return host_site

def getInnerHeightWebSite(browser):
    inner_height = browser.execute_script("return window.innerHeight;")
    return inner_height

def getScrollbarHeightWebSite(browser):
    scrollbar_height = browser.execute_script(
        "return document.documentElement.scrollHeight - document.documentElement.clientHeight;")
    return scrollbar_height

def getScrapProductsTiendasJumbo(soup_object, website_host):
    articles = soup_object.select(".vtex-product-summary-2-x-container")
    products = []
    for element in articles:
        product = {}
        url = element.select_one(".vtex-product-summary-2-x-clearLink")
        if url: product["url"] = f'{website_host}{url.get("href")}'
        name = element.select_one(".vtex-product-summary-2-x-brandName")
        if name: product["name"] = name.text
        brand = element.select_one(".vtex-product-summary-2-x-productBrandName")
        if brand: product["brand"] = brand.text
        regular_price = element.select_one(".tiendasjumboqaio-jumbo-minicart-2-x-price")
        if regular_price: product["regular_price"] = regular_price.text.replace("$\u00a0", "")
        actual_price = element.select_one("#items-price > div > div")
        if actual_price: product["actual_price"] = actual_price.text.replace("$\u00a0", "")
        if product: products.append(product)
    return products

def getWalmartHTML():
    url = "https://super.walmart.com.mx/all-departments"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    response = requests.request("GET", url, headers=headers)
    return response.content

def getScrapWalmartCategoriesDespensa(soup_object):
    elements = soup_object.select('.w_C9 > div .flex')
    categories = []
    for div in elements:
        categorie = {}
        a_element = div.select_one('.ma0 > a')
        categorie["name"] = a_element.text
        if excludeCategorie(categorie["name"]):
            continue
        categorie["url"] = a_element.get("href")
        list_elements = div.select('.list > li')
        subcategories = []
        for element in list_elements:
            subcategorie = {}
            a_element = element.select_one('li > a')
            subcategorie["name"] = a_element.text
            subcategorie["url"] = a_element.get("href")
            subcategories.append(subcategorie)
        categorie["subcategories"] = subcategories
        categories.append(categorie)
    return categories

def excludeCategorie(categorie):
    categories_to_exclude = [
        "Juguetería y Deportes",
        "Ropa y Zapatería",
        "Artículos para el Hogar y autos",
        "Electrónica",
        "Higiene y Belleza",
        "Farmacia",
        "Bebés",
        "Mascotas"
    ]
    return True if categorie in categories_to_exclude else False