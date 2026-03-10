from patterns import VULNERABILITY_PATTERNS

def detect_vulnerability(text):

    text = text.lower()

    text = text.replace("-", " ")

    for vuln_type, keywords in VULNERABILITY_PATTERNS.items():

        for keyword in keywords:

            if keyword in text:
                return vuln_type

    return "Unknown"