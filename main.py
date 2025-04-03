from datetime import datetime
from pathlib import Path

import pandas as pd

# importar e tratar as bases de dados
emails_pd = pd.read_csv(r"database/emails.csv")
stores_pd = pd.read_csv(r"database/stores.csv", encoding="unicode_escape", sep=";")
sales_pd = pd.read_csv(r"database/sales.csv")

# calcular indicadores desejados

sales_pd = sales_pd.merge(stores_pd, on="Store ID")
dict_stores = {
    store: sales_pd.loc[sales_pd["Store"] == store, :] for store in stores_pd["Store"]
}
# buscando o dia atual para utiliza-lo nos calculos do indicador do dia - ultimo dia disponível na planilha de vendas
day_index = datetime.strptime(sales_pd["Data"].max(), "%d/%m/%Y")


# calculo de 3 indicadores
for store in dict_stores:
    store_sales = dict_stores[store]
    day_store_sales = store_sales.loc[store_sales["Data"] == day_index, :]
    # faturamento
    store_revenue = store_sales["Final Value"].sum()
    day_store_revenue = day_store_sales["Final Value"].sum()
    # diversidade de produtos 
    year_products = len(store_sales["Product"].unique())
    day_products = len(day_store_sales["Product"].unique())
    # ticket medio
    order_values = store_sales.groupby("Code").sum(numeric_only=True)
    year_average_order_value = order_values["Final Value"].mean()
    day_order_values = day_store_sales.groupby("Code").sum(numeric_only=True)
    day_average_order_value = day_order_values["Final Value"].mean()

# mandar os OnePages para cada gerente de loja respectivo

# salvar um arquivo de backup em uma pasta
backup_path = Path(
    r"/home/vieli/folio/D-Mail/backup_file_stores"
)  # TODO: fazer isso atraves de um UI talvez
backup_path.mkdir(parents=True, exist_ok=True)
backup_files = backup_path.iterdir()
backup_names = [file.name for file in backup_files]
for store in dict_stores:
    # identificar se a pasta ja existe
    if store not in backup_names:
        new_folder = backup_path / store
        new_folder.mkdir()
    # salvar dentro da pasta
    file_name = f"{day_index.month}_{day_index.day}_{store}.xlsx"
    file_path = backup_path / store / file_name
    dict_stores[store].to_excel(file_path)

# mandar um email separado para a diretoria com tudo
