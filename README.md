# Movie Data Scraper

This project is a Python script that scrapes box office data from Box Office Mojo for a specified year. The script retrieves the data, saves it as an HTML file, and extracts the relevant information into a CSV file.

## Features

- Scrapes box office data for movies released in a specified year.
- Saves the raw HTML content to a local directory.
- Parses the HTML to extract movie data and saves it in CSV format.
- Automatically creates necessary directories for storing HTML and CSV files.

## Requirements

- Python 3.x
- `requests`
- `requests-html`
- `pandas`

You can install the required packages using pip:

```bash
pip install requests requests-html pandas
```

## Usage

1. Clone this repository or download the script.
2. Navigate to the directory containing the script.
3. Run the script using Python:

   ```bash
   python scrape.py
   ```

4. When prompted, enter the desired year (e.g., `2024`) to fetch box office data for that year.

## Directory Structure

The script will create the following directory structure:

```
/your_project_directory
│
├── html/                # Contains saved HTML files of box office data
│   └── world-{year}.html
│
├── data/                # Contains extracted movie data in CSV format
│   └── movies_{year}.csv
│
└── your_script_name.py  # The main script file
```

## Example

If you run the script and input `2019`, it will create:

- An HTML file: `html/world-2019.html`
- A CSV file: `data/movies_2019.csv`

## Notes

- Ensure you have an active internet connection when running the script as it fetches data from an online source.
- The script checks for existing files before saving new ones to avoid overwriting.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project uses data from [Box Office Mojo](https://www.boxofficemojo.com/).
