# 

# \# Tennis Scoring Application – Hypothesis-Based Testing

# 

# A Software Engineering Lab 7 project demonstrating property-based testing using Python, Hypothesis, and Pytest.

# 

# \## 1. Project Overview

# 

# This project implements a tennis scoring utility with three main functions:

# 

# \- `parse\_score()` – Parses two non-negative integer scores.

# \- `game\_lead()` – Calculates the difference between two tennis point scores.

# \- `set\_spread()` – Calculates the difference between the maximum and minimum game counts.

# 

# The project demonstrates how property-based testing can discover unexpected inputs and help improve software reliability.

# 

# \## 2. Technologies Used

# 

# \- Python 3.11

# \- Hypothesis

# \- Pytest

# 

# \## 3. Project Structure

# 

# ```text

# tennis-scoring-hypothesis-testing/

# │

# ├── tennis\_scoring.py

# ├── tennis\_scoring\_original.py

# ├── test\_tennis\_scoring.py

# ├── test\_original\_fuzz.py

# ├── requirements.txt

# ├── README.md

# │

# └── screenshots/

# &#x20;   ├── 01\_original\_output.png

# &#x20;   ├── 02\_fuzz\_failures.png

# &#x20;   ├── 03\_fixed\_output.png

# &#x20;   └── 04\_final\_tests\_passed.png

# ```

# 

# \## 4. Installation

# 

# Clone the repository:

# 

# ```bash

# git clone https://github.com/akashsb2005/tennis-scoring-hypothesis-testing.git

# cd tennis-scoring-hypothesis-testing

# ```

# 

# Install dependencies:

# 

# ```bash

# pip install -r requirements.txt

# ```

# 

# \## 5. Running the Application

# 

# Execute:

# 

# ```bash

# python tennis\_scoring.py

# ```

# 

# Example input:

# 

# ```text

# 3-2

# 40-30

# 5,6,7

# ```

# 

# Expected output:

# 

# ```text

# Points A and B: (3, 2)

# Lead in Points: 1

# Spread: 2

# ```

# 

# \## 6. Property-Based Testing

# 

# Hypothesis generates a variety of inputs to test application behavior beyond manually selected examples.

# 

# The original implementation was tested using:

# 

# ```bash

# python -m pytest test\_original\_fuzz.py -v

# ```

# 

# The fuzz tests exposed failures involving malformed inputs and non-string values.

# 

# The corrected implementation includes validation for invalid input formats, negative values, and unsupported tennis point scores.

# 

# \## 7. Running the Final Tests

# 

# Execute:

# 

# ```bash

# python -m pytest test\_tennis\_scoring.py -v

# ```

# 

# Final observed result:

# 

# \*\*17 passed\*\*

# 

# The test suite checks valid and invalid inputs for all three functions.

# 

# \## 8. Screenshots and Evidence

# 

# \### Original Application Output

# 

# !\[Original output](screenshots/01\_original\_output.png)

# 

# \### Hypothesis Fuzz Testing – Original Failures

# 

# !\[Fuzz failures](screenshots/02\_fuzz\_failures.png)

# 

# \### Corrected Application Output

# 

# !\[Fixed output](screenshots/03\_fixed\_output.png)

# 

# \### Final Successful Test Results

# 

# !\[Final tests](screenshots/04\_final\_tests\_passed.png)

# 

# \## 9. Conclusion

# 

# This project demonstrates the use of property-based testing to identify unexpected input cases, improve input validation, and verify the reliability of a Python application using Hypothesis and Pytest.

# 

# \---

# 

# \*\*Project:\*\* SE Lab 7 – Tennis Scoring Application  

# \*\*Author:\*\* Akash Bagoji



