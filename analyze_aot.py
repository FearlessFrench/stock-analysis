import csv

def add_numbers(a, b, c, d, e):
    """Adds five numbers and prints the result."""
    result = a + b + c + d + e
    print(f"The sum of {a}, {b}, {c}, {d}, and {e} is {result}")

def analyze_aot_stock():
    """Reads stock data, analyzes AOT stock price trends, and saves the analysis."""
    input_file = "stock_data.csv"
    output_file = "aot_analysis.txt"
    aot_prices = []

    # Read stock data
    with open(input_file, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Stock'] == 'AOT':
                aot_prices.append(float(row['Price']))

    # Analyze trend
    if not aot_prices:
        analysis = "No data available for AOT stock."
    else:
        trend = "increasing" if aot_prices[-1] > aot_prices[0] else "decreasing"
        analysis = (
            f"AOT stock prices analyzed.\n"
            f"Starting price: {aot_prices[0]}\n"
            f"Ending price: {aot_prices[-1]}\n"
            f"Trend: {trend}"
        )

    # Save analysis
    with open(output_file, mode='w') as outfile:
        outfile.write(analysis)

# Call the function
analyze_aot_stock()
