# Olist Brazilian E-Commerce EDA

This is my first large independent Data Analyst portfolio project. I want to
work through the analytical process myself and be able to explain each decision
I make along the way.

I chose the [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
because I want to learn how to work with a real dataset spread across several
CSV files. I have now completed a second inspection focused on understanding
what one row represents in each table and recording my observations.

## Where I am now

I have completed my initial and secondary data inspections.

I reviewed all nine source CSV files using `inspect_data.py`. I looked at their
shape, sample rows, column names, inferred types, missing values, unique value
counts, and exact duplicate counts.

During the second inspection, I documented my current understanding of each
table's grain (what one row represents) in [Data Model Notes](docs/data_model.md).
These notes cover all nine source tables and record observations that I will
revisit as I investigate the data further.

I found **261,831 exact duplicate rows** in the geolocation table. I have not
yet decided whether to remove them; that decision depends on how I use the
table. No cleaning transformations have been implemented.


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
|-- docs/
|   `-- data_model.md
`-- src/
    |-- config.py
    |-- inspect_data.py
    `-- data_cleaning.py
```

`config.py` contains project paths. `inspect_data.py` reads CSVs directly with
pandas and prints descriptive information. `data_cleaning.py` currently contains
only a note and is not part of my current workflow; it does not load, change,
or export data.

`docs/data_model.md` holds my table-grain notes and inspection findings,
which I moved out of `inspect_data.py`.

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

## What comes next

My next focus is to investigate candidate keys and relationships between
tables, checking uniqueness and cardinality before choosing joins. I will
revisit the geolocation duplicates when I understand how I need that table.

## My progress record

I will update this README as I investigate the data, recording what I found,
what I decided, and why :)
