import pandas as pd

# importar e tratar as bases de dados    
emails_pd = pd.read_csv(r"database/emails.csv")
stores_pd = pd.read_csv(r"database/stores.csv", encoding="unicode_escape", sep=";")
sales_pd = pd.read_csv(r"database/sales.csv")

# calcular indicadores desejados

# mandar os OnePages para cada gerente de loja respectivo

# salvar um arquivo de backup em uma pasta

# mandar um email separado para a diretoria com tudo