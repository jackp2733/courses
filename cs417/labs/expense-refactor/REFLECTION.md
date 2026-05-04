# Reflection

# 1. Before / After

Before refactoring, everything was inside main. That made it hard to change anything. The categories were also hard coded, so I would have to edit the file every time I wanted to change them. The parsing was only for CSV, so adding JSON would have been hard.

After refactoring the code is split into separate functions. Parsing, categorizing, and building the report are all separate. This makes it much easier to change things without breaking everything else.

# 2. What I did

Part 1, I split parsing into two functions. One for CSV and one for JSON. They both return the same format so the rest of the code does not care where the data came from.

Part 2, I passed the categories into the function instead of using a global variable. This makes it easier to test and change.

Part 3, I separated logic from input and output. The build_report function only does calculations and returns data. The main function handles reading files and printing.

# 3. Hardest part

The hardest part was Part 3. At first I still had print statements inside build_report. The test failed and I was confused. Then I realized everything related to input and output had to be moved to main.

# 4. Future change

If we had to get data from an API, I would just add a new function to fetch the data. Then I would pass that data into build_report. I would not need to change the rest of the code.
