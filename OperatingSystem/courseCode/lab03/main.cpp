//实验三.cpp

#include <iostream>
#include <time.h>
#include <stdlib.h>
using namespace std;

#define PROJECT_SIZE 256 //寻址大小
#define VIRTUAL_MEMORY 32768 //虚存大小
#define MM_SIZE 100;//内存空间默认从0-99
//分配表大小也设成MM_SIZE大小

//假定按照工程中的顺序执行，从0-255

typedef struct Real
{
	bool flag; //true表示被占用，反之表示未被占用
	int page; //虚存中的页码
}real;

typedef struct REAL
{
	int page;
	int order;
}REAL;

typedef struct jiedizhi
{
	int head;//空白可分配空间首地址
	int size;//空白可分配空间大小
	bool flag;//分配标志，true表示已分配，false表示未分配
}jiedizhi;

void lru(int pageNo[], int realSize)
{
	int shixiaocishu = 0;
	int weimanbiaozhi;
	double mingzhonglv;
	REAL* r = new REAL [realSize];
	for(int i = 0; i < realSize; i++)//初始化
		r[i].order = 0;
	for(int i = 0; i < PROJECT_SIZE; i++)
	{
		weimanbiaozhi = 0;
		for(int j = 0; j < realSize; j++)
		{
			if(r[j].page == pageNo[i])//已有该页，更新r[i].order
			{
				weimanbiaozhi = 1;
				for(int k = 0; k < realSize; k++)
					if(r[k].order != 0)
						r[k].order++;
				r[j].order = 1;
				r[j].page = pageNo[i];
				break;
			}
			if(r[j].order == 0)//未满
			{
				shixiaocishu++;
				weimanbiaozhi = 2;
				for(int k = 0; k <realSize; k++)
					if(r[k].order != 0)
						r[k].order++;
				r[j].order = 1;
				r[j].page = pageNo[i];
			}
		}
		if(weimanbiaozhi == 0)//已满必须被替代
		{
			shixiaocishu++;
			for(int j = 0; j < realSize; j++)
				if(r[j].order == realSize)
				{
					for(int k = 0; k <realSize; k++)
						if(r[k].order != 0)
							r[k].order++;
					r[j].order = 1;
					r[j].page = pageNo[i];
					break;
				}
		}
	}
	cout << "失效次数：" << shixiaocishu << endl;
	mingzhonglv = 1 - shixiaocishu * 1.0 / PROJECT_SIZE;
	cout << "命中率：" << mingzhonglv << endl;
}
void opt(int pageNo[], int realSize)
{
	int Flag;//标识实存是否装满
	int ff;//标识是否删除此页
	int taotai;//标记淘汰
	int zuiwanshiyongtemp;
	int zuiwanshiyongnum;
	int shixiaocishu = 0;
	double mingzhonglv;
	real* r = new real [realSize];
	for(int i = 0; i < realSize; i++)//初始化实存内容，全部未被占用
		r[i].flag = false;
	for(int i = 0; i < PROJECT_SIZE; i++)
	{
		Flag = -1;
		for(int j = 0; j < realSize; j++)
		{
			if(r[j].page == pageNo[i])
			{
				Flag = 999999;
				break;
			}
			if(r[j].flag == false)//未装满
			{
				Flag = j;
				break;
			}
		}
		switch(Flag)
		{
		case 999999://页表中已装有此页
			break;
		case -1://装满了
			shixiaocishu++;
			for(int j = 0; j < realSize; j++)
			{
				taotai = 0;
				for(ff = i + 1; ff < PROJECT_SIZE; ff++)
				{
					if(pageNo[ff] == r[j].page)//后续仍需访问该页
					{
						taotai = 1;
						break;
					}
				}
				if(taotai == 0)
					//后续不会再访问该页
				{
					r[j].flag = true;
					r[j].page = pageNo[i];
					taotai = 2;
					break;
				}
			}
			if(taotai != 2)//淘汰最晚使用的页面
			{
				zuiwanshiyongtemp = 0;//最晚使用序号
				zuiwanshiyongnum = 0;//最晚使用时间
				for(int j = 0; j < realSize; j++)
				{
					for(ff = i + 1; ff < PROJECT_SIZE; ff++)
						if(pageNo[ff] == r[j].page)//后续第一次使用时间
							if(ff > zuiwanshiyongnum)
							{
								zuiwanshiyongtemp = j;
								zuiwanshiyongnum = ff;
							}
				}
				r[zuiwanshiyongtemp].page = pageNo[i];
				r[zuiwanshiyongtemp].flag = true;
			}
			break;
		default://未装满
			shixiaocishu++;
			r[Flag].page = pageNo[i];
			r[Flag].flag = true;
		}
	}
	cout << "失效次数：" << shixiaocishu << endl;
	mingzhonglv = 1 - shixiaocishu * 1.0 / PROJECT_SIZE;
	cout << "命中率：" << mingzhonglv << endl;
	return;
}

int chushihua(jiedizhi* d)//默认初始化的数据输入正确，这里先不做正误判断
{
	int num, head, size;
	cout << "未被分配空间的初始化：" << endl << "共有段数：" <<endl;
	cin >> num;
	cout << "依次输入未被分配的空间（head:0-99,size:0-99）：" << endl;
	for(int i = 0; i < num; i++)
	{
		cin >> head;
		while((head > 99) | (head < 0))
		{
			cout << "请填写0-99之间的数字:" << flush;
			cin >> head;
		}
		cin >> size;
		while((size > 99) | (size <= 0))
		{
			cout << "请填写0-99之间的数字:" << flush;
			cin >> size;
		}
		d[i].flag = 0;
		d[i].head = head;
		d[i].size = size;
	}
	for(int i = 0; i < num; i++)
		cout << i << ":" << " flag: " << d[i].flag
		<< " head: " << d[i].head << " size: " 
		<< d[i].size << endl;
	return num;
}
void shoucipipei(jiedizhi* d, int& num)
{
	int n, x, y;
	cout << "用首次适应法：" << endl << "输入要一共需要分配的空间个数："<<flush;
	cin >> n;
	for(int j = 0; j < n; j++)
	{
		cin >> x;
		y = 0;
		for(int i = 0; i < num; i++)
			if(x <= d[i].size)
			{
				y = 1;
				d[i].head += x;
				d[i].size -= x;
				if(d[i].size == 0)
				{
					for(int k = i; k < num - 1; k++)
//如果前面一项空白处被占据则前移
					{
						d[k].flag = d[k + 1].flag;
						d[k].head = d[k + 1].head;
						d[k].size = d[k + 1].size;
					}
					d[num-1].flag = 1;
					num--;
				}
				break;
			}
			if(y == 0)//未被分配
				cout << "太大" << endl;
			//合并算法
			else
				for(int i = 0; i < num; i++)
					cout << i << ": " << d[i].size << endl;
	}
}
void paixu(jiedizhi d[],int& num)
{
	int temp, jiaohuan;
	for(int i = 0; i < num; i++)
	{
		temp = i;
		for(int j = i + 1; j < num; j++)
		{
			if(d[temp].size > d[j].size)
				temp = j;
		}
		jiaohuan = d[temp].head;
		d[temp].head = d[i].head;
		d[i].head = jiaohuan;
		jiaohuan = d[temp].size;
		d[temp].size = d[i].size;
		d[i].size = jiaohuan;
	}
	for(int i = 0; i < num; i++)
		cout << i << ": " << d[i].size << endl;
}
void zuijiapipei(jiedizhi* d, int& num)
{
	int n, x, y;
	cout << "用最佳适应法：" << endl << "输入要一共需要分配的空间个数："<<flush;
	cin >> n;
	paixu(d, num);
	for(int j = 0; j < n; j++)
	{
		cin >> x;
		y = 0;
		for(int i = 0; i < num; i++)
			if(x <= d[i].size)
			{
				y = 1;
				d[i].head += x;
				d[i].size -= x;
				if(d[i].size == 0)
				{
					for(int k = i; k < num - 1; k++)
//如果前面一项空白处被占据则前移
					{
						d[k].flag = d[k + 1].flag;
						d[k].head = d[k + 1].head;
						d[k].size = d[k + 1].size;
					}
					d[num-1].flag = 1;
					num--;
				}
				paixu(d,num);//重新排序
				break;
			}
			if(y == 0)//未被分配
				cout << "太大" << endl;
			//合并算法
	}
}
void jiedizhiguanli()
{
	int num = MM_SIZE;
	jiedizhi* d = new jiedizhi[num];
	num = chushihua(d);
	shoucipipei(d,num);
	zuijiapipei(d,num);
}

int main()
{
	time_t t;
	srand(time(&t));
	int* a,* pageNo;
	int pageSize, pageNum, realSize, option;
	a = new int [PROJECT_SIZE];
	pageNo = new int[PROJECT_SIZE];
	for(int i = 0; i < PROJECT_SIZE/4; i++)
	{
		a[4 * i] = rand() % VIRTUAL_MEMORY;
		a[4 * i + 3] = rand() % VIRTUAL_MEMORY;
	}
	for(int i = 0; i < PROJECT_SIZE/4; i++)
	{
		a[4 * i + 1] = a[4 * i] + 1;
		a[4 * i + 2] = a[4 * i] + 2;
		cout << i << ": " << a[4 * i] << " " << a[4 * i + 1] 
 << " " << a[4 * i + 2] << " " << a[4 * i + 3] << endl;
	}
	cout << "pageSize:(K) " << flush;
	cin >> pageSize;
	cout << "realSize:(页) " << flush;
	cin >> realSize;
	pageNum = 32 / pageSize;
	for(int i = 0; i < PROJECT_SIZE; i++)
		pageNo[i] = a[i] % pageNum;
	for(int i = 0; i < PROJECT_SIZE/4; i++)
		cout << i << ": " << pageNo[4 * i] << " " << pageNo[4 * i + 1] 
<< " " << pageNo[4 * i + 2] << " " << pageNo[4 * i + 3] << endl;
	cout << "opt/lru(0/1)?" << flush;
	cin >> option;
	switch(option)
	{
	case 0:  //opt
		opt(pageNo, realSize);
		break;
	case 1:  //lru
		lru(pageNo, realSize);
		break;
	default:
		cout << "input wrong!" << endl;
		break;
	}
	delete [] a;
	delete [] pageNo;
	jiedizhiguanli();

	return 0;
}