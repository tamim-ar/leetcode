import os
import re

TOTAL_PROBLEMS = 3691
SOLUTIONS_FOLDER = "solutions"  

BADGE_STYLE = "flat-square"
LOGO_COLOR = {
    "LeetCode": "323232",
    "C++": "7DD3FC",
    "Java": "4298E2",
    "Python": "60A4FB",
    "TypeScript": "93C5FD",
    "MySQL": "BAE6FD",
    "JavaScript": "F7DF1E",
    "C": "A8B9CC",
    "C#": "239120",
    "PHP": "777BB4"
}

LANGUAGE_EXTENSIONS = {
    "C++": [".cpp", ".cc", ".cxx", ".h", ".hpp"],
    "Java": [".java"],
    "Python": [".py"],
    "TypeScript": [".ts"],
    "MySQL": [".sql"],
    "JavaScript": [".js"],
    "C": [".c"],
    "C#": [".cs"],
    "PHP": [".php"]
}

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
    badges = {
        "progress": f"https://img.shields.io/badge/Solved-{solved}%2F{total}%20({percentage}%25)-{LOGO_COLOR['LeetCode']}?style={BADGE_STYLE}&logo=leetcode",
        "C++": f"https://img.shields.io/badge/C%2B%2B23-{counts['C++']}%20solutions-{LOGO_COLOR['C++']}?style={BADGE_STYLE}&logo=cplusplus",
        "Java": f"https://img.shields.io/badge/Java-{counts['Java']}%20solutions-{LOGO_COLOR['Java']}?style={BADGE_STYLE}&logo=java",
        "Python": f"https://img.shields.io/badge/Python%203-{counts['Python']}%20solutions-{LOGO_COLOR['Python']}?style={BADGE_STYLE}&logo=python",
        "TypeScript": f"https://img.shields.io/badge/TypeScript-{counts['TypeScript']}%20solutions-{LOGO_COLOR['TypeScript']}?style={BADGE_STYLE}&logo=typescript",
        "MySQL": f"https://img.shields.io/badge/MySQL-{counts['MySQL']}%20solutions-{LOGO_COLOR['MySQL']}?style={BADGE_STYLE}&logo=mysql",
        "JavaScript": f"https://img.shields.io/badge/JavaScript-{counts['JavaScript']}%20solutions-{LOGO_COLOR['JavaScript']}?style={BADGE_STYLE}&logo=javascript",
        "C": f"https://img.shields.io/badge/C-{counts['C']}%20solutions-{LOGO_COLOR['C']}?style={BADGE_STYLE}&logo=c",
        "C#": f"https://img.shields.io/badge/C%23-{counts['C#']}%20solutions-{LOGO_COLOR['C#']}?style={BADGE_STYLE}&logo=csharp",
        "PHP": f"https://img.shields.io/badge/PHP-{counts['PHP']}%20solutions-{LOGO_COLOR['PHP']}?style={BADGE_STYLE}&logo=php"
    }
    return badges

def update_readme(badges):
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    replacements = {
        r"https://img\.shields\.io/badge/Solved-[^\s)]+": badges["progress"],
        r"https://img\.shields\.io/badge/C%2B%2B23-[^\s)]+": badges["C++"],
        r"https://img\.shields\.io/badge/Java-[^\s)]+": badges["Java"],
        r"https://img\.shields\.io/badge/Python%203-[^\s)]+": badges["Python"],
        r"https://img\.shields\.io/badge/TypeScript-[^\s)]+": badges["TypeScript"],
        r"https://img\.shields\.io/badge/MySQL-[^\s)]+": badges["MySQL"],
        r"https://img\.shields\.io/badge/JavaScript-[^\s)]+": badges["JavaScript"],
        r"https://img\.shields\.io/badge/C-[^\s)]+": badges["C"],
        r"https://img\.shields\.io/badge/C%23-[^\s)]+": badges["C#"],
        r"https://img\.shields\.io/badge/PHP-[^\s)]+": badges["PHP"]
    }
    for pattern, new_url in replacements.items():
        content = re.sub(pattern, new_url, content)

    content = re.sub(
        r"(https://img\.shields\.io/badge/Solved-[^\s)]+)-323232\?style=flat-square&logo=leetcode\)",
        r"\1)",
        content
    )

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    solved = count_subfolders(SOLUTIONS_FOLDER)  
    counts = count_solutions_by_language()
    badges = generate_badges(solved, TOTAL_PROBLEMS, counts)
    update_readme(badges)

    print("\n🚀 README Badges Updated Successfully!\n")
    print(f"📊 Solved: {solved}/{TOTAL_PROBLEMS} ({round((solved / TOTAL_PROBLEMS) * 100, 2)}%)\n")
    print("📌 Solutions by Language:")
    for lang, count in counts.items():
        print(f"   • {lang:<10}: {count} solutions")
    print("\n✅ Done!\n")
