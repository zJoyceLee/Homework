//实验4.2

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
	bool isFile;//是否为文件或目录，可添加其他属性，如链接等
	int cengshu;//方便之后对于同级可以互相访问的操作，第三题
	string department;//文件名称或者目录名称
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
	//树的执行方法
	//if(Parent->first == NULL)//没有第一个孩子
	//	Parent->first = this;
	//else //找到第一个最右边的孩子
	//{
	//	p = Parent->first;
	//	while(p->bro)
	//		p = p->bro;
	//	p->bro = this;
	//}
	cout << "请输入本文件或者目录的名称:" << flush;
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
	cout << "按照先序构造文件、目录树：" << endl;
	preorder(root, root->first);
	current = root;//current的初始值置为root
	levelordertree();
}
template <class T>
void tree <T>::preorder(treenode <T>*& root, treenode <T>*& self)
{
	string temp;
	cout << "是否为空：（0为空,其余默认非空）" << flush;
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
		cout << "显示文件和目录的从属关系：" << endl;
		treeprint(root);
	}
	else
		cout << "空树！" << endl;
}
template <class T>
void tree <T>::levelorder()
{
	cout << "层序输出此树：" << endl;
	int cengshu;
	if(!root)//已有此树
	{
		cout << "空树" << endl;
 		return;
	}
	queue <treenode <T>* > q;
	q.push(root);
	cengshu = root->cengshu;
	while(!q.empty())
	{
		if((q.front())->cengshu>cengshu)
		{
			cout << endl;//层数+1，换行机制
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
	cout << "层序输出此树：" << endl;
	int cengshu;
	if(!root)//已有此树
	{
		cout << "空树" << endl;
 		return;
	}
	queue <treenode <T>* > q;
	q.push(root);
	cengshu = root->cengshu;
	while(!q.empty())
	{
		if((q.front())->cengshu>cengshu)
		{
			cout << endl;//层数+1，换行机制
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
	cout << "进入信息查找模块：" << endl;
	string find;
	cout << "查找目录或者文件的名称:" << flush;
//假设此处所有的文件或者目录不重名。
	cin >> find;
	preordersearch(root, find, flag);
	if(flag == 0)
	{
		cout << "没有该元素!" << endl;
		return;
	}
	cout << "元素：" << current->department << endl;
	if(current->parent)
		cout << "从属：" << current->parent->department << flush;
	else
		cout << "已为根目录。" << flush;
	cout << endl << "包含文件或目录:" << endl;
	if(current->first == NULL)//没有第一个孩子
		cout << "空。" << endl;
	else //找到第一个最右边的孩子
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
		cout << "该项为文件。" << endl;
	else
		cout << "该项为目录。" << endl;
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
//树图
//                                    root
//  zhou       fen        a         b          c         d
//         zhou1 zhou2         fen1 fen2 fen3          e   f

//二叉树图
//           root
//      zhou
//           fen
//    zhou1            a
//       zhou2              b
//                  fen1           c
//                     fen2             d
//                         fen3      e
//                                      f

//输入
//1 zhou 0 1 fen 1 zhou1 0 1 zhou2 0 0 1 a 0 1 b 1 fen1 0
//1 fen2 0 1 fen3 0 0 1 c 0 1 d 1 e 0 1 f 0 0 0

//levelordertree()
//层数 问题 & isFile 问题
