# D-Mail
Projeto de automação de processos, calcula índices para gerar relatórios de desempenho de lojas fictícias

Processo de gestão de indicadores

trabalho em uma grande rede com 25 lojas espalhadas por todo o pais
todo dia de manha é enviado um OnePage para os gerentes das lojas com 3 indicadore, sendo eles:

- Faturamento
- Diversidade do Produto (quantos produtos diferentes foram vendidos no periodo)
- Ticket médio por venda

Demonstrados conforme o:

- Valor do dia
- Meta do dia
- Cenário (se ficou acima da meta ou não)

e os mesmo 3 indicadore para ano também, valor acomulado

- Valor ano
- Meta Ano
- Cenário Ano

Os indicadores serão cálculados a partir de base de dados disponibilizados com as vendas.

O que deve ser feito é analisar as bases de dados a disposição, calcular os indicadores e enviar um email com os OnePage para cada um dos gerentes,
mais um email para a diretoria com uma clasificação das lojas por desempenho.

As planilhas finais devem ser salvas dentro de uma pasta para cada loja com a data da planilha, para criar um histórico de backup.

## Objetivos

- mandar os OnePages para cada gerente de loja respectivo

- salvar um arquivo de backup em uma pasta

- mandar um email separado para a diretoria com uma visão das lojas e seus desempenhos

## Instalação recomendada

* Criar um ambiente virtual com o comando: 
    
        python -m venv {nome_ambiente_virtual}

* Ativar o ambiente virtual:

        {nome_ambiente_virtual}\Scripts\activate

* Baixar as bibliotecas dentro do ambiente virtual: 
        
        pip install -r requirements.txt


Isso instalará todas as bibliotecas necessárias para o funcionamento correto onde for utilizado

## Tecnologias Utilizadas

* pandas
* smtplib