pizza_price = float(input("Enter base pizza price (₹): ")) 
quantity = int(input("How many pizzas? ")) 
has_promo = input("Have a promo code? (yes/no): ").lower() 

subtotal = pizza_price * quantity 
gst = subtotal * 0.18 

if subtotal >= 1000:
    delivery_fee = 0
else:
    delivery_fee = 100

if has_promo == "yes":
    promo_discount = subtotal * 0.10
else:
    promo_discount = 0

final_amount = subtotal + gst + delivery_fee - promo_discount

print("\n" + "="*30)
print("PIZZA DELIVERY COST CALCULATOR")
print("="*30)
print(f"Base Price:      ₹{subtotal:>10.2f}")
print(f"GST (18%):       ₹{gst:>10.2f}")

if delivery_fee == 0:
    print(f"Delivery Charge:   FREE DELIVERY!")
else:
    print(f"Delivery Charge: ₹{delivery_fee:>10.2f}")

print(f"Promo Discount: -₹{promo_discount:>10.2f}")
print("-" * 30)
print(f"TOTAL AMOUNT:    ₹{final_amount:>10.2f}")
print("="*30)

if delivery_fee == 0:
    print(f"Tip: You saved ₹100 on delivery!")
else:
    amount_needed = 1000 - subtotal
    print(f"Tip: Order ₹{amount_needed:.2f} more for FREE delivery!")
print("="*30)