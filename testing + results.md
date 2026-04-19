## Person 2 - Mean Reversion Bot

Best version:
- window = 5
- threshold = 0.02
- volume filter = volume > avg_volume
- trade_size = 5
- max_inventory = 100

Best backtest result:
- Final_Value: 100043.36
- Executed: 36
- Rejected: 0
- Timeouts: 0
- Status: COMPLETED

Additional tests:
- threshold = 0.01 → Final_Value: 100018.47, Executed: 523
- threshold = 0.015 → Final_Value: 100029.76, Executed: 114
- window = 8, threshold = 0.02 → Final_Value: 100032.33, Executed: 122
- stricter volume filter (volume > 1.1 * avg_volume) → Final_Value: 100042.30, Executed: 34

Conclusion:
- Best-performing mean reversion version used:
  - window = 5
  - threshold = 0.02
  - volume > avg_volume
- More selective trading improved performance.
- Overtrading reduced profits.

## Overview Table

| Version | Idea | Final Value | Executed | Rejected | Timeouts | Notes |
|---|---|---:|---:|---:|---:|---|
| baseline | template bot | 170297.57 | 525257 | 0 | 0 | Extremely aggressive; surprisingly strongest so far |
| v1 | momentum | 97247.66 | 493926 | 0 | 0 | Overtrading, loses money |
| v2 | mean reversion | 100018.47 | 523 | 0 | 0 | Threshold 0.01, too many weak trades |
| v3 | mean reversion | 100040.57 | 51 | 0 | 0 | Threshold 0.02, much better |
| v4 | mean reversion | 100029.76 | 114 | 0 | 0 | Threshold 0.015, worse than v3 |
| v5 | mean reversion | 100032.33 | 122 | 0 | 0 | Window 8, threshold 0.02 |
| v6 | mean reversion + volume filter | 100043.36 | 36 | 0 | 0 | Best Person 2 version |
| v7 | mean reversion + stricter volume filter | 100042.30 | 34 | 0 | 0 | Slightly worse than v6 |
