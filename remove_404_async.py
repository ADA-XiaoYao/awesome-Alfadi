import os
import re
import aiohttp
import asyncio

# 用于存放所有 404 链接
broken_links = []

# 正则匹配 GitHub 仓库 Markdown 链接
pattern = re.compile(r'\[([^\]]+)\]\((https://github\.com/[^\)]+)\)')

# 异步检查 URL 是否 404
async def check_url(session, name, url):
    try:
        async with session.head(url, allow_redirects=True, timeout=10) as resp:
            if resp.status == 404:
                print(f"[404] {url}")
                broken_links.append(url)
                return True
    except Exception:
        print(f"[Error] {url}")
        broken_links.append(url)
        return True
    return False

# 异步处理单个 Markdown 文件
async def process_file(session, file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    tasks = []

    # 先收集任务
    for line in lines:
        matches = pattern.findall(line)
        for name, url in matches:
            tasks.append(check_url(session, name, url))

    results = await asyncio.gather(*tasks)

    # 删除 404 链接对应行
    idx = 0
    for line in lines:
        matches = pattern.findall(line)
        remove_line = False
        for i, (name, url) in enumerate(matches):
            if url in broken_links:
                remove_line = True
                break
        if not remove_line:
            new_lines.append(line)
        idx += 1

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

# 遍历所有 Markdown 文件
async def main():
    async with aiohttp.ClientSession() as session:
        md_files = []
        for root, dirs, files in os.walk("."):
            for file in files:
                if file.endswith(".md"):
                    md_files.append(os.path.join(root, file))

        tasks = [process_file(session, file) for file in md_files]
        await asyncio.gather(*tasks)

    # 生成报告文件
    with open("404_report.txt", "w", encoding="utf-8") as f:
        for url in broken_links:
            f.write(url + "\n")
    print("\n✅ All 404 links removed. Report saved to 404_report.txt")

if __name__ == "__main__":
    asyncio.run(main())
