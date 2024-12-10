function res=fun(a)
    ind = find(a>0);
    res = sum(a(ind));
end