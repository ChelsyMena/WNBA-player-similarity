import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

class BasketballReference:
    """
    Scrapes WNBA data from https://www.basketball-reference.com/ and stores it in a Pandas DataFrame.
    """

    __stat_types = ['per_game_stats', 'totals_stats', 'per_minute_stats', 'per_poss_stats', 'advanced_stats']

    def __init__(self):
        pass  # No need for super() since we removed SportsReference dependency

    @property
    def stat_types(self):
        """Returns a list of possible stat types to scrape."""
        return BasketballReference.__stat_types

    def get_season_player_stats(self, year=None, years=None, stat_type=None, stat_types=None):
        if years is None:
            years = [year]
        if stat_types is None:
            stat_types = [stat_type]

        all_data = []
        for y in years:
            for st in stat_types:
                url = self._create_url(y, st)
                print(f"Fetching data from: {url}")
                df = self._scrape_table(url)
                if df is not None:
                    df["Season"] = y
                    df["Stat Type"] = st
                    all_data.append(df)

        return pd.concat(all_data, ignore_index=True) if all_data else None

    def _create_url(self, year, stat_type):
        """Generates the URL for the given year and stat type."""
        stat_type = re.match(r'(.*)(_stats)', stat_type)[1]
        return f'https://www.basketball-reference.com/wnba/years/{year}_{stat_type}.html#{stat_type}'

    def _scrape_table(self, url):
        """Scrapes the stats table from the given URL."""
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table")

        if table:
            # Clean the table HTML
            for br in table.find_all("br"):
                br.replace_with("\n")

            df = pd.read_html(str(table))[0]
            df = df[df.Player != "Player"]  # Remove duplicate headers
            df = df.loc[:, ~df.columns.str.contains("Unnamed")]  # Remove empty columns
            return df
        else:
            print(f"No table found at {url}")
            return None


if __name__ == '__main__':

    import time
    import warnings
    warnings.filterwarnings("ignore")

    import os
    loc = os.path.dirname(os.path.abspath(__file__))

    wnba_stats = BasketballReference()
    stat_types = ['per_poss_stats']

    for start_year in range(1997, 2025, 4):

        end_year = min(start_year + 4, 2025)

        df = wnba_stats.get_season_player_stats(years=[x for x in range(start_year, end_year)], stat_types=stat_types)

        file_path = os.path.join(loc, f'data_{start_year}_{end_year-1}.csv')
        df.to_csv(file_path, index=False)

        print(f"Data from {start_year} to {end_year-1} saved.")

        time.sleep(5)  # Wait for 5 seconds before the next iteration
