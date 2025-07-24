#include<iostream>
#include<vector>

using namespace std;

// How many times a sorted array has been rotated
// If it is not sorted and rotated array return -1;
// but couldn't come up logic for determining that it isn't so linear soln for now

void helper(const vector<int>& nums,const int size){
    int swap=0;
    int solIdx=-1;
    for(int i=0;i<size-1;++i){
        if(nums[i]>nums[i+1]){
            ++swap;
            solIdx=i;
        }
    }

    if(swap==0){
        cout<<0<<"\n";
        return;
    }

    if(nums[size-1]>nums[0]){
        swap++;
        solIdx=size-1;
    }
    
    if(swap>1){
        cout<<-1<<"\n";
        return;
    }
    cout<<size-solIdx-1<<"\n";
}

int main(){
    int size;
    cin>>size;
    vector<int> nums(size);
    for(int& x:nums) cin>>x;
    helper(nums,size);
}