# HarbourDesk

HarbourDesk is an order and payment operations application with a local identity provider, order history, wallet, notifications, and reporting.

## Run

From the project directory, run `python3 -m app` or double-click [HarbourDesk.command](HarbourDesk.command). Open **http://localhost:8010** in Firefox. The identity provider runs at **http://127.0.0.1:8011**. Press Control-C in the server terminal to stop both services.

Python 3.9+ is required. The SQLite database is stored at `runtime/lab.sqlite3` and is initialized on first run. Set `LAB_DB` to use a separate database.

## Development

Run `python3 -m unittest discover -s tests -v` for the application tests. See the [product rules](docs/PRODUCT.md), [API](docs/API.md), and [data dictionary](docs/DATA-MODEL.md).
