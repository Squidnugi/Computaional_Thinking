import csv


def bucket_sort_csv(input_file, output_file, column_index):
    # Create empty buckets
    buckets = {}

    # Read the CSV file and fill the buckets
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # Read the header row

        for row in csv_reader:
            value = float(row[column_index])  # Assuming the values to be sorted are floats
            if value in buckets:
                buckets[value].append(row)
            else:
                buckets[value] = [row]

    # Sort the buckets by keys (values) and concatenate them
    sorted_data = []
    for key in sorted(buckets.keys()):
        sorted_data.extend(buckets[key])

    # Write the sorted data to a new CSV file
    with open(output_file, 'w', newline='') as csv_output:
        csv_writer = csv.writer(csv_output)
        csv_writer.writerow(header)  # Write the header row
        csv_writer.writerows(sorted_data)


# Example usage:
input_file = 'input.csv'
output_file = 'sorted_output.csv'
column_index_to_sort = 0  # Change this to the column index you want to sort by

bucket_sort_csv(input_file, output_file, column_index_to_sort)