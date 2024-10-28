import pandas as pd


def save_to_excel(data, filename="prices.xlsx"):
    """
    Save data to an Excel file
    """
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
