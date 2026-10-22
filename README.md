# Python do Zero ao Especialista

Plano de estudos de 12 meses, em 4 níveis, para trabalhar como **Analista de Dados, Engenheiro de Dados, Cientista de Dados ou Desenvolvedor Python**.

| Arquivo | O que é |
| --- | --- |
| [`index.html`](index.html) | Site do plano (sumário, níveis, cronograma, portfólio e Aula 1) |
| [`slides.html`](slides.html) | Apresentação de 20 slides (setas ← → ou deslize no celular, `f` = tela cheia) |
| [`python-do-zero-ao-especialista.pdf`](python-do-zero-ao-especialista.pdf) | Plano completo em PDF (A4) |
| [`slides.pdf`](slides.pdf) | Slides em PDF (16:9) |
| [`plano.md`](plano.md) | Texto-fonte do plano em Markdown |

## Níveis

1. **Iniciante** (meses 1–3): lógica, variáveis, operadores, condicionais, loops, funções, listas, tuplas, dicionários, sets, arquivos, erros, Git
2. **Intermediário** (meses 4–6): POO, APIs, Web Scraping, SQL com Python, NumPy, Pandas, Matplotlib, Seaborn
3. **Avançado** (meses 7–9): Excel com Python, Power BI com Python, automação, Streamlit, dashboards
4. **Especialista** (meses 10–12): Machine Learning, IA Generativa, FastAPI, Docker

## Regerar o site e o PDF

Edite `plano.md` e rode:

```bash
pip install markdown playwright
playwright install chromium
python scripts/build.py
```
