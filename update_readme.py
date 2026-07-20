import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

TOTAL_PROBLEMS = 3999
SOLUTIONS_FOLDER = "solutions"

BADGE_STYLE = "flat-square"
LOGO_COLOR = {
    "LeetCode": "323232",
    "Python": "60A4FB",
    "Java": "4298E2",
    "JavaScript": "F7DF1E",
    "TypeScript": "3178C6",
    "C": "555555",
    "C++": "00599C",
    "C#": "9B4F96",
    "PHP": "777BB4",
    "MySQL": "BAE6FD",
}

LANGUAGE_EXTENSIONS = {
    "Python": [".py"],
    "Java": [".java"],
    "JavaScript": [".js"],
    "TypeScript": [".ts"],
    "C": [".c", ".h"],
    "C++": [".cpp", ".hpp", ".cc", ".cxx"],
    "C#": [".cs"],
    "PHP": [".php"],
    "MySQL": [".sql"],
}


def count_solutions():
    if not os.path.exists(SOLUTIONS_FOLDER):
        return 0
    with os.scandir(SOLUTIONS_FOLDER) as entries:
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
        "progress": f"https://img.shields.io/badge/Solved-{solved}%2F{total}%20({percentage}%25)-323232?style={BADGE_STYLE}&logo=leetcode",
        "C++": f"https://img.shields.io/badge/C%2B%2B23-{counts['C++']}%20solutions-{LOGO_COLOR['C++']}?style={BADGE_STYLE}&logo=cplusplus",
        "Java": f"https://img.shields.io/badge/Java-{counts['Java']}%20solutions-{LOGO_COLOR['Java']}?style={BADGE_STYLE}&logo=java",
        "Python": f"https://img.shields.io/badge/Python%203-{counts['Python']}%20solutions-{LOGO_COLOR['Python']}?style={BADGE_STYLE}&logo=python",
        "TypeScript": f"https://img.shields.io/badge/TypeScript-{counts['TypeScript']}%20solutions-{LOGO_COLOR['TypeScript']}?style={BADGE_STYLE}&logo=typescript",
        "MySQL": f"https://img.shields.io/badge/MySQL-{counts['MySQL']}%20solutions-{LOGO_COLOR['MySQL']}?style={BADGE_STYLE}&logo=mysql",
        "JavaScript": f"https://img.shields.io/badge/JavaScript-{counts['JavaScript']}%20solutions-{LOGO_COLOR['JavaScript']}?style={BADGE_STYLE}&logo=javascript",
        "C": f"https://img.shields.io/badge/C-{counts['C']}%20solutions-{LOGO_COLOR['C']}?style={BADGE_STYLE}&logo=c",
        "C#": f"https://img.shields.io/badge/C%23-{counts['C#']}%20solutions-{LOGO_COLOR['C#']}?style={BADGE_STYLE}&logo=csharp",
        "PHP": f"https://img.shields.io/badge/PHP-{counts['PHP']}%20solutions-{LOGO_COLOR['PHP']}?style={BADGE_STYLE}&logo=php",
    }


def update_readme(badges):
    readme_template = """<div align="center">
  <h1>🏆 LeetCode Solutions</h1>
  
  Solutions to [LeetCode](https://leetcode.com/problemset/all/) problems
  
  ---
  
  ![LeetCode Progress]({progress})
  <br/>
  ![Python]({Python})
  ![Java]({Java})
  ![TypeScript]({TypeScript})
  ![JavaScript]({JavaScript})
  <br/>
  ![C++]({C++})
  ![C]({C})
  ![C#]({C#})
  ![PHP]({PHP})
  ![MySQL]({MySQL})
  
  ---
</div>

## ✨ Features
- ✅ Clean & optimized solutions
- ✅ Multiple programming language solutions
- ✅ Perfect for learning algorithms and data structures

## 👨‍💻 Author
**Tamim Ahasan Rijon**  
📧 [tamimahasan.ar@gmail.com](mailto:tamimahasan.ar@gmail.com)  
🌐 [Portfolio](https://tamim-ar.netlify.app/)  
🔗 [LinkedIn](https://www.linkedin.com/in/tamim-ar/) • [GitHub](https://github.com/tamim-ar) • [X/Twitter](https://x.com/tamim__ahasan)  
📷 [Instagram](https://www.instagram.com/tamim__ahasan/) • [Facebook](https://www.facebook.com/hellotamim/)

## 🤝 Contributing
Contributions are welcome! 🚀  
To add or improve solutions:
1. **Fork** this repository  
2. Create a feature branch → `git checkout -b feature/your-solution`  
3. Commit changes → `git commit -m 'Add solution'`  
4. Push to your branch → `git push origin feature/your-solution`  
5. Open a **Pull Request** 🎯

## 📜 License
Licensed under the [MIT License](./LICENSE).
"""
    content = readme_template.format(**badges)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    solved = count_solutions()
    counts = count_solutions_by_language()
    badges = generate_badges(solved, TOTAL_PROBLEMS, counts)
    update_readme(badges)

    print("\n🚀 README Badges Updated Successfully!\n")
    print(
        f"📊 Solved: {solved}/{TOTAL_PROBLEMS} ({round((solved / TOTAL_PROBLEMS) * 100, 2)}%)\n"
    )
    print("📌 Solutions by Language:")
    for lang, count in counts.items():
        print(f"   • {lang:<10}: {count} solutions")
    print("\n✅ Done!\n")
