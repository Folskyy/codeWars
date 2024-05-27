#include <iostream>
#include <vector>

using namespace std;

int findOdd (vector<int> v){//retorna o numero de repeticoes do numero em um v
    int contador = 0, aux = 0;
    for(int i=0; i<v.size(); i++){
      for(int j = 0; j < v.size(); j++){
        if(v [i] == v[j])
          contador++;
      }
      if(contador > aux && contador%2 != 0)
        aux = v[i];
      contador = 0;
    }
    return aux;
  }