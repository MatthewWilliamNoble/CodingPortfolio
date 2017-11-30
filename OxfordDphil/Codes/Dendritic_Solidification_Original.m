%%%%++++%%%%++++%%%%
%
%   Name:   
%   Matthew W. Noble
%
%   Purpose:    
%   Dendritic Solidification. Recreate Ryo Kobayashi model from: "Modelling and numerical simulations of dendritic crystal growth"
%
%   Original Author:    
%   N. Singh 
%
%%%%++++%%%%++++%%%%

%%%%    Preamble

clear;  clc;

pi = 3.14159265358;

%%%%    Parameters

k = 1.8;                %Latent heat
TAU = 0.0003;           %PF relaxation time
EPS = 0.01;             %Interfacial width
DELTA = 0.020;          %Modulation of the interfacial width.
ANGLEO = pi/2;          %Orientation of the anisotropy axis.
ANISO = 6;              %Anisotropy 2*pi/ANISO
ALPHA = 0.5;            %m(T) = ALPHA/pi * atan(GAMMA*(TEQ-T))
GAMMA = 10.0;
TEQ = 1.0;              %Melting temperature.

%%%%    Box

NX = 200;
NY = 200;
H = 0.03;               %Spatial resolution

%%%%    Time

DT = 0.0003;            %Temporal Resolution
timesteps = 2000000;    %Number of timesteps

%%%%    Initial temperature and phase field information

T = zeros(NY,NX);
p = zeros(NY,NX);
for i1 = 1:NY
    for i2 = 1:NX
        if ((i1-NY/2)*(i1-NY/2)+(i2-NX/2)*(i2-NX/2)<100)
            p(i1,i2) = 1.0;
        else
            p(i1,i2) = 0.0;
        end
    end
end

%%%%    Pre Allocation of matrices for faster calculations

grad_p_X = zeros(NY,NX);
grad_p_Y = zeros(NY,NX);
aX = zeros(NY,NX);
aY = zeros(NY,NX);
eps2 = zeros(NY,NX);
angle = zeros(NY,NX);
epsilon_prime = zeros(NY,NX);
epsilon = zeros(NY,NX);
dXdY = zeros(NY,NX);
dYdX = zeros(NY,NX);
grad_eps2_X = zeros(NY,NX);
grad_eps2_Y = zeros(NY,NX);
lap_p = zeros(NY,NX);
lap_T = zeros(NY,NX);

%%%%    Main body

for index = 1:timesteps
    
    %   Calculation of all the relevant matrices.
    
    for i1 = 1:NY
        for i2 = 1:NX
            ip = mod(i2,NX)+1;
            im = mod((NX+i2-2),NX)+1;
            jp = mod(i1,NY)+1;
            jm = mod((NY+i1-2),NY)+1;
            grad_p_X(i1,i2) = ((p(i1,ip) - p(i1,im))/H);
            grad_p_Y(i1,i2) = ((p(jp,i2) - p(jm,i2))/H);
            lap_p(i1,i2) = (2.0*(p(i1,ip)+p(i1,im)+p(jp,i2)+p(jm,i2))+p(jp,ip)+p(jm,im)+p(jp,im)+p(jm,ip)-12.0*p(i1,i2))/(3.0*H*H);
            lap_T(i1,i2) = (2.0*(T(i1,ip)+T(i1,im)+T(jp,i2)+T(jm,i2))+T(jp,ip)+T(jm,im)+T(jp,im)+T(jm,ip)-12.0*T(i1,i2))/(3.0*H*H);
        end
    end
    
    for i1 = 1:NY
        for i2 = 1:NX
            if (grad_p_X(i1,i2) == 0.0 && grad_p_Y(i1,i2) > 0.0)
                angle(i1,i2) = 0.5*pi;
            end
            
            if (grad_p_X(i1,i2) == 0.0 && grad_p_Y(i1,i2) <= 0.0)
                angle(i1,i2) = -0.5*pi;
            end
            
            if (grad_p_X(i1,i2) > 0.0 && grad_p_Y(i1,i2) > 0.0)
                angle(i1,i2) = atan(grad_p_Y(i1,i2)/grad_p_X(i1,i2));
            end
            
            if (grad_p_X(i1,i2) > 0.0 && grad_p_Y(i1,i2) <= 0.0)
                angle(i1,i2) = 2.0*pi+atan(grad_p_Y(i1,i2)/grad_p_X(i1,i2));
            end
            
            if (grad_p_X(i1,i2) < 0.0)
                angle(i1,i2) = pi+atan(grad_p_Y(i1,i2)/grad_p_X(i1,i2));
            end
        end
    end
    
    for i1 = 1:NY
        for i2 = 1:NX
            epsilon(i1,i2) = EPS*(1.0 + DELTA*cos(ANISO*(angle(i1,i2)-ANGLEO)));
            epsilon_prime(i1,i2) = -EPS*ANISO*DELTA*sin(ANISO*(angle(i1,i2)-ANGLEO));
        end
    end
    
    for i1 = 1:NY
        for i2 = 1:NX
            aY(i1,i2) = -epsilon(i1,i2)* epsilon_prime(i1,i2) * grad_p_Y(i1,i2);
            aX(i1,i2) = epsilon(i1,i2) * epsilon_prime(i1,i2) * grad_p_X(i1,i2);
            eps2(i1,i2) = epsilon(i1,i2) * epsilon(i1,i2);
        end
    end
    
    for i1 = 1:NY
        for i2 = 1:NX
            ip = mod(i2,NX)+1;
            im = mod((NX+i2-2),NX)+1;
            jp = mod(i1,NY)+1;
            jm = mod((NY+i1-2),NY)+1;
            dXdY(i1,i2) = (aY(i1,ip)-aY(i1,im))/H;
            dYdX(i1,i2) = (aX(jp,i2)-aX(jm,i2))/H;
            grad_eps2_X(i1,i2) = (eps2(i1,ip)-eps2(i1,im))/H;
            grad_eps2_Y(i1,i2) = (eps2(jp,i2)-eps2(jm,i2))/H;
        end
    end
    
    for i1 = 1:NY
        for i2 = 1:NX
            po = p(i1,i2);
            m = (ALPHA/pi)*atan(GAMMA*(TEQ-T(i1,i2)));
            scal = grad_eps2_X(i1,i2)*grad_p_X(i1,i2)+grad_eps2_Y(i1,i2)*grad_p_Y(i1,i2);
            %   Evolution of the phase field variable.
            p(i1,i2) = p(i1,i2)+((dXdY(i1,i2)+dYdX(i1,i2)+eps2(i1,i2)*lap_p(i1,i2)+scal+po*(1.0-po)*(po-0.5+m))*DT/TAU);
            %   Evolution of the temperature field.
            T(i1,i2) = T(i1,i2)+(lap_T(i1,i2)*DT)+(k*(p(i1,i2)-po));
        end
    end
    
    %   Visualisation of the output.
    
    figure(1)
    image(p*50)
    colormap('hot')
    drawnow
    
end