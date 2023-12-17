import csv
from project import Project
import datetime

MENU = ("Menu:\n(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new "
        "project\n(U)pdate project\n(Q)uit")
def main():
    file_path = 'projects.txt'
    projects = read_projects_file(file_path)
    print(MENU)
    user_input = input(">>> ").lower()
    while user_input != 'q':
        if user_input == 'l':
            file_name = input("Enter filename to load projects from: ")
            projects = read_projects_file(file_name)

        elif user_input == 's':
            file_name = input("Enter filename to save projects to: ")
            write_projects_to_file(file_name, projects)

        elif user_input == 'd':
            display_projects(projects)

        elif user_input == 'f':
            filter_date = input("Show projects that start after date (dd/mm/yyyy): ")
            filtered_projects = filter_projects_by_date(projects, filter_date)
            display_projects(filtered_projects)

        elif user_input == 'a':
            new_project = add_new_project()
            projects.append(new_project)

        elif user_input == 'u':
            project_choice = int(input("Project choice: "))
            update_project(projects, project_choice)

        else:
            print("Invalid option. Please try again.")
        user_input = input(">>> ").lower()
    print("Thank you for using custom-built project management software.")


def read_projects_file(file_path):
    projects = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)
        for row in reader:
            projects.append(Project(*row))
    return projects


def write_projects_to_file(file_path, projects):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(['Name', 'Start Date', 'Priority', 'Estimate', 'Completion'])
        for project in projects:
            writer.writerow([project.name, project.start_date.strftime('%d/%m/%Y'),
                             project.priority, project.estimate, project.completion])


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion < 100]
    completed_projects = [project for project in projects if project.completion == 100]

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")
    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects_by_date(projects, filter_date):
    filter_date = datetime.datetime.strptime(filter_date, "%d/%m/%Y").date()
    print(f"Filter Date: {filter_date}")
    filtered_projects = [project for project in projects if project.start_date > filter_date]
    print("Filtered Projects:")
    for project in filtered_projects:
        print(f"  {project.start_date}")
    return filtered_projects


def add_new_project():
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    estimate = input("Cost estimate: $")
    completion = input("Percent complete: ")
    return Project(name, start_date, priority, estimate, completion)


def update_project(projects, choice):
    if 0 <= choice < len(projects):
        project = projects[choice]
        print(project)
        new_percentage = int(input("New Percentage: "))
        project.completion = new_percentage

        new_priority = input("New Priority: ")
        if new_priority:
            project.priority = int(new_priority)

        print("Project updated successfully.")
    else:
        print("Invalid project choice. Please try again.")

if __name__ == "__main__":
    main()
