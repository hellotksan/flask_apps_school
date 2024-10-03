# 関数outer
def outer(func):
    # 関数内関数inner
    def inner(*args, **kwargs):
        print('===開始===')
        func(*args, **kwargs)
        print('===終了===')
    return inner

# タプル
nums = (10, 20, 30, 40)
# 関数show_sum
@outer
def show_sum(nums):
    sum = 0
    for num in nums:
        sum += num
    print(sum)

# 辞書
users = {'山田': 30, '田中': 40, '中村': 50}
@outer
def show_info(users):
    for name, age in users.items():
        print(f'名前:{name}, 年齢:{age}')

# 関数の実行
show_sum(nums)
show_info(users)
