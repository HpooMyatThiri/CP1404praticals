"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"
TOTAL_SUBJECT = 3

def main():
    data = get_data()
    print(data)
    display_subject_details(data)




def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data_list = []
    for line in input_file:
        line = line.strip().split(',')
        data_list.append(line)
    return data_list
    input_file.close()

def display_subject_details(data):
    """This function takes data and print subject details as a result"""
    for number in range(TOTAL_SUBJECT):
        subject = data[number]
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[-1]} students")

main()