#!/bin/sh
set -eu
HD_PRODUCT_ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$HD_PRODUCT_ROOT"
exec ./lab preview
