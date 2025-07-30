def score_resume(resume):
    score = 0

    # 教育背景评分
    if "博士" in resume.education:
        score += 30
    elif "硕士" in resume.education:
        score += 20
    elif "本科" in resume.education:
        score += 10

    # 技能匹配度评分（假设职位需要 Python 和 SQL）
    required_skills = {"python", "sql"}
    match = required_skills.intersection(set(map(str.lower, resume.skills)))
    score += len(match) * 10

    # 项目经历评分
    score += len(resume.projects) * 5

    return min(score, 100)
