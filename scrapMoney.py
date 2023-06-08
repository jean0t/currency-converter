from requests import get
from bs4 import BeautifulSoup

def getCurrencyCotation(cod1: str, cod2: str, amount: str) -> str:
    url = f"https://www.x-rates.com/calculator/?from={cod1}&to={cod2}&amount={amount}"
    request = get(url= url).text
    parser = BeautifulSoup(request, "html.parser")
    #print(parser)
    elements = parser.find("span", class_="ccOutputRslt")
    
    return elements.text[:-4]

if __name__ == "__main__":
    a = getCurrencyCotation("USD", "JPY", "1")
    a = float(a)
    print(round(a, 2))