from binance.client import Client
from binance.enums import *
import config 
import PySimpleGUI as sg


#ORDERS
client = Client(config.API_KEY, config.API_SECRET,) 



#GUI
sg.theme('Reddit')    #Theme 
sg.theme_input_text_color('#000000')
sg.theme_input_background_color('#FFFFFF')

##BUY TAB
buyordertypechoices = ('Limit', 'Market', 'Stop Market') 
layoutBuy =[[sg.Text('Ticker:',         size=(10,1)),       sg.Input('',size=(15,2), key='buyticker')],
            [sg.Text('Order type',      size=(10,1)),       sg.Combo(buyordertypechoices, size=(10, len(buyordertypechoices)), pad=(10,2), key='buyordertype')],
            [sg.Text('Price',           size=(10,1)),       sg.Input('',size=(15,2), key='buyprice')],
            [sg.Text('Amount',          size=(10,1)),       sg.Input('',size=(15,2), key='buyquantity')],
            [sg.Button('buy.')]]
##SELL TAB
sellordertypechoices = ('Limit', 'Market', 'Stop Market') 
layoutSell =[[sg.Text('Ticker:',         size=(10,1)),       sg.Input('',size=(15,2), key='sellticker')],
            [sg.Text('Order type',      size=(10,1)),       sg.Combo(sellordertypechoices, size=(10, len(buyordertypechoices,)), pad=(10,2), key='sellordertype')],
            [sg.Text('Price',           size=(10,1)),       sg.Input('',size=(15,2), key='sellprice')],
            [sg.Text('Amount',          size=(10,1)),       sg.Input('',size=(15,2), key='sellquantity')],
            [sg.Button('sell.')]]

tabgrp = [sg.TabGroup([[sg.Tab('Buy', layoutBuy,), sg.Tab('Sell', layoutSell)]])],    
        
window = sg.Window("ttool", tabgrp, element_padding=(5,9),font=('Verdana',14), finalize=True)

window['buyticker'].Widget.config(insertbackground='black')
window['buyprice'].Widget.config(insertbackground='black')
window['buyquantity'].Widget.config(insertbackground='black')
window['sellticker'].Widget.config(insertbackground='black')
window['sellprice'].Widget.config(insertbackground='black')
window['sellquantity'].Widget.config(insertbackground='black')

##Variables
#Buy side
event, value = window.read()
####
try:
    buyticker = value['buyticker'].rstrip().upper()
    listbuyordertype = value['buyordertype']
    try:
        buyordertype = listbuyordertype
        if buyordertype == 'Limit':
            newbuyordertype = buyordertype.replace('Limit', ORDER_TYPE_LIMIT)
        if buyordertype == 'Market':
            newbuyordertype = buyordertype.replace('Market', ORDER_TYPE_MARKET)
        if buyordertype == 'Stop loss':
            newbuyordertype = buyordertype.replace('Stop Market', ORDER_TYPE_STOP_LOSS)
    except IndexError:
        pass
    buypricewithoutfloat = value['buyprice'].rstrip()
    buyamountwithoutfloat = value['buyquantity'].rstrip()
    try:
        buyprice = float(buypricewithoutfloat)
        buyamount = float(buyamountwithoutfloat)
    except ValueError:
        pass
except KeyError:
    pass


#Sell side
try:
    sellticker = value['sellticker'].rstrip().upper()
    listsellordertype = value['sellordertype']
    try:
        sellordertype = listsellordertype
        if sellordertype == 'Limit':
            newsellordertype = sellordertype.replace('Limit', ORDER_TYPE_LIMIT)
        elif sellordertype == 'Market':
            newsellordertype = sellordertype.replace('Market', ORDER_TYPE_MARKET)
        elif sellordertype == 'Stop Market':
            newsellordertype = sellordertype.replace('Stop Market', ORDER_TYPE_STOP_LOSS)
    except IndexError:
        pass
    sellpricewithoutfloat = value['sellprice'].rstrip()
    sellamountwithoutfloat = value['sellquantity'].rstrip()
    try:
        sellprice = float(sellpricewithoutfloat)
        sellamount = float(sellamountwithoutfloat)
    except ValueError:
        pass
except KeyError:
    pass


    print(sellordertype)
    print(newsellordertype)


##Orders
#Buy orders

try:
    buyOrder = client.create_order(
        symbol=buyticker,
        side=SIDE_BUY,
        type=newbuyordertype,
        quantity=buyamount,
        price=buyprice)
except NameError:
    pass

#Sell orders
def sellorders():
    try:
        if sellordertype == 'Limit':
            client.create_order(
                symbol=sellticker,
                side=SIDE_SELL,
                type=newsellordertype,
                timeInForce=TIME_IN_FORCE_GTC
                quantity=sellamount,
                price=sellprice)
        elif sellordertype =='Market':
            client.order_market_buy(
                symbol=sellticker,
                quantity=sellamount)
        elif sellordertype == 'Stop Market':
            client.create_order(
                symbol=sellticker,
                side=SIDE_SELL,
                type=ORDER_TYPE_STOP_LOSS,
                quantity=sellamount,
                stopPrice=sellprice)
    except NameError:
        pass

#Sending order message    
def sendingorder():
    if event == 'buy.':
        print(f'Buying {buyamount} {buyticker} at {buyprice} ')
    if event == 'sell.':
        print(f'Selling {sellamount} {sellticker} at {sellprice} ')

def testFunc():
    while True:     # The Event Loop
        event, value = window.read()
        if event == sg.WIN_CLOSED:         #exit   
            break  
        if event == 'buy.':
            return sendingorder, buyOrder, window
        if event == 'sell.':
            return sendingorder, sellorders, window



####################

