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

extract_plain_text_cases = [
    # single section
    ({"sections": [{"header": "Evaporation", "content": "Water rises as vapor."}]},
     "Evaporation Water rises as vapor."),

    # multiple sections (matches real Qwen output shape)
    ({"sections": [
        {"header": "Evaporation", "content": "Water rises as vapor."},
        {"header": "Condensation", "content": "Vapor cools into droplets."}
    ]},
     "Evaporation Water rises as vapor. Condensation Vapor cools into droplets."),

    # empty header and content (whitespace quirk)
    ({"sections": [{"header": "", "content": ""}]}, " "),

    # empty header, real content
    ({"sections": [{"header": "", "content": "Just content here."}]},
     " Just content here."),

    # three sections
    ({"sections": [
        {"header": "A", "content": "one"},
        {"header": "B", "content": "two"},
        {"header": "C", "content": "three"}
    ]},
     "A one B two C three"),

    # no sections at all (empty list)
    ({"sections": []}, ""),
]