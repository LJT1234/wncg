for num in range(100,1000):
	bw=num//100
	sw=(num-bw*100)//10
	gw=num%10
	if int(bw)**3+int(sw)**3+int(gw)**3==num:
		print('水仙花数:',num)
