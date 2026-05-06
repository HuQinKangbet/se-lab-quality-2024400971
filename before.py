# 重构后：消除重复代码、删除无用变量、提取公共函数
def calculate_average(score_list, title):
    """提取公共逻辑：计算平均分并打印结果"""
    total = 0
    count = 0
    for score in score_list:
        if score >= 0:
            total += score
            count += 1
    if count == 0:
        return 0
    avg = total / count
    print(f"{title}计算完成")
    print("总分：", total)
    print("平均分：", avg)
    return avg

def calculate_student_score(score_list):
    return calculate_average(score_list, "学生分数")

def calculate_teacher_score(score_list):
    return calculate_average(score_list, "教师分数")

if __name__ == "__main__":
    student_scores = [85, 92, 78, 90]
    teacher_scores = [95, 88, 96]
    calculate_student_score(student_scores)
    calculate_teacher_score(teacher_scores)
