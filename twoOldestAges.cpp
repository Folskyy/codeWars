#include <vector>
#include <array>

std::array<int, 2> two_oldest_ages(std::vector<int> ages){
    int max[2] = {ages[1], ages[0]};

    for(int i = 2; i < ages.size(); i++){
        if(max[0] > max[1]){
            int aux = max[0];
            max[0] = max[1];
            max[1] = aux;
        }
        
        if(ages[i] > max[1]){
            int aux = max[1];
            max[1] = ages[i];
            max[0] = aux;
        }
        else if(ages[i] > max[0])
            max[0] = ages[i];
    }
    return {max[0], max[1]};
}

#include<iostream>
int main(){
    std::vector<int> input[3] = {{1, 2, 10, 8}, {1, 5, 87, 45, 8, 8}, {1, 3, 10, 0}};

    for(int i = 0; i < 3; i++){
        std::array<int, 2> arr = two_oldest_ages(input[i]);
        std::cout << "Input[" << i << "]: " << "[" << arr[0] << ", " << arr[1] << "]" << std::endl;
    }

    return 0;
}