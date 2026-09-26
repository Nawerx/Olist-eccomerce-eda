# Olist Brazilian E-Commerce EDA

This is my first large independent Data Analyst portfolio project. I want to
work through the analytical process myself and be able to explain each decision
I make along the way.

I chose the [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
because I want to learn how to work with a real dataset spread across several
CSV files. After reviewing the initial inspection results, I am now moving
into exploratory data analysis.

## Where I am now

I have completed my initial inspection and am now starting the analysis stage.

I reviewed all nine source CSV files using `inspect_data.py`. I looked at their
shape, sample rows, column names, inferred types, missing values, unique value
counts, and exact duplicate counts.

During this inspection, I did not identify defects that I considered to require
cleaning. I therefore decided to skip a separate cleaning stage and begin
analysis with the original data, rather than make changes without a reason.

This records the outcome of my initial review, not a guarantee that every
possible issue has been ruled out. If a specific problem appears during
analysis, I will investigate it and document any necessary change then.

I have not yet implemented the analysis or reached business conclusions.

## How I am organizing the work

I am keeping the structure small so that it follows the work I have actually
reached. I keep the original CSV files in `data/raw/` so that I can return to
the source when checking an observation.

```text
Olist-E-commerce-eda/
|-- README.md
|-- requirements.txt
|-- .gitignore
|-- data/
|   |-- raw/
|   |-- cleaned/
|   `-- processed/
`-- src/
    |-- config.py
    |-- inspect_data.py
    `-- data_cleaning.py
```

`config.py` contains project paths. `inspect_data.py` reads CSVs directly with
pandas and prints descriptive information. `data_cleaning.py` currently contains
only a note and is not part of my current workflow; it does not load, change,
or export data.

The `cleaned/` and `processed/` folders contain no datasets. I will use them
only if my work creates a need for them. I have not decided what their contents
should be.

## Running the inspection

I include the nine original CSV files in `data/raw/` so that the inspection
can be reproduced after cloning the repository without a separate download.
The dataset source is linked above. Generated datasets in `data/cleaned/` and
`data/processed/` remain excluded from Git.

From the `Olist-E-commerce-eda` directory, with the project's Python environment
activated:

```powershell
python -m pip install -r requirements.txt
python src/inspect_data.py olist_orders_dataset.csv
```

To inspect more than one file:

```powershell
python src/inspect_data.py olist_customers_dataset.csv olist_order_items_dataset.csv
```

To inspect every CSV currently in `data/raw/`:

```powershell
python src/inspect_data.py
```

The arguments are the actual filenames, not short table aliases. The script
prints observations without writing output files or applying transformations.
It uses pandas' inferred types. I will check whether they are appropriate
whenever an analysis requires a particular interpretation or calculation.

## How I am moving into analysis

I will develop the analysis step by step, letting questions emerge from the
data. I have not fixed a list of topics, metrics, or output tables in advance.
When I need to combine tables or calculate a measure, I will investigate the
relevant columns and relationships before making that decision.

## My progress record

I will update this README as I investigate the data, recording what I found,
what I decided, and why :)
