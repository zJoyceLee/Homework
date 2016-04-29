#pragma once
// STL
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <map>

class Recognizer {
public:
	Recognizer()
    {
        basic_words[0] = "begin";
        basic_words[1] = "call";
        basic_words[2] = "const";
        basic_words[3] = "do";
        basic_words[4] = "end";
        basic_words[5] = "if";
        basic_words[6] = "odd";
        basic_words[7] = "procedure";
        basic_words[8] = "read";
        basic_words[9] = "then";
        basic_words[10] = "var";
        basic_words[11] = "while";
        basic_words[12] = "write";
    }

	~Recognizer() {}

	std::map<std::string, int> RecognizeIdentifier(std::string inputString);

protected:
	bool IsSeparator(char ch){
		return !(
			IsNumber(ch)
			|| (ch >= 'a' && ch <= 'z')
			|| (ch >= 'A' && ch <= 'Z'));
	}

	bool IsNumber(char ch){
		return ch >= '0' && ch <= '9';
	}

	bool IsBasicWord(std::string str){
		for (int i = 0; i < 13; ++i){
			if (str == basic_words[i])
				return true;
		}
		return false;
	}

private:
	std::string basic_words[13];
};

#include "Recognizer.tcc"
