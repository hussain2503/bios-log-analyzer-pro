import re

PATTERN = re.compile(r"\b(ERROR|WARNING|WARN|CRITICAL|FAIL)\b", re.IGNORECASE)

def parse_log(file_path):
    parsed_data = []

    with open(file_path, "r") as file:
        for line_no, line in enumerate(file, start=1):
            match = PATTERN.search(line)
            if match:
                parsed_data.append({
                    "line": line_no,
                    "type": match.group().upper(),
                    "message": line.strip()
                })

    return parsed_data