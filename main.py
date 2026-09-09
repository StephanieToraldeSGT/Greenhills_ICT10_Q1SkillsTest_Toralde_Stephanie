from pyscript import display, document

def create_receipt(e):

    subtotal = float(document.getElementById('coffee').value)
    VAT = subtotal + 0.12
    total_amount = subtotal + VAT

    display(f'₱ {subtotal}', target='result1')
    display(f'₱ {VAT}', target='result2')
    display(f'₱{total_amount}', target='result3')

 # prices of the coffee, how does one code any of this
    
val1 = 100; (document.getElementById('item1').value)
val2 = 120; (document.getElementById('item2').value)
val3 = 120; (document.getElementById('item3').value)
val4 = 150; (document.getElementById('item4').value)
val5 = 150; (document.getElementById('item5').value)
    
