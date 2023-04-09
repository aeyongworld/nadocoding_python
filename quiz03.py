site = "http://naver.com"
siteSlice = site[7:]
index = siteSlice.index(".")
print(index)
siteSlice2 = siteSlice[:5]


print("생성된 비밀번호 : " + siteSlice2[:3] + str(len(siteSlice2)) + str(siteSlice2.count('e')) + "!")





# 모법답안

# url = "http://naver.com"
url = "http://google.com"
my_str = url.replace("http://", "") # 규칙1
# print(my_str)
my_str = my_str[:my_str.index(".")] # 규칙2
# my_str[0:5] -> 0 ~ 5 직전까지. (0, 1, 2, 3, 4)
# print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다." .format(url, password))
