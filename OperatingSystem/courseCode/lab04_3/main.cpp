//ʵ��4.3
#include <iostream>
#include <string>
using namespace std;

typedef struct user
{
	int jibie;//����Ӹߵ��� ��0��ʼ
	string mingcheng;
	int duquanxian;//��Ȩ�ޣ���Ȩ��Ĭ�Ϻͼ�����ͬ
	int xiequanxian;//дȨ�ޣ���Ȩ��Ĭ�Ϻͼ�����ͬ
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
		cout << "�����ڵļ���Ϊ" << jibie << "��" << endl;
		cout << "����Ҫ�����" << x.mingcheng << "����Ȩ�ļ���Ϊ" << flush;
		cin >> tequan;
		if(tequan < jibie)//�����ܴ��ڷ����ߵļ���
			cout << "��Ϊ�Է�����ļ�����ߡ�" << endl;
		else
			x.duquanxian = tequan;
		cout << x.mingcheng << "���ڵĶ�����Ϊ" << x.duquanxian
			 << endl << x.mingcheng << "���ڵ�д����Ϊ" << x.xiequanxian << endl;
	}
}user;

int main()
{
	string shui;
	user joyce(2, "joyce");//ϵͳĬ�ϼ��𣬳������ô��û��޸ı��˵�Ȩ��
	user a(0, "a");user chipmunk(1, "chipmunk");user c(2, "c");user human(2, "human");user dave(3, "dave");
	cout << "��������" << joyce.mingcheng << endl
		 << "�����޸�Ȩ��(С�ڸ�ֵ)Ϊ" << joyce.jibie << endl
		 << "��Ҫ�����˭Ȩ�ޣ�" << flush;
	cin >> shui;
	if((shui == "a")||(shui == "chipmunk")||(shui == "c")||(shui == "human"))
		cout << "�Է����������ͬ����ߣ�" << endl;
	else if(shui == "dave")
		joyce.tequan(dave);
	else
		cout << "û�и��û���" << endl;
	return 0;
}
