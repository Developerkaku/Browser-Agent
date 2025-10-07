#!/usr/bin/env bash
set -e

pip install --upgrade pip
pip install uv

pip install browser-use
pip install playwright
uvx playwright install chromium
