#include<iostream>
#include<vector>

using namespace std;

void helper(const vector<int>& arr){
    bool left=false;
    int i=0,j=arr.size()-1;
    while(i<=j){
        if(!left){
            cout<<arr[i++]<<" ";
            left=true;
        }
        else{
            cout<<arr[j--]<<" ";
            left=false;
        }
    }
    cout<<"\n";
}

int main(){
    int test;
    cin>>test;
    while(test--){
        int size;
        cin>>size;
        vector<int> arr(size);
        for(int& num:arr) cin>>num;
        helper(arr);
    }
}