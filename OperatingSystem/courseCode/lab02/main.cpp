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
	case '0'://ʹ�á���ֹ�������㷨
		p.safe();
		break;
	case '1'://��ʹ�á���ֹ�������㷨
p.matrix();
		break;
	}
	return 0;
}