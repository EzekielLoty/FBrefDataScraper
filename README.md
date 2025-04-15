# FBref Data Scraper

This is a simple data scraping tool that extracts football player statistics tables from [FBref](https://fbref.com/) team pages. It parses raw HTML files (saved directly from the FBref website) and outputs structured CSV files with player data for further analysis.

## 📁 Project Structure

```
FBrefDataScraper/
│
├── libraries/
│   ├── requirements.txt       # Python dependencies
│── tott2425.txt           # HTML content of a team's page (e.g., Tottenham Hotspur 2024/25)
│── fbrefdata.py           # Main scraping script
```

## 🔧 Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/EzekielLoty/FBrefDataScraper/
   ```

2. Install dependencies:
   ```bash
   pip install -r libraries/requirements.txt
   ```

3. Replace `tott2425.txt` with HTML from any FBref team stats page.

   - Go to a team page like: https://fbref.com/en/squads/361ca564/Tottenham-Hotspur-Stats
   - Open **Developer Tools** (Right-click > Inspect or `F12`)
   - Copy the full HTML of the page (`<html>...</html>`)
   - Save it as a `.txt` file (e.g., `arsenal2425.txt`)

4. Run the scraper:
   ```bash
   python fbrefdata.py
   ```

## 📊 Output

The script processes all available player statistical tables and outputs CSV files named after each section (e.g., `standard_stats.csv`, `shooting.csv`, etc.). These files are saved in the current working directory.

## 📌 Features

- Parses player statistics from FBref HTML pages
- Automatically handles multi-level headers
- Cleans and standardizes age data
- Drops irrelevant summary rows like "Squad Total" and "Opponent Total"
- Exports structured `.csv` files for each statistics table

## ⚠️ Notes

- **FBref has restricted access to their site via requests**, so this scraper uses saved HTML instead of fetching it live.
- Be sure to copy the complete page source for accurate parsing.
- This tool works best with unmodified HTML straight from the FBref page.

## 🧪 Requirements

- Python 3.7+
- `pandas`
- `beautifulsoup4`
- `numpy`
