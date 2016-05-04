//实验4.1
//main.cpp

#include <iostream>
#include <string>
#include <stdlib.h>
using namespace std;

#define USER_NUM 2;

typedef struct yonghu
{
	string yonghuming;//用户名
	//权限拓展
}yonghu;
typedef struct ufd
{
	string wenjianming;//文件名
	bool baohuma[3];//保护码：允许写、读、执行
	int changdu;//文件长度
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
		cout << "请输入文件名：" << flush;
		cin >> wenjianming;
		cout << "请输入保护码（读、写、执行）：" << flush;
		cin >> baohuma[0] >> baohuma[1] >> baohuma[2];
		cout << "请输入文件长度：" << flush;
		cin >> changdu;
		isnull = 0;
		duzhizhen = 0;
		xiezhizhen = changdu;
	}
}ufd;
typedef struct mfd
{
	yonghu ming;//用户名
	ufd* zhizhen;//文件目录首地址指针
}mfd;

void chushihuayonghulist(mfd* m)//暂定一共有两个基本用户
{
	m[0].ming.yonghuming = "zhou";//第一个用户为zhou
	m[0].zhizhen = new ufd[10];
	//cout << m[0].ming.yonghuming << " " << m[0].zhizhen[0].baohuma[0]
	//	  << m[0].zhizhen[0].baohuma[1] << m[0].zhizhen[0].baohuma[2]
	//	  << " " << m[0].zhizhen[0].duzhizhen
    //     << m[0].zhizhen[0].xiezhizhen << endl;
	m[1].ming.yonghuming = "fen";//第二个用户为fen
	m[1].zhizhen = new ufd[10];
}
void print(mfd* m, int whichuser, int i)
{
	cout.width(14);
	cout.fill(' ');
	cout.setf(ios::left);
	cout << m[whichuser].zhizhen[i].wenjianming;//文件名
	cout << m[whichuser].zhizhen[i].baohuma[0]
 		 << m[whichuser].zhizhen[i].baohuma[1]
		 << m[whichuser].zhizhen[i].baohuma[2]//保护码
		 << "         " << flush;
	cout.width(12);
	cout.fill(' ');
	cout << m[whichuser].zhizhen[i].changdu//文件长度
		 << m[whichuser].zhizhen[i].duzhizhen
		 << " "
		 << m[whichuser].zhizhen[i].xiezhizhen//读写指针
		 << endl;
}
void create(mfd* m, int whichuser)
{
	int flag = -1;
	int temp;
	cout << "进入文件建立处理程序：" << endl;
	for(int i = 0; i < 10; i++)
		if(m[whichuser].zhizhen[i].isnull)
		{
			flag = i;
			break;
		}
	if(flag != -1)
	{
		cout << "第" << flag <<"个文件位置为空，正在创建新文件..." << endl;
		cout << "文件名：" << flush;
		cin >> m[whichuser].zhizhen[flag].wenjianming;
		cout << "保护码：" << flush;
		for(int i = 0; i < 3; i++)
		{
			cin >> temp;
			if(temp == 0)
				m[whichuser].zhizhen[flag].baohuma[i] = false;
			else if(temp == 1)
				m[whichuser].zhizhen[flag].baohuma[i] = true;
			else
			{
				cout << "信息输入错误！【0/1】" << flush;
				i--;
			}
		}
		cout << "文件长度：" << flush;
		cin >> m[whichuser].zhizhen[flag].changdu;
		m[whichuser].zhizhen[flag].xiezhizhen =
m[whichuser].zhizhen[flag].changdu;
		m[whichuser].zhizhen[flag].isnull = 0;
		cout << "新文件创建完毕!" << endl
			 << "现文件系统详细表单如下所示：" << endl;
	}
	else
	{
		cout << "对不起，存储空间已满，不能再进行新建！" << endl;
		cout << "为您转入主菜单..." << endl;
		system("pause");
		system("cls");
		return;
	}
	cout << "用户名"
	     << m[whichuser].ming.yonghuming << "所包含的文件目录：" << endl;
	cout << "文件名      保护码      文件长度    读写指针" << endl;
	for(int i = 0; i < 10; i++)
	{
		if(m[whichuser].zhizhen[i].isnull)
			continue;
		print(m, whichuser, i);
	}
	cout << "退出文件建立处理程序!" << endl;
	cout << "为您转入主菜单..." << endl;
	system("pause");
	system("cls");
}
void deletefile(mfd* m, int whichuser)
{
	int flag = -1;
	cout << "进入文件删除处理程序：" << endl;
	cout << "用户名"
	     << m[whichuser].ming.yonghuming << "所包含的文件目录：" << endl;
	cout << "文件名      保护码      文件长度    读写指针" << endl;
	for(int i = 0; i < 10; i++)
	{
		if(m[whichuser].zhizhen[i].isnull)
			continue;
		print(m, whichuser, i);
	}
	cout << "所要删除文件序号：" << flush;
	cin >> flag;
	if(flag >= 0 && flag < 10)
	{
		if(m[whichuser].zhizhen[flag].baohuma[1] == false)
		{
			cout << "您目前没有删除权限！" << endl;
			cout << "为您转入主菜单..." << endl;
			system("pause");
			system("cls");
			return;
		}
		else
		{
			m[whichuser].zhizhen[flag].isnull = true;
			cout << "删除成功！" << endl;
		}
	}
	else
	{
		cout << "删除信息输入错误！" << endl
			 << "为您转入主菜单..." << endl;
		system("pause");
		system("cls");
		return;
	}
	cout << "现文件系统详细表单如下所示：" << endl;
	cout << "用户名"
	 	 << m[whichuser].ming.yonghuming << "所包含的文件目录：" << endl;
	cout << "文件名      保护码      文件长度    读写指针" << endl;
	for(int i = 0; i < 10; i++)
	{
		if(m[whichuser].zhizhen[i].isnull)
			continue;
		print(m, whichuser, i);
	}
	cout << "退出文件删除处理程序!" << endl;
	cout << "为您转入主菜单..." << endl;
	system("pause");
	system("cls");
	return;
}
void readfile(mfd* m, int whichuser)
{
	int flag = -1;
	cout << "进入文件读取处理程序：" << endl;
	cout << "用户名"
	     << m[whichuser].ming.yonghuming << "所包含的文件目录：" << endl;
	cout << "文件名      保护码      文件长度    读写指针" << endl;
	for(int i = 0; i < 10; i++)
	{
		if(m[whichuser].zhizhen[i].isnull)
			continue;
		print(m, whichuser, i);
	}
	cout << "所要读取文件序号：" << flush;
	cin >> flag;
	if(flag >= 0 && flag < 10)
	{
		if(m[whichuser].zhizhen[flag].isnull
||(m[whichuser].zhizhen[flag].baohuma[0] == false))
		{
			cout << "您目前没有读取权限或不在文件范围！" << endl;
			cout << "为您转入主菜单..." << endl;
			system("pause");
			system("cls");
			return;
		}
		else
		{
			cout << "我在读..." << endl;
			m[whichuser].zhizhen[flag].duzhizhen =
m[whichuser].zhizhen[flag].changdu;
//置读指针到文件最后
		}
	}
	else
	{
		cout << "读取信息输入错误！" << endl
			 << "为您转入主菜单..." << endl;
		system("pause");
		system("cls");
		return;
	}
	cout << "现文件系统详细表单如下所示：" << endl;
	cout << "用户名"
	 	 << m[whichuser].ming.yonghuming << "所包含的文件目录：" << endl;
	cout << "文件名      保护码      文件长度    读写指针" << endl;
	for(int i = 0; i < 10; i++)
	{
		if(m[whichuser].zhizhen[i].isnull)
			continue;
		print(m, whichuser, i);
	}
	cout << "退出文件读取处理程序!" << endl;
	cout << "为您转入主菜单..." << endl;
	system("pause");
	system("cls");
}
void writefile(mfd* m, int whichuser)
{
	int flag = -1;
	cout << "进入文件写入处理程序：" << endl;
	cout << "用户名"
	     << m[whichuser].ming.yonghuming << "所包含的文件目录：" << endl;
	cout << "文件名      保护码      文件长度    读写指针" << endl;
	for(int i = 0; i < 10; i++)
	{
		if(m[whichuser].zhizhen[i].isnull)
			continue;
		print(m, whichuser, i);
	}
	cout << "所要写入文件序号：" << flush;
	cin >> flag;
	if(flag >= 0 && flag < 10)
	{
		if(m[whichuser].zhizhen[flag].isnull
||(m[whichuser].zhizhen[flag].baohuma[1] == false))
		{
			cout << "您目前没有写入权限或不在文件范围！" << endl;
			cout << "为您转入主菜单..." << endl;
			system("pause");
			system("cls");
			return;
		}
		else
		{
			cout << "我在写..." << endl;
			int chang;
			cout << "写入长度:" << flush;
			cin >> chang;
			m[whichuser].zhizhen[flag].changdu += chang;
			m[whichuser].zhizhen[flag].xiezhizhen += chang;
		}
	}
	else
	{
		cout << "写入信息输入错误！" << endl
			 << "为您转入主菜单..." << endl;
		system("pause");
		system("cls");
		return;
	}
	cout << "现文件系统详细表单如下所示：" << endl;
	cout << "用户名"
	 	 << m[whichuser].ming.yonghuming << "所包含的文件目录：" << endl;
	cout << "文件名      保护码      文件长度    读写指针" << endl;
	for(int i = 0; i < 10; i++)
	{
		if(m[whichuser].zhizhen[i].isnull)
			continue;
		print(m, whichuser, i);
	}
	cout << "退出文件写入处理程序!" << endl;
	cout << "为您转入主菜单..." << endl;
	system("pause");
	system("cls");
}
void modifyfile(mfd* m, int whichuser)
{
	int flag = -1;
	cout << "进入文件权限修改程序：" << endl;
	cout << "用户名"
	     << m[whichuser].ming.yonghuming << "所包含的文件目录：" << endl;
	cout << "文件名      保护码      文件长度    读写指针" << endl;
	for(int i = 0; i < 10; i++)
	{
		if(m[whichuser].zhizhen[i].isnull)
			continue;
		print(m, whichuser, i);
	}
	cout << "所要修改权限的文件序号：" << flush;
	cin >> flag;
	if(flag >= 0 && flag < 10)
	{
		if(m[whichuser].zhizhen[flag].isnull)
		{
			cout << "不在文件范围！" << endl;
			cout << "为您转入主菜单..." << endl;
			system("pause");
			system("cls");
			return;
		}
		else
		{
			cout << "我在修改..." << endl;
			int xiugai;
			cout << "读权限:" << flush;
			cin >> xiugai;
			while(xiugai != 0 && xiugai != 1)
				cout << "输入错误，请重新输入：" << flush;
			if(xiugai == 0)
				m[whichuser].zhizhen[flag].baohuma[0] = false;
			if(xiugai == 1)
				m[whichuser].zhizhen[flag].baohuma[0] = true;
			cout << "写权限:" << flush;
			cin >> xiugai;
			while(xiugai != 0 && xiugai != 1)
				cout << "输入错误，请重新输入：" << flush;
			if(xiugai == 0)
				m[whichuser].zhizhen[flag].baohuma[1] = false;
			if(xiugai == 1)
				m[whichuser].zhizhen[flag].baohuma[1] = true;
			cout << "执行权限:" << flush;
			cin >> xiugai;
			while(xiugai != 0 && xiugai != 1)
				cout << "输入错误，请重新输入：" << flush;
			if(xiugai == 0)
				m[whichuser].zhizhen[flag].baohuma[2] = false;
			if(xiugai == 1)
				m[whichuser].zhizhen[flag].baohuma[2] = true;
		}
	}
	else
	{
		cout << "修改权限信息输入错误！" << endl
			 << "为您转入主菜单..." << endl;
		system("pause");
		system("cls");
		return;
	}
	cout << "现文件系统详细表单如下所示：" << endl;
	cout << "用户名"
	 	 << m[whichuser].ming.yonghuming << "所包含的文件目录：" << endl;
	cout << "文件名      保护码      文件长度    读写指针" << endl;
	for(int i = 0; i < 10; i++)
	{
		if(m[whichuser].zhizhen[i].isnull)
			continue;
		print(m, whichuser, i);
	}
	cout << "退出权限修改处理程序!" << endl;
	cout << "为您转入主菜单..." << endl;
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
		cout << "请输入你的用户名：(英文字符“!!”表明取消尝试并退出)" << flush;
		cin >> user.yonghuming;
		if(user.yonghuming == "!!")
			return 0;
		for(int i  = 0; i < usernum; i++)
			if(user.yonghuming == m[i].ming.yonghuming)
			{
				whichuser = i;
				cout << "成功进入系统！" << endl;
				break;
			}
		if(whichuser != -1)
			break;
		else
			cout << "信息错误！" << endl << "try again!" << endl;
	}
	while(true)
	{
		cout << "请输入你要执行的操作：" << endl
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
			cout << "即将退出文件管理系统！" << endl;
			return 0;
		case 2:
			deletefile(m, whichuser);
			break;
		case 3://这里把打开和关闭直接放入读写操作中
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
