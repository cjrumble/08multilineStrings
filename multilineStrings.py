# MULTILINE STRINGS LESSON

# Create a Python Multiline String with Examples
# Use triple quotes to create a multiline string mulitline string in triple quotes
# It is the simplest method to let a long string split into different lines.
# You will need to enclose it with a pair of Triple quotes, one at the start and second in the end.
"""Learn Python
Programming"""
# String containing newline characters
line_str = "I'm learning Python.\nI refer to TechBeamers.com tutorials.\nIt is the most popular site for Python programmers."
# Now, we’ll try to slice it into multiple lines using triple quotes.
# String containing newline characters
line_str = "I'm learning Python.\nI refer to TechBeamers.com tutorials.\nIt is the most popular site for Python programmers."
print("Long string with newlines: \n" + line_str)
# Creating a multiline string
multiline_str = """I'm learning Python.
I refer to TechBeamers.com tutorials.
It is the most popular site for Python programmers."""
print("Multiline string: \n" + multiline_str)
# output is:
# Long string with newlines:    I
# I'm learning Python.
# I refer to TechBeamers.com tutorials.
# It is the most popular site for Python programmers.
# Multiline string:
# I'm learning Python.
# I refer to TechBeamers.com tutorials.
# It is the most popular site for Python programmers.

# This method retains the newline ‘\n’ in the generated string. If you want to remove the ‘\n’, then use the strip()/replace() function.

# Use brackets to define a multiline string
# Python multiline string example using brackets
multiline_str = ("I'm learning Python. "
                 "I refer to TechBeamers.com tutorials. "
                 "It is the most popular site for Python programmers.")
print(multiline_str)
# It provides the following result:
# I'm learning Py
# thon. I refer to TechBeamers.com tutorials. It is the most popular site for Python programmers.
# You can see there is no newline character in the output.However,
# if you want it, then add it while creating the string.

# Python multiline string with newlines example using brackets
multiline_str = ("I'm learning Python.\n"
                 "I refer to TechBeamers.com tutorials.\n"
                 "It is the most popular site for Python programmers.")
print(multiline_str)
# Here is the output after execution:
# I'm learning Python. I refer to TechBeamers.com tutorials. I
# t is the most popular site for Python programmers.

# Backslash to join string on multiple lines

# Python multiline string example using backslash
multiline_str = "I'm learning Python. " \
                "I refer to TechBeamers.com tutorials. " \
                "It is the most popular site for Python programmers."
print(multiline_str)
# The above code gives the following result:
# I'm learning Python. I refer to TechBeamers.com tutorials. I
# t is the most popular site for Python programmers.

# Python multiline string example using backslash and newlines
multiline_str = "I'm learning Python.\n" \
                "I refer to TechBeamers.com tutorials.\n" \
                "It is the most popular site for Python programmers."
print(multiline_str)
# The output:
# I'm learning Python.
# I refer to TechBeamers.com tutorials.
# It is the most popular site for Python programmers.

# Join() method to create a string with newlines
# The final approach is applying the string join() function to convert a string into multiline.
# It handles the space characters itself while contaminating the strings.
# Python multiline string example using string join()
multiline_str = ' '.join(("I'm learning Python.",
                          "I refer to TechBeamers.com tutorials.",
                          "It is the most popular site for Python programmers."))
print(multiline_str)
# It outputs the following result:
# I'm learning Python. I refer to TechBeamers.com tutorials. It is the most popular site for Python programmers.
# Python multiline string with newlines example using string join()
multiline_str = ''.join(("I'm learning Python.\n",
                         "I refer to TechBeamers.com tutorials.\n",
                         "It is the most popular site for Python programmers."))
print(multiline_str)
# The result is:
# I'm learning Python.
# I refer to TechBeamers.com tutorials.
# It is the most popular site for Python programmers.