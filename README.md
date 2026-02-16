# Openspace Organizer
Smart Workspace Allocation

## Introduction
Openspace Organizer is a Python-based solution designed to automate the logic of seating assignments in shared work environments.
The system models the physical workspace through a hierarchical object-oriented approach (Openspace -> Table -> Seat), ensuring that every participant is assigned a spot while respecting the facility's capacity and layout constraints.

## Project Architecture
The software is built on Object-Oriented Programming (OOP) principles to ensure scalability and clean code:

- Openspace: The primary coordinator class. It acts as the global container, managing multiple tables and overseeing the participant assignment process.

- Table: Represents a physical work unit containing a predefined number of Seat objects.

- Seat: The atomic unit of the project, tracking occupancy status and the name of the assigned person.

## Environment Management

1. **Prerequisites**
- Anaconda or Miniconda installed on your system.
- Git installed for version control.

2. **Environment Setup**
To replicate the development environment on your local machine, navigate to the project root and run:

3. **Updating Dependencies**

If the environment.yml file is updated with new libraries, sync your local environment.

##U sage Workflow

- **Input Data**: You can use .csv or .xlsx format. No header. If excel file, please fill the firt column with the names.
- **Execution**: Run the main script through your terminal:
- **Output**: The system will print the final seating arrangement to the console, save an excel file in your project folder and provide you with a 2D visualization.

## Technical Highlights
String Representation: Every class implements the __str__() method, providing clear, human-readable descriptions of objects during debugging or console output.
Flexible Scaling: The design allows for easy adjustments to the number of tables or seat capacity without modifying the core data-loading logic.
Error Handling: Basic checks are in place to ensure the program doesn't crash if the Excel file is missing or formatted incorrectly.
