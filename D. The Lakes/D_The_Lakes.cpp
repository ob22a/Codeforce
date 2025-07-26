#include<iostream>
#include<vector>
#include<cstring>

using namespace std;

int rowSize;
int colSize;
bool seen[1001][1001]={};

int dfs(const vector<vector<int>>& grid,int i,int j){
    if(i<0 || i>rowSize-1 || j<0 || j>colSize-1 || grid[i][j]==0 ||seen[i][j]) return 0;
    
    seen[i][j]=true;
    
    int sum=grid[i][j];
    sum+=dfs(grid,i,j+1);
    sum+=dfs(grid,i+1,j);
    sum+=dfs(grid,i,j-1);
    sum+=dfs(grid,i-1,j);

    return sum;
}

void helper(const vector<vector<int>>& grid){
    memset(seen, false, sizeof(seen));
    int sol=0;
    for(int i=0;i<rowSize;++i){
        for(int j=0;j<colSize;++j){
            if(grid[i][j]==0 || seen[i][j]) continue;
            int val=dfs(grid,i,j);
            sol=max(sol,val);
        }
    }
    cout<<sol<<"\n";
}

int main(){
    int t;
    cin>>t;
    while (t--){
        int n,m;
        cin>>n>>m;
        rowSize=n;
        colSize=m;
        vector<vector<int>> grid(n,vector<int>(m));
        for(vector<int>& row:grid){
            for(int& x:row) cin>>x;
        }
        helper(grid);
    }
}