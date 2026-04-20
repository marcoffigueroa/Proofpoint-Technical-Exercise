# The Library's Lost Books

## Description

A library recently digitized its collection, but the digital catalog became corrupted. Some book records are missing crucial information or contain errors. This script reads a CSV file, cleans the data, removes duplicates, and presents an organized catalog.

## Input Format

The script reads `books.csv`, a comma-separated file with three columns:

```
Title,Author,Publication Year
```

## Data Issues Handled

| Issue | Fix Applied |
|---|---|
| Missing title | Row is discarded entirely |
| Missing author | Replaced with `"Author Unknown"` |
| Missing year | Replaced with `0` |
| Non-numeric year (e.g. `"unknown"`) | Replaced with `0` |
| Negative or far-future year | Replaced with `0` |
| Duplicate entries | Deduplicated, keeping one record |

Valid year range: `-3000` to the current year.

## Output

Books are displayed in two groups:

1. **Books with known author** — grouped alphabetically by author, then sorted by year within each author.
2. **Books with unknown author** — grouped by publication year.

## Usage

```bash
python biblioteca.py
```

Make sure `books.csv` is in the same directory as the script.

## File Structure

```
.
├── biblioteca.py   # Main script
├── books.csv       # Input catalog (may contain dirty data)
└── README.md
```