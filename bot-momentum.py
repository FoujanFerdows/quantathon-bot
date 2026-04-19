from collections import deque


class Bot:
    """
    Short-term momentum: compares fast vs slow average of recent closes.
    Buys on uptrend, sells on downtrend, with capped inventory and small clips.
    """

    def __init__(self):
        self.fast_n = 3
        self.slow_n = 8
        self.max_history = 30
        self.recent_closes = deque(maxlen=self.max_history)

        self.trade_qty = 10
        self.max_long = 400
        self.max_short = 200

    def _avg(self, values):
        if not values:
            return None
        return sum(values) / len(values)

    def get_action(self, tick, cash, inventory):
        close = float(tick["close"])
        self.recent_closes.append(close)

        if len(self.recent_closes) < self.slow_n:
            return {"action": "HOLD", "quantity": 0}

        closes = list(self.recent_closes)
        fast_vals = closes[-self.fast_n :]
        slow_vals = closes[-self.slow_n :]
        fast_avg = self._avg(fast_vals)
        slow_avg = self._avg(slow_vals)

        if fast_avg is None or slow_avg is None:
            return {"action": "HOLD", "quantity": 0}

        fee = 0.001
        min_cushion = close * self.trade_qty * (1.0 + fee) * 1.01

        # Rising recent closes: fast window above slow window
        if fast_avg > slow_avg:
            if inventory >= self.max_long:
                return {"action": "HOLD", "quantity": 0}
            if cash < min_cushion:
                return {"action": "HOLD", "quantity": 0}
            return {"action": "BUY", "quantity": self.trade_qty}

        # Falling recent closes: fast below slow
        if fast_avg < slow_avg:
            if inventory <= -self.max_short:
                return {"action": "HOLD", "quantity": 0}
            return {"action": "SELL", "quantity": self.trade_qty}

        return {"action": "HOLD", "quantity": 0}

