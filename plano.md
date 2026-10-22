# Python do Zero ao Especialista

Plano de estudos · outubro de 2026

## Como funciona o curso

São 30 tópicos em 4 níveis e 12 módulos, em cerca de 12 meses com 10–12 h por semana. Cada aula segue sempre as mesmas 15 etapas, e cada módulo fecha com uma avaliação completa.

**As 15 etapas de cada aula**

1. Explicação como se você tivesse 10 anos
2. Explicação técnica
3. Exemplos reais (código comentado)
4. Como empresas usam
5. Erros comuns
6. Analogias simples
7. Resumo
8. Flashcards
9. Mapa mental com setas
10. Exercícios básicos
11. Exercícios intermediários
12. Exercícios avançados
13. Mini projeto
14. Desafio empresarial
15. Correção das suas respostas (você envia no chat, eu corrijo linha a linha)

Toda aula abre com um cartão fixo: **→ Para que serve · → Onde é utilizado · → Salário médio da área · → Ferramentas relacionadas · → Empresas que utilizam.**

**Fechamento de cada módulo:** prova (15 questões + 2 práticas), gabarito comentado, resumo executivo, plano de revisão espaçada (1, 3, 7 e 21 dias), questões de entrevista e um estudo de caso empresarial.

**Como estudar comigo:** peça no chat “próxima aula” ou o nome do tópico. Responda os exercícios numerados (ex.: `B1`, `I2`, `A1`) e eu corrijo, dou nota de 0 a 10 e mostro a versão profissional do código. Só avance quando acertar 80% ou mais.

## Carreiras-alvo e salários 2026

As quatro carreiras usam a mesma base (Python + SQL + Git) e se separam a partir do nível Avançado. Faixas mensais CLT no Brasil, 2026; vagas remotas internacionais pagam 2 a 3 vezes mais.

| Carreira | Júnior (R$/mês) | Pleno (R$/mês) | Sênior (R$/mês) | Foco do trabalho |
| --- | --- | --- | --- | --- |
| Analista de Dados | 4.000 – 7.000 | 7.000 – 12.000 | 12.000 – 18.000 | SQL, Pandas, dashboards, perguntas de negócio |
| Engenheiro de Dados | 6.000 – 10.000 | 12.000 – 18.000 | 15.000 – 28.000 | Pipelines, nuvem, bancos de dados, Docker |
| Cientista de Dados | 5.000 – 8.500 | 9.000 – 15.000 | 16.000 – 25.000 | Estatística, Machine Learning, IA |
| Desenvolvedor Python | 4.000 – 7.000 | 8.000 – 14.000 | 15.000 – 25.000 | APIs (FastAPI), backend, automação |

Empresas como Itaú, Nubank e iFood costumam pagar acima dessas faixas. Valores do Engenheiro de Dados júnior e do Analista sênior são estimativas interpoladas das fontes abaixo.

Fontes: [Jobrise – Mercado tech 2026](https://jobrise.io/pt/blog/mercado-de-tech-no-brasil-2026-vai-contratar/) · [Jobrise – Cientista de Dados 2026](https://jobrise.io/pt/blog/salario-cientista-de-dados-brasil-2026/) · [Jobrise – Python Developer SP 2026](https://jobrise.io/pt/blog/python-developer-vagas-sao-paulo/) · [Monitor do Mercado – Dados e BI](https://monitordomercado.com.br/noticias/342106-traduzir-dados-complexos-em-lucro-para-as-empresas-coloca-o-cientista-de-dados-no-topo-da-lista-de-desejos-de-qualquer-recrutador-hoje-em-dia/)

## Nível 1 — Iniciante (meses 1–3)

Meta: escrever programas completos sozinho e versionar tudo no GitHub. Ao final você consegue automatizar planilhas simples e resolver testes de lógica de entrevistas júnior.

**Módulo 1 — Fundamentos** (lógica, variáveis, operadores, condicionais, loops)

**Módulo 2 — Estruturas e funções** (funções, listas, tuplas, dicionários, sets)

**Módulo 3 — Programas robustos** (arquivos, tratamento de erros, Git e GitHub)

| Tópico | Para que serve | Onde é utilizado | Ferramentas | Empresas |
| --- | --- | --- | --- | --- |
| Lógica de programação | Quebrar problemas em passos que o computador executa | Toda vaga de tecnologia; testes técnicos | Fluxogramas, pseudocódigo, VS Code | Todas; testes da Stone, Itaú, Mercado Livre |
| Variáveis | Guardar e nomear informações | Qualquer script ou sistema | Python 3.12+, VS Code, Jupyter | Todas |
| Operadores | Calcular, comparar e combinar condições | Regras de negócio, cálculos financeiros | Python, Jupyter | Bancos (juros), varejo (descontos) |
| Condicionais | Tomar decisões no código | Aprovação de crédito, alertas, validações | Python | Nubank, PicPay, seguradoras |
| Loops | Repetir tarefas milhares de vezes | Processar arquivos, linhas, clientes | Python, tqdm | Todas que processam lotes |
| Funções | Reaproveitar e organizar código | Toda base de código profissional | Python, pytest | Todas |
| Listas | Coleções ordenadas e mutáveis | Filas de pedidos, resultados de consultas | Python | iFood, Magalu |
| Tuplas | Dados fixos e seguros | Coordenadas, registros de banco | Python | Uber, 99 (geolocalização) |
| Dicionários | Dados por chave (como JSON) | APIs, configurações, cadastros | Python, json | Todas que usam APIs |
| Sets | Valores únicos e comparação de grupos | Remover duplicados, cruzar clientes | Python | E-commerces, CRMs |
| Arquivos | Ler e gravar TXT, CSV, JSON | Integrações, relatórios, logs | pathlib, csv, json | Bancos, ERPs (TOTVS) |
| Tratamento de erros | Programas que não quebram | Pipelines e sistemas em produção | try/except, logging | Todas em produção |
| Git e GitHub | Versionar e colaborar | 100% das equipes de software | Git, GitHub, VS Code | Microsoft, Google, Nubank |

**Salário de referência:** estágio R$ 1.500 – 3.000; júnior R$ 3.500 – 7.000 (Python + SQL + Git).

## Nível 2 — Intermediário (meses 4–6)

Meta: analisar dados reais de ponta a ponta — buscar, limpar, consultar e visualizar. Este é o nível que já qualifica para vagas de Analista de Dados júnior.

**Módulo 4 — POO e integrações** (Programação Orientada a Objetos, APIs, Web Scraping)

**Módulo 5 — Dados com Python** (SQL com Python, NumPy, Pandas)

**Módulo 6 — Visualização** (Matplotlib, Seaborn)

| Tópico | Para que serve | Onde é utilizado | Ferramentas | Empresas |
| --- | --- | --- | --- | --- |
| POO | Modelar sistemas com classes e objetos | Sistemas grandes, bibliotecas, APIs | class, dataclasses, pydantic | Todas com software próprio |
| APIs | Trocar dados entre sistemas | Cotações, pagamentos, CRM, ERP | requests, httpx, Postman | Banco Central (API PIX/Selic), Mercado Pago |
| Web Scraping | Coletar dados de sites | Monitorar preços, concorrentes, vagas | BeautifulSoup, Playwright, Scrapy | Buscapé, Zoom, consultorias |
| SQL com Python | Consultar bancos direto do código | Todo trabalho com dados | sqlite3, SQLAlchemy, PostgreSQL | Itaú, Ambev, Natura |
| NumPy | Cálculo numérico rápido | Base do Pandas e do ML | NumPy, Jupyter | Toda área de dados |
| Pandas | Limpar, transformar e analisar tabelas | Relatórios, análises, ETL | Pandas, Polars, Jupyter | Nubank, iFood, Magalu, Ambev |
| Matplotlib | Gráficos com controle total | Relatórios técnicos e científicos | Matplotlib | Pesquisa, bancos |
| Seaborn | Gráficos estatísticos bonitos e rápidos | Análise exploratória | Seaborn | Times de Data Science |

**Salário de referência:** Analista de Dados júnior R$ 4.000 – 7.000; pleno R$ 7.000 – 12.000.

## Nível 3 — Avançado (meses 7–9)

Meta: entregar produtos de dados que outras pessoas usam — relatórios automáticos, dashboards e integrações com BI. Aqui você escolhe sua trilha principal (Análise ou Engenharia).

**Módulo 7 — Excel e BI** (Excel com Python, Power BI com Python)

**Módulo 8 — Automação** (automação de tarefas: arquivos, e-mails, agendamentos, web)

**Módulo 9 — Apps de dados** (Streamlit, Dashboards)

| Tópico | Para que serve | Onde é utilizado | Ferramentas | Empresas |
| --- | --- | --- | --- | --- |
| Excel com Python | Ler, gerar e formatar planilhas automaticamente | Financeiro, controladoria, RH | openpyxl, xlsxwriter, Pandas, xlwings | Bancos, varejo, indústria, Big Four |
| Power BI com Python | Preparar dados e criar visuais avançados no BI | Relatórios gerenciais | Power BI, Power Query, scripts Python | Ambev, Raízen, Vale, Itaú |
| Automação de tarefas | Eliminar trabalho manual repetitivo | Backoffice, conciliações, relatórios diários | schedule, smtplib, Playwright, pyautogui | Todas (RPA é área própria) |
| Streamlit | Transformar scripts em apps web | Protótipos, ferramentas internas | Streamlit, Plotly | Startups, times de dados |
| Dashboards | Mostrar KPIs para decisão | Diretoria, vendas, operações | Streamlit, Dash, Plotly, Power BI | Toda empresa orientada a dados |

**Salário de referência:** Analista de Dados pleno R$ 7.000 – 12.000; Analista de BI júnior R$ 5.500 – 8.500.

## Nível 4 — Especialista (meses 10–12)

Meta: colocar modelos e serviços em produção, como em um time profissional. Este nível separa o júnior do pleno nas entrevistas.

**Módulo 10 — Machine Learning** (scikit-learn, avaliação de modelos, pipelines)

**Módulo 11 — IA Generativa** (LLMs via API, RAG, agentes simples)

**Módulo 12 — Produção** (FastAPI, Docker, deploy)

| Tópico | Para que serve | Onde é utilizado | Ferramentas | Empresas |
| --- | --- | --- | --- | --- |
| Machine Learning | Prever resultados a partir de dados | Crédito, churn, fraude, recomendação | scikit-learn, XGBoost, MLflow | Nubank, Itaú, iFood, Mercado Livre |
| IA Generativa | Gerar texto, resumir, responder sobre documentos | Atendimento, busca interna, automação de documentos | APIs de LLM (Claude, OpenAI), LangChain, bancos vetoriais | Bradesco, Itaú, startups de IA |
| FastAPI | Expor código e modelos como API | Backend, servir modelos de ML | FastAPI, Pydantic, Uvicorn | Netflix, Uber, Microsoft, fintechs |
| Docker | Rodar o mesmo ambiente em qualquer lugar | Deploy, pipelines, microserviços | Docker, Docker Compose, Kubernetes | Praticamente todas em nuvem |

**Salário de referência:** Cientista de Dados pleno R$ 9.000 – 15.000; Engenheiro de Dados pleno R$ 12.000 – 18.000; sênior até R$ 25.000 – 30.000.

## Cronograma semanal

Rotina de 11 horas por semana, um tópico a cada 1–2 semanas. Constância vence intensidade: 1h30 por dia rende mais que 10 horas num só sábado.

| Dia | Tempo | Atividade |
| --- | --- | --- |
| Segunda | 1h30 | Etapas 1–7: teoria, exemplos, erros comuns, resumo |
| Terça | 1h30 | Digitar e rodar todos os exemplos (nunca copiar e colar) |
| Quarta | 1h30 | Exercícios básicos e intermediários + envio para correção |
| Quinta | 1h30 | Exercícios avançados + revisão dos flashcards |
| Sexta | 1h | Revisão espaçada de tópicos antigos |
| Sábado | 3h | Mini projeto + desafio empresarial, commit no GitHub |
| Domingo | 1h | Descanso ativo: ler código de outros no GitHub ou um artigo técnico |

**Regras de ouro**

- Escreva código todos os dias, mesmo 15 minutos.
- Errou? Leia a mensagem de erro inteira antes de pedir ajuda.
- Cada mini projeto vira um repositório com README.
- Estude SQL em paralelo desde o Módulo 3: ele aparece em quase toda vaga de dados.

## Portfólio para o GitHub

Ao final você terá 8 projetos publicados, cada um ligado a uma carreira-alvo. Recrutadores olham o GitHub antes do currículo em vagas júnior.

| # | Projeto | Nível | Carreira que comprova | Tecnologias |
| --- | --- | --- | --- | --- |
| 1 | Calculadora de salário líquido (INSS + IR) | Iniciante | Dev Python | Funções, condicionais |
| 2 | Organizador automático de pastas e relatórios | Iniciante | Automação | Arquivos, erros, Git |
| 3 | Monitor de preços com alerta por e-mail | Intermediário | Engenharia de Dados | Scraping, APIs, SQL |
| 4 | Análise de vendas de um e-commerce (dataset Olist) | Intermediário | Analista de Dados | Pandas, SQL, Seaborn |
| 5 | Relatório Excel mensal gerado com um clique | Avançado | Analista / BI | openpyxl, Pandas |
| 6 | Dashboard de KPIs em Streamlit publicado online | Avançado | Analista de Dados | Streamlit, Plotly |
| 7 | Modelo de previsão de churn com API | Especialista | Cientista de Dados | scikit-learn, FastAPI |
| 8 | Assistente de perguntas sobre PDFs (RAG) em Docker | Especialista | Dev Python / IA | LLM API, FastAPI, Docker |

## Aula 1 — Lógica de Programação

Lógica é a habilidade de transformar um problema em passos pequenos, claros e em ordem. É a base de todos os outros 29 tópicos.

**→ Para que serve:** resolver qualquer problema com código. **→ Onde é utilizado:** em toda vaga de tecnologia e em todos os testes técnicos. **→ Salário médio:** júnior R$ 3.500 – 7.000. **→ Ferramentas:** pseudocódigo, fluxogramas (draw.io), Python, VS Code. **→ Empresas:** todas; Itaú, Mercado Livre e Stone usam testes de lógica na seleção.

### 1. Como se você tivesse 10 anos

O computador é um robô muito obediente, mas que não pensa sozinho. Se você mandar “faz um sanduíche”, ele trava. Você precisa dizer: pegue o pão, abra o pão, passe manteiga, coloque o queijo, feche o pão. Lógica é aprender a dar ordens tão claras que até o robô entende.

### 2. Explicação técnica

Um **algoritmo** é uma sequência finita e ordenada de instruções que leva uma **entrada** a uma **saída**. Todo algoritmo combina só três estruturas:

- **Sequência:** instruções executadas uma após a outra.
- **Decisão (seleção):** escolher um caminho conforme uma condição verdadeira ou falsa (`if`).
- **Repetição (iteração):** repetir um bloco enquanto uma condição valer (`for`, `while`).

O processo profissional é: entender o problema → definir entrada e saída → escrever em pseudocódigo → testar à mão → só então codificar.

### 3. Exemplos reais

```python
# Problema: dizer se um aluno foi aprovado (média >= 7)
# Entrada: duas notas | Saída: mensagem

nota1 = float(input("Nota 1: "))   # sequência
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2) / 2

if media >= 7:                       # decisão
    print(f"Aprovado com média {media:.1f}")
else:
    print(f"Reprovado com média {media:.1f}")
```

```python
# Repetição: somar as vendas da semana
vendas = [1200, 950, 1800, 700, 2100]
total = 0
for valor in vendas:
    total = total + valor
print("Total da semana:", total)    # 6750
```

### 4. Como empresas usam

- **Banco (Nubank, Itaú):** SE renda ≥ 3× parcela E score ≥ 600 ENTÃO aprova crédito SENÃO recusa.
- **iFood:** PARA CADA entregador próximo, calcule a distância e escolha o menor tempo estimado.
- **E-commerce (Magalu):** SE carrinho ≥ R$ 199 ENTÃO frete grátis.
- **RH:** PARA CADA funcionário, calcule horas extras e gere o holerite.

### 5. Erros comuns

- Começar a programar antes de entender o problema.
- Esquecer casos extremos: nota negativa, lista vazia, divisão por zero.
- Errar a ordem dos passos (calcular a média antes de ler as notas).
- Usar `>` quando o certo era `>=` (aluno com 7,0 reprovado).
- Criar loop infinito ao esquecer de atualizar a condição do `while`.

### 6. Analogias

- **Receita de bolo** = algoritmo (ingredientes = entrada, bolo = saída).
- **Semáforo** = decisão (verde segue, vermelho para).
- **Lavar a louça prato por prato** = repetição.
- **GPS** = vários caminhos possíveis; lógica é escolher o melhor.

### 7. Resumo

Lógica = entrada → processamento → saída, usando sequência, decisão e repetição. Pense primeiro, codifique depois e sempre teste os casos extremos.

### 8. Flashcards

| Frente | Verso |
| --- | --- |
| O que é um algoritmo? | Sequência finita e ordenada de passos que resolve um problema |
| Quais as 3 estruturas da lógica? | Sequência, decisão e repetição |
| O que é pseudocódigo? | O algoritmo escrito em linguagem humana, antes do código |
| O que é caso extremo? | Entrada incomum que pode quebrar o programa (vazio, zero, negativo) |
| Por que testar à mão? | Para achar erros de lógica antes de escrever código |
| Diferença entre `for` e `while`? | `for` repete um número conhecido de vezes; `while` repete enquanto uma condição for verdadeira |

### 9. Mapa mental

```text
LÓGICA DE PROGRAMAÇÃO
 ├─→ Problema → Entrada → Processamento → Saída
 ├─→ Sequência → um passo após o outro
 ├─→ Decisão → if / elif / else → condição Verdadeira ou Falsa
 ├─→ Repetição → for (quantidade conhecida)
 │             → while (até a condição mudar) → cuidado: loop infinito
 └─→ Método → entender → pseudocódigo → teste à mão → código → testar extremos
```

### 10. Exercícios básicos

- **B1.** Escreva em pseudocódigo os passos para sacar dinheiro num caixa eletrônico.
- **B2.** Leia um número e diga se ele é par ou ímpar.
- **B3.** Leia a idade de uma pessoa e diga se ela pode votar (16+), se é obrigatório (18 a 70) ou se é facultativo.

### 11. Exercícios intermediários

- **I1.** Leia 5 números e mostre o maior e o menor, sem usar `max()` e `min()`.
- **I2.** Mostre a tabuada de qualquer número de 1 a 10.
- **I3.** Peça uma senha até o usuário acertar, com no máximo 3 tentativas.

### 12. Exercícios avançados

- **A1.** Diga se um número é primo, testando divisores só até a raiz quadrada dele. Explique por que isso basta.
- **A2.** Calcule o troco de uma compra usando o menor número de cédulas e moedas (R$ 100, 50, 20, 10, 5, 2, 1).
- **A3.** Implemente o jogo “adivinhe o número” (1 a 100) que diz “maior” ou “menor” e conta as tentativas.

### 13. Mini projeto — Calculadora de salário líquido

Leia o salário bruto, desconte INSS e IR por faixas (use as tabelas oficiais vigentes) e mostre bruto, descontos e líquido. Trate entradas inválidas (texto, valor negativo). Publique no GitHub com um README.

### 14. Desafio empresarial — Regras de crédito

Uma fintech aprova empréstimos assim: renda ≥ R$ 2.000; parcela ≤ 30% da renda; sem dívida em atraso; idade entre 18 e 75. Escreva o pseudocódigo e depois o Python que recebe os dados do cliente e responde “Aprovado” ou o **motivo exato** da recusa. Liste 5 casos de teste, incluindo extremos (renda exatamente R$ 2.000, parcela exatamente 30%).

### 15. Correção

Envie no chat suas respostas com o código (ex.: “B1: …”). Corrijo cada uma com nota de 0 a 10, aponto erros de lógica e de estilo e mostro a solução como um profissional escreveria.
