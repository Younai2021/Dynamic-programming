x = [-2,11,-4,13,-5,-2]
def cal_mcs_2(ss):
    """
    # 动态规划算法：求最大连续子序列      时间复杂度（O(n)）
        1） 令状态 k[j] 为最大连续子序列最后一个元素。令dk[j]表示最大连续子序列和
        2）这个最大连续子序列和为从 dk[i] ~ dk[j]
    # 分两种情况：
        1)最大和就是k[j]。它之前的序列和都小於k[j]
        2)最大和是dk[j-1]+k[j]。
    # 于是得到状态转移方程：
        dk[j] = max{dk[j-1]+k[j], k[j]}      边界为 dk[0] = j[0]

    # 动态规划算法计算特点（步骤）：
        从后往前算，每步计算结果都记录进表。
        计算结束后，再遍历记录表。
    :param ss:
    :return:
    """
    dp = [ 0 for i in ss]
    dp[0] = 0
    for i in range(0, len(ss)):
        dp[i] = max(  dp[i-1] + ss[i], ss[i] ) # 如果dp[i-1]<0 则dp[i]直接变为ss[i]
    curr_sum = dp[0]

    for Sum in dp: # dp中选取最大的
        if Sum > curr_sum:
            curr_sum = Sum
    print(dp)
    return curr_sum

print('最大连续子序列的和为：',cal_mcs_2(x))