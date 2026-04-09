def generate_html(parsed_data, analysis, output_file="reports/report.html"):
    html = """
    <html>
    <head>
        <title>BIOS Log Report</title>
        <style>
            body { font-family: Arial; }
            .ERROR { color: red; }
            .CRITICAL { color: darkred; font-weight: bold; }
            .WARNING, .WARN { color: orange; }
        </style>
    </head>
    <body>
        <h1>BIOS Log Analysis Report</h1>
    """

    html += f"<h2>Severity Score: {analysis['severity_score']}</h2>"
    html += "<h3>Counts:</h3><ul>"
    
    for k, v in analysis["counts"].items():
        html += f"<li>{k}: {v}</li>"
    
    html += "</ul><h3>Log Details:</h3>"

    for entry in parsed_data:
        html += f"<p class='{entry['type']}'>{entry['line']}: {entry['message']}</p>"

    html += "</body></html>"

    with open(output_file, "w") as f:
        f.write(html)

    print(f"HTML report generated: {output_file}")