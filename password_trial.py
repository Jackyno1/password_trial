#密碼重試程式
#密碼'a123456', 最多輸三次

i = 0
while i < 4:
	password = input('請問密碼:')
	if password != 'a123456':
		print('密碼錯誤, 還有', 2 - i , '次機會')
		i = i + 1
	else:
		print('登入成功!')
		i = 0
