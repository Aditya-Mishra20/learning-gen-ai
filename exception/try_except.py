def serve_chai(flavor):
    try:
        print(f"Serving a cup of {flavor} chai.")
        if flavor not in ["masala", "ginger", "cardamom"]:
            raise ValueError("We only serve masala, ginger, or cardamom chai.")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print("Chai served successfully!")
    finally:
        print("Thank you for visiting our chai shop.")
        
        
    
serve_chai("masala")
serve_chai("mint")