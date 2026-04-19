class Bot:
    def __init__(self):
        self.prices = []
        self.volumes = []
        self.window = 5
        self.trade_size = 5
        self.max_inventory = 100
        self.threshold = 0.02

    def get_action(self, tick, cash, inventory):
        close = tick['close']
        volume = tick['volume']

        self.prices.append(close)
        self.volumes.append(volume)

        if len(self.prices) < self.window:
            return {"action": "HOLD", "quantity": 0}

        recent_prices = self.prices[-self.window:]
        recent_volumes = self.volumes[-self.window:]

        avg_price = sum(recent_prices) / len(recent_prices)
        avg_volume = sum(recent_volumes) / len(recent_volumes)

        deviation = (close - avg_price) / avg_price

        high_volume = volume > avg_volume

        if deviation < -self.threshold and high_volume and inventory < self.max_inventory:
            return {"action": "BUY", "quantity": self.trade_size}
        elif deviation > self.threshold and high_volume and inventory > -self.max_inventory:
            return {"action": "SELL", "quantity": self.trade_size}
        else:
            return {"action": "HOLD", "quantity": 0}
