import pytest

strip_formatting_cases = [
    ("##Heading##", "Heading"),
    ("No symbols here", "No symbols here"),
    ("Multiple ## in ## text", "Multiple  in  text"),
]