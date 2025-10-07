#!/usr/bin/env bash
set -e

python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install uv
uv pip install browser-use
uvx playwright install chromium
