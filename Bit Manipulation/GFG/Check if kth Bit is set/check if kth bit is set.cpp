bool checkKthBit(int n, int k)
    {
        int mask=1<<k;
        return (n&mask) > 0 ? 1:0;
    }
