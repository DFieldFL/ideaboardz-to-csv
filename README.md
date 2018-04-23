# Ideaboardz to CSV
This project converts an Ideaboardz to a CSV by putting stickies from a section in a single CSV column separated by a newline.

## Setup
1. Install dependencies `pip install -r requirements.txt`
2. Install Firefox browser
3. Ensure geckodriver is in your PATH. Driver can be download here https://github.com/mozilla/geckodriver/releases
4. Copy `config.template.py` to `config.py` and modify `GECKO_DRIVER` location match where you put the geckodriver

## Run Application
1. `python exportToCsv.py`
2. When prompted enter in the full URL to your Ideaboardz
3. The output will be in the current directory named `out.csv`
