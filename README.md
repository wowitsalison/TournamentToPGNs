# TournamentToPGNs
This Python script allows you to download all PGN files from a tournament page on chessgames.com. It scrapes the tournament page for game links, retrieves each game's PGN, and saves them locally.

# Features
- Downlaods all PGNs from a specified chessgames.com tournament page
- Saves PGNs with a consistent naming format
- User-Agent header included to avoid being blocked by the chessgames.com server

# Requirements
- Python 3
- Required Python libraries:
  - requests
  - beautifulsoup4
  - os
 
# Installation
1. Clone or download this repository
2. Install the required python packages:
   `pip install requests beautifulsoup4`

# Usage
1. Set the following variables in the script:
   - `tournament_link`: The URL of the chessgames.com tournament page (e.g., `https://www.chessgames.com/perl/chess.pl?tid=53788`).
   - `save_location`: The file path where the PGNs will be saved (e.g., `C:\Users\YourName\Desktop\PGNs`).
   - `tournament_name`: A descriptive name for the tournament (e.g., `Zukertort_Steinitz_1886`). Avoid spaces as this will be used in the file names.
2. Run the script: `python pgn_downloader.py`

# Output
- Each PGN file will be saved in the specified `save_location` with the format: \
  `<tournament_name>_<game_number>.pgn`\
  Example: \
  `Zukertort_Steinitz_1886_01.pgn,
  Zukertort_Steinitz_1886_02.pgn`

# Notes
- Ensure the `save_location` directory exists before running the script
- Only works with chessgames.com tournament pages
- The script includes error handling for missing or invalid game links but may not handle all edge cases

# Improvements
Potential enhancements for this project:
- Add further edge case handling
- Add functionality to automatically create the `save_location` directory if it does not exist
- Add functionality to automatically name tournament from tournament page

# License
This project is licensed under the MIT License. See the LICENSE file for details.
