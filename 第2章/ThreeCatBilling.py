num1,num2,num3=5,6,9
price1,price2,price3=8.1,8.2,8
fish1,fish2,fish3='����','����','����'
date='2017��12��'
Total_Num=num1+num2+num3      #�ܵ�����
Total_Amount=num1*price1+num2*price2+num3*price3 #�ܽ��
print("-----"*4+"����è���˵�"+"-----"*4)
print('����ص�   '+'��������   '+'   ����  '+'����������'+' ���ۣ�Ԫ��')
print('��С��    '+date+'1�� '+fish1+'  '+str(num1)+'         '+str(price1))
print('��С��    '+date+'2�� '+fish2+'  '+str(num2)+'         '+str(price2))
print('��  ��    '+date+'3�� '+fish3+'  '+str(num3)+'         '+str(price3))
print("----"*12+'--')
print('�����ܼ�%d�����г��۸��ܼ�%.2fԪ��ÿ��ƽ����������Լ%d��(%f��)'
      %(Total_Num,Total_Amount,int(Total_Num/3),Total_Num/3))



      

