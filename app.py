import pandas as pd
import pyarrow.parquet as pq

# Path of the Parquet file
parquet_file = 'part-example-a89704a8-cf16-4113-bc0e-927557be3f45-c000.gz.parquet'
json_file = 'output6.json'
csv_file = 'output6.csv'

# Read the Parquet file
table = pq.read_table(parquet_file)
df = table.to_pandas()

# Print the DataFrame in console
print(df)

# Export the DataFrame to a JSON file
df.to_json(json_file, orient='records', lines=True, date_format='iso')
print(f"Data exported to {json_file}")

# Export the DataFrame to a CSV file
df.to_csv(csv_file, index=False)
print(f"Data exported to {csv_file}")
