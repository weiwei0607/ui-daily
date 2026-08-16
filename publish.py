#!/usr/bin/env python3
"""一次 commit 指定檔案到 GitHub（用 Git Data API，免逐檔 sha）。
用法：GH_TOKEN=xxx python3 publish.py "<commit msg>" <path1> <path2> ...
路径相对 repo 根目录。"""
import os, sys, json, base64, urllib.request

TOKEN = os.environ["GH_TOKEN"]
REPO = os.environ.get("GH_REPO", "weiwei0607/ui-daily")
BRANCH = os.environ.get("GH_BRANCH", "master")
API = f"https://api.github.com/repos/{REPO}"

def req(method, url, body=None):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(url, data=data, method=method,
        headers={"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github+json",
                 "User-Agent": "ui-daily-publisher"})
    with urllib.request.urlopen(r, timeout=30) as resp:
        return json.loads(resp.read().decode())

def main():
    msg = sys.argv[1]
    files = sys.argv[2:]
    if not files:
        print("no files"); return
    ref = req("GET", f"{API}/git/ref/heads/{BRANCH}")
    base_commit = ref["object"]["sha"]
    base_tree = req("GET", f"{API}/git/commits/{base_commit}")["tree"]["sha"]
    tree = []
    for path in files:
        with open(path, "rb") as f:
            content = base64.b64encode(f.read()).decode()
        blob = req("POST", f"{API}/git/blobs", {"content": content, "encoding": "base64"})
        tree.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    new_tree = req("POST", f"{API}/git/trees", {"base_tree": base_tree, "tree": tree})["sha"]
    commit = req("POST", f"{API}/git/commits", {"message": msg, "tree": new_tree, "parents": [base_commit]})["sha"]
    req("PATCH", f"{API}/git/refs/heads/{BRANCH}", {"sha": commit})
    print(f"committed {commit[:8]} ({len(files)} files)")

if __name__ == "__main__":
    main()
