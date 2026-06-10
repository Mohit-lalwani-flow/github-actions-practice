# print("This is python test file")

import sys

print("Testing pipeline failure...")
# This forces the script to exit with code 1, causing the pipeline to fail
# Intentionally break the script (Go Red 🔴)
# sys.exit(1) 

# Fix it (Go Green 🟢)
# Code 0 means success, which tells GitHub Actions everything passed
sys.exit(0)