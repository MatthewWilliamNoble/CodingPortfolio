function out = Biharmonic2D(in, res)

h = res;
k = res;

f_xxxx = (circshift(in,[ 0, -2]) - 4.*circshift(in,[ 0, -1]) + 6.*circshift(in,[ 0, 0]) - 4.*circshift(in,[ 0, 1]) + circshift(in,[ 0, 2]))./h^4;
f_yyyy = (circshift(in,[ -2, 0]) - 4.*circshift(in,[ -1, 0]) + 6.*circshift(in,[ 0, 0]) - 4.*circshift(in,[ 1, 0]) + circshift(in,[ 2, 0]))./k^4;
f_xxyy = (circshift(in,[ -1, -1]) - 2.*circshift(in,[ 0, -1]) + circshift(in,[ 1, -1]) - 2.*circshift(in,[ -1, 0]) + 4.*circshift(in,[ 0, 0]) - 2.*circshift(in,[ 1, 0]) + circshift(in,[ -1, 1]) - 2.*circshift(in,[ 0, 1]) + circshift(in,[ 1, 1]))./(h^2 .* k^2);

out = f_xxxx + f_xxyy + f_xxyy + f_yyyy;

end