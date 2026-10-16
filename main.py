import re
from collections import Counter
import matplotlib.pyplot as plt

# Read log file
def read_log(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        return file.readlines()

# Analyze logs
def analyze_logs(logs):
    users = []
    failed_attempts = 0

    for line in logs:
        user_match = re.search(r'User: (\w+)', line)
        if user_match:
            users.append(user_match.group(1))

        if "failed login" in line.lower():
            failed_attempts += 1

    user_count = Counter(users)
    return user_count, failed_attempts

# 🔐 Simulated intruder capture
def capture_intruder():
    print("\n[SIMULATION] Capturing intruder image...")
    print("[SIMULATION] Image saved as intruder.jpg")

# Generate report
def generate_report(user_count, failed_attempts):
    report = "\n--- DIGITAL FORENSIC REPORT ---\n"
    report += "\nUser Activity:\n"

    for user, count in user_count.items():
        report += f"{user}: {count} actions\n"

    report += f"\nTotal Failed Login Attempts: {failed_attempts}\n"

    if failed_attempts > 2:
        report += "\n[WARNING] Suspicious Activity Detected!\n"
        capture_intruder()   # 👈 added feature

    print(report)

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(report)

# Generate graph
def generate_graph(user_count):
    users = list(user_count.keys())
    counts = list(user_count.values())

    plt.figure()
    plt.bar(users, counts)
    plt.title("User Activity Analysis")
    plt.xlabel("Users")
    plt.ylabel("Actions")

    plt.savefig("graph.png")
    plt.show()

# Main
def main():
    file_path = input("Enter log file path (or press Enter for default): ").strip()

    if file_path == "":
        file_path = "sample_log.txt"

    logs = read_log(file_path)

    user_count, failed_attempts = analyze_logs(logs)

    generate_report(user_count, failed_attempts)

    generate_graph(user_count)

if __name__ == "__main__":
    main()