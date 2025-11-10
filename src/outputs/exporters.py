thonimport json
import csv

def export_to_json(data, filename):
    """Export data to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def export_to_csv(data, filename):
    """Export data to a CSV file."""
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)