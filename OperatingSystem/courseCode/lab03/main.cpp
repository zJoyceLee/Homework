//ʵ����.cpp

#include <iostream>
#include <time.h>
#include <stdlib.h>
using namespace std;

#define PROJECT_SIZE 256 //Ѱַ��С
#define VIRTUAL_MEMORY 32768 //����С
#define MM_SIZE 100;//�ڴ�ռ�Ĭ�ϴ�0-99
//������СҲ���MM_SIZE��С

//�ٶ����չ����е�˳��ִ�У���0-255

typedef struct Real
{
	bool flag; //true��ʾ��ռ�ã���֮��ʾδ��ռ��
	int page; //����е�ҳ��
}real;

typedef struct REAL
{
	int page;
	int order;
}REAL;

typedef struct jiedizhi
{
	int head;//�հ׿ɷ���ռ��׵�ַ
	int size;//�հ׿ɷ���ռ��С
	bool flag;//�����־��true��ʾ�ѷ��䣬false��ʾδ����
}jiedizhi;

void lru(int pageNo[], int realSize)
{
	int shixiaocishu = 0;
	int weimanbiaozhi;
	double mingzhonglv;
	REAL* r = new REAL [realSize];
	for(int i = 0; i < realSize; i++)//��ʼ��
		r[i].order = 0;
	for(int i = 0; i < PROJECT_SIZE; i++)
	{
		weimanbiaozhi = 0;
		for(int j = 0; j < realSize; j++)
		{
			if(r[j].page == pageNo[i])//���и�ҳ������r[i].order
			{
				weimanbiaozhi = 1;
				for(int k = 0; k < realSize; k++)
					if(r[k].order != 0)
						r[k].order++;
				r[j].order = 1;
				r[j].page = pageNo[i];
				break;
			}
			if(r[j].order == 0)//δ��
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
		if(weimanbiaozhi == 0)//�������뱻���
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
	cout << "ʧЧ������" << shixiaocishu << endl;
	mingzhonglv = 1 - shixiaocishu * 1.0 / PROJECT_SIZE;
	cout << "�����ʣ�" << mingzhonglv << endl;
}
void opt(int pageNo[], int realSize)
{
	int Flag;//��ʶʵ���Ƿ�װ��
	int ff;//��ʶ�Ƿ�ɾ����ҳ
	int taotai;//�����̭
	int zuiwanshiyongtemp;
	int zuiwanshiyongnum;
	int shixiaocishu = 0;
	double mingzhonglv;
	real* r = new real [realSize];
	for(int i = 0; i < realSize; i++)//��ʼ��ʵ�����ݣ�ȫ��δ��ռ��
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
			if(r[j].flag == false)//δװ��
			{
				Flag = j;
				break;
			}
		}
		switch(Flag)
		{
		case 999999://ҳ������װ�д�ҳ
			break;
		case -1://װ����
			shixiaocishu++;
			for(int j = 0; j < realSize; j++)
			{
				taotai = 0;
				for(ff = i + 1; ff < PROJECT_SIZE; ff++)
				{
					if(pageNo[ff] == r[j].page)//����������ʸ�ҳ
					{
						taotai = 1;
						break;
					}
				}
				if(taotai == 0)
					//���������ٷ��ʸ�ҳ
				{
					r[j].flag = true;
					r[j].page = pageNo[i];
					taotai = 2;
					break;
				}
			}
			if(taotai != 2)//��̭����ʹ�õ�ҳ��
			{
				zuiwanshiyongtemp = 0;//����ʹ�����
				zuiwanshiyongnum = 0;//����ʹ��ʱ��
				for(int j = 0; j < realSize; j++)
				{
					for(ff = i + 1; ff < PROJECT_SIZE; ff++)
						if(pageNo[ff] == r[j].page)//������һ��ʹ��ʱ��
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
		default://δװ��
			shixiaocishu++;
			r[Flag].page = pageNo[i];
			r[Flag].flag = true;
		}
	}
	cout << "ʧЧ������" << shixiaocishu << endl;
	mingzhonglv = 1 - shixiaocishu * 1.0 / PROJECT_SIZE;
	cout << "�����ʣ�" << mingzhonglv << endl;
	return;
}

int chushihua(jiedizhi* d)//Ĭ�ϳ�ʼ��������������ȷ�������Ȳ��������ж�
{
	int num, head, size;
	cout << "δ������ռ�ĳ�ʼ����" << endl << "���ж�����" <<endl;
	cin >> num;
	cout << "��������δ������Ŀռ䣨head:0-99,size:0-99����" << endl;
	for(int i = 0; i < num; i++)
	{
		cin >> head;
		while((head > 99) | (head < 0))
		{
			cout << "����д0-99֮�������:" << flush;
			cin >> head;
		}
		cin >> size;
		while((size > 99) | (size <= 0))
		{
			cout << "����д0-99֮�������:" << flush;
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
	cout << "���״���Ӧ����" << endl << "����Ҫһ����Ҫ����Ŀռ������"<<flush;
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
//���ǰ��һ��հ״���ռ����ǰ��
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
			if(y == 0)//δ������
				cout << "̫��" << endl;
			//�ϲ��㷨
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
	cout << "�������Ӧ����" << endl << "����Ҫһ����Ҫ����Ŀռ������"<<flush;
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
//���ǰ��һ��հ״���ռ����ǰ��
					{
						d[k].flag = d[k + 1].flag;
						d[k].head = d[k + 1].head;
						d[k].size = d[k + 1].size;
					}
					d[num-1].flag = 1;
					num--;
				}
				paixu(d,num);//��������
				break;
			}
			if(y == 0)//δ������
				cout << "̫��" << endl;
			//�ϲ��㷨
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
	cout << "realSize:(ҳ) " << flush;
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