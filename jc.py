import re
import requests
import os

def is_github_404(url):
    try:
        resp = requests.head(url, allow_redirects=True, timeout=5)
        return resp.status_code == 404
    except requests.RequestException:
        return True

def clean_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    pattern = re.compile(r'\[([^\]]+)\]\((https://github\.com/[^\)]+)\)')
    
    for line in lines:
        matches = pattern.findall(line)
        keep_line = True
        for name, url in matches:
            if is_github_404(url):
                print(f"Removing 404 repo: {url}")
                keep_line = False
                break
        if keep_line:
            new_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

# 扫描所有 Markdown 文件
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)
            clean_md_file(path)

print("All 404 GitHub links removed.")
