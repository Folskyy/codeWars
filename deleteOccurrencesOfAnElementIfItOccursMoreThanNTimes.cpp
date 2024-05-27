#include<vector>
#include<map>

using namespace std;

vector<int> deleteNth (vector<int> arr, int num){
  vector<int> arrAux;
  map<int, int> contador;

  for(int elemento : arr){
    if(contador[elemento] < num)
      arrAux.push_back(elemento);
    contador[elemento]++;
  }
  return arrAux;
}
