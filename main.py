import yaml
from data.stream import get_market_data
from agent.brain import decide_trade
from agent.executor import execute_trade

with open("config.yaml") as f:
    config = yaml.safe_load(f)

print("AETHER ONLINE — Watching Solana...")

while True:
    data = get_market_data()
    decision = decide_trade(data, config)
    
    if decision['action'] != 'hold':
        execute_trade(decision, config)
    
    print(f"[AETHER] {decision['action'].upper()}: {decision['reason']}")
    break  # Remove for live loop
