#pragma once
#include <string>
#include <map>

class Glossary
{
public:

	Glossary()
	{
		basic_words.insert(std::pair<std::string, std::string>("begin", "beginsym"));
		basic_words.insert(std::pair<std::string, std::string>("call", "callsym"));
		basic_words.insert(std::pair<std::string, std::string>("const", "constsym"));
		basic_words.insert(std::pair<std::string, std::string>("do", "dosym"));
		basic_words.insert(std::pair<std::string, std::string>("end", "endsym"));
		basic_words.insert(std::pair<std::string, std::string>("if", "ifsym"));
		basic_words.insert(std::pair<std::string, std::string>("odd", "oddsym"));
		basic_words.insert(std::pair<std::string, std::string>("procedure", "proceduresym"));
		basic_words.insert(std::pair<std::string, std::string>("read", "readsym"));
		basic_words.insert(std::pair<std::string, std::string>("then", "thensym"));
		basic_words.insert(std::pair<std::string, std::string>("var", "varsym"));
		basic_words.insert(std::pair<std::string, std::string>("while", "whilesym"));
		basic_words.insert(std::pair<std::string, std::string>("write", "writesym"));

		operators.insert(std::pair<std::string, std::string>("+", "plus"));
		operators.insert(std::pair<std::string, std::string>("-", "minus"));
		operators.insert(std::pair<std::string, std::string>("*", "times"));
		operators.insert(std::pair<std::string, std::string>("/", "slash"));
		operators.insert(std::pair<std::string, std::string>("=", "eql"));
		operators.insert(std::pair<std::string, std::string>("#", "neq"));
		operators.insert(std::pair<std::string, std::string>("<", "lss"));
		operators.insert(std::pair<std::string, std::string>("<=", "leq"));
		operators.insert(std::pair<std::string, std::string>(">", "gtr"));
		operators.insert(std::pair<std::string, std::string>(">=", "geq"));
		operators.insert(std::pair<std::string, std::string>(":=", "becomes"));

		delimiters.insert(std::pair<std::string, std::string>("(", "lparen"));
		delimiters.insert(std::pair<std::string, std::string>(")", "rparen"));
		delimiters.insert(std::pair<std::string, std::string>(",", "comma"));
		delimiters.insert(std::pair<std::string, std::string>(";", "semicolon"));
		delimiters.insert(std::pair<std::string, std::string>(".", "period"));
	}

	~Glossary(){}

	std::string GetValue(std::string key)
	{
		if (IsNumber(key))
			return "number";

		std::map<std::string, std::string>::iterator it;

		it = basic_words.find(key);
		if (it != basic_words.end())
			return it->second;

		it = operators.find(key);
		if (it != operators.end())
			return it->second;

		it = delimiters.find(key);
		if (it != delimiters.end())
			return it->second;

		if (CanBeIdentifier(key))
			return "ident";

		return "unknown";
	}

	bool IsOperator(std::string str)//For Recgnizer.RecognizeWord()
	{
		std::map<std::string, std::string>::iterator it = operators.find(str);
		return it != operators.end();
	}

protected:

	bool IsNumber(std::string key)
	{
		return key.length() > 0 && key.find_first_not_of("1234567890") == std::string::npos
			|| key.length() > 1 && ( key[0] == '-' || key[0] == '+') && key.substr(1).find_first_not_of("1234567890") == std::string::npos;
	}

	bool CanBeIdentifier(std::string key)
	{
		return key.length() > 0
			&& key.find_first_not_of("1234567890abcdefghijklmnopqrstuvwxyz") == std::string::npos
			&& std::string("1234567890").find(key[0]) == std::string::npos;
	}

private:
	std::map<std::string, std::string> basic_words;
	std::map<std::string, std::string> operators;
	std::map<std::string, std::string> delimiters;

};
