#!/bin/sh
set -eu
HD_PRODUCT_ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$HD_PRODUCT_ROOT"
if [ -n "${LAB_PYTHON:-}" ]; then
  exec "$LAB_PYTHON" -m app
fi
exec python3 -m app
