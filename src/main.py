import argparse
from parser import parse_log
from analyzer import analyze
from report import generate_html

def main():
    parser = argparse.ArgumentParser(description="BIOS Log Analyzer")
    parser.add_argument("--file", required=True, help="Path to BIOS log file")

    args = parser.parse_args()

    parsed_data = parse_log(args.file)
    analysis = analyze(parsed_data)

    print("\n=== SUMMARY ===")
    print("Counts:", analysis["counts"])
    print("Severity Score:", analysis["severity_score"])
    print("Boot Issues:", len(analysis["boot_issues"]))

    generate_html(parsed_data, analysis)

if __name__ == "__main__":
    main()