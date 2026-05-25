import pandas as pd
import numpy as np
from typing import List, Dict

def get_sample_data():
    """Generate sample data for demonstration"""
    months = ["January", "February", "March", "April", "May", "June"]
    values = [150, 200, 175, 250, 300, 280]
    return pd.DataFrame({"mes": months, "valor": values})

def calculate_statistics(data: List[float]):
    """Calculate basic statistics"""
    if not data:
        return {"media": 0, "maximo": 0, "minimo": 0}
    return {
        "media": float(np.mean(data)),
        "maximo": float(np.max(data)),
        "minimo": float(np.min(data))
    }

def format_number(num: float, decimals: int = 2):
    """Format a number with decimals"""
    return f"{num:.{decimals}f}"
