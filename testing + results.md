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
