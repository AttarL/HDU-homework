function I = surf_int(f,vars,t,a,b)
if length(f)==1
    if length(vars)~=1
        E = simplify(sum(diff(vars,t(1)).^2));
        F = sum(diff(vars,t(1)).*diff(vars,t(2)));
        G = simplify(sum(diff(vars,t(2)).^2));
    else
        E = simplify(1+diff(vars,t(1))^2);
        F = diff(vars,t(1))*diff(vars,t(2));
        G = simplify(1+diff(vars,t(2))^2);
    end
    I = int(int(simplify(f*sqrt(E*G-F^2)),t(1),a(1),a(2)),t(2),b(1),b(2));
else
    if length(vars)~=1
        A = diff(vars(2),t(1))*diff(vars(3),t(2)) - diff(vars(3),t(1))*diff(vars(2),t(2));
        B = diff(vars(3),t(1))*diff(vars(1),t(2)) - diff(vars(1),t(1))*diff(vars(3),t(2));
        C = diff(vars(1),t(1))*diff(vars(2),t(2)) - diff(vars(2),t(1))*diff(vars(1),t(2));
    else
        A = - diff(vars,t(1));
        B = - diff(vars,t(2));
        C = 1;
    end
    f = f(:); abc = [A, B, C];
    I = int(int(simplify(abc*f),t(1),a(1),a(2)),t(2),b(1),b(2));
end


