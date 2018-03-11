//Write a function that takes a string as input and returns the string reversed.

class Solution {
public:
    string reverseString(string s) {
        string newstr;
        for (int i = s.length()-1; i>=0; i--)
        {
            newstr += s[i];
        }
        return newstr;
    }
};
