#汇率转换器
meiyuan=float(input("请输入美元金额："))
rmb=meiyuan*7.0957
print(meiyuan,"美元","=",rmb,"元")


number_of_confirmed= int(input("请输入确诊人数:"))
number_of_cured= int(input("请输入治愈人数:"))
bili=number_of_cured/number_of_confirmed
print("治愈比例为",bili*100,"%",sep="")


number=int(input("请输入一个四位数:"))
qian=number//1000
bai=number%1000//100
shi=number%100//10
ge=number%10
sum=(qian+shi+bai+ge)
print("四位数字之和为：",sum)


shuliang=int(input("请输入物品的购买数量:"))
danjia=float(input("请输入这个物品的单价:"))
sum=(shuliang* danjia)
print("总价为:",sum,"元")