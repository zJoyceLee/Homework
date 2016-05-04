//ʵ��4.2

#include <iostream>
#include <stdlib.h>
#include <string>
#include <queue>
using namespace std;

template <class T> class tree;
template <class T>
class treenode
{
	friend class tree <T>;
private:
	treenode* parent;
	treenode* first;
	treenode* bro;
	bool isFile;//�Ƿ�Ϊ�ļ���Ŀ¼��������������ԣ������ӵ�
	int cengshu;//����֮�����ͬ�����Ի�����ʵĲ�����������
	string department;//�ļ����ƻ���Ŀ¼����
public:
	treenode (){parent = first = bro = NULL; isFile = true; cengshu = 0;
department = "root";}
	treenode (treenode <T>*& Parent);
};
template <class T>
treenode<T>::treenode (treenode <T>*& Parent)
{
	parent = Parent;
	cengshu = Parent->cengshu + 1;
	isFile = true;
	first = bro = NULL;
	//����ִ�з���
	//if(Parent->first == NULL)//û�е�һ������
	//	Parent->first = this;
	//else //�ҵ���һ�����ұߵĺ���
	//{
	//	p = Parent->first;
	//	while(p->bro)
	//		p = p->bro;
	//	p->bro = this;
	//}
	cout << "�����뱾�ļ�����Ŀ¼������:" << flush;
	cin >> department;
}

template<class T>
class tree
{
private:
	treenode <T>* root;
	treenode <T>* current;
public:
	tree();
	void search();
	void preorder(treenode <T>*& root,treenode <T>*& self);
	void treeprint(treenode <T>* root);
	void treeprint();
	void levelorder();
	void levelordertree();
	void preordersearch(treenode <T>* root,string find, int& flag);
};
template <class T>
tree <T>::tree()
{
	root = new treenode <T>;
	cout << "�����������ļ���Ŀ¼����" << endl;
	preorder(root, root->first);
	current = root;//current�ĳ�ʼֵ��Ϊroot
	levelordertree();
}
template <class T>
void tree <T>::preorder(treenode <T>*& root, treenode <T>*& self)
{
	string temp;
	cout << "�Ƿ�Ϊ�գ���0Ϊ��,����Ĭ�Ϸǿգ�" << flush;
	cin >> temp;
	if(temp == "0")
	{
		self = NULL;
		return;
	}
	root->isFile = false;
	self = new treenode <T>(root);
	preorder(self,self->first);
	preorder(root,self->bro);
}
template <class T>
void tree <T>::treeprint(treenode <T>* root)
{
	treenode <T>* child;
	for(child = root->first; child; child = child->bro)
	{
		cout << root->department << "-" << child->department << endl;
		treeprint(child);
	}
}
template <class T>
void tree <T>::treeprint()
{
	if(root)
	{
		system("pause");
		system("cls");
		cout << "��ʾ�ļ���Ŀ¼�Ĵ�����ϵ��" << endl;
		treeprint(root);
	}
	else
		cout << "������" << endl;
}
template <class T>
void tree <T>::levelorder()
{
	cout << "�������������" << endl;
	int cengshu;
	if(!root)//���д���
	{
		cout << "����" << endl;
 		return;
	}
	queue <treenode <T>* > q;
	q.push(root);
	cengshu = root->cengshu;
	while(!q.empty())
	{
		if((q.front())->cengshu>cengshu)
		{
			cout << endl;//����+1�����л���
			cengshu = (q.front())->cengshu;
		}
		cout << (q.front())->department << " " << flush;
		if((q.front())->first)
			q.push((q.front())->first);
		if((q.front())->bro)
			q.push((q.front())->bro);
		q.pop();
	}
	cout << endl;
}
template <class T>
void tree <T>::levelordertree()
{
	treenode <T>* p;
	cout << "�������������" << endl;
	int cengshu;
	if(!root)//���д���
	{
		cout << "����" << endl;
 		return;
	}
	queue <treenode <T>* > q;
	q.push(root);
	cengshu = root->cengshu;
	while(!q.empty())
	{
		if((q.front())->cengshu>cengshu)
		{
			cout << endl;//����+1�����л���
			cengshu = (q.front())->cengshu;
		}
		cout << (q.front())->department << " " << flush;
		if((q.front())->isFile)
			cout << " 1 " << flush;
		else
			cout << " 0 " << flush;
		if((q.front())->first)
		{
			q.push((q.front())->first);
			p = (q.front())->first;
			while(p->bro)
			{
				q.push(p->bro);
				p = p->bro;
			}
		}
		q.pop();
	}
	cout << endl;
}
template <class T>
void tree <T>::search()
{
	treenode <T>* p;
	int flag = 0;
	system("pause");
	system("cls");
	cout << "������Ϣ����ģ�飺" << endl;
	string find;
	cout << "����Ŀ¼�����ļ�������:" << flush;
//����˴����е��ļ�����Ŀ¼��������
	cin >> find;
	preordersearch(root, find, flag);
	if(flag == 0)
	{
		cout << "û�и�Ԫ��!" << endl;
		return;
	}
	cout << "Ԫ�أ�" << current->department << endl;
	if(current->parent)
		cout << "������" << current->parent->department << flush;
	else
		cout << "��Ϊ��Ŀ¼��" << flush;
	cout << endl << "�����ļ���Ŀ¼:" << endl;
	if(current->first == NULL)//û�е�һ������
		cout << "�ա�" << endl;
	else //�ҵ���һ�����ұߵĺ���
	{
		p = current->first;
		while(p->bro)
		{
			cout << p->department << " " << flush;
			p = p->bro;
		}
		cout << p->department << endl;
	}
	if(current->isFile)
		cout << "����Ϊ�ļ���" << endl;
	else
		cout << "����ΪĿ¼��" << endl;
}
template <class T>
void tree <T>::preordersearch(treenode <T>* root,string find, int& flag)
{
	if(root->department == find)
	{
		flag = 1;
		current = root;
		return;
	}
	if((flag == 0)&&root->first)
		preordersearch(root->first, find, flag);
	if((flag == 0)&&root->bro)
		preordersearch(root->bro, find, flag);
}

int main()
{
	tree <int> tre;
	tre.treeprint();
	tre.search();
	return 0;
}
//��ͼ
//                                    root
//  zhou       fen        a         b          c         d
//         zhou1 zhou2         fen1 fen2 fen3          e   f

//������ͼ
//           root
//      zhou
//           fen
//    zhou1            a
//       zhou2              b
//                  fen1           c
//                     fen2             d
//                         fen3      e
//                                      f

//����
//1 zhou 0 1 fen 1 zhou1 0 1 zhou2 0 0 1 a 0 1 b 1 fen1 0
//1 fen2 0 1 fen3 0 0 1 c 0 1 d 1 e 0 1 f 0 0 0

//levelordertree()
//���� ���� & isFile ����
