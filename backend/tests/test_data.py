import pytest

strip_formatting_cases = [
    ("##Heading##", "Heading"),
    ("No symbols here", "No symbols here"),
    ("Multiple ## in ## text", "Multiple  in  text"),
    ("", ""),                                  # empty string
    ("#", ""),                                 # single symbol only
    ("####", ""),                              # only symbols, no text
    ("# Heading", " Heading"),                 # single leading hash + space
    ("### Subheading ###", " Subheading "),    # markdown-style h3
    ("No hash at all here.", "No hash at all here."),
    ("Price: #1 bestseller", "Price: 1 bestseller"),  # non-markdown use of #
    ("a#b#c#d", "abcd"),                       # symbols scattered mid-word
    ("#####Heavy##### formatting#####", "Heavy formatting"),
]