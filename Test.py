#!/usr/bin/env python
# coding: utf-8

# # 1 เขียนโปรแกรมคำนวณอายุ

# In[1]:


Y = 2562
B=(input(" ปี พ.ศ. เกิด "))
c=int(B)
a=Y-c
print("อายุของคุณ",a,"ปี")


# # 2 โปรแกรมคำนวณการซื้อสินค้า

# In[2]:


p1 = float(input("ราคาสินค้าชิ้นที่ 1  "))
p2 = float(input("ราคาสินค้าชิ้นที่ 2  "))
p3 = float(input("ราคาสินค้าชิ้นที่ 3  "))
print("สินค้าชิ้นที่ 1  ราคา ",p1,"  บาท")
print("สินค้าชิ้นที่ 2  ราคา ",p2,"  บาท")
print("สินค้าชิ้นที่ 3  ราคา ",p3,"  บาท")
money=p1+p2+p3
print("สรุปราคารวมสินค้า  ",money,"  บาท")
print("Good Bye!!")


# # 3 เขียนโปรแกรมแสดงผลสูตรคูณแม่ 2 โดยใช้คำสั่ง for

# In[3]:


m=2
for i in range(1,13):
         result = m*i
         print(" 2 x ",i," = ",result)


# In[4]:


#4 โปรแกรมวนซ้ำโดนใช้ While


# In[5]:


h = "Hello"
w = "World"
i = 0
while  i < 5: 
    print(h)
    if i <  4 :
        print(w)
    i += 1


# In[ ]:




