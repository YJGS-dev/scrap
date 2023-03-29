from fastapi import FastAPI, Path
from scrap import (
    getWalmartHTML,
    getHTMLParser,
    getScrapWalmartCategoriesDespensa,
    getDriver,
    getTiendasJumboHTML,
    getHostWebSite,
    getScrapProductsTiendasJumbo
)

app = FastAPI()

@app.get("/api/walmart")
async def walmart():
    html = getWalmartHTML()
    soup_object = getHTMLParser(html)
    data = {
        "department": "Despensa",
        "url": "https://super.walmart.com.mx/",
        "categories": []
    }
    categories = getScrapWalmartCategoriesDespensa(soup_object)
    data["categories"] = categories
    return data


@app.get("/api/tiendas_jumbo/{url:path}")
async def tiendas_jumbo(url: str = Path(..., description="URL de la categoria del sitio")):
    url = url
    browser = getDriver()
    html = getTiendasJumboHTML(url, browser)
    website_host = getHostWebSite(browser)
    browser.close()
    data = {
        "url": website_host,
        "products": []
    }
    soup_object = getHTMLParser(html)
    products = getScrapProductsTiendasJumbo(soup_object, website_host)
    data["products"] = products
    return data
