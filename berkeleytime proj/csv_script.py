import csv

# Read data from the text file
with open('btcourses.txt', 'r') as file:
    lines = file.readlines()

# Define CSV file path
csv_file = 'courses.csv'

# Define CSV column headers
fields = ['abbreviation', 'courseNumber', 'description', 'title', 'gradeAverage', 'letterAverage', 'openSeats', 'enrolledPercentage', 'enrolled', 'enrolledMax', 'units']

# Write data to CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    
    # Write headers
    writer.writeheader()
    
    # Initialize course_data dictionary to store course information
    course_data = {}
    
    # Iterate over lines and extract course information
    for line in lines:
        line = line.strip()
        if line:
            key, value = line.split(': ', 1)
            course_data[key] = value
        else:
            # If the line is empty, it indicates the end of a course block
            if course_data:
                writer.writerow({
                    'abbreviation': course_data.get('abbreviation', ''),
                    'courseNumber': course_data.get('courseNumber', ''),
                    'description': course_data.get('description', ''),
                    'title': course_data.get('title', ''),
                    'gradeAverage': course_data.get('gradeAverage', ''),
                    'letterAverage': course_data.get('letterAverage', ''),
                    'openSeats': course_data.get('openSeats', ''),
                    'enrolledPercentage': course_data.get('enrolledPercentage', ''),
                    'enrolled': course_data.get('enrolled', ''),
                    'enrolledMax': course_data.get('enrolledMax', ''),
                    'units': course_data.get('units', '')
                })
                # Reset course_data for the next course
                course_data = {}

    # Check if there is any remaining course data to write after the last line
    if course_data:
        writer.writerow({
            'abbreviation': course_data.get('abbreviation', ''),
            'courseNumber': course_data.get('courseNumber', ''),
            'description': course_data.get('description', ''),
            'title': course_data.get('title', ''),
            'gradeAverage': course_data.get('gradeAverage', ''),
            'letterAverage': course_data.get('letterAverage', ''),
            'openSeats': course_data.get('openSeats', ''),
            'enrolledPercentage': course_data.get('enrolledPercentage', ''),
            'enrolled': course_data.get('enrolled', ''),
            'enrolledMax': course_data.get('enrolledMax', ''),
            'units': course_data.get('units', '')
        })

print("CSV file created successfully.")
import csv

# Read data from the text file
with open('btcourses.txt', 'r') as file:
    lines = file.readlines()

# Define CSV file path
csv_file = 'courses.csv'

# Define CSV column headers
fields = ['abbreviation', 'courseNumber', 'description', 'title', 'gradeAverage', 'letterAverage', 'openSeats', 'enrolledPercentage', 'enrolled', 'enrolledMax', 'units']

# Write data to CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    
    # Write headers
    writer.writeheader()
    
    # Initialize course_data dictionary to store course information
    course_data = {}
    
    # Iterate over lines and extract course information
    for line in lines:
        line = line.strip()
        if line:
            # Ensure the line contains a colon and can be split into exactly two parts
            if ': ' in line:
                key, value = line.split(': ', 1)
                course_data[key] = value
            else:
                print(f"Skipping malformed line: {line}")
        else:
            # If the line is empty, it indicates the end of a course block
            if course_data:
                writer.writerow({
                    'abbreviation': course_data.get('abbreviation', ''),
                    'courseNumber': course_data.get('courseNumber', ''),
                    'description': course_data.get('description', ''),
                    'title': course_data.get('title', ''),
                    'gradeAverage': course_data.get('gradeAverage', ''),
                    'letterAverage': course_data.get('letterAverage', ''),
                    'openSeats': course_data.get('openSeats', ''),
                    'enrolledPercentage': course_data.get('enrolledPercentage', ''),
                    'enrolled': course_data.get('enrolled', ''),
                    'enrolledMax': course_data.get('enrolledMax', ''),
                    'units': course_data.get('units', '')
                })
                # Reset course_data for the next course
                course_data = {}

    # Check if there is any remaining course data to write after the last line
    if course_data:
        writer.writerow({
            'abbreviation': course_data.get('abbreviation', ''),
            'courseNumber': course_data.get('courseNumber', ''),
            'description': course_data.get('description', ''),
            'title': course_data.get('title', ''),
            'gradeAverage': course_data.get('gradeAverage', ''),
            'letterAverage': course_data.get('letterAverage', ''),
            'openSeats': course_data.get('openSeats', ''),
            'enrolledPercentage': course_data.get('enrolledPercentage', ''),
            'enrolled': course_data.get('enrolled', ''),
            'enrolledMax': course_data.get('enrolledMax', ''),
            'units': course_data.get('units', '')
        })

print("CSV file created successfully.")
