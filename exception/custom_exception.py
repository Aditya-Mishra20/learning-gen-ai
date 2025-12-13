def brew_chai(flavor):
    
        if flavor not in ["masala", "ginger", "cardamom"]:
            raise ValueError(f"{flavor} chai is not available.")
        print(f"Brewed a cup of {flavor} chai.")
        
    
    
brew_chai("masala")
brew_chai("mint")