# ETL com analise de dados

Projeto focado no uso de uma API do Banco Central, em que os dados são extraídos, tratados, carregados em um banco de dados na nuvem e utilizados em um dashboard.

## API do Banco Central

A API do Banco Central tem dados sobre estatisticas de transações Pix, quantidade e volume financeiro de transações Pix liquidadas mensalmente. Não inclui Pix liquidados nos livros do participante, isto é, transações não enviadas para liquidação no SPI. 

## Link da API

https://dadosabertos.bcb.gov.br/dataset/pix

https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/documentacao

## Preview do dashboard
https://github.com/user-attachments/assets/b3a967d5-e993-4925-9005-c3c6d3e9cdb2

## Como rodar o projeto

### Pré-requisitos
Certifique-se de possuir os seguintes requisitos instalados:

- Python 3.13 ou superior
- Conta no Supabase

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/https://github.com/pedrocobalquini/ETL_Dados_PIX.git
```

---

### 2. Criar e Ativar Ambiente Virtual

```bash
python -m venv .venv

.venv\Scripts\Activate
```

---

## 3. Instalar Dependências

Instale todas as bibliotecas necessárias através do arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### Configuração do Banco de Dados - Supabase

### 4. Criar Projeto no Supabase

1. Acesse o painel do Supabase.
2. Crie um novo projeto.

Após a criação, copie:

- URL do Projeto
- Chave do projeto do `service_role`
- Cole essas informações em um arquivo `.env`

---

### 5. Criar as Tabelas

No painel do Supabase:

1. Acesse **SQL Editor**
2. Clique em **New Query**
3. Execute o script abaixo:

```sql
CREATE TABLE transacoes_pix (
    id SERIAL PRIMARY KEY,
    data_transacao DATE NOT NULL,
    pagador VARCHAR(2) NOT NULL,
    receptor VARCHAR(2) NOT NULL,
    regiao_pagador VARCHAR(15) NOT NULL,
    regiao_receptor VARCHAR(15) NOT NULL,
    idade_pagador VARCHAR(20) NOT NULL,
    idade_receptor VARCHAR(20) NOT NULL,
    forma_iniciacao VARCHAR(15) NOT NULL,
    natureza_pix VARCHAR(3) NOT NULL,
    finalidade VARCHAR(30) NOT NULL,
    valor_pix NUMERIC(18,2) NOT NULL,
    quantidade_pix INTEGER NOT NULL,
    criado_em TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

Dados do Supabase para o Power BI
- Vá na aba `connect` e troque o método de conexão para `Session pooler`
- Copie os valores de host, porta e user

---

### Executando a Aplicação

### 6. Rodar o Processo ETL

Execute:

```bash
python src/main.py
```

---

### 7. Validar os Dados

Verifique no Supabase:

1. Table Editor
2. Selecione a tabela criada
3. Confirme se os registros foram carregados corretamente

---

### Atualização dos Dados

Sempre que o ETL for executado:

```bash
python src/main.py
```

- Os dados serão enviados automaticamente para o banco hospedado no Supabase, eles são atualizados a partir da data atual, sendo o último conjunto de dados disponíveis. 

- No Power BI basta atualizar o conjunto de dados para refletir as informações mais recentes.

- Os dados demoram para atualizar, mas isso é algo relacionado a política adotada pelo Bacen para os dados na api. Com base nisso, os dados gerados são sempre de 3 meses anteriores a data atual.

---



