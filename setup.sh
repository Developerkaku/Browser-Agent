#!/usr/bin/env bash
set -e

python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install browser-use
pip install playwright
plarwright install chromium
