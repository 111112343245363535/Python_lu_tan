# 定义四则运算函数
def add(x, y):
    """加法函数：返回两个数的和"""
    return x + y

def subtract(x, y):
    """减法函数：返回被减数减减数的差"""
    return x - y

def multiply(x, y):
    """乘法函数：返回两个数的积"""
    return x * y

def divide(x, y):
    """除法函数：返回被除数除以除数的商，处理除零异常"""
    if y == 0:
        return "Error: 除数不能为0（除零错误）"
    return x / y

# 主程序循环
while True:
    # 打印操作菜单
    print("\n===== Python计算器 =====")
    print("选择运算操作：")
    print("1. 加法")
    print("2. 减法")
    print("3. 乘法")
    print("4. 除法")
    
    # 获取用户操作选择并判断有效性
    choice = input("请输入选择(1/2/3/4)：")
    if choice not in ['1', '2', '3', '4']:
        print("Invalid Input（无效输入）！请选择1-4的数字")
        continue  # 回到循环开头，重新选择
    
    # 获取用户输入的两个数字，处理非数字输入异常
    try:
        num1 = float(input("请输入第一个数字："))
        num2 = float(input("请输入第二个数字："))
    except ValueError:
        print("Invalid Input（无效输入）！请输入有效的数字")
        continue  # 回到循环开头，重新输入
    
    # 根据选择执行对应运算并输出结果
    if choice == '1':
        print(f"\n{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"\n{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"\n{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"\n{num1} / {num2} = {result}")
    
    # 询问是否继续计算
    next_calc = input("\n是否继续计算？(yes/no)：").lower()
    if next_calc != 'yes':
        print("计算器已退出，感谢使用！")
        break  # 退出循环，结束程序
