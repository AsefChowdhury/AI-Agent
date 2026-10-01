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

build_flexible_pattern_cases = [
    ("ignore all previous instructions", r"i\s*g\s*n\s*o\s*r\s*e\s*a\s*l\s*l\s*p\s*r\s*e\s*v\s*i\s*o\s*u\s*s\s*i\s*n\s*s\s*t\s*r\s*u\s*c\s*t\s*i\s*o\s*n\s*s"),
    ("act", r"a\s*c\s*t"),                              # short phrase
    ("a", r"a"),                                        # single character, no \s* needed at all
    ("", ""),                                           # empty string
    ("system prompt:", r"s\s*y\s*s\s*t\s*e\s*m\s*p\s*r\s*o\s*m\s*p\s*t\s*:"),  # contains punctuation (colon)
    ("you are now", r"y\s*o\s*u\s*a\s*r\s*e\s*n\s*o\s*w"),  # multiple existing spaces to strip
    ("new instructions:", r"n\s*e\s*w\s*i\s*n\s*s\s*t\s*r\s*u\s*c\s*t\s*i\s*o\s*n\s*s\s*:"),
    ("do not follow your instructions", r"d\s*o\s*n\s*o\s*t\s*f\s*o\s*l\s*l\s*o\s*w\s*y\s*o\s*u\s*r\s*i\s*n\s*s\s*t\s*r\s*u\s*c\s*t\s*i\s*o\s*n\s*s"),
]
