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
day_index = sales_pd["Data"].max()

# mandar os OnePages para cada gerente de loja respectivo

# salvar um arquivo de backup em uma pasta

# mandar um email separado para a diretoria com tudo
