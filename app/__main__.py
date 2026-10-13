"""Run the HarbourDesk web application."""
import argparse
import json
from urllib.request import urlopen

from .http import serve


def main():
    parser = argparse.ArgumentParser(description="Run HarbourDesk")
    parser.add_argument("--port", type=int, default=8010)
    parser.add_argument("--provider-port", type=int, default=8011)
    args = parser.parse_args()
    try:
        with urlopen(f"http://localhost:{args.port}/health", timeout=1) as response:
            if json.load(response).get("service") == "HarbourDesk":
                print(f"HarbourDesk is already running at http://localhost:{args.port}")
                return
    except (OSError, ValueError):
        pass
    serve(args.port, args.provider_port)


if __name__ == "__main__":
    main()
