# Python ZeroDivisionError Bug

This repository demonstrates a subtle bug that can lead to a `ZeroDivisionError` in Python, even when seemingly handling zero values correctly.

The `bug.py` file contains a function that's intended to gracefully handle division by zero. However, due to an oversight, the code still throws an error in a specific scenario.