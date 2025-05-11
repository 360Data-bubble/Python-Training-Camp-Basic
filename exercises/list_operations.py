"""
练习: 列表操作

描述：
实现对学生列表的添加、删除和修改操作。

请补全下面的函数，对学生列表进行各种操作。
"""

def student_list_operations(students, operation, *args):
    """
    对学生列表进行操作
    
    参数:
    - students: 学生列表
    - operation: 操作类型 ("add", "remove", "update")
    - args: 操作所需的额外参数
    
    返回:
    - 操作后的学生列表
    """
    # 请在下方编写代码
    if operation == "add":
        return students + list(args)
    elif operation == "remove":
        try:
            for items in args:
                students.remove(items)
            return students
        except ValueError:
            return students
    elif operation == "update":
        args1,args2 = args
        index = students.index(args1)
        students[index] = args2
        return students
