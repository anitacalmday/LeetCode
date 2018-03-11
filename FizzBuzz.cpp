//Write a program that outputs the string representation of numbers from 1 to n.

//But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> output; 
        for (int i=1; i<n+1; i++)
        {
       //     cout << stoi(i) << endl;
            if (i % 3==0 && i % 5 ==0)
                output.push_back("FizzBuzz");
                //cout << "Fizz" << endl;
            else if(i % 5 ==0)
                output.push_back("Buzz");
               // cout << "Buzz" << endl; 
            else if(i % 3 == 0 )
                 output.push_back("Fizz");
           //     cout << "FizzBuzz" << endl;
            
            else output.push_back(std::to_string(i) );
        }
        return output;
    }
};
