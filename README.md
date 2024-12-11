### Objective

Imagine you work in Thoughtful’s robotic automation factory, and your objective is to write a function for one of its robotic arms that will dispatch the packages to the correct stack according to their volume and mass.

### Rules

Sort the packages using the following criteria:

- A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
- A package is **heavy** when its mass is greater or equal to 20 kg.

You must dispatch the packages in the following stacks:

- **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.
- **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.
- **REJECTED**: packages that are **both** heavy and bulky are rejected.

### Implementation

Implement the function **`sort(width, height, length, mass)`** (units are centimeters for the dimensions and kilogram for the mass). This function must return a string: the name of the stack where the package should go.

### Files
- `app.py`: ontains the implementation of the `sort` function which determines the stack for the packages based on their dimensions and mass.
- `test_sort.py`: Includes test cases to validate the logic of the `sort` function.

### How to Run

1. **Run the Application**
   - To interactively input dimensions and mass, use:
     ```bash
     python3 app.py
     ```

2. **Run the Tests**
   - To execute the test cases and validate the `sort` function, use:
     ```bash
     python3 test_sort.py
     ```