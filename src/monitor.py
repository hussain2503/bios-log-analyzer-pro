import time
from parser import parse_log
from analyzer import analyze

def monitor_log(file_path):
    print(f"Monitoring file: {file_path}")
    print("Press CTRL+C to stop\n")

    last_modified = 0

    while True:
        try:
            current_modified = None

            # Get last modified time of file
            import os
            current_modified = os.path.getmtime(file_path)

            if current_modified != last_modified:
                print("\n🔄 File updated! Re-analyzing...\n")

                parsed_data = parse_log(file_path)
                analysis = analyze(parsed_data)

                print("Counts:", analysis["counts"])
                print("Severity Score:", analysis["severity_score"])
                print("Boot Issues:", len(analysis["boot_issues"]))

                last_modified = current_modified

            time.sleep(3)  # check every 3 seconds

        except KeyboardInterrupt:
            print("\n🛑 Monitoring stopped")
            break