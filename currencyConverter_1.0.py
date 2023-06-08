from PySimpleGUI import Window, Text, Combo, WIN_CLOSED, Button, InputText
from scrapMoney import getCurrencyCotation

currency_codes = ["BRL", "USD", "EUR", "ARS", "INR", "GBP", "CAD", "JPY"]
layout = [
    [Combo(currency_codes, size=(20, 1), key="cod1"), Text("To"), Combo(currency_codes, size=(20, 1), key="cod2")],
    [Text("Quantity: "), InputText("", size=10, key="quantity"), Button("See Result", border_width=2)],
    [Text("", key="output", size=(40), border_width=(20), justification="c")]
]

window = Window("Currency Converter", layout= layout, size= (400, 150), element_justification="c", margins=(20,20))

while True:
    event, values = window.read()
    if event in (None, "Exit", WIN_CLOSED):
        break

    elif event == "See Result":
        try:
            float(values["quantity"])
            cod1, cod2, quantity = values["cod1"], values["cod2"], values["quantity"]
            cotation = float(getCurrencyCotation(cod1= cod1, cod2= cod2, amount= quantity))
            message = f"{quantity} {cod1} is equal to {round(cotation,2)} {cod2}"
            window["output"].update(message)
        except:
            window["output"].update("An error occurred")


window.close()
