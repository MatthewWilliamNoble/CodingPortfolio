%%%%++++%%%%++++%%%%
%
%   Name:
%   Matthew W. Noble
%
%   Purpose:
%   Model of my Cahn-Hilliard equations.
%
%%%%++++%%%%++++%%%%

%%%%    Preamble

clear;  close all;  clc

%%%%    Parameters

D_SIA = 100;    D_vac = 1;
gamma_SIA = 1;  gamma_vac = 1;

%%%%    Box

width = 200;
res = 5;

%%%%    Time

dt = 0.001;   
stoptime = 100000000;

%%%%    Initial conditions

base_vac = 0.25;    base_SIA = 0.05;    
sigma_init_SIA = 0.05;  sigma_init_vac = 0.05;

[t, A, B] = Initial_Conditions(width, base_SIA, base_vac, sigma_init_SIA, sigma_init_vac);

annhilation = 0.001;
creation = annhilation * base_SIA * base_vac;

%%%%    Define Image

axes('Position',[0 0 1 1])
axis off
hi = image(A);
hi.CDataMapping = 'scaled';

ht = text(10,width-10,'Time = 0', 'FontSize',18);

% ht.Color = [.95 .2 .8];
colormap(jet);

drawnow

while t <= stoptime

    anew = A + ( D_vac.*4.*Laplacian2D(A.^3,res) + D_vac.*4.*Laplacian2D(A, res) - D_vac.*4.*Laplacian2D(A.^2, res) - D_vac.*gamma_vac.*Biharmonic2D(A,res) + creation - annhilation.*A.*B ) .* dt;
    bnew = B + ( D_SIA.*4.*Laplacian2D(B.^3,res) + D_SIA.*4.*Laplacian2D(B, res) - D_SIA.*4.*Laplacian2D(B.^2, res) - D_SIA.*gamma_SIA.*Biharmonic2D(B,res) + creation - annhilation.*A.*B ) .* dt;
   
    A = anew;
    B = bnew;
    
    hi.CData = A;
    ht.String = ['Time = ' num2str(t)];
    drawnow limitrate
    
    t = t + dt;
    
end
