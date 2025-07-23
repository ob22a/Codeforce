#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

void solution(vector<int> arr){
    vector<int> original;
    for(int num:arr) original.emplace_back(num);
    sort(arr.begin(),arr.end());
    if(original==arr){
        cout<<"NO";
        return;
    }
    for(int i=0;i<)
}

int main(){
    int numberOfTestCases;
    cin>>numberOfTestCases;
    vector<vector<int>> testCases(numberOfTestCases);
    for(int i=0;i<numberOfTestCases;++i){
        int lenArr;
        cin>>lenArr;
        vector<int> arr(lenArr);
        for(int j=0;j<lenArr;++j) cin>>arr[j];
        testCases[i]=arr;
    }



}