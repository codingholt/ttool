from binance.client import Client
from binance.enums import *
import config 
import PySimpleGUI as sg

#ORDERS
client = Client(config.API_KEY, config.API_SECRET,) 



#GUI
sg.theme('LightBrown12')    #Theme 
##BUY TAB
layoutBuy =[[sg.Text('Ticker:',     size=(10,1)),       sg.Input('',size=(15,2), key='buyticker')],
            [sg.Text('Price',       size=(10,1)),       sg.Input('',size=(15,2), key='buyprice')],
            [sg.Text('Amount',      size=(10,1)),       sg.Input('',size=(15,2), key='buyquantity')],
            [sg.Button('buy.')]]

window = sg.Window("ttool", layoutBuy,)

##Variables
#Buy side
event, value = window.read()
buyticker = value['buyticker'].rstrip()
buypricewithoutfloat = value['buyprice'].rstrip()
buyamountwithoutfloat = value['buyquantity'].rstrip()
buyprice = float(buypricewithoutfloat)
buyamount = float(buyamountwithoutfloat)
#Sell side


##Orders
#Buy orders
limitbuyOrder = client.create_order(
    symbol='BNBBTC',
    side=SIDE_BUY,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=buyamount,
    price=buyprice)



def my_function():
    while True:     # The Event Loop
        event, value = window.read()
        if event in (None, 'EXIT'):            # quit if exit button or X
            break
        if event == 'buy.':
        
            print(f'Buying {buyamount} {buyticker} at {buyprice}')
        if event == 'sell':
            return limitbuyOrder,
        print(f'Buying {buyamount} {buyticker} at {buyprice}')





##############################################

#ORDERS

# client = Client(config.API_KEY, config.API_SECRET,)         #API key 


##STORE THE VARIABLES

##CREATE ORDERS


##RETURN ORDERS

##############################################

##CREATE LOGS AND ERROR MESSAGES

