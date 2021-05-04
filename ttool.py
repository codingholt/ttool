from binance.client import Client
# from tkinter import *
import PySimpleGUI as sg

# import apikeys:
# client = Client(config.API_KEY, config.API_SECRET)

sg.theme('DarkAmber')
# layout = [[sg.Text('ttool')],
#                 [sg.Text('Ticker:', size =(35,1),)],    
#                 [sg.InputText('1', key='ticker')],
#                 [sg.Text('Price', size = (35, 1))], 
#                 [sg.InputText(key='price')],
# #                 [sg.Submit(), sg.Cancel()]]

# window = sg.Window('ttool', layout=layout, margins=(100, 50), resizable=True)

###TAB EXAMPLE 
layout = 
with sg.FlexForm('', auto_size_text=True) as form:

    with sg.FlexForm('', auto_size_text=True) as form2:

        layout_tab_1 = [[sg.Text('First tab', size=(20, 1), font=('helvetica', 15))],
                        [sg.InputText(), sg.Text('Enter some info')],
                        [sg.Submit(button_color=('red', 'yellow')), sg.Cancel(button_color=('white', 'blue'))]]

        layout_tab_2 = [[sg.Text('Second Tab', size=(20, 1), font=('helvetica', 15))],
                        [sg.InputText(), sg.Text('Enter some info')],
                        [sg.Submit(button_color=('red', 'yellow')), sg.Cancel(button_color=('white', 'blue'))]]

        results = sg.ShowTabbedForm('Tabbed form example', (form, layout_tab_1, 'First Tab'),
                                    (form2, layout_tab_2,'Second Tab'))


# window = sg.Window('ttool - API input', layout=layout, margins=(100, 50), resizable=True)

sg.Popup(results)
