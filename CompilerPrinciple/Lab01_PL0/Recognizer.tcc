#pragma once

std::map<std::string, int> Recognizer::RecognizeIdentifier(std::string inputString) {
    std::vector<std::string> temp_string_list;
    unsigned int start = -1;

    for (unsigned int end = 0; end < inputString.length(); ++end) {
        if (IsSeparator(inputString[end])) {
            temp_string_list.push_back(inputString.substr(start + 1, end - (start + 1)));
            start = end;
        }
    }

    std::map<std::string, int> result;
    for(std::string str : temp_string_list) {
        std::transform(str.begin(), str.end(), str.begin(), tolower);

        if (str.length() > 0 && !IsBasicWord(str) && !IsNumber(str[0])) {
            std::map<std::string, int>::iterator it = result.find(str);
            if (it == result.end()) {
                result.insert(std::pair<std::string, int>(str, 1));
            } else {
                ++it->second;
            }
        }
    }

    return result;
}
