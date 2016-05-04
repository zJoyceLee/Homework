//main.cpp
#include <iostream>
#include "PCB.h"
using namespace std;

int main()
{
	PCBTABLE <int> p;
	char option;
	cout << "option:" << flush;
	cin >> option;
	switch(option)
	{
	case '0'://使用“防止死锁”算法
		p.safe();
		break;
	case '1'://不使用“防止死锁”算法
p.matrix();
		break;
	}
	return 0;
}