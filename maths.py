import numpy as np
from pandas.core.frame import DataFrame


def store_calculations(dataframe: DataFrame) -> tuple[float, int, float]:
    # faturamento
    df_revenue = dataframe["Final Value"].sum()
    # diversidade de produtos
    df_products_diversity = len(dataframe["Product"].unique())
    # ticket medio
    df_order_values = dataframe.groupby("Code Sale").sum(numeric_only=True)
    df_average_order_value = (
        df_order_values["Final Value"].mean()
        if not df_order_values.empty
        else np.float64(0.0)
    )
    return df_revenue, df_products_diversity, df_average_order_value


def board_calculations(dataframe: DataFrame):
    df_revenue = dataframe.groupby("Loja")[["Store", "Final Value"]].sum()
    df_ranked_revenue = df_revenue.sort_values(by="Final Value", ascending=False)
    return df_ranked_revenue
