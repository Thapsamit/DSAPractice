class Solution 
{
    public:
    //Function to find distance of nearest 1 in the grid for each cell.
	vector<vector<int>>nearest(vector<vector<int>>grid)
	{
	    int n = grid.size();
	    int m = grid[0].size();
	    vector<vector<int>>vis (n,vector<int>(m,0));
	    vector<vector<int>>dis (n,vector<int>(m,0));
	    queue<pair<pair<int,int>,int>> qu;
	    int ngrow[] = {-1,0,1,0};
	    int ngcol[] = {0,1,0,-1};
	    for(int i=0; i<n;i++){
	        for(int j=0; j<m;j++){
	            if(grid[i][j]==1){
	                qu.push({{i,j},0});
	                vis[i][j] = 1;
	            }
	            else{
	                vis[i][j] = 0;
	            }
	        }
	    }
	    while(!qu.empty()){
	        int crow = qu.front().first.first;
	        int ccol = qu.front().first.second;
	        int dist = qu.front().second;
	        dis[crow][ccol] = dist;
	        qu.pop();
	        for(int i = 0; i<4;i++){
	            int nrow = crow+ngrow[i];
	            int ncol = ccol+ngcol[i];
	            if(nrow>=0 && nrow<n && ncol>=0 && ncol<m && vis[nrow][ncol]==0){
	                vis[nrow][ncol] = 1;
	                qu.push({{nrow,ncol},dist+1});
	                
	            }
	        }
	    }
	    return dis;
	}