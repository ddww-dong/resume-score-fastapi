# Resume Scoring System (FastAPI + SQLite)

一个基于 FastAPI + SQLite 构建的简历评分系统，支持上传简历信息（JSON），根据教育背景、技能匹配度、项目经历等维度自动评分并返回结果。


---

## 项目亮点

-  使用 FastAPI 快速构建高性能 API 服务
-  支持基于学历、技能、项目的自动评分逻辑
-  使用 SQLite 存储评分结果，便于后续分析
-  包含测试脚本与异常处理，代码结构清晰
-  自动生成 Swagger 文档，支持在线测试接口

---
<!-- 
## 项目结构
resume_score/
├── main.py # FastAPI 主应用入口
├── models.py # Pydantic 数据模型定义
├── scorer.py # 简历评分逻辑
├── database.py # SQLite 数据库操作
├── tests.py # 接口测试脚本
├── example_resume.json # 简历示例
├── requirements.txt # 项目依赖
└── README.md
 -->

---

## 📦 快速开始

#### 克隆仓库并安装依赖

git clone https://github.com/ddww-dong/resume-score-fastapi.git
cd resume-score-fastapi  
python -m venv .venv  
source .venv/bin/activate  # Windows: .venv\Scripts\activate  
pip install -r requirements.txt

#### 运行应用

uvicorn main:app --reload

访问文档页面：
👉 http://127.0.0.1:8000/docs


#### 示例：上传简历并评分

示例请求体（example_resume.json）：  
{  
  "name": "张三",  
  "education": "硕士",  
  "skills": ["Python", "SQL", "FastAPI"],  
  "projects": [  
    {  
      "name": "简历评分系统",  
      "description": "基于 FastAPI 实现的评分  平台",
      "tech_stack": ["FastAPI", "SQLite"]  
    }  
  ], 
  "target_position": "后端开发" 
} 

响应示例： 
{ 
  "name": "张三", 
  "score": 65 
} 

# 接口测试
python test.py
