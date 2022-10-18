pair<int, int> get(int x, int y){
        x=x^y;
        y=x^y;
        x=x^y;
        pair<int,int> ans= {x,y};
        return ans;
    }
