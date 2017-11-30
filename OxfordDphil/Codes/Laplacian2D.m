function out = Laplacian2D(in, res)

h = res;
k = res;

f_xx = (circshift(in,[ 0, 1]) - 2 .* circshift(in,[ 0, 0]) + circshift(in,[ 0, -1]))./h.^2;
f_yy = (circshift(in,[ 1, 0]) - 2 .* circshift(in,[ 0, 0]) + circshift(in,[ -1, 0]))./k.^2;

out = f_xx + f_yy;

end