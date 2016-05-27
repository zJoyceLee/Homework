#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <sstream>

#include "LR0_Analyser.h"
#include "Analyser.h"
#include "Glossary.h"

using namespace std;

vector<pair<string, string>> Escape(vector<pair<string, string>> lexResult);

int main()
{
	LR0_Analyser la;

	la.AddProduction("E", "E", "+", "E");
	la.AddProduction("E", "E", "*", "E");
	la.AddProduction("E", "(", "E", ")");
	la.AddProduction("E", "i");

	la.AddAction(0, "(", 'S', 2);
	la.AddAction(0, "i", 'S', 3);
	la.AddAction(1, "+", 'S', 4);
	la.AddAction(1, "*", 'S', 5);
	la.AddAction(1, LR0_Analyser::END_OF_INPUT, 'A', 0);
	la.AddAction(2, "(", 'S', 2);
	la.AddAction(2, "i", 'S', 3);
	la.AddAction(3, "+", 'r', 4);
	la.AddAction(3, "*", 'r', 4);
	la.AddAction(3, ")", 'r', 4);
	la.AddAction(3, LR0_Analyser::END_OF_INPUT, 'r', 4);
	la.AddAction(4, "(", 'S', 2);
	la.AddAction(4, "i", 'S', 3);
	la.AddAction(5, "(", 'S', 2);
	la.AddAction(5, "i", 'S', 3);
	la.AddAction(6, "+", 'S', 4);
	la.AddAction(6, "*", 'S', 5);
	la.AddAction(6, ")", 'S', 9);
	la.AddAction(7, "+", 'r', 1);
	la.AddAction(7, "*", 'S', 5);
	la.AddAction(7, ")", 'r', 1);
	la.AddAction(7, LR0_Analyser::END_OF_INPUT, 'r', 1);
	la.AddAction(8, "+", 'r', 2);
	la.AddAction(8, "*", 'r', 2);
	la.AddAction(8, ")", 'r', 2);
	la.AddAction(8, LR0_Analyser::END_OF_INPUT, 'r', 2);
	la.AddAction(9, "+", 'r', 3);
	la.AddAction(9, "*", 'r', 3);
	la.AddAction(9, ")", 'r', 3);
	la.AddAction(9, LR0_Analyser::END_OF_INPUT, 'r', 3);

	la.AddGoto(0, "E", 1);
	la.AddGoto(2, "E", 6);
	la.AddGoto(4, "E", 7);
	la.AddGoto(5, "E", 8);

	Analyser analyser;
	string input_string;

	while (cout << "Input expression: ", getline(cin, input_string))
	{
		vector<pair<string, string>> lex_result = analyser.AnalyseLexical(input_string);

		int error_index = -1;
		for (size_t i = 0; i < lex_result.size(); ++i)
		{
			if (lex_result[i].second == "unknown")
				error_index = i;
		}
		if (error_index != -1)
		{
			cout << "Error on: " << lex_result[error_index].first << endl;
			continue;
		}
		vector<pair<string, string>> escape_result = Escape(lex_result);
		la.Input(escape_result);

		if ((error_index = la.Analyse()) != -1)
		{
			if (error_index == lex_result.size())
				cout << "Error on: the end of input" << endl;
			else
				cout << "Error on: " << lex_result[error_index].first << endl;
			continue;
		}

		cout << "Right!" << endl;;
	}
}

int StringToInt(string str)
{
	stringstream ss;
	ss << str;
	int result;
	ss >> result;
	return result;
}

vector<pair<string, string>> Escape(vector<pair<string, string>> lexResult)
{
	map<string, string> escape_tactics;
	Glossary glossary;
	escape_tactics.insert(pair<string, string>(glossary.GetValue("+"), string("+")));
	escape_tactics.insert(pair<string, string>(glossary.GetValue("-"), string("+")));
	escape_tactics.insert(pair<string, string>(glossary.GetValue("*"), string("*")));
	escape_tactics.insert(pair<string, string>(glossary.GetValue("/"), string("*")));
	escape_tactics.insert(pair<string, string>(glossary.GetValue("name"), string("i")));
	escape_tactics.insert(pair<string, string>(glossary.GetValue("100"), string("i")));
	escape_tactics.insert(pair<string, string>(glossary.GetValue("("), string("(")));
	escape_tactics.insert(pair<string, string>(glossary.GetValue(")"), string(")")));

	vector<pair<string, string>> result;
	for (pair<string, string> p : lexResult)
	{
		map<string, string>::iterator it = escape_tactics.find(p.second);
		pair<string, string> new_pair;
		new_pair.first = it->second;
		if (p.second == glossary.GetValue("+"))
			result.push_back(pair<string, string>("+", "+"));
		if (p.second == glossary.GetValue("-"))
			result.push_back(pair<string, string>("+", "-"));
		if (p.second == glossary.GetValue("*"))
			result.push_back(pair<string, string>("*", "*"));
		if (p.second == glossary.GetValue("/"))
			result.push_back(pair<string, string>("*", "/"));
		if (p.second == glossary.GetValue("name"))
			result.push_back(pair<string, string>("i", p.first));
		if (p.second == glossary.GetValue("100"))
			result.push_back(pair<string, string>("i", p.first));
		if (p.second == glossary.GetValue("("))
			result.push_back(pair<string, string>("(", "("));
		if (p.second == glossary.GetValue(")"))
			result.push_back(pair<string, string>(")", ")"));

	}
	return result;
}
