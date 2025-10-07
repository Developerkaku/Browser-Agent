#!/usr/bin/env bash
set -e

pip install --upgrade pip
pip install browser-use
pip install playwright
playwright install chromium
