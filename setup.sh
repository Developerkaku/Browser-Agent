#!/usr/bin/env bash
set -e

pip install --upgrade pip
pip install uv

uv pip install browser-use
uv pip install playwright
uvx playwright install chromium
