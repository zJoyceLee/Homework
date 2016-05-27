#pragma once
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <map>
class Expector
{
public:

	Expector(std::vector<std::pair<std::string, std::string>> lexicals)
	{
		this->lexicals = lexicals;
	}

	~Expector();

	bool Expect()
	{

	}
private:
	std::vector<std::pair<std::string, std::string>> lexicals;
};
