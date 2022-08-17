from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Dropship Calculator")
root.iconbitmap("assets\logo.ico")
root.configure(background='white')
root.resizable(0, 0)

## Entry Style
estyle = ttk.Style()
estyle.element_create("plain.field", "from", "clam")
estyle.layout("EntryStyle.TEntry",
                   [('Entry.plain.field', {'children': [(
                       'Entry.background', {'children': [(
                           'Entry.padding', {'children': [(
                               'Entry.textarea', {'sticky': 'nswe'})],
                      'sticky': 'nswe'})], 'sticky': 'nswe'})],
                      'border':'2', 'sticky': 'nswe'})])
estyle.configure("EntryStyle.TEntry",
                 background="white", 
                 foreground="black",
                 fieldbackground="white")

### ----------------------------->> Classes

# Class for Input Labels
class labels:
    def __init__(self, master, text, row, column, pady=5):
        # Create variables
        self.master = master
        self.text = text
        self.row  = row
        self.column = column
        self.pady = pady

        # Create a label
        label = Label(self.master, text=self.text, font=("Calibri", 17), bg="white")
        label.grid(row=self.row, column=self.column, padx=(15, 30), pady=self.pady, sticky="W")

# Class for Entry Boxes
class entrys:
    def __init__(self, master, textvariable, row, column):
        # Create variables
        self.master = master
        self.textvariable = textvariable
        self.row = row
        self.column = column

        # Create a Entry Box
        entry = ttk.Entry(self.master, textvariable=self.textvariable, style="EntryStyle.TEntry", font=('Calibri', 20), width=10)
        entry.grid(row=self.row, column=self.column, padx=(5, 15))



### Main Title
mainTitle = Label(root, text="Dropship Calculator", font=("Calibri", 22,  'bold'), bg="white")
mainTitle.grid(row=0, column=1, pady=(10,7), padx=(15, 0), columnspan=3, sticky='w')


### ----------------------------->> Labels

## Create Name Labels ----->>
aliPriceLabel = labels(root, text="Ali Price", row=1, column=1)
aliShippingLabel = labels(root, text="Ali Shipping", row=2, column=1)
ebayShippingLabel = labels(root, text="eBay Shipping", row=3, column=1)
profitLabel = labels(root, text="Expected Profit", row=4, column=1)

itemPriceLabel = labels(root, text="Item Price", row=5, column=1, pady=(20,0))
profitRateLabel = labels(root, text="Profit Rate", row=6, column=1, pady=(5,20))

## Create blank labels ----->>

# for itemPriceOut Label
itemPriceOut = Label(root, text='$ 0.00', font=("Calibri", 20), bg="white")
itemPriceOut.grid(row=5, column=2, sticky="W", padx=(0, 15), pady=(20,0), columnspan=2)

# for profitRateOut Label
profitRateOut = Label(root, text='0.00 %', font=("Calibri", 20), bg="white")
profitRateOut.grid(row=6, column=2, sticky="W", padx=(0, 15), pady=(5,20), columnspan=2)

## '$' icon label ----->>
for i in range(4):
    dollarLabel = Label(root, text='$', font=('Calibri', 20), bg="white")
    
    if i >= 4:
        dollarLabel.grid(row=i+1, column=2, pady=(20,0))
    else:
        dollarLabel.grid(row=i+1, column=2)



#### ----------------------------->> Entry Boxes

# Create Tkiner Variables
aliPriceVar = StringVar()
aliShippingVar = StringVar()
ebayShippingVar = StringVar()
profitVar = StringVar()
x = StringVar()

# Create Entry boxes
aliPriceEntry = entrys(root, textvariable=aliPriceVar, row=1, column=3)
aliShippingEntry = entrys(root, textvariable=aliShippingVar, row=2, column=3)
ebayShippinEntry = entrys(root, textvariable=ebayShippingVar, row=3, column=3)
profitEntry = entrys(root, textvariable=profitVar, row=4, column=3)

#### ----------------------------->> Tracing Variables

# Funtion for tracing
def callback(entryVar):
    ## Check variable's value none or not
    
    # For aliPriceVar
    if aliPriceVar.get() == '':
        aliPriceValue = 0
    else:
        aliPriceValue = float(aliPriceVar.get())

    # For aliShippingVar
    if aliShippingVar.get() == '':
        aliShippingValue = 0
    else:
        aliShippingValue = float(aliShippingVar.get())

    # For ebayShippingVar
    if ebayShippingVar.get() == '':
        ebayShippingValue = 0
    else:
        ebayShippingValue = float(ebayShippingVar.get())

    # For profitVar
    if profitVar.get() == '':
        profitValue = 0
    else:
        profitValue = float(profitVar.get())

    ## Calculations

    # Calculate eBay Item Price
    itemPrice = ((1.08*aliPriceValue) + aliShippingValue + (0.16*ebayShippingValue) + 0.30 + profitValue) / 0.82

    # Calculate Profit Rate
    if aliPriceValue == 0:
        profitRate = 0
    else:
        profitRate = (profitValue/aliPriceValue) * 100

    
    # Distroy previous itemPriceOut Label
    global itemPriceOut
    itemPriceOut.destroy()

    # Distroy previous profitRateOut Label
    global profitRateOut
    profitRateOut.destroy()

    # Check entrys values 0 or not
    if aliPriceValue == 0 and aliShippingValue == 0 and aliShippingValue == 0 and aliShippingValue == 0:
        itemPriceOut = Label(root, text="$ 0.00", font=("Calibri", 20), bg="white")
        profitRateOut = Label(root, text="0.00 %", font=("Calibri", 20), bg="white")
    else:
        itemPriceOut = Label(root, text='$ ' + str("%.2f" % itemPrice), font=("Calibri", 20), bg="white")
        profitRateOut = Label(root, text=str("%.2f" % profitRate) + " %", font=("Calibri", 20), bg="white" )
    
    # Grid itemPriceOut label
    itemPriceOut.grid(row=5, column=2, sticky="W", padx=(0,15), pady=(20,0), columnspan=2)

    # Grid profitRateOut label
    profitRateOut.grid(row=6, column=2, sticky="W", padx=(0,15), pady=(5,20), columnspan=2)

    # Calculate Profit Rate

# Tracing each variables
aliPriceVar.trace("w", lambda *args, aliPriceVar=aliPriceVar: callback(aliPriceVar))
aliShippingVar.trace("w", lambda *args, aliShippingVar=aliShippingVar: callback(aliShippingVar))
ebayShippingVar.trace("w", lambda *args, ebayShippingVar=ebayShippingVar: callback(ebayShippingVar))
profitVar.trace("w", lambda *args, profitVar=profitVar: callback(profitVar))

root.mainloop()