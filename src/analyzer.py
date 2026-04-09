from collections import Counter

SEVERITY_SCORE = {
    "CRITICAL": 3,
    "ERROR": 2,
    "WARNING": 1,
    "WARN": 1,
    "FAIL": 2
}

BOOT_ISSUES = ["boot failed", "no boot device", "timeout"]

def analyze(parsed_data):
    counter = Counter()
    severity_total = 0
    boot_flags = []

    for entry in parsed_data:
        t = entry["type"]
        counter[t] += 1
        severity_total += SEVERITY_SCORE.get(t, 0)

        msg_lower = entry["message"].lower()
        for issue in BOOT_ISSUES:
            if issue in msg_lower:
                boot_flags.append(entry)

    return {
        "counts": dict(counter),
        "severity_score": severity_total,
        "boot_issues": boot_flags
    }