find . -type d -name "__pycache__" -exec rm -r {} +
find . -type f -name "*.csv" -delete
find . -type f -name "*.txt" -delete
