
## Person 2 - Mean Reversion Bot

Best version so far:
- window = 5
- threshold = 0.02
- volume filter = volume > avg_volume
- trade_size = 5
- max_inventory = 100

Backtest result:
- Final_Value: 100043.36
- Executed: 36
- Rejected: 0
- Timeouts: 0
- Status: COMPLETED

OVERVIEW - TABLE
| Version  | Idea           | Final Value | Executed | Rejected | Timeouts | Notes                      |
| -------- | -------------- | ----------: | -------: | -------: | -------: | -------------------------- |
| baseline | template bot   |   170297.57 |   525257 |        0 |        0 | Trades almost every bar    |
| v1       | momentum       |    97247.66 |   493926 |        0 |        0 | Very frequent trading      |
| v2       | mean reversion |   100018.47 |      523 |        0 |        0 | Conservative and selective |
