#include<iostream>
#include<vector>

using namespace std;

void helper(const vector<int>& nums,const int& n, const int& sum){
    // If total sum is larger than target then -1
    int zerofreq=nums[0],onefreq=nums[1],twofreq=nums[2];
    long long total=1*onefreq+2*twofreq;
    if(total==sum || total<sum-1){
        cout<<-1<<"\n";
        return;
    }
   
    while(zerofreq--) cout<<0<<" ";
    while(twofreq--) cout<<2<<" ";
    while(onefreq--){
        if(onefreq) cout<<1<<" ";
        else cout<<1;
    }
    cout<<'\n';
}

int main(){
    int t;
    cin>>t;
    while(t--){
        int n,s;
        cin>>n>>s;
        vector<int> nums(3);
        for(int i=0;i<n;++i){
            int x;
            cin>>x;
            nums[x]++;
        }
        helper(nums,n,s);
    }
}