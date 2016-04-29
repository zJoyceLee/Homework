// STL
#include <iostream>
#include <fstream>
#include <map>
#include <string>
// Current Project
#include "Recognizer.hpp"

std::vector<std::string> readAllLines(const std::string & path) {
    std::vector<std::string> ret;

    std::ifstream ifs(path);
    if(!ifs) {
        throw std::runtime_error("cannot open file: " + path);
    }

    std::string line;
    while(true) {
        std::getline(ifs, line);
        if(!ifs)
            break;
        ret.push_back(line);
    }
    return ret;
}

void test(const std::string & inputPath, const std::string & outputPath) {
    Recognizer r;

    std::ifstream ifs(inputPath);
    if(!ifs) {
        throw std::runtime_error("cannot open file: " + inputPath);
    }
    std::stringstream buffer;
    buffer << ifs.rdbuf();
    std::string inputString(buffer.str());
    ifs.close();

    std::map<std::string, int> result = r.RecognizeIdentifier(inputString);
	std::ofstream fout(outputPath);
	for (std::pair<std::string, int> mypair: result){
		fout << "(" << mypair.first << ":\t" << mypair.second << ")" << std::endl;
	}
	fout.close();
	std::cout << outputPath << " write done!" << std::endl;
}

int main(int argc, char * argv[]) {

    test("./testInput/test01.pl0", "./testOutput/test01.txt");
    test("./testInput/test02.pl0", "./testOutput/test02.txt");
    test("./testInput/test03.pl0", "./testOutput/test03.txt");
    test("./testInput/test04.pl0", "./testOutput/test04.txt");
    test("./testInput/test05.pl0", "./testOutput/test05.txt");

	return 0;
}
