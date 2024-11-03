import csv
from datetime import date

# Class to handle medicine data input
class MedicineBook:
    def __init__(self):
        self.data = {}

    def input_data(self):
        self.data['Headline'] = input("Enter Headline: ")
        self.data['Name'] = input("Enter Name: ")
        self.data['Source'] = input("Enter Source: ")
        self.data['Common Name'] = input("Enter Common Name: ")
        self.data['Duration'] = input("Enter Duration: ")
        self.data['Characteristic Symptoms'] = input("Enter Characteristic Symptoms: ")

    def save_to_csv(self, filename='medicine_data.csv'):
        # Write data to CSV file
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # If file is empty, write header first
            if file.tell() == 0:
                writer.writerow(self.data.keys())
            writer.writerow(self.data.values())
        print(f"Data saved to {filename}")

# Example usage
medicine_book = MedicineBook()

while True:
    medicine_book.input_data()
    medicine_book.save_to_csv()

    # Option to add more data
    more = input("Do you want to add more records? (yes/no): ").lower()
    if more != 'yes':
        break
