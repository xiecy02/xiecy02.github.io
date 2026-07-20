
import os
import datetime
import subprocess

# ================= 配置区 =================
BLOG_POSTS_PATH = r"D:\code\xiecy02.github.io\content\posts"
# ==========================================

def create_note():
    # 1. 输入标题
    title = input("📝 标题 (回车默认为‘随记’): ").strip() or "随记"
    
    # 2. 输入自定义文件名（新增功能）
    custom_name = input("💾 请输入文件名 (留空则默认使用时间命名): ").strip()
    
    # 3. 选择分类
    print("选择分类: [1] Study  [2] Life")
    choice = input("请输入数字: ").strip()
    category = "Life" if choice == "2" else "Study"

    now = datetime.datetime.now()
    
    # 4. 判断文件名逻辑
    if custom_name:
        # 如果用户自己输入了名字，确保它以 .md 结尾
        if not custom_name.endswith(".md"):
            file_name = f"{custom_name}.md"
        else:
            file_name = custom_name
    else:
        # 如果用户直接回车，依然使用时间戳命名
        file_name = f"{now.strftime('%Y-%m-%d-%H%M%S')}.md"
        
    full_path = os.path.join(BLOG_POSTS_PATH, file_name)

    # 5. 模板内容
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
        # 确保 content/posts 目录存在，如果不存在会自动创建
        os.makedirs(BLOG_POSTS_PATH, exist_ok=True)
        
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(template)
        print(f"✅ 已生成: {file_name}")
        subprocess.run(["code", full_path], shell=True)
    except Exception as e:
        print(f"❌ 错误: {e}")

if __name__ == "__main__":
    create_note()
