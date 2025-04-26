from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scraper import scrape_steam, scrape_epic
from model import GameSearchRequest

app = FastAPI()

# Permitir acceso desde frontend local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/search")
def search_games(request: GameSearchRequest):
    steam_prices = scrape_steam(request.name)
    epic_prices = scrape_epic(request.name)
    all_prices = steam_prices + epic_prices

    def extract_price(price):
        try:
            numbers = [float(p.replace(',', '.')) for p in price.replace('$','').split() if p.replace(',','.').replace('.','',1).isdigit()]
            return numbers[0] if numbers else 9999
        except:
            return 9999

    all_prices.sort(key=lambda x: extract_price(x['price']))
    return {
        "results": all_prices
    }
