import pandas as pd
import numpy as np
from typing import List, Dict

def get_sample_data():
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]
    valores = [150, 200, 175, 250, 300, 280]
    return pd.DataFrame({"mes": meses, "valor": valores})

def calculate_statistics(data: List[float]):
    if not data:
        return {"media": 0, "maximo": 0, "minimo": 0}
    return {
        "media": float(np.mean(data)),
        "maximo": float(np.max(data)),
        "minimo": float(np.min(data))
    }

def format_number(num: float, decimals: int = 2):
    return f"{num:.{decimals}f}"
