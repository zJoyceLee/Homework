//ʵ��4.1
//main.cpp

#include <iostream>
#include <string>
#include <stdlib.h>
using namespace std;

#define USER_NUM 2;

typedef struct yonghu
{
	string yonghuming;//�û���
	//Ȩ����չ
}yonghu;
typedef struct ufd
{
	string wenjianming;//�ļ���
	bool baohuma[3];//�����룺����д������ִ��
	int changdu;//�ļ�����
	int duzhizhen;
	int xiezhizhen;
	int isnull;
	ufd()
	{
		duzhizhen = xiezhizhen = changdu = 0;
		isnull = 1;
		baohuma[0] = baohuma[1] = baohuma[2] = false;
		wenjianming = "*******";
	};
	void create()
	{
		cout << "�������ļ�����" << flush;
		cin >> wenjianming;
		cout << "�����뱣���루����д��ִ�У���" << flush;
		cin >> baohuma[0] >> baohuma[1] >> baohuma[2];
		cout << "�������ļ����ȣ�" << flush;
		cin >> changdu;
		isnull = 0;
		duzhizhen = 0;
		xiezhizhen = changdu;
	}
}ufd;
typedef struct mfd
{
	yonghu ming;//�û���
	ufd* zhizhen;//�ļ�Ŀ¼�׵�ַָ��
}mfd;

void chushihuayonghulist(mfd* m)//�ݶ�һ�������������û�
{
	m[0].ming.yonghuming = "zhou";//��һ���û�Ϊzhou
	m[0].zhizhen = new ufd[10];
	//cout << m[0].ming.yonghuming << " " << m[0].zhizhen[0].baohuma[0]
	//	  << m[0].zhizhen[0].baohuma[1] << m[0].zhizhen[0].baohuma[2]
	//	  << " " << m[0].zhizhen[0].duzhizhen
    //     << m[0].zhizhen[0].xiezhizhen << endl;
	m[1].ming.yonghuming = "fen";//�ڶ����û�Ϊfen
	m[1].zhizhen = new ufd[10];
}
void print(mfd* m, int whichuser, int i)
{
	cout.width(14);
	cout.fill(' ');
	cout.setf(ios::left);
	cout << m[whichuser].zhizhen[i].wenjianming;//�ļ���
	cout << m[whichuser].zhizhen[i].baohuma[0]
 		 << m[whichuser].zhizhen[i].baohuma[1]
		 << m[whichuser].zhizhen[i].baohuma[2]//������
		 << "         " << flush;
	cout.width(12);
	cout.fill(' ');
	cout << m[whichuser].zhizhen[i].changdu//�ļ�����
		 << m[whichuser].zhizhen[i].duzhizhen
		 << " "
		 << m[whichuser].zhizhen[i].xiezhizhen//��дָ��
		 << endl;
}
void create(mfd* m, int whichuser)
{
	int flag = -1;
	int temp;
	cout << "�����ļ������������" << endl;
	for(int i = 0; i < 10; i++)
		if(m[whichuser].zhizhen[i].isnull)
		{
			flag = i;
			break;
		}
	if(flag != -1)
	{
		cout << "��" << flag <<"���ļ�λ��Ϊ�գ����ڴ������ļ�..." << endl;
		cout << "�ļ�����" << flush;
		cin >> m[whichuser].zhizhen[flag].wenjianming;
		cout << "�����룺" << flush;
		for(int i = 0; i < 3; i++)
		{
			cin >> temp;
			if(temp == 0)
				m[whichuser].zhizhen[flag].baohuma[i] = false;
			else if(temp == 1)
				m[whichuser].zhizhen[flag].baohuma[i] = true;
			else
			{
				cout << "��Ϣ������󣡡�0/1��" << flush;
				i--;
			}
		}
		cout << "�ļ����ȣ�" << flush;
		cin >> m[whichuser].zhizhen[flag].changdu;
		m[whichuser].zhizhen[flag].xiezhizhen =
m[whichuser].zhizhen[flag].changdu;
		m[whichuser].zhizhen[flag].isnull = 0;
		cout << "���ļ��������!" << endl
			 << "���ļ�ϵͳ��ϸ��������ʾ��" << endl;
	}
	else
	{
		cout << "�Բ��𣬴洢�ռ������������ٽ����½���" << endl;
		cout << "Ϊ��ת�����˵�..." << endl;
		system("pause");
		system("cls");
		return;
	}
	cout << "�û���"
	     << m[whichuser].ming.yonghuming << "���������ļ�Ŀ¼��" << endl;
	cout << "�ļ���      ������      �ļ�����    ��дָ��" << endl;
	for(int i = 0; i < 10; i++)
	{
		if(m[whichuser].zhizhen[i].isnull)
			continue;
		print(m, whichuser, i);
	}
	cout << "�˳��ļ������������!" << endl;
	cout << "Ϊ��ת�����˵�..." << endl;
	system("pause");
	system("cls");
}
void deletefile(mfd* m, int whichuser)
{
	int flag = -1;
	cout << "�����ļ�ɾ���������" << endl;
	cout << "�û���"
	     << m[whichuser].ming.yonghuming << "���������ļ�Ŀ¼��" << endl;
	cout << "�ļ���      ������      �ļ�����    ��дָ��" << endl;
	for(int i = 0; i < 10; i++)
	{
		if(m[whichuser].zhizhen[i].isnull)
			continue;
		print(m, whichuser, i);
	}
	cout << "��Ҫɾ���ļ���ţ�" << flush;
	cin >> flag;
	if(flag >= 0 && flag < 10)
	{
		if(m[whichuser].zhizhen[flag].baohuma[1] == false)
		{
			cout << "��Ŀǰû��ɾ��Ȩ�ޣ�" << endl;
			cout << "Ϊ��ת�����˵�..." << endl;
			system("pause");
			system("cls");
			return;
		}
		else
		{
			m[whichuser].zhizhen[flag].isnull = true;
			cout << "ɾ���ɹ���" << endl;
		}
	}
	else
	{
		cout << "ɾ����Ϣ�������" << endl
			 << "Ϊ��ת�����˵�..." << endl;
		system("pause");
		system("cls");
		return;
	}
	cout << "���ļ�ϵͳ��ϸ��������ʾ��" << endl;
	cout << "�û���"
	 	 << m[whichuser].ming.yonghuming << "���������ļ�Ŀ¼��" << endl;
	cout << "�ļ���      ������      �ļ�����    ��дָ��" << endl;
	for(int i = 0; i < 10; i++)
	{
		if(m[whichuser].zhizhen[i].isnull)
			continue;
		print(m, whichuser, i);
	}
	cout << "�˳��ļ�ɾ���������!" << endl;
	cout << "Ϊ��ת�����˵�..." << endl;
	system("pause");
	system("cls");
	return;
}
void readfile(mfd* m, int whichuser)
{
	int flag = -1;
	cout << "�����ļ���ȡ�������" << endl;
	cout << "�û���"
	     << m[whichuser].ming.yonghuming << "���������ļ�Ŀ¼��" << endl;
	cout << "�ļ���      ������      �ļ�����    ��дָ��" << endl;
	for(int i = 0; i < 10; i++)
	{
		if(m[whichuser].zhizhen[i].isnull)
			continue;
		print(m, whichuser, i);
	}
	cout << "��Ҫ��ȡ�ļ���ţ�" << flush;
	cin >> flag;
	if(flag >= 0 && flag < 10)
	{
		if(m[whichuser].zhizhen[flag].isnull
||(m[whichuser].zhizhen[flag].baohuma[0] == false))
		{
			cout << "��Ŀǰû�ж�ȡȨ�޻����ļ���Χ��" << endl;
			cout << "Ϊ��ת�����˵�..." << endl;
			system("pause");
			system("cls");
			return;
		}
		else
		{
			cout << "���ڶ�..." << endl;
			m[whichuser].zhizhen[flag].duzhizhen =
m[whichuser].zhizhen[flag].changdu;
//�ö�ָ�뵽�ļ����
		}
	}
	else
	{
		cout << "��ȡ��Ϣ�������" << endl
			 << "Ϊ��ת�����˵�..." << endl;
		system("pause");
		system("cls");
		return;
	}
	cout << "���ļ�ϵͳ��ϸ��������ʾ��" << endl;
	cout << "�û���"
	 	 << m[whichuser].ming.yonghuming << "���������ļ�Ŀ¼��" << endl;
	cout << "�ļ���      ������      �ļ�����    ��дָ��" << endl;
	for(int i = 0; i < 10; i++)
	{
		if(m[whichuser].zhizhen[i].isnull)
			continue;
		print(m, whichuser, i);
	}
	cout << "�˳��ļ���ȡ�������!" << endl;
	cout << "Ϊ��ת�����˵�..." << endl;
	system("pause");
	system("cls");
}
void writefile(mfd* m, int whichuser)
{
	int flag = -1;
	cout << "�����ļ�д�봦�����" << endl;
	cout << "�û���"
	     << m[whichuser].ming.yonghuming << "���������ļ�Ŀ¼��" << endl;
	cout << "�ļ���      ������      �ļ�����    ��дָ��" << endl;
	for(int i = 0; i < 10; i++)
	{
		if(m[whichuser].zhizhen[i].isnull)
			continue;
		print(m, whichuser, i);
	}
	cout << "��Ҫд���ļ���ţ�" << flush;
	cin >> flag;
	if(flag >= 0 && flag < 10)
	{
		if(m[whichuser].zhizhen[flag].isnull
||(m[whichuser].zhizhen[flag].baohuma[1] == false))
		{
			cout << "��Ŀǰû��д��Ȩ�޻����ļ���Χ��" << endl;
			cout << "Ϊ��ת�����˵�..." << endl;
			system("pause");
			system("cls");
			return;
		}
		else
		{
			cout << "����д..." << endl;
			int chang;
			cout << "д�볤��:" << flush;
			cin >> chang;
			m[whichuser].zhizhen[flag].changdu += chang;
			m[whichuser].zhizhen[flag].xiezhizhen += chang;
		}
	}
	else
	{
		cout << "д����Ϣ�������" << endl
			 << "Ϊ��ת�����˵�..." << endl;
		system("pause");
		system("cls");
		return;
	}
	cout << "���ļ�ϵͳ��ϸ��������ʾ��" << endl;
	cout << "�û���"
	 	 << m[whichuser].ming.yonghuming << "���������ļ�Ŀ¼��" << endl;
	cout << "�ļ���      ������      �ļ�����    ��дָ��" << endl;
	for(int i = 0; i < 10; i++)
	{
		if(m[whichuser].zhizhen[i].isnull)
			continue;
		print(m, whichuser, i);
	}
	cout << "�˳��ļ�д�봦�����!" << endl;
	cout << "Ϊ��ת�����˵�..." << endl;
	system("pause");
	system("cls");
}
void modifyfile(mfd* m, int whichuser)
{
	int flag = -1;
	cout << "�����ļ�Ȩ���޸ĳ���" << endl;
	cout << "�û���"
	     << m[whichuser].ming.yonghuming << "���������ļ�Ŀ¼��" << endl;
	cout << "�ļ���      ������      �ļ�����    ��дָ��" << endl;
	for(int i = 0; i < 10; i++)
	{
		if(m[whichuser].zhizhen[i].isnull)
			continue;
		print(m, whichuser, i);
	}
	cout << "��Ҫ�޸�Ȩ�޵��ļ���ţ�" << flush;
	cin >> flag;
	if(flag >= 0 && flag < 10)
	{
		if(m[whichuser].zhizhen[flag].isnull)
		{
			cout << "�����ļ���Χ��" << endl;
			cout << "Ϊ��ת�����˵�..." << endl;
			system("pause");
			system("cls");
			return;
		}
		else
		{
			cout << "�����޸�..." << endl;
			int xiugai;
			cout << "��Ȩ��:" << flush;
			cin >> xiugai;
			while(xiugai != 0 && xiugai != 1)
				cout << "����������������룺" << flush;
			if(xiugai == 0)
				m[whichuser].zhizhen[flag].baohuma[0] = false;
			if(xiugai == 1)
				m[whichuser].zhizhen[flag].baohuma[0] = true;
			cout << "дȨ��:" << flush;
			cin >> xiugai;
			while(xiugai != 0 && xiugai != 1)
				cout << "����������������룺" << flush;
			if(xiugai == 0)
				m[whichuser].zhizhen[flag].baohuma[1] = false;
			if(xiugai == 1)
				m[whichuser].zhizhen[flag].baohuma[1] = true;
			cout << "ִ��Ȩ��:" << flush;
			cin >> xiugai;
			while(xiugai != 0 && xiugai != 1)
				cout << "����������������룺" << flush;
			if(xiugai == 0)
				m[whichuser].zhizhen[flag].baohuma[2] = false;
			if(xiugai == 1)
				m[whichuser].zhizhen[flag].baohuma[2] = true;
		}
	}
	else
	{
		cout << "�޸�Ȩ����Ϣ�������" << endl
			 << "Ϊ��ת�����˵�..." << endl;
		system("pause");
		system("cls");
		return;
	}
	cout << "���ļ�ϵͳ��ϸ��������ʾ��" << endl;
	cout << "�û���"
	 	 << m[whichuser].ming.yonghuming << "���������ļ�Ŀ¼��" << endl;
	cout << "�ļ���      ������      �ļ�����    ��дָ��" << endl;
	for(int i = 0; i < 10; i++)
	{
		if(m[whichuser].zhizhen[i].isnull)
			continue;
		print(m, whichuser, i);
	}
	cout << "�˳�Ȩ���޸Ĵ������!" << endl;
	cout << "Ϊ��ת�����˵�..." << endl;
	system("pause");
	system("cls");
}

int main()
{
	mfd* m;
	m = new mfd[10];
	yonghu user;
	chushihuayonghulist(m);
	int option;
	int whichuser = -1;
	int usernum = USER_NUM;
	while(true)
	{
		cout << "����������û�����(Ӣ���ַ���!!������ȡ�����Բ��˳�)" << flush;
		cin >> user.yonghuming;
		if(user.yonghuming == "!!")
			return 0;
		for(int i  = 0; i < usernum; i++)
			if(user.yonghuming == m[i].ming.yonghuming)
			{
				whichuser = i;
				cout << "�ɹ�����ϵͳ��" << endl;
				break;
			}
		if(whichuser != -1)
			break;
		else
			cout << "��Ϣ����" << endl << "try again!" << endl;
	}
	while(true)
	{
		cout << "��������Ҫִ�еĲ�����" << endl
			<< "1.create" << endl
			<< "2.delete" << endl
			<< "3.read" <<endl
			<< "4.write" << endl
			<< "5.modify" << endl
			<< "0.bye" << endl;
		cin >> option;
		switch(option)
		{
		case 1:
			create(m,whichuser);
			break;
		case 0:
			cout << "�����˳��ļ�����ϵͳ��" << endl;
			return 0;
		case 2:
			deletefile(m, whichuser);
			break;
		case 3://����Ѵ򿪺͹ر�ֱ�ӷ����д������
			readfile(m, whichuser);
			break;
		case 4:
			writefile(m, whichuser);
			break;
		case 5:
			modifyfile(m, whichuser);
			break;
		}
	}
	return 0;
}
