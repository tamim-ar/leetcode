# update_readme.py

import os
import re

# ===== CONFIG =====
TOTAL_PROBLEMS = 3656   # Fixed total problems count
SOLUTIONS_FOLDER = "solutions"  # Folder with all solution files/folders

BADGE_STYLE = "flat-square"
LOGO_COLOR = {
    "LeetCode": "323232",
    "C++": "7DD3FC",
    "Java": "4298E2",
    "Python": "60A4FB",
    "TypeScript": "93C5FD",
    "MySQL": "BAE6FD"
}

LANGUAGE_EXTENSIONS = {
    "C++": [".cpp", ".cc", ".cxx", ".h", ".hpp"],
    "Java": [".java"],
    "Python": [".py"],
    "TypeScript": [".ts"],
    "MySQL": [".sql"]
}
# ==================

def count_subfolders(folder):
    with os.scandir(folder) as entries:
        return sum(1 for entry in entries if entry.is_dir())

def count_solutions_by_language():
    counts = {lang: 0 for lang in LANGUAGE_EXTENSIONS}
    for root, _, files in os.walk(SOLUTIONS_FOLDER):
        for file in files:
            for lang, exts in LANGUAGE_EXTENSIONS.items():
                if any(file.endswith(ext) for ext in exts):
                    counts[lang] += 1
    return counts

def generate_badges(solved, total, counts):
    percentage = round((solved / total) * 100, 2) if total > 0 else 0
    return {
        "progress": f"https://img.shields.io/badge/Solved-{solved}%2F{total}%20({percentage}%25)-{LOGO_COLOR['LeetCode']}?style={BADGE_STYLE}&logo=leetcode",
        "C++": f"https://img.shields.io/badge/C%2B%2B23-{counts['C++']}%20solutions-{LOGO_COLOR['C++']}?style={BADGE_STYLE}&logo=cplusplus",
        "Java": f"https://img.shields.io/badge/Java-{counts['Java']}%20solutions-{LOGO_COLOR['Java']}?style={BADGE_STYLE}&logo=java",
        "Python": f"https://img.shields.io/badge/Python%203-{counts['Python']}%20solutions-{LOGO_COLOR['Python']}?style={BADGE_STYLE}&logo=python",
        "TypeScript": f"https://img.shields.io/badge/TypeScript-{counts['TypeScript']}%20solutions-{LOGO_COLOR['TypeScript']}?style={BADGE_STYLE}&logo=typescript",
        "MySQL": f"https://img.shields.io/badge/MySQL-{counts['MySQL']}%20solutions-{LOGO_COLOR['MySQL']}?style={BADGE_STYLE}&logo=mysql"
    }

def update_readme(badges):
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    replacements = {
        r"https://img\.shields\.io/badge/Solved-[^\s)]+": badges["progress"],
        r"https://img\.shields\.io/badge/C%2B%2B23-[^\s)]+": badges["C++"],
        r"https://img\.shields\.io/badge/Java-[^\s)]+": badges["Java"],
        r"https://img\.shields\.io/badge/Python%203-[^\s)]+": badges["Python"],
        r"https://img\.shields\.io/badge/TypeScript-[^\s)]+": badges["TypeScript"],
        r"https://img\.shields\.io/badge/MySQL-[^\s)]+": badges["MySQL"]
    }
    for pattern, new_url in replacements.items():
        content = re.sub(pattern, new_url, content)

    # Fix possible duplicated LeetCode badge suffixes like '-323232?style=flat-square&logo=leetcode)'
    content = re.sub(
        r"(https://img\.shields\.io/badge/Solved-[^\s)]+)-323232\?style=flat-square&logo=leetcode\)",
        r"\1)",
        content
    )

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    solved = count_subfolders(SOLUTIONS_FOLDER)  # count folders inside solutions/
    counts = count_solutions_by_language()
    badges = generate_badges(solved, TOTAL_PROBLEMS, counts)
    update_readme(badges)

    print("\n🚀 README Badges Updated Successfully!\n")
    print(f"📊 Solved: {solved}/{TOTAL_PROBLEMS} ({round((solved / TOTAL_PROBLEMS) * 100, 2)}%)\n")
    print("📌 Solutions by Language:")
    for lang, count in counts.items():
        print(f"   • {lang:<10}: {count} solutions")
    print("\n✅ Done!\n")
