
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
	bool fin;//是否完成
}PCB;

template <class T>
class PCBTABLE
{
public:
	PCBTABLE():num(0),head(NULL),resource(0){  front();}
	void front();//初始化过程，装入所有初始数据，
	//为各有关变量置初值，检查每个进程请求的资源
	//总数是否超过系统所能提供的资源数。
	//void print();//输出一次分配分配结果
	void printall();//输出总体情况
	//void relieve();//当测得资源不够分配或分配后
	//可能产生死锁，回收已假定分配了的资源。
	//void termination();//检查每个进程时候都已完成
	//或者发生死锁。如果进程全部完成或发生死锁，
	//则将全局变量advance置成true，不然置成false。
	//void back();//收回当前进程的全部资源，并将此进
	//程的vpstatus置1。 
	//void rr();//为检查进程的分配资源数是否超过了它
	//的最大申请量，或是释放的资源数是否超过占有数，
	//这里是检查例外情况。
	//void rrrr();//为各进程设置能执行完标志T，对于还
	//不能完成的进程将它的标志置1，能完成的进程标志
	//T置0。
	void safe();//测试在当前分配状态下，会不会发生
	//死锁，若不会，死锁函数值返回true，否则返回
	//false。
	bool allocate(int allocatepid);//按申请向当前进程分配或收回资源。
	int find();
 void matrix();
private:
	PCB* head;
	int resource;//系统总容量
	int num;//进程总数
};
template <class T>
void PCBTABLE<T>::front()
{
	if(head)//初始情况下未分配
	{
		cout<<"初始出错！"<<endl;
		return;
	}
	//int need, allocation, max;//局部变量
	cout<<"进程数："<<flush;
	cin>>num;
	head = new PCB [num];
	cout<<"系统资源初始值："<<flush;
	cin>>resource;
	cout<<"请输入初始资源请求need和已分配资源数allocation："<<endl;
	//for(int i = 0; i < num; i++)
	//{
	//	head[i].pid = i;//进程号
	//	while(1)
	//	{
	//		cout<<i<<":"<<flush;
	//		cin>>need;
	//		cin>>allocation;
	//		max = need + allocation;
	//		if(need <= resource)//不超过系统总容量
	//			break;
	//		else
	//			cout << "max超过resource，请重新输入：" << endl;
	//	}
	//	head[i].max = max;
	//	head[i].fin = 0;
	//	head[i].need = need;
	//	head[i].allocation = allocation;
	//}
	for(int i = 0; i < num; i++)
	{
		head[i].pid = i;//进程号
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
		cout<<"空"<<flush;
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
			cout<<"资源不够"<<endl;
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
			cout << "资源不够" << endl;
			return;
		}
	}
}
#endif