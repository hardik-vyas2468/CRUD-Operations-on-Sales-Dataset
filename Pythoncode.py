# Starting dataset
dataset = []

# Function to create and insert new records in dataset
def create_record(record):
    dataset.append(record)
    print("Record added successfully.")

# Function to read and retrieve specific records from dataset
def read_record(criteria):
    results = [record for record in dataset if all(record[key] == value for key, value in criteria.items())]
    if results:
        for result in results:
            print(result)
    else:
        print("No records found.")

# Function to update records in the dataset
def update_record(criteria, updates):
    updated = False
    for record in dataset:
        if all(record[key] == value for key, value in criteria.items()):
            for key, value in updates.items():
                record[key] = value
            updated = True
            print("Record updated successfully.")
    if not updated:
        print("No matching records found to update.")

# Function to delete records from the dataset
def delete_record(criteria):
    global dataset
    new_dataset = [record for record in dataset if not all(record[key] == value for key, value in criteria.items())]
    if len(new_dataset) < len(dataset):
        dataset = new_dataset
        print("Record(s) deleted successfully.")
    else:
        print("No matching records found to delete.")

create_record({"id": 1, "name": "John Doe", "age": 30})
create_record({"id": 2, "name": "Jane Doe", "age": 25})
print("\nDataset after creation:")
print(dataset)

print("\nReading records with age 25:")
read_record({"age": 25})

print("\nUpdating record with id 1:")
update_record({"id": 1}, {"age": 31})
print("\nDataset after update:")
print(dataset)

print("\nDeleting record with id 2:")
delete_record({"id": 2})
print("\nDataset after deletion:")
print(dataset)
