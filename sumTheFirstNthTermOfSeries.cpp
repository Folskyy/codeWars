#include<iostream>
#include<string>
#include<iomanip>

std::string seriesSum(int num){
  double sum = 1; int div = 4;

  if(num == 0)
    return "0.00";

  for(int i = 1; i < num; i++){//iteration to add the divisions (1/div) at the 'sum'
    sum += double(1.00/div);
    div += 3;
  }

  std::stringstream stream;//stringstream var to an easy conversion double to string
  stream << std::fixed << std::setprecision(2) << sum;//settin the number of decimal places
  std::string result = stream.str();//assigning the string at the object stringstream to the string result

  return result;
}