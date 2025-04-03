# D-Mail
#### **Automação de processos e Gestão de Indicadores de desempenho de lojas**

O projeto **D-Mail** automatiza o cálculo de indicadores e a geração de relatórios de desempenho para uma base de dados fictícia com 25 lojas espalhadas por todo o país. O sistema facilita o envio de **OnePages** diários para gerentes, além de um resumo consolidado dos dados para a diretoria

## Descrição do Processo

Diariamente, o sistema analisa as bases de dados disponíveis, calcula indicadores de desempenho e automatiza a entrega de relatórios. Os indicadores analisados são:

- **Faturamento**
- **Diversidade do Produto** (número de produtos diferentes vendidos no periodo)
- **Ticket médio por venda**

Cada indicador é apresentado conforme::

- **Valor do dia**
- **Meta do dia**
- **Cenário** (indica se o desempenho ficou acima ou abaixo da meta)

e suas contrapartes anuais acumuladas

- **Valor acumulado do ano**
- **Meta anual**
- **Cenário anual**

### Funcionalidades Principais
1. Envio de Relatórios Diários (OnePage)
   Um relatório é enviado para cada gerente, detalhando o desempenho diário e anual da sua respectiva loja.
2. Consolidado para a diretoria
   Um email separado é enviado para a diretoria, contendo uma visão geral do desempenho das lojas, classificadas por seus resultados
3. Backup Automático
   As planilhas finais dsão organizadas são organizadas dentro de pastas para cada loja com a data da geração da planilha, para criar um histórico de backup.

---

## Objetivos

- Automatizar o cálculo e envio de relatórios diários personalizados para gerentes e diretoria.

- Criar e manter backups organizados em pastas com base na data e na loja correspondente.

- Fornecer uma visão consolidada e classificada do desempenho das lojas para a diretoria.

---

## Instalação recomendada

### Requisitos

* Python 3.8 ou superior

### Passos de instalação

* Criar um ambiente virtual: 
    
        python -m venv {nome_ambiente_virtual}

* Ativar o ambiente virtual:

  * No Windows:

        {nome_ambiente_virtual}\Scripts\activate
  * No Linux/macOS:

        source {nome_ambiente_virtual}\bin\activate

* Instalar as dependências: 
        
        pip install -r requirements.txt

---

## Tecnologias Utilizadas

* pandas (Manipular e análise de dados)
* smtplib (Envio automatizado de emails)

---

<!-- ## Estrutura do Projeto

```
D-Mail/
├── data/                     # Diretório para armazenar as bases de dados
├── reports/                  # Diretório para armazenar os relatórios gerados
│   ├── loja1/
│   │   ├── 2025-01-17.xlsx   # Exemplo de relatório salvo
├── src/                      # Código-fonte do projeto
│   ├── calculate_indicators.py
│   ├── generate_reports.py
│   ├── send_emails.py
├── requirements.txt          # Lista de dependências do projeto
├── README.md                 # Documentação do projeto
``` -->

## Uso

1. **Preparar a base de dados:** Garanta que os arquivos corretos estejam no diretório ```data/```.
2. Alterar os emails no arquivo de gerentes, para variáções com o email do respectivo usuário.
3. Executar o programa:
```bash
python3 main.py
```
4. Verificar os Relatórios: Os relatórios gerados serão entregues para os emails descritos no arquivo de gerentes.
