import importlib
import pandas as pd
from engine import run_backtest   # only works if engine.py exposes this function

BOTS = [
    ("baseline", "template bot", "bot_template"),
    ("v1", "momentum", "bot_momentum"),
    ("v2", "mean reversion", "bot_meanrev"),
]

results = []

for version, idea, module_name in BOTS:
    module = importlib.import_module(module_name)
    BotClass = module.Bot

    output = run_backtest("train_data.csv", BotClass())

    results.append({
        "Version": version,
        "Idea": idea,
        "Final Value": output["final_value"],
        "Executed": output["executed"],
        "Rejected": output["rejected"],
        "Timeouts": output["timeouts"],
        "Notes": ""
    })

df = pd.DataFrame(results)
df.to_csv("backtest_results.csv", index=False)

print(df)

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
