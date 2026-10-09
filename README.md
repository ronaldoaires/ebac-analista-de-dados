# Data Analyst Career Course — EBAC

> A selection of exercises, challenges and projects from the **"Profissão: Analista de Dados" (Data Analyst Career)** program at **EBAC** (Escola Britânica de Artes Criativas & Tecnologia), a Brazilian online school for technology and creative careers.

**Author:** Ronaldo Aires — [GitHub](https://github.com/ronaldoaires) · [LinkedIn](https://www.linkedin.com/in/ronaldoaires/)

---

## About this repository

This repository collects **selected examples** of the exercises, challenges and projects I did while taking the Data Analyst program at EBAC. The goal of the course is to give students a solid foundation in the concepts and techniques needed to work as a data analyst.

**Important:** this is not the full record of the course. The program covered much more than what is stored here, and I learned far beyond these files. The examples below are a sample that shows how I applied the topics in practice. You can see the full program on the [official EBAC course page](https://ebaconline.com.br/new/curso-de-analista-de-dados).

### Language note

The course was taught in **Brazilian Portuguese**, so the exercise statements, file names, variable names, comments and outputs in this repository are mostly in Portuguese. The folder names below are translated for convenience.

## What the course covers

The program is much broader than the examples stored here. Based on the [official course page](https://ebaconline.com.br/new/curso-de-analista-de-dados), it covers:

- **Analytics fundamentals and the data lifecycle:** the role of the data analyst compared to data engineers and data scientists, common data formats (CSV, JSON, XML, Parquet), and the full lifecycle from collection to delivery, including data quality and governance
- **Programming logic, ETL and version control:** Python fundamentals (variables, conditionals, loops, functions), ETL vs. ELT, and Git/GitHub to version scripts, queries and deliverables
- **Statistics for business decisions:** descriptive and inferential statistics, hypothesis testing, linear regression and ANOVA, always tied to real business questions
- **Python for data cleaning, preparation and visualization:** handling missing values, outliers and inconsistencies, normalization, collecting data from public APIs (such as IBGE and the Brazilian Central Bank) in compliance with LGPD, and exploring results with Matplotlib, Seaborn and Plotly
- **Advanced Excel and Google Sheets:** conditional and lookup formulas, pivot tables, Power Query, and Google Sheets collaboration features (QUERY, IMPORTRANGE, Looker Studio)
- **SQL for analytical queries:** JOINs, aggregations (GROUP BY, HAVING), window functions and CTEs, in PostgreSQL and BigQuery
- **Data modeling and DAX in Power BI:** star schema modeling, DAX measures (including time intelligence) and performance tuning with Performance Analyzer
- **Visual storytelling and dashboard security:** dashboards with visual hierarchy and executive narrative, row-level security (RLS) and workspace permissions
- **AI applied to Power BI:** Key Influencers, Decomposition Tree, Q&A, Smart Narrative, Anomaly Detection and Copilot, always with critical review of the results
- **Communication and agile management of BI projects:** turning ambiguous requests into metrics and dashboards, prioritizing with Scrum and Kanban, and presenting results to different stakeholders
- **Prompt engineering and generative AI for analysts:** structuring effective prompts, recognizing risks such as hallucination and bias, and using generative AI to support analysis with manual review
- **Enterprise-scale data infrastructure:** corporate ETL pipelines with Pentaho and Apache Hop, low-code automation with n8n, and cloud data architecture (Azure Data Factory, Data Lake, Synapse, Databricks and PySpark)

This repository only includes examples of some of these topics.

## Repository structure

| Folder | Meaning (Portuguese → English) | Content (selected examples) |
|---|---|---|
| `Atividades/` | *Atividades* = Activities | Some of the exercises done during the lessons |
| `desafios/` | *Desafios* = Challenges | Some of the practical challenges (for example, `02-gerador-de-tabuada.py`, a multiplication table generator) |
| `projetos/` | *Projetos* = Projects | Selected projects that apply skills learned in the course |
| `requirements.txt` | | Python packages needed to run the files |

## Getting started

### Requirements

- [Git](https://git-scm.com/downloads)
- [Python 3](https://www.python.org)

### Installation

```bash
# Clone the repository
git clone https://github.com/ronaldoaires/ebac-analista-de-dados.git
cd ebac-analista-de-dados

# (Optional) create and activate a virtual environment
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

# Install the dependencies
pip install -r requirements.txt
```

### Running a file

Navigate to the folder that contains the file and run it with Python. For example:

```bash
cd desafios
python 02-gerador-de-tabuada.py
```

Adapt the commands to your operating system and to the folder where you cloned the repository.

## How this fits with my current work

My main work today is building modern web applications with Laravel, Filament, Livewire and Tailwind. This course gave me a structured foundation in data analysis, Python, SQL, statistics and BI, skills that complement software development whenever a project needs to measure, report and make decisions based on data.

You can see my development work here:

- **[blog-institucional](https://github.com/ronaldoaires/blog-institucional)** — Laravel 13, Filament and AI-assisted development (code and docs in English)
- **[curso-de-php8](https://github.com/ronaldoaires/curso-de-php8)** — a blog system in plain PHP 8 with MVC, Composer and Twig

## About the author

I'm Ronaldo Aires, a developer and civil engineer based in Mato Grosso, Brazil. I build modern web applications and create courses that turn real project experience into clear, practical learning material. I'm open to international opportunities, collaborations and remote work.

- GitHub: [github.com/ronaldoaires](https://github.com/ronaldoaires)
- LinkedIn: [linkedin.com/in/ronaldoaires](https://www.linkedin.com/in/ronaldoaires/)
- Email: [ceo@unset.com.br](mailto:ceo@unset.com.br)

## License

Released under the MIT License. See the [LICENSE](LICENSE) file for details.
