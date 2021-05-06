from binance.client import Client
from binance.enums import *
import config 
import PySimpleGUI as sg

#ORDERS
client = Client(config.API_KEY, config.API_SECRET,) 



#GUI
sg.theme('LightBrown12')    #Theme 

##BUY TAB
buyordertypechoices = ('Limit', 'Market', 'Stop loss') 
layoutBuy =[[sg.Text('Ticker:',         size=(10,1)),       sg.Input('',size=(15,2), key='buyticker')],
            [sg.Text('Order type',      size=(10,1)),       sg.Listbox(buyordertypechoices, size=(10, len(buyordertypechoices)), key='buyordertype')],
            [sg.Text('Price',           size=(10,1)),       sg.Input('',size=(15,2), key='buyprice')],
            [sg.Text('Amount',          size=(10,1)),       sg.Input('',size=(15,2), key='buyquantity')],
            [sg.Button('buy.')]]
##SELL TAB
sellordertypechoices = ('Limit', 'Market', 'Stop loss') 
layoutSell =[[sg.Text('Ticker:',         size=(10,1)),       sg.Input('',size=(15,2), key='sellticker')],
            [sg.Text('Order type',      size=(10,1)),       sg.Listbox(buyordertypechoices, size=(10, len(buyordertypechoices)), key='sellordertype')],
            [sg.Text('Price',           size=(10,1)),       sg.Input('',size=(15,2), key='sellprice')],
            [sg.Text('Amount',          size=(10,1)),       sg.Input('',size=(15,2), key='sellquantity')],
            [sg.Button('sell.')]]



window = sg.Window("ttool", layoutBuy,)

##Variables
#Buy side
event, value = window.read()
####
try:
    buyticker = value['buyticker'].rstrip()
    listbuyordertype = value['buyordertype']
    buyordertype = listbuyordertype[0]
    if buyordertype == 'Limit':
        newbuyordertype = buyordertype.replace('Limit', ORDER_TYPE_LIMIT)
    if buyordertype == 'Market':
        newbuyordertype = buyordertype.replace('Market', ORDER_TYPE_MARKET)
    if buyordertype == 'Stop loss':
        newbuyordertype = buyordertype.replace('Stop loss', ORDER_TYPE_STOP_LOSS)
    buypricewithoutfloat = value['buyprice'].rstrip()
    buyamountwithoutfloat = value['buyquantity'].rstrip()
    buyprice = float(buypricewithoutfloat)
    buyamount = float(buyamountwithoutfloat)
except KeyError:
    pass
#Sell side
try:
    event, value = window.read()
    sellticker = value['sellticker'].rstrip()
    listbuyordertype = value['sellordertype']
    sellordertype = listbuyordertype[0]
    if sellordertype == 'Limit':
        newsellordertype = sellordertype.replace('Limit', ORDER_TYPE_LIMIT)
    if sellordertype == 'Market':
        newsellordertype = sellordertype.replace('Market', ORDER_TYPE_MARKET)
    if sellordertype == 'Stop loss':
        newsellordertype = sellordertype.replace('Stop loss', ORDER_TYPE_STOP_LOSS)
    sellpricewithoutfloat = value['sellprice'].rstrip()
    sellamountwithoutfloat = value['sellquantity'].rstrip()
    sellprice = float(sellpricewithoutfloat)
    sellamount = float(sellamountwithoutfloat)
except KeyError:
    pass

##Orders
#Buy orders

try:
    buyOrder = client.create_order(
        symbol=buyticker,
        side=SIDE_BUY,
        type=newbuyordertype,
        timeInForce=TIME_IN_FORCE_GTC,
        quantity=buyamount,
        price=buyprice)
except NameError:
    pass

#Sell orders
try:
    sellOrder = client.create_order(
        symbol=sellticker,
        side=SIDE_SELL,
        type=newsellordertype,
        timeInForce=TIME_IN_FORCE_GTC,
        quantity=sellamount,
        price=sellprice)
except NameError:
    pass
    
def loopreadfunc():
    while True:     # The Event Loop
        event, value = window.read()
        if event in (None):            # quit if exit button or X
            break
        if event == 'buy.':
            return buyOrder
        if event == 'sell.':
            return sellOrder

def sendingorder():
    if event == 'buy.':
        print(f'Buying {buyamount} {buyticker} at {buyprice}')
    if event == 'sell.':
        print(f'Selling {sellamount} {sellticker} at {sellprice}')


##############################################

#ORDERS

# client = Client(config.API_KEY, config.API_SECRET,)         #API key 


##STORE THE VARIABLES

##CREATE ORDERS


##RETURN ORDERS

##############################################

##CREATE LOGS AND ERROR MESSAGES

