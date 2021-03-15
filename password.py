set_password = 'a123456'
n = 1
while n <= 3:
    password = input('請輸入密碼: ')
    if password == set_password:
        print('登入成功')
        break
    else:
    	if n < 3 :
    	    print('密碼錯誤! 還有', 3-n, '次機會')
    	else:
    		print('登入失敗, 請用原信箱重設密碼')
    n += 1
    