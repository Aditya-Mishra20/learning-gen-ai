def process_order(item, quantity):
    try:
        price = {"masala": 50}[item]
        cost = price * quantity
        print(f"Total cost for {quantity} {item} chai(s): ₹{cost}")
    except KeyError :
        print(f"Error: We do not serve {item} chai.")
    except TypeError:
        print("Error: Quantity must be a number.")
        
        
        
process_order("masala", 2)
process_order("mint", 3)
process_order("masala", "two")    