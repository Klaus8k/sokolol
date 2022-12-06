# import sqlite3

# con = sqlite3.connect('db.sqlite3')
# cur = con.cursor()

# # data = [(33,23),(44,43),(44,43)]
# # cur.executemany('insert into test_table values(?,?)', data)
# # con.commit()

# def show_test_table():
#     print(cur.execute('select * from test_table').fetchall())


# show_test_table()
# # fff



# # print(dir(con)).0

class Solution:
    def twoSum(self, nums: list, target: int):
        
        for i in nums:
            count = 0
            for x in nums[nums.index(i)+1:]:
                # print([nums.index(i),nums.index(x)])
                count += 1
                
                if x + i == target:
                    # print([nums.index(i),count])
                    if x == i:
                        return [nums.index(i),count]
                    else: 
                        return [nums.index(i),nums.index(x)]

                        

x = Solution()
print(x.twoSum([3,3],6))
print(x.twoSum([2,5,5,11],10))
