from binance.client import Client
import PySimpleGUI as sg


#GUI
sg.theme('DarkAmber')    #Theme 
##BUY TAB
layoutBuy = [[sg.Text('Ticker:', size=(10,1)),sg.Input('',key='ticker')],
            [sg.Text('Price', size=(10,1)),sg.Input('',key='price')],
            [sg.Text('Amount', size=(10,1)),sg.Input('',key='quantity')],
            [sg.Text('percentage amount', size=(10,1)),sg.Slider(0,100, key='percentage Amount')],
            [sg.Button('buy.')]]

window = sg.Window("ttool", layoutBuy)
event, values = window.read() 

window.close()

#store the inputs
price = float(values['price'])

##############################################

#ORDERS
##MAKE CONNENCTION WITH BINANCE

##STORE THE VARIABLES

##CREATE ORDERS


##RETURN ORDERS

##CREATE LOGS AND ERROR MESSAGES

