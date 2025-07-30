import requests

resume = {
    "name": "张三",
    "education": "硕士",
    "skills": ["Python", "SQL", "FastAPI"],
    "projects": [
        {
            "name": "简历评分系统",
            "description": "基于 FastAPI 实现的简历评分平台",
            "tech_stack": ["FastAPI", "SQLite"]
        }
    ],
    "target_position": "后端开发"
}

resp = requests.post("http://127.0.0.1:8000/score", json=resume)
print(resp.json())
