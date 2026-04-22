# 📊 DataSales — Sistema de Gestão de Vendas

Sistema web desenvolvido com **Django** para gerenciamento de vendas, produtos e vendedores, com dashboard dinâmico para análise de dados em tempo real.

---

## 🚀 Funcionalidades

* ✔ Cadastro de produtos
* ✔ Cadastro de vendas
* ✔ Cadastro de vendedores
* ✔ Edição e consulta de dados
* ✔ Controle automático de estoque
* ✔ Dashboard com métricas em tempo real
* ✔ Ranking dos 5 melhores vendedores
* ✔ Top 5 produtos mais vendidos
* ✔ Gráfico interativo de vendas por produto

---

## 🧠 Dashboard

O sistema possui um painel analítico que exibe:

* 📈 Total de vendas
* 💰 Faturamento total
* 🏆 Top 5 vendedores
* 📦 Top 5 produtos
* 📊 Gráfico de vendas por produto

Os dados são atualizados automaticamente conforme novas vendas são registradas.

---

## 🛠️ Tecnologias Utilizadas

* **Back-end:** Python + Django
* **Banco de Dados:** SQLite
* **Front-end:** HTML, CSS, JavaScript
* **Gráficos:** Chart.js

---

## ⚙️ Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/felipepassos068/DataSales.git
cd DataSales
```

---

### 2. Criar ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Executar o projeto

```bash
python manage.py runserver
```

Acesse no navegador:

http://127.0.0.1:8000/

---

## 🗄️ Banco de Dados

⚠️ **Atenção**

O arquivo `db.sqlite3` foi incluído **apenas para fins de teste e demonstração**, contendo dados já populados.

Em um ambiente profissional, o banco de dados não deve ser versionado.

---

## 📂 Estrutura do Projeto

```
DataSales/
│
├── config/              # Configurações do Django
├── vendas/              # App principal (models, views, lógica)
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── db.sqlite3           # Banco de dados (teste)
├── manage.py
├── requirements.txt
└── README.md
```

---

## 👨‍💻 Autores

* Felipe Passos de Albuquerque
* Wdson Rhayron

---

## 🧩 Contribuições

* **Felipe Passos de Albuquerque**

  * Desenvolvimento do back-end com Django
  * Modelagem do banco de dados
  * Implementação das regras de negócio (vendas, estoque e validações)
  * Criação do dashboard e APIs para consumo no front-end
  * Integração entre back-end e front-end

* **Wdson Rhayron**

  * Desenvolvimento do front-end
  * Estruturação das páginas e navegação
  * Interface e experiência do usuário (UI/UX)
  * Integração visual com o sistema

---

## 📈 Possíveis melhorias

* 🔐 Sistema de autenticação (login de usuários)
* 🎨 Interface mais moderna
* 🌐 Criação de API REST completa
* ☁️ Deploy em produção
* 📊 Filtros avançados no dashboard

---

## ⭐ Considerações finais

Este projeto simula um sistema real de gestão de vendas, cobrindo desde o cadastro até a análise de dados, com foco em prática de desenvolvimento web e integração entre front-end e back-end.

---
