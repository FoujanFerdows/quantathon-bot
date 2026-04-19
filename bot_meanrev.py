class Bot:
    def __init__(self):
        # Store recent prices
        self.prices = []
        
        # Parameters (you can tune later)
        self.window = 5
        self.trade_size = 5
        self.max_inventory = 100
        self.threshold = 0.01  # 1%

    def get_action(self, tick, cash, inventory):
        close = tick['close']
        
        # Store price
        self.prices.append(close)

        # Not enough data yet → do nothing
        if len(self.prices) < self.window:
            return {"action": "HOLD", "quantity": 0}

        # Get recent prices
        recent_prices = self.prices[-self.window:]
        avg_price = sum(recent_prices) / len(recent_prices)

        # Calculate how far current price is from average
        deviation = (close - avg_price) / avg_price

        # BUY if price is lower than average (expect bounce)
        if deviation < -self.threshold and inventory < self.max_inventory:
            return {"action": "BUY", "quantity": self.trade_size}

        # SELL if price is higher than average (expect drop)
        elif deviation > self.threshold and inventory > -self.max_inventory:
            return {"action": "SELL", "quantity": self.trade_size}

        # Otherwise do nothing
        else:
            return {"action": "HOLD", "quantity": 0}
