class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu =  {"masala": 50, "ginger": 60, "cardamom": 70}
    try:
        if flavor not in menu:
            raise InvalidChaiError(f"{flavor} chai is not available.")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer.")
        total = menu[flavor] * cups
        print(f"Total bill for {cups} cup(s) of {flavor} chai: ₹{total}")
    except Exception as e:
        print(f"Error: {e}")
    finally: 
        print("Thank you for ordering from our chai shop.")
        
        
        
bill("masala", 3)
bill("mint", 2)
bill("ginger", "two")