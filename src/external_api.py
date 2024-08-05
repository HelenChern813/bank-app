import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

URL = "https://api.apilayer.com/exchangerates_data/latest"
load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_exchange_rate(base_currency: str, target_currency: str = "RUB") -> Any:
    """Функция возращает актуальный курс"""

    headers = {"apikey": API_KEY}
    params = {"base": base_currency, "symbols": target_currency}
    response = requests.get(URL, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        return data["rates"][target_currency]
    else:
        raise Exception(f"Ошибка запроса {response.status_code}")


def summ_amount(transaction: Dict) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции (amount ) в рублях"""

    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        amount_float = float(transaction["operationAmount"]["amount"])
        return amount_float
    else:
        exchange_rate = convert_exchange_rate(transaction["operationAmount"]["currency"]["code"])
        amount_float = float(transaction["operationAmount"]["amount"]) * exchange_rate
        return amount_float
