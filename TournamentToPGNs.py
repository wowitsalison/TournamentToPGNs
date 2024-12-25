from bs4 import BeautifulSoup
import requests
import os


tournament_link = "https://www.chessgames.com/perl/chess.pl?tid=53788" # Must be chessgames.com tournament link
save_location = r"\YOUR\FILE\PATH\HERE"
tournament_name = "Zukertort_Steinitz_1886" # Avoid spaces for file naming

# Include a User-Agent header to identify the client
headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36" }


def download_pgns(tournament_url, save_location, headers):
    # Fetch the tournament page
    tournament_response = requests.get(tournament_url, headers=headers)
    try:
        tournament_soup = BeautifulSoup(tournament_response.text, 'html.parser')
        # Find all links on page
        game_links = tournament_soup.find_all("a")
        # Filter out all links but game links
        game_links = [link.get('href') for link in game_links if link.get('href') and "www.chessgames.com/perl/chessgame?gid=" in link.get('href')]

        # Cycle through each game individually
        for counter, link in enumerate(game_links, start=1):
            game_response = requests.get(link, headers=headers)
            try:
                # Fetch the game page
                game_soup = BeautifulSoup(game_response.text, 'html.parser')

                # Find download link
                download_link = game_soup.find("a", href=lambda href: href and "downloadGamePGN" in href).get('href')
                download_link = f"https://www.chessgames.com{download_link}"

                # Fetch the PGN
                pgn_response = requests.get(download_link, headers=headers)

                # Save the PGN
                filename = os.path.join(save_location, f"{tournament_name}_{counter:02d}.pgn")
                with open(filename, "w") as file:
                    file.write(pgn_response.text)
                    print(f"Download finished: {tournament_name} game {counter:02d}")

            except Exception as e:
                print(f"Error downloading PGN: {e}")

        print("Tournament download complete.")

    except Exception as e:
        print(f"Error fetching tournament data: {e}")


if __name__ == "__main__":
    download_pgns(tournament_link, save_location, headers)