
//PCB.h
#ifndef PCB_H
#define PCB_H

#include <iostream>
using namespace std;

typedef struct P
{
	int pid;
	int need;
	int allocation;
	int max;
	bool fin;//�Ƿ����
}PCB;

template <class T>
class PCBTABLE
{
public:
	PCBTABLE():num(0),head(NULL),resource(0){  front();}
	void front();//��ʼ�����̣�װ�����г�ʼ���ݣ�
	//Ϊ���йر����ó�ֵ�����ÿ�������������Դ
	//�����Ƿ񳬹�ϵͳ�����ṩ����Դ����
	//void print();//���һ�η��������
	void printall();//����������
	//void relieve();//�������Դ�������������
	//���ܲ��������������Ѽٶ������˵���Դ��
	//void termination();//���ÿ������ʱ�������
	//���߷����������������ȫ����ɻ���������
	//��ȫ�ֱ���advance�ó�true����Ȼ�ó�false��
	//void back();//�ջص�ǰ���̵�ȫ����Դ�������˽�
	//�̵�vpstatus��1�� 
	//void rr();//Ϊ�����̵ķ�����Դ���Ƿ񳬹�����
	//������������������ͷŵ���Դ���Ƿ񳬹�ռ������
	//�����Ǽ�����������
	//void rrrr();//Ϊ������������ִ�����־T�����ڻ�
	//������ɵĽ��̽����ı�־��1������ɵĽ��̱�־
	//T��0��
	void safe();//�����ڵ�ǰ����״̬�£��᲻�ᷢ��
	//�����������ᣬ��������ֵ����true�����򷵻�
	//false��
	bool allocate(int allocatepid);//��������ǰ���̷�����ջ���Դ��
	int find();
 void matrix();
private:
	PCB* head;
	int resource;//ϵͳ������
	int num;//��������
};
template <class T>
void PCBTABLE<T>::front()
{
	if(head)//��ʼ�����δ����
	{
		cout<<"��ʼ����"<<endl;
		return;
	}
	//int need, allocation, max;//�ֲ�����
	cout<<"��������"<<flush;
	cin>>num;
	head = new PCB [num];
	cout<<"ϵͳ��Դ��ʼֵ��"<<flush;
	cin>>resource;
	cout<<"�������ʼ��Դ����need���ѷ�����Դ��allocation��"<<endl;
	//for(int i = 0; i < num; i++)
	//{
	//	head[i].pid = i;//���̺�
	//	while(1)
	//	{
	//		cout<<i<<":"<<flush;
	//		cin>>need;
	//		cin>>allocation;
	//		max = need + allocation;
	//		if(need <= resource)//������ϵͳ������
	//			break;
	//		else
	//			cout << "max����resource�����������룺" << endl;
	//	}
	//	head[i].max = max;
	//	head[i].fin = 0;
	//	head[i].need = need;
	//	head[i].allocation = allocation;
	//}
	for(int i = 0; i < num; i++)
	{
		head[i].pid = i;//���̺�
		cout<<i<<":"<<flush;
		cin>>head[i].need;
		cin>>head[i].allocation;
		head[i].max = head[i].need + head[i].allocation;
		head[i].fin = 0;
	}
	printall();
}
template <class T>
void PCBTABLE<T>::printall()
{
	if(!head)
	{		
		cout<<"��"<<flush;
		return;
	}
	cout << "Process		Need		Allocation	Max" << endl;
	for(int i = 0; i < num; i++)
		cout << head[i].pid << "		" << head[i].need 
          << "		" << head[i].allocation << "		" 
          << head[i].max << endl;
}
template <class T>
int PCBTABLE<T>::find()
{
	static int pid = 0;
	int i = pid;
	while(1)
	{
		if(head[i].fin == 0)
		{
			pid = (i + 1) % num;
			return i;
		}
		i = (i + 1) % num;
	}
}
template <class T>
void PCBTABLE<T>::safe()
{
	int allocatepid;
	int count = 0;
	int failcount = 0;
	cout<<"(I)		process		need		allocation	remainder" << endl;
	while(1)
	{
		allocatepid = find();
		if(allocate(allocatepid))
		{
			cout<<"("<<allocatepid<<")		" 
				<< head[allocatepid].pid << "		" 
				<< head[allocatepid].need << "		" 
				<<head[allocatepid].allocation << "		" 
				<< resource << endl;
			count++;
			if(count == num)
			{
				cout << "all clear.safe..." << endl;
				return;
			}
		}
		failcount++;
		if(failcount == (num * num))
		{
			cout<<"��Դ����"<<endl;
			return;
		}
	}
}
template <class T>
bool PCBTABLE<T>::allocate(int allocatepid)
{
	if(head[allocatepid].need <= resource)
	{
		head[allocatepid].fin = 1;
		resource += head[allocatepid].allocation;
		return true;
	}
	return false;
}
template <class T>
void PCBTABLE<T>::matrix()
{
	int count = 0;
	int j = 0;
	while(1)
	{
		for(int i = 0; i < num; i++)
		{
			if(!head[i].fin&&(head[i].need <= resource))
			{
				head[i].fin = 1;
				resource += head[i].allocation;
				count++;
			}
		}
		j++;
		if(count == num)
		{
			cout << "all clear..." << endl;
			return;
		}
		else if(j == num)
		{
			cout << "��Դ����" << endl;
			return;
		}
	}
}
#endif