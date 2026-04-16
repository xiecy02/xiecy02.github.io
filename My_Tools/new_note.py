import os
import datetime
import subprocess

# ================= 配置区 =================
BLOG_POSTS_PATH = r"D:\My_GitHub\xiecy02.github.io\content\posts"
# ==========================================

def create_note():
    title = input("📝 标题 (回车默认为‘随记’): ").strip() or "随记"
    print("选择分类: [1] Study  [2] Life")
    choice = input("请输入数字: ").strip()
    category = "Life" if choice == "2" else "Study"

    now = datetime.datetime.now()
    file_name = f"{now.strftime('%Y-%m-%d-%H%M%S')}.md"
    full_path = os.path.join(BLOG_POSTS_PATH, file_name)

    # 1. 具体的时刻信息（保留在正文第一行）
    # 2. 链接和图片语法隐藏在注释里，随用随复制，不填不显示
    template = f"""---
title: "{title}"
date: {now.strftime('%Y-%m-%dT%H:%M:%S+08:00')}
categories: ["{category}"]
draft: false
---

> 🕒 记录时刻：{now.strftime('%H:%M:%S')}

在此开始输入正文...


"""

    try:
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(template)
        print(f"✅ 已生成: {file_name}")
        subprocess.run(["code", full_path], shell=True)
    except Exception as e:
        print(f"❌ 错误: {e}")

if __name__ == "__main__":
    create_note()