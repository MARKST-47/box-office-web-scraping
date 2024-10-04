import os
import requests
import datetime
import pandas as pd
from requests_html import HTML

BASE_DIR = os.path.dirname(__file__)

now = datetime.datetime.now()
year = now.year

def url_to_txt(url, year):
    # Create 'html' directory to save HTML files
    html_dir = os.path.join(BASE_DIR, 'html')
    os.makedirs(html_dir, exist_ok=True)
    
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        filename = f'world-{year}.html'
        filepath = os.path.join(html_dir, filename)
        # Check if the file already exists
        if not os.path.exists(filepath):
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html_text)
        return html_text
    return ''

def parse_and_extract(url, name):
    html_text = url_to_txt(url, name)

    r_html = HTML(html=html_text)
    table_class = ".imdb-scroll-table"
    r_table = r_html.find(table_class)
    
    table_data = []
    if len(r_table) == 1:
        parsed_table = r_table[0]
        rows = parsed_table.find("tr")
        header_row = rows[0]
        header_cols = header_row.find("th")
        header_names = [x.text for x in header_cols]
        
        path = os.path.join(BASE_DIR, 'data')
        os.makedirs(path, exist_ok=True)
        filepath = os.path.join(path, f'movies_{name}.csv')
        
        # Check if the CSV file already exists
        if not os.path.exists(filepath):
            for row in rows[1:]:
                cols = row.find("td")
                row_data = []
                for col in cols:
                    row_data.append(col.text)
                table_data.append(row_data)

            df = pd.DataFrame(table_data, columns=header_names)
            df.to_csv(filepath, index=False)

def get_movies_by_year():
    year_input = input("Enter the year (e.g., 2019): ")
    assert len(year_input) == 4  # Ensure a valid year format
    url = f'https://www.boxofficemojo.com/year/world/{year_input}'
    parse_and_extract(url, name=year_input)

if __name__ == "__main__":
    get_movies_by_year()
