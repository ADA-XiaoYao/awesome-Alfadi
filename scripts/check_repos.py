import re
import requests
import datetime
from pathlib import Path

GITHUB_TOKEN = ""
HEADERS = {
    "Accept": "application/vnd.github+json"
}
if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"

README_PATH = Path("../README.md")

# 规则
MIN_STARS = 30
MAX_NO_UPDATE_DAYS = 365


def extract_github_links(text):
    pattern = r"https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)"
    return set(re.findall(pattern, text))


def get_repo_info(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    r = requests.get(url, headers=HEADERS)
    if r.status_code != 200:
        return None
    return r.json()


def score_repo(data):
    score = 100
    reasons = []

    stars = data.get("stargazers_count", 0)
    if stars < MIN_STARS:
        score -= 30
        reasons.append("low stars")

    pushed_at = data.get("pushed_at")
    if pushed_at:
        last_push = datetime.datetime.strptime(
            pushed_at, "%Y-%m-%dT%H:%M:%SZ"
        )
        days = (datetime.datetime.utcnow() - last_push).days
        if days > MAX_NO_UPDATE_DAYS:
            score -= 40
            reasons.append("inactive")

    if not data.get("license"):
        score -= 10
        reasons.append("no license")

    if data.get("archived"):
        score -= 50
        reasons.append("archived")

    return score, reasons


def main():
    text = README_PATH.read_text(encoding="utf-8")
    repos = extract_github_links(text)

    good, bad, pending = [], [], []

    for owner, repo in repos:
        info = get_repo_info(owner, repo)
        if not info:
            pending.append(f"{owner}/{repo} - api error")
            continue

        score, reasons = score_repo(info)

        line = f"{owner}/{repo} | score={score} | {','.join(reasons)}"

        if score >= 70:
            good.append(line)
        elif score >= 40:
            pending.append(line)
        else:
            bad.append(line)

        print(line)

    Path("../data").mkdir(exist_ok=True)

    Path("../data/good.txt").write_text("\n".join(good), encoding="utf-8")
    Path("../data/pending.txt").write_text("\n".join(pending), encoding="utf-8")
    Path("../data/bad.txt").write_text("\n".join(bad), encoding="utf-8")


if __name__ == "__main__":
    main()
