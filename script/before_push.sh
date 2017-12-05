#! /usr/bin/env bash

# Convert Markdown to reStructuredText
pandoc --from=markdown --to=rst --output=README.rst README.md
