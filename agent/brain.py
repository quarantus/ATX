from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini")

def decide_trade(data, config):
    prompt = PromptTemplate.from_template(
        "Token: {token}\n5m change: {change_5m}%\nVolume: ${volume_5m}\n"
        "Risk limit: {risk_per_trade}% per trade\n"
        "Goal: Snipe if momentum > {min_momentum_5m}x and volume high.\n"
        "Respond in JSON: {{'action': 'buy/sell/hold', 'reason': '...'}}\n"
    )
    chain = prompt | llm
    result = chain.invoke({**data, **config})
    return result.json()
