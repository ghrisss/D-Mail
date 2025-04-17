from pathlib import Path
from string import Template

import pandas as pd

from mailer import send_email
from maths import board_calculations, store_calculations


def check_folder_existence(folder_path: Path) -> bool:
    if not folder_path.exists():
        folder_path.mkdir()
    return True


# definicoes de metas TODO: colocar como um input talvez
day_revenue_goal = 1000
year_revenue_goal = 1650000
day_products_goal = 4
year_products_goal = 120
day_average_order_value_goal = 500
year_average_order_value_goal = 500

# importar e tratar as bases de dados
emails_pd = pd.read_csv(r"database/emails.csv", encoding="utf-8")
stores_pd = pd.read_csv(r"database/stores.csv", encoding="utf-8", sep=";")
sales_pd = pd.read_csv(
    r"database/sales.csv",
    parse_dates=["Data"],
    date_format="%d/%m/%Y",
    thousands=".",
    decimal=",",
    converters={
        "Unit Value": lambda x: float(
            x.replace("R$", "").replace(".", "").replace(",", ".").strip()
        ),
        "Final Value": lambda x: float(
            x.replace("R$", "").replace(".", "").replace(",", ".").strip()
        ),
    },
)

with open("templates/mail-body.html") as file:
    template = file.read()
mail_html = Template(template)

# calcular indicadores desejados
sales_pd = sales_pd.merge(stores_pd, on="Store ID")
dict_stores = {
    store: sales_pd.loc[sales_pd["Store"] == store, :] for store in stores_pd["Store"]
}
# buscando o dia atual para utiliza-lo nos calculos do indicador do dia - ultimo dia disponível na planilha de vendas
day_index_timestamp = sales_pd["Data"].max()
day_index = day_index_timestamp

# salvar um arquivo de backup em uma pasta
backup_path = Path(
    r"/home/vieli/folio/D-Mail/backup_file_stores"
)  # TODO: fazer isso atraves de um UI talvez
backup_path.mkdir(parents=True, exist_ok=True)
for store in dict_stores:
    # identificar se a pasta ja existe
    check_folder_existence(folder_path=backup_path / store)
    # salvar dentro da pasta
    file_name = f"{day_index.month}_{day_index.day}_{store}.xlsx"
    file_path = backup_path / store / file_name
    dict_stores[store].to_excel(file_path)

    # calculo de 3 indicadores
    store_sales = dict_stores[store]
    day_store_sales = store_sales.loc[store_sales["Data"] == day_index, :]

    day_store_revenue, day_products, day_average_order_value = store_calculations(
        day_store_sales
    )
    year_store_revenue, year_products, year_average_order_value = store_calculations(
        store_sales
    )

    body_text = mail_html.safe_substitute(
        name=emails_pd.loc[emails_pd["Store"] == store, "Manager"].values[0],
        day=day_index.day,
        month=day_index.month,
        store=store,
        day_store_revenue=day_store_revenue,
        day_revenue_goal=day_revenue_goal,
        day_revenue_color="green" if day_store_revenue >= day_revenue_goal else "red",
        day_products=day_products,
        day_products_goal=day_products_goal,
        day_products_color="green" if day_products >= day_products_goal else "red",
        day_average_order_value=day_average_order_value,
        day_average_order_value_goal=day_average_order_value_goal,
        day_aov_color="green"
        if day_average_order_value >= day_average_order_value_goal
        else "red",
        year_store_revenue=year_store_revenue,
        year_revenue_goal=year_revenue_goal,
        year_revenue_color="green"
        if year_store_revenue >= year_revenue_goal
        else "red",
        year_products=year_products,
        year_products_goal=year_products_goal,
        year_products_color="green" if year_products >= year_products_goal else "red",
        year_average_order_value=year_average_order_value,
        year_average_order_value_goal=year_average_order_value_goal,
        year_aov_color="green"
        if year_average_order_value >= year_average_order_value_goal
        else "red",
    )
    print(
        f"\u2713 Concluiu a análise para a loja {store} para o dia {day_index.day}/{day_index.month}"
    )

    # mandar os OnePages para cada gerente de loja respectivo
    send_email(
        email_to=emails_pd.loc[emails_pd["Store"] == store, "E-mail"].values[0],
        subject=f"OnePage Dia {day_index.day}/{day_index.month} - Loja {store}",
        store=store,
        body_text=body_text,
        file_to_attach=file_path,
    )

# mandar um email separado para a diretoria com tudo
ranked_store_revenue = board_calculations(sales_pd)
file_name = f"{day_index.month}_{day_index.day}_annual_rank.xlsx"
annual_rank_path = backup_path / "annual-rank"
check_folder_existence(annual_rank_path)
ranked_store_revenue.to_excel(annual_rank_path / file_name)

ranked_stores_day_revenue = board_calculations(
    sales_pd.loc[sales_pd["Data"] == day_index, :]
)
file_name = f"{day_index.month}_{day_index.day}_daily_rank.xlsx"
daily_rank_path = backup_path / "daily-rank"
check_folder_existence(folder_path=daily_rank_path)
ranked_stores_day_revenue.to_excel(daily_rank_path / file_name)

with open("templates/board-body.html") as file:
    template = file.read()
board_mail_html = Template(template)

board_body_text = board_mail_html.safe_substitute(
    day_best_store_name=ranked_stores_day_revenue.index[0],
    day_best_store_revenue=ranked_stores_day_revenue.iloc[0, 0],
    day_worst_store_name=ranked_stores_day_revenue.index[-1],
    day_worst_store_revenue=ranked_stores_day_revenue.iloc[0, -1],
    year_best_store_name=ranked_store_revenue.index[0],
    year_best_store_revenue=ranked_store_revenue.iloc[0, 0],
    year_worst_store_name=ranked_store_revenue.index[-1],
    year_worst_store_revenue=ranked_store_revenue.iloc[0, -1],
)

# TODO: tem de enviar dois anexos nesse caso. Verificar de enviar o parametro como uma lista e resolver la no metodo
send_email(
    email_to=emails_pd.loc[emails_pd["Store"] == "Diretoria", "E-mail"].values[0],
    subject=f"Relatorio Diretoria para o Dia {day_index.day}/{day_index.month}",
    store=None,
    body_text=body_text,
    file_to_attach=annual_rank_path / file_name,
)
