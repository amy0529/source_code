fish_tuple=('����','����','����','����','����','�ڹ�')
fish_sum=[0,0,0,0,0,0,0,0,0,0,0,0]  #��¼ÿ��ˮ��Ʒ�������ͽ��
fish_records=['1��1��','����',18,10.5,'1��1��','����',8,6.2,'1��1��','����',7,4.7,'1��2��','����',2,7.2,'1��2��','����',3,12,'1��2��','����',6,15,'1��3��','�ڹ�',1,71,'1��3��','����',1,9.8]
fish_records[2]-=1  #��ȥҰè���ߵ���һ��
#-------------------�޸ĺ�����ֵ�۸�
i=1
fishs_len=len(fish_records)
while i<fishs_len:
    if fish_records[i]=='����':
        fish_records[i+1]=fish_records[i+1]*1.1  #���㶼��ֵ10%
    i+=4                                         #ѭ����������
#-------------------ͳ��ÿ��ˮ��Ʒ�������ͽ��
i=0
while i<fishs_len:
    if fish_tuple[0]==fish_records[i+1]:         #ͳ������
        fish_sum[0]+=fish_records[i+2]           #��¼����
        fish_sum[1]+=fish_records[i+2]*fish_records[i+3]#��¼���
    elif fish_tuple[1]==fish_records[i+1]:       #ͳ������
        fish_sum[2]+=fish_records[i+2]           #��¼����
        fish_sum[3]+=fish_records[i+2]*fish_records[i+3]#��¼���
    elif fish_tuple[2]==fish_records[i+1]:       #ͳ������
        fish_sum[4]+=fish_records[i+2]           #��¼����
        fish_sum[5]+=fish_records[i+2]*fish_records[i+3]#��¼���
    elif fish_tuple[3]==fish_records[i+1]:       #ͳ�Ʋ���
        fish_sum[6]+=fish_records[i+2]           #��¼����
        fish_sum[7]+=fish_records[i+2]*fish_records[i+3]#��¼���
    elif fish_tuple[4]==fish_records[i+1]:       #ͳ�ƺ���
        fish_sum[8]+=fish_records[i+2]           #��¼����
        fish_sum[9]+=fish_records[i+2]*fish_records[i+3]#��¼���
    elif fish_tuple[5]==fish_records[i+1]:       #ͳ������
        fish_sum[10]+=fish_records[i+2]           #��¼����
        fish_sum[11]+=fish_records[i+2]*fish_records[i+3]#��¼���
    i+=4                                         #ѭ����������
j=0
amount=0            #���۶��ʼ����ֵ
total_nums=0        #��������ʼ����ֵ
while j<len(fish_sum):
    if j%2==0:
       total_nums+=fish_sum[j]
    else:
       amount+=fish_sum[j]
    j+=1

#-------------------����ɱ�,������
cost=180+20+1+amount*0.05     #��ɱ�
profit=amount-cost            #������
#-------------------��ӡ����è����ͳ�ƽ��
i=0

while i<len(fish_tuple):
    print('%s������%d ,�����%f'%(fish_tuple[i],fish_sum[i*2],fish_sum[i*2+1]))
    i+=1
print('-'*30)
print('����è�ܹ�����%d��ˮ��Ʒ,Ԥ�����۶�Ϊ%.2fԪ,�ɱ�Ϊ%.2fԪ,����Ϊ%.2fԪ'%(total_nums,amount,cost,profit))
#==============================ִ�н������
����������21 ,�����224.300000
����������8 ,�����49.600000
����������7 ,�����32.900000
����������2 ,�����14.400000
����������6 ,�����99.000000
�ڹ�������1 ,�����71.000000
------------------------------
����è�ܹ�����45��ˮ��Ʒ,Ԥ�����۶�Ϊ491.20Ԫ,�ɱ�Ϊ225.56Ԫ,����Ϊ265.64Ԫ

