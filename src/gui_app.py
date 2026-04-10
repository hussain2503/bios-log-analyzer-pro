import tkinter as tk
from tkinter import filedialog, scrolledtext
from parser import parse_log
from analyzer import analyze

def open_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    parsed_data = parse_log(file_path)
    analysis = analyze(parsed_data)

    output_box.delete(1.0, tk.END)

    output_box.insert(tk.END, "=== BIOS LOG ANALYSIS ===\n\n")
    output_box.insert(tk.END, f"Counts: {analysis['counts']}\n")
    output_box.insert(tk.END, f"Severity Score: {analysis['severity_score']}\n")
    output_box.insert(tk.END, f"Boot Issues: {len(analysis['boot_issues'])}\n\n")

    output_box.insert(tk.END, "---- LOG DETAILS ----\n")
    for entry in parsed_data:
        output_box.insert(tk.END, f"{entry['line']}: {entry['message']}\n")


# GUI window
root = tk.Tk()
root.title("BIOS Log Analyzer Pro")
root.geometry("700x500")

btn = tk.Button(root, text="Select Log File", command=open_file)
btn.pack(pady=10)

output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=25)
output_box.pack(padx=10, pady=10)

root.mainloop()