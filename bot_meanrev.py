class Bot:
    def __init__(self):
        self.ai_model = "Placeholder_for_Model"

    def get_action(self, tick, cash, inventory):
        if tick['close'] < 100 and cash > 5000:         
            return {"action": "BUY", "quantity": 10}    
        
        elif tick['volume'] > 150 and inventory > 0:    
            return {"action": "SELL", "quantity": 5}    
            
        else:
            return {"action": "HOLD", "quantity": 0}    





    
        

"""
RULES FOR THIS FILE:
1. Keep the names 'class Bot:' and 'def get_action' (content within can be deleted) exactly as they are.
2. Write your trading logic INSIDE 'get_action'.
3. Everything else (including __init__) can be changed or deleted!
4. __init__ is meant for uploading pre-trained machine learning models, but you can use it as you wish. 

(You can delete this comment now.)
"""
