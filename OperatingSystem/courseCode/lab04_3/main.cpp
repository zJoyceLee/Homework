//实验4.3
#include <iostream>
#include <string>
using namespace std;

typedef struct user
{
	int jibie;//级别从高到低 从0开始
	string mingcheng;
	int duquanxian;//读权限，特权，默认和级别相同
	int xiequanxian;//写权限，特权，默认和级别相同
	user(int Jibie, string Mingcheng)
	{
		jibie = Jibie;
		duquanxian = jibie;
		xiequanxian = jibie;
		mingcheng = Mingcheng;
	}
	void tequan(user &x)
	{
		int tequan;
		cout << "您现在的级别为" << jibie << "级" << endl;
		cout << "您想要分配给" << x.mingcheng << "读特权的级别为" << flush;
		cin >> tequan;
		if(tequan < jibie)//级别不能大于分配者的级别
			cout << "您为对方分配的级别过高。" << endl;
		else
			x.duquanxian = tequan;
		cout << x.mingcheng << "现在的读级别为" << x.duquanxian
			 << endl << x.mingcheng << "现在的写级别为" << x.xiequanxian << endl;
	}
}user;

int main()
{
	string shui;
	user joyce(2, "joyce");//系统默认级别，程序中用此用户修改别人的权限
	user a(0, "a");user chipmunk(1, "chipmunk");user c(2, "c");user human(2, "human");user dave(3, "dave");
	cout << "您现在是" << joyce.mingcheng << endl
		 << "您的修改权限(小于该值)为" << joyce.jibie << endl
		 << "您要分配给谁权限？" << flush;
	cin >> shui;
	if((shui == "a")||(shui == "chipmunk")||(shui == "c")||(shui == "human"))
		cout << "对方级别和您相同或更高！" << endl;
	else if(shui == "dave")
		joyce.tequan(dave);
	else
		cout << "没有该用户！" << endl;
	return 0;
}
