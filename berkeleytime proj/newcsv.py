import csv
import json

# Load JSON data from the file
with open('btcourses.txt', 'r') as file:
    json_data = json.load(file)

# Define CSV file path
csv_file = 'courses.csv'

# Define CSV column headers
fields = ['abbreviation', 'courseNumber', 'description', 'title', 'gradeAverage', 'letterAverage', 'openSeats', 'enrolledPercentage', 'enrolled', 'enrolledMax', 'units']

# Write data to CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()  # Write headers

    # Extract courses from JSON and write to CSV
    for edge in json_data['data']['allCourses']['edges']:
        course = edge['node']
        writer.writerow({
            'abbreviation': course.get('abbreviation', ''),
            'courseNumber': course.get('courseNumber', ''),
            'description': course.get('description', ''),
            'title': course.get('title', ''),
            'gradeAverage': course.get('gradeAverage', ''),
            'letterAverage': course.get('letterAverage', ''),
            'openSeats': course.get('openSeats', ''),
            'enrolledPercentage': course.get('enrolledPercentage', ''),
            'enrolled': course.get('enrolled', ''),
            'enrolledMax': course.get('enrolledMax', ''),
            'units': course.get('units', '')
        })

print("CSV file created successfully.")
