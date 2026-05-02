import re


def _parse_llm_output(text):
    def extract(block, field):
        m = re.search(
            rf'\*\*{re.escape(field)}:\*\*\s*(.*?)(?=\n\*\*|\Z)',
            block, re.DOTALL | re.IGNORECASE
        )
        return m.group(1).strip() if m else ""

    pm = re.search(
        r'\*\*Profile\s+analysis:\*\*\s*(.*?)(?=\n+---|\n+###|\Z)',
        text, re.DOTALL | re.IGNORECASE
    )
    if pm:
        profile = pm.group(1).strip()
    else:
        profile = re.split(r'\n+---+\n+|\n+###', text, maxsplit=1)[0].strip()

    concepts = []
    themes = ""
    for section in re.split(r'\n+---+\n+', text):
        hm = re.search(r'###\s*Concept\s*(\d+):\s*(.+)', section)
        if not hm:
            if concepts:
                themes = section.strip()
            continue
        concepts.append({
            "number":     int(hm.group(1)),
            "title":      hm.group(2).strip(),
            "mechanic":   extract(section, "Circular mechanic"),
            "user":       extract(section, "Target user"),
            "value_chain":extract(section, "Value chain inefficiency addressed"),
            "pressure":   extract(section, "Pressure addressed"),
            "description":extract(section, "Concept description"),
            "prototype":  extract(section, "Prototype-readiness sentence"),
            "verdict":    extract(section, "Prototype-readiness verdict"),
            "alignment":  extract(section, "Outcome alignment"),
            "assumptions":extract(section, "Assumptions to test"),
            "analogues":  extract(section, "Citations"),
        })

    profile = re.sub(r'\n+(?:\s*[-*]\s+.+\n*)+$', '', profile).strip()

    profile_lines = profile.splitlines()
    if profile_lines and re.match(
        r'^(#{1,3}|\*{1,2})\s*profile\s+analysis',
        profile_lines[0].strip(), re.IGNORECASE
    ):
        profile = '\n'.join(profile_lines[1:]).strip()

    return profile, themes, sorted(concepts, key=lambda c: c["number"])