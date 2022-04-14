#!/bin/bash
echo "running black..."
poetry run black pywebcomponents/ tests/
echo "done. running flake8 silently..."
poetry run flake8 pywebcomponents/ tests/
echo "done. running mypy..."
poetry run mypy pywebcomponents/ tests/
echo "done. running pytest..."
poetry run pytest
echo "DONE!"
tput bel