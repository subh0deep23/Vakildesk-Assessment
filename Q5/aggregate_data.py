from typing import List, Dict, Callable

def aggregate_data(data: List[Dict], key: str, aggregator: Callable):
    # Step 1: Create a dictionary to hold the grouped values
    grouped_data = {}
    
    # Step 2: Iterate through the list of dictionaries and group by the key
    for entry in data:
        if key in entry:
            group_key = entry[key]
            if group_key not in grouped_data:
                grouped_data[group_key] = []
            grouped_data[group_key].append(entry)
    
    # Step 3: Apply the aggregator function to each group
    aggregated_result = {}
    for group_key, items in grouped_data.items():
        # Extract the values you want to aggregate (you can modify this as per your need)
        aggregated_result[group_key] = aggregator(items)
    
    return aggregated_result

# Sample data
data = [
    {'region': 'North', 'sales': 150},
    {'region': 'South', 'sales': 200},
    {'region': 'North', 'sales': 100},
    {'region': 'East', 'sales': 300},
    {'region': 'South', 'sales': 250}
]

# Aggregator function: Sum sales for each region
def sum_sales(items):
    return sum(item['sales'] for item in items)

# Aggregating the data by 'region'
result = aggregate_data(data, 'region', sum_sales)

print(result)
