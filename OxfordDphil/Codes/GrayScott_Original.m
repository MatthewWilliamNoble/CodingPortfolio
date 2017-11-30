%%%%++++%%%%++++%%%%
%
%   Name:
%   Matthew W. Noble
%
%   Purpose:
%   Model of the Gray-Scott equations.
%
%%%%++++%%%%++++%%%%

%%%%    Preamble

clear;  close all;  clc

%%%%    Kill and Feed rates

% f = 0.055;    k = 0.062;    %     LABYRINTH
% f = 0.018;    k = 0.051;    %     PLANKTON RIPPLES
f = 0.026;    k = 0.053;    %     HEXAGONS

%%%%    Parameters

da = 1;    db = 0.5;

%%%%    Box

width = 300;
res = 2;

%%%%    Time

dt = 0.1;    stoptime = 40000;

%%%%    Initialisation

[t, A, B] = Initial_Conditions(width);

%%%%    Define Image

axes('Position',[0 0 1 1])
axis off
hi = image(A);
hi.CDataMapping = 'scaled';

ht = text(10,width-10,'Time = 0', 'FontSize',18);

%ht.Color = [.95 .2 .8];
colormap(jet);

drawnow

%%%%    Main Body

while t<stoptime
    
    anew = A + (da*Laplacian2D(A, res) - A.*B.^2 + f*(1-A))*dt;
    bnew = B + (db*Laplacian2D(B, res) + A.*B.^2 - (k+f)*B)*dt;
    
    A = anew;
    B = bnew;
    
    hi.CData = A;
    
    t = t+dt;
    
    ht.String = ['Time = ' num2str(t)];
    
    drawnow limitrate
    
end