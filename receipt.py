#Customize the display with "===" just to make it look nice.
print("="*44)
print(" STORE RECEIPT".center(44)) # center() used to center text 
print("="*44)


#Declare variables and add values.
item1_name = "Notebook"
item1_price = "4.99"
item1_qty = "2"

item2_name = "Pen Pack"
item2_price = "7.50"
item2_qty = "1"

item3_name = "Backpack"
item3_price = "34.99"
item3_qty = "1"

tax_rate = "0.075"   # 7.5% sales tax


#Converting string prices and quantity and tax_rate to a specific number type
item1_pre = float(item1_price)
item1_qt = int(item1_qty)
item2_pre = float(item2_price)
item2_qt = int(item2_qty)
item3_pre = float(item3_price)
item3_qt = int(item3_qty)
tx_rate = float(tax_rate)


#Alls Calculate
#calculate price * qty alls
tot1 = item1_pre * item1_qt
tot2 = item2_pre * item2_qt
tot3 = item3_pre * item3_qt

#Calculate subtotal and tax total  and
subtotal = tot1 + tot2 +tot3
tax = subtotal * tx_rate 
total = subtotal + tax


#Alls display
#display for price and qty alls
#for give space  left and spific size use "<:any number "
print(f"{item1_name:<16} ${item1_pre:<5} X {item1_qt:<4} ${tot1:<6}")
print(f"{item2_name:<16} ${item2_pre:<5} X {item2_qt:<4} ${tot2:<6}")
print(f"{item3_name:<16} ${item3_pre:<4} X {item3_qt:<4} ${tot3:<6}")

print("-"*44)

#display subtotal and tax 
print(f"{'Subtotal:':<30} ${subtotal}")
print(f"{'Tax:':<30} ${tax:.2f}") #(:.2f) - give just 2 decimal place

print("="*44)

#display total
print(f"{'Total:':<30} ${total:.2f}") 