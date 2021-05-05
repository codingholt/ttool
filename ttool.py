# from binance.client import Client
import config 
import PySimpleGUI as sg


#GUI
sg.theme('LightBrown12')    #Theme 
##BUY TAB
layoutBuy =[[sg.Text('Ticker:',     size=(10,1)),       sg.Input('',size=(15,2), key='ticker')],
            [sg.Text('Price',       size=(10,1)),       sg.Input('',size=(15,2), key='price')],
            [sg.Text('Amount',      size=(10,1)),       sg.Input('',size=(15,2), key='quantity')],
            [sg.Button('buy.')]]

window = sg.Window("ttool", layoutBuy,)

while True:     # The Event Loop
    event, value = window.read()
    if event in (None, 'EXIT'):            # quit if exit button or X
        break
    if event == 'buy.':
        ticker = value['ticker'].rstrip()
        pricewithoutfloat = value['price'].rstrip()
        amountwithoutfloat = value['quantity'].rstrip()
        price = float(pricewithoutfloat)
        amount = float(amountwithoutfloat)

    print(f'Buying: {ticker}')        
    print(f'At....${price}')
    print(f'Quantity: {amount}')





##############################################

#ORDERS

# client = Client(config.API_KEY, config.API_SECRET,)         #API key 


##STORE THE VARIABLES

##CREATE ORDERS


##RETURN ORDERS

##############################################

##CREATE LOGS AND ERROR MESSAGES

