
1. The section with Optional types helped catch a bug where a value could be None. The error showed that you cannot add an int to None. This mistake is easy to make in Python because types are not enforced and None values will randomly pop up.

2. The benefit of type hints is that they allow errors to be caught before running the program. The cost is that you have to write extra annotations and run a separate tool. If Python enforced types at runtime it would prevent errors but make coding slower and less flexible with more bugs.

3. TypedDict should be used when a dictionary has a fixed structure with known keys like a student record. A normal dict should be used when the keys can vary such as a lookup table. TypedDict is better for catching key errors and bugs early.