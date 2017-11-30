%%%%++++%%%%++++%%%%
%
%   Name:
%   Matthew W. Noble
%
%   Purpose:
%   Anisotropic diffusion of halo SIA, isotropic diffusion of cluster vacancy. Random
%   time injection. Random space injection.
%
%%%%++++%%%%++++%%%%

%%%%    Preamble

clear;  clc;

Pi = 3.14159265358;

%%%%    Parameters

TAU_SIA = 0.0003;       %   PF relaxation time.
TAU_Vac = 0.0003;       %   PF relaxation time.

K_Annhilation = 0.5;    %   Annhilation

EPS_SIA = 0.01;         %   Interfacial width
DELTA_SIA = 0.045;      %   Modulation of the interfacial width.
%DELTA_SIA = 0.0        %   Turn anisotropy off.
ANGLEO_SIA = 0.0;       %   Orientation of the anisotropy axis. Radians.
ANISO_SIA = 4.0;        %   Anisotropy 2*pi/ANISO

EPS_Vac = 0.01;         %   Interfacial width
%DELTA_Vac = 0.045;     %   Modulation of the interfacial width.
DELTA_Vac = 0.0;        %   Turn anisotropy off.
ANGLEO_Vac = 0.0;       %   Orientation of the anisotropy axis. Radians.
ANISO_Vac = 4.0;        %   Anisotropy 2*pi/ANISO

RADIUS_Outer = 15;
RADIUS_Inner = 10;

%%%%    Box

NX = 100;
NY = 100;
H = 0.02;               %   Spatial resolution.

%%%%    Time

DT = 0.0002;            %   Temporal Resolution.
Timesteps = 10000;      %   Number of timesteps.

%%%%    Pre Allocation of matrices for faster calculations

C_SIA = zeros(NY,NX);
C_Vac = zeros(NY,NX);
C_Total = zeros(NY,NX);

grad_p_X_SIA = zeros(NY,NX);
grad_p_Y_SIA = zeros(NY,NX);
aX_SIA = zeros(NY,NX);
aY_SIA = zeros(NY,NX);
eps2_SIA = zeros(NY,NX);
angle_SIA = zeros(NY,NX);
epsilon_prime_SIA = zeros(NY,NX);
epsilon_SIA = zeros(NY,NX);
dXdY_SIA = zeros(NY,NX);
dYdX_SIA = zeros(NY,NX);
grad_eps2_X_SIA = zeros(NY,NX);
grad_eps2_Y_SIA = zeros(NY,NX);
lap_p_SIA = zeros(NY,NX);

grad_p_X_Vac = zeros(NY,NX);
grad_p_Y_Vac = zeros(NY,NX);
aX_Vac = zeros(NY,NX);
aY_Vac = zeros(NY,NX);
eps2_Vac = zeros(NY,NX);
angle_Vac = zeros(NY,NX);
epsilon_prime_Vac = zeros(NY,NX);
epsilon_Vac = zeros(NY,NX);
dXdY_Vac = zeros(NY,NX);
dYdX_Vac = zeros(NY,NX);
grad_eps2_X_Vac = zeros(NY,NX);
grad_eps2_Y_Vac = zeros(NY,NX);
lap_p_Vac = zeros(NY,NX);

%%%%    Main Body

for index = 1:Timesteps
    
    %   Damage event
    
    if mod(index,randi(10)) == 1.0
        
        Y_Val = randi(NY-RADIUS_Outer);
        X_Val = randi(NX-RADIUS_Outer);
        
        for i_y = 1:1:NY
            for i_x = 1:1:NX
                if ((i_y-Y_Val)^2 + (i_x-X_Val)^2 < RADIUS_Inner^2)
                    C_SIA(i_y,i_x) = C_SIA(i_y,i_x);
                elseif ((i_y-Y_Val)^2 + (i_x-X_Val)^2 < RADIUS_Outer^2)
                    C_SIA(i_y,i_x) = C_SIA(i_y,i_x) + 1.0;
                else
                    C_SIA(i_y,i_x) = C_SIA(i_y,i_x);
                end
                
                if ((i_y-Y_Val)^2 + (i_x-X_Val)^2 < RADIUS_Inner^2)
                    C_Vac(i_y,i_x) = C_Vac(i_y,i_x) + 1.0;
                elseif ((i_y-Y_Val)^2 + (i_x-X_Val)^2 < RADIUS_Outer^2)
                    C_Vac(i_y,i_x) = C_Vac(i_y,i_x);
                else
                    C_Vac(i_y,i_x) = C_Vac(i_y,i_x);
                end
                
            end
        end
        
        %	Matrix calculations
        
        for i_y = 1:NY
            for i_x = 1:NX
                
                %   SIA
                
                ip_SIA = mod(i_x,NX)+1;
                im_SIA = mod((NX+i_x-2),NX)+1;
                jp_SIA = mod(i_y,NY)+1;
                jm_SIA = mod((NY+i_y-2),NY)+1;
                grad_p_X_SIA(i_y,i_x) = ((C_SIA(i_y,ip_SIA) - C_SIA(i_y,im_SIA))/H);
                grad_p_Y_SIA(i_y,i_x) = ((C_SIA(jp_SIA,i_x) - C_SIA(jm_SIA,i_x))/H);
                lap_p_SIA(i_y,i_x) = (2.0*(C_SIA(i_y,ip_SIA)+C_SIA(i_y,im_SIA)+C_SIA(jp_SIA,i_x)+C_SIA(jm_SIA,i_x))+C_SIA(jp_SIA,ip_SIA)+C_SIA(jm_SIA,im_SIA)+C_SIA(jp_SIA,im_SIA)+C_SIA(jm_SIA,ip_SIA)-12.0*C_SIA(i_y,i_x))/(3.0*H*H);
                
                %   Vac
                
                ip_Vac = mod(i_x,NX)+1;
                im_Vac = mod((NX+i_x-2),NX)+1;
                jp_Vac = mod(i_y,NY)+1;
                jm_Vac = mod((NY+i_y-2),NY)+1;
                grad_p_X_Vac(i_y,i_x) = ((C_Vac(i_y,ip_Vac) - C_Vac(i_y,im_Vac))/H);
                grad_p_Y_Vac(i_y,i_x) = ((C_Vac(jp_Vac,i_x) - C_Vac(jm_Vac,i_x))/H);
                lap_p_Vac(i_y,i_x) = (2.0*(C_Vac(i_y,ip_Vac)+C_Vac(i_y,im_Vac)+C_Vac(jp_Vac,i_x)+C_Vac(jm_Vac,i_x))+C_Vac(jp_Vac,ip_Vac)+C_Vac(jm_Vac,im_Vac)+C_Vac(jp_Vac,im_Vac)+C_Vac(jm_Vac,ip_Vac)-12.0*C_Vac(i_y,i_x))/(3.0*H*H);
            end
        end
        
        for i_y = 1:NY
            for i_x = 1:NX
                
                %   SIA
                
                if (grad_p_X_SIA(i_y,i_x) == 0.0 && grad_p_Y_SIA(i_y,i_x) > 0.0)
                    angle_SIA(i_y,i_x) = 0.5*Pi;
                end
                
                if (grad_p_X_SIA(i_y,i_x) == 0.0 && grad_p_Y_SIA(i_y,i_x) <= 0.0)
                    angle_SIA(i_y,i_x) = -0.5*Pi;
                end
                
                if (grad_p_X_SIA(i_y,i_x) > 0.0 && grad_p_Y_SIA(i_y,i_x) > 0.0)
                    angle_SIA(i_y,i_x) = atan(grad_p_Y_SIA(i_y,i_x)/grad_p_X_SIA(i_y,i_x));
                end
                
                if (grad_p_X_SIA(i_y,i_x) > 0.0 && grad_p_Y_SIA(i_y,i_x) <= 0.0)
                    angle_SIA(i_y,i_x) = 2.0*Pi+atan(grad_p_Y_SIA(i_y,i_x)/grad_p_X_SIA(i_y,i_x));
                end
                
                if (grad_p_X_SIA(i_y,i_x) < 0.0)
                    angle_SIA(i_y,i_x) = Pi+atan(grad_p_Y_SIA(i_y,i_x)/grad_p_X_SIA(i_y,i_x));
                end
                
                %   Vac
                
                if (grad_p_X_Vac(i_y,i_x) == 0.0 && grad_p_Y_Vac(i_y,i_x) > 0.0)
                    angle_Vac(i_y,i_x) = 0.5*Pi;
                end
                
                if (grad_p_X_Vac(i_y,i_x) == 0.0 && grad_p_Y_Vac(i_y,i_x) <= 0.0)
                    angle_Vac(i_y,i_x) = -0.5*Pi;
                end
                
                if (grad_p_X_Vac(i_y,i_x) > 0.0 && grad_p_Y_Vac(i_y,i_x) > 0.0)
                    angle_Vac(i_y,i_x) = atan(grad_p_Y_Vac(i_y,i_x)/grad_p_X_Vac(i_y,i_x));
                end
                
                if (grad_p_X_Vac(i_y,i_x) > 0.0 && grad_p_Y_Vac(i_y,i_x) <= 0.0)
                    angle_Vac(i_y,i_x) = 2.0*Pi+atan(grad_p_Y_Vac(i_y,i_x)/grad_p_X_Vac(i_y,i_x));
                end
                
                if (grad_p_X_Vac(i_y,i_x) < 0.0)
                    angle_Vac(i_y,i_x) = Pi+atan(grad_p_Y_Vac(i_y,i_x)/grad_p_X_Vac(i_y,i_x));
                end
            end
        end
        
        for i_y = 1:NY
            for i_x = 1:NX
                
                %   SIA
                
                epsilon_SIA(i_y,i_x) = EPS_SIA*(1.0 + DELTA_SIA*cos(ANISO_SIA*(angle_SIA(i_y,i_x)-ANGLEO_SIA)));
                epsilon_prime_SIA(i_y,i_x) = -EPS_SIA*ANISO_SIA*DELTA_SIA*sin(ANISO_SIA*(angle_SIA(i_y,i_x)-ANGLEO_SIA));
                
                %   Vac
                
                epsilon_Vac(i_y,i_x) = EPS_Vac*(1.0 + DELTA_Vac*cos(ANISO_Vac*(angle_Vac(i_y,i_x)-ANGLEO_Vac)));
                epsilon_prime_Vac(i_y,i_x) = -EPS_Vac*ANISO_Vac*DELTA_Vac*sin(ANISO_Vac*(angle_Vac(i_y,i_x)-ANGLEO_Vac));
            end
        end
        
        for i_y = 1:NY
            for i_x = 1:NX
                
                %   SIA
                
                aY_SIA(i_y,i_x) = -epsilon_SIA(i_y,i_x)* epsilon_prime_SIA(i_y,i_x) * grad_p_Y_SIA(i_y,i_x);
                aX_SIA(i_y,i_x) = epsilon_SIA(i_y,i_x) * epsilon_prime_SIA(i_y,i_x) * grad_p_X_SIA(i_y,i_x);
                eps2_SIA(i_y,i_x) = epsilon_SIA(i_y,i_x) * epsilon_SIA(i_y,i_x);
              
                %   Vac
                
                aY_Vac(i_y,i_x) = -epsilon_Vac(i_y,i_x)* epsilon_prime_Vac(i_y,i_x) * grad_p_Y_Vac(i_y,i_x);
                aX_Vac(i_y,i_x) = epsilon_Vac(i_y,i_x) * epsilon_prime_Vac(i_y,i_x) * grad_p_X_Vac(i_y,i_x);
                eps2_Vac(i_y,i_x) = epsilon_Vac(i_y,i_x) * epsilon_Vac(i_y,i_x);
            end
        end
        
        for i_y = 1:NY
            for i_x = 1:NX
                
                %   SIA
                
                ip_SIA = mod(i_x,NX)+1;
                im_SIA = mod((NX+i_x-2),NX)+1;
                jp_SIA = mod(i_y,NY)+1;
                jm_SIA = mod((NY+i_y-2),NY)+1;
                dXdY_SIA(i_y,i_x) = (aY_SIA(i_y,ip_SIA)-aY_SIA(i_y,im_SIA))/H;
                dYdX_SIA(i_y,i_x) = (aX_SIA(jp_SIA,i_x)-aX_SIA(jm_SIA,i_x))/H;
                grad_eps2_X_SIA(i_y,i_x) = (eps2_SIA(i_y,ip_SIA)-eps2_SIA(i_y,im_SIA))/H;
                grad_eps2_Y_SIA(i_y,i_x) = (eps2_SIA(jp_SIA,i_x)-eps2_SIA(jm_SIA,i_x))/H;
                
                %   Vac
                
                ip_Vac = mod(i_x,NX)+1;
                im_Vac = mod((NX+i_x-2),NX)+1;
                jp_Vac = mod(i_y,NY)+1;
                jm_Vac = mod((NY+i_y-2),NY)+1;
                dXdY_Vac(i_y,i_x) = (aY_Vac(i_y,ip_Vac)-aY_Vac(i_y,im_Vac))/H;
                dYdX_Vac(i_y,i_x) = (aX_Vac(jp_Vac,i_x)-aX_Vac(jm_Vac,i_x))/H;
                grad_eps2_X_Vac(i_y,i_x) = (eps2_Vac(i_y,ip_Vac)-eps2_Vac(i_y,im_Vac))/H;
                grad_eps2_Y_Vac(i_y,i_x) = (eps2_Vac(jp_Vac,i_x)-eps2_Vac(jm_Vac,i_x))/H;
            end
        end
        
        for i_y = 1:NY
            for i_x = 1:NX
                
                %   SIA
                
                scal_SIA = grad_eps2_X_SIA(i_y,i_x)*grad_p_X_SIA(i_y,i_x)+grad_eps2_Y_SIA(i_y,i_x)*grad_p_Y_SIA(i_y,i_x);
                
                %   Evolution of the SIA concentration
                
                C_SIA(i_y,i_x) = C_SIA(i_y,i_x)+((dXdY_SIA(i_y,i_x)+dYdX_SIA(i_y,i_x)+eps2_SIA(i_y,i_x)*lap_p_SIA(i_y,i_x)+scal_SIA - K_Annhilation*C_Vac(i_y,i_x)*C_SIA(i_y,i_x))*DT/TAU_SIA);
               
                %   Vac
                
                scal_Vac = grad_eps2_X_Vac(i_y,i_x)*grad_p_X_Vac(i_y,i_x)+grad_eps2_Y_Vac(i_y,i_x)*grad_p_Y_Vac(i_y,i_x);
               
                %   Evolution of the Vacancy concentration
                
                C_Vac(i_y,i_x) = C_Vac(i_y,i_x)+((dXdY_Vac(i_y,i_x)+dYdX_Vac(i_y,i_x)+eps2_Vac(i_y,i_x)*lap_p_Vac(i_y,i_x)+scal_Vac - K_Annhilation*C_Vac(i_y,i_x)*C_SIA(i_y,i_x))*DT/TAU_Vac);
               
                %   Calculating the combined simulation
                
                C_Total(i_y,i_x) = C_SIA(i_y,i_x) + C_Vac(i_y,i_x);
            end
        end
        
    else
        
        %	Matrix calculations
        
        for i_y = 1:NY
            for i_x = 1:NX
                
                %   SIA
                
                ip_SIA = mod(i_x,NX)+1;
                im_SIA = mod((NX+i_x-2),NX)+1;
                jp_SIA = mod(i_y,NY)+1;
                jm_SIA = mod((NY+i_y-2),NY)+1;
                grad_p_X_SIA(i_y,i_x) = ((C_SIA(i_y,ip_SIA) - C_SIA(i_y,im_SIA))/H);
                grad_p_Y_SIA(i_y,i_x) = ((C_SIA(jp_SIA,i_x) - C_SIA(jm_SIA,i_x))/H);
                lap_p_SIA(i_y,i_x) = (2.0*(C_SIA(i_y,ip_SIA)+C_SIA(i_y,im_SIA)+C_SIA(jp_SIA,i_x)+C_SIA(jm_SIA,i_x))+C_SIA(jp_SIA,ip_SIA)+C_SIA(jm_SIA,im_SIA)+C_SIA(jp_SIA,im_SIA)+C_SIA(jm_SIA,ip_SIA)-12.0*C_SIA(i_y,i_x))/(3.0*H*H);
                
                %   Vac
                
                ip_Vac = mod(i_x,NX)+1;
                im_Vac = mod((NX+i_x-2),NX)+1;
                jp_Vac = mod(i_y,NY)+1;
                jm_Vac = mod((NY+i_y-2),NY)+1;
                grad_p_X_Vac(i_y,i_x) = ((C_Vac(i_y,ip_Vac) - C_Vac(i_y,im_Vac))/H);
                grad_p_Y_Vac(i_y,i_x) = ((C_Vac(jp_Vac,i_x) - C_Vac(jm_Vac,i_x))/H);
                lap_p_Vac(i_y,i_x) = (2.0*(C_Vac(i_y,ip_Vac)+C_Vac(i_y,im_Vac)+C_Vac(jp_Vac,i_x)+C_Vac(jm_Vac,i_x))+C_Vac(jp_Vac,ip_Vac)+C_Vac(jm_Vac,im_Vac)+C_Vac(jp_Vac,im_Vac)+C_Vac(jm_Vac,ip_Vac)-12.0*C_Vac(i_y,i_x))/(3.0*H*H);
            end
        end
        
        for i_y = 1:NY
            for i_x = 1:NX
                
                %   SIA
                
                if (grad_p_X_SIA(i_y,i_x) == 0.0 && grad_p_Y_SIA(i_y,i_x) > 0.0)
                    angle_SIA(i_y,i_x) = 0.5*Pi;
                end
                
                if (grad_p_X_SIA(i_y,i_x) == 0.0 && grad_p_Y_SIA(i_y,i_x) <= 0.0)
                    angle_SIA(i_y,i_x) = -0.5*Pi;
                end
                
                if (grad_p_X_SIA(i_y,i_x) > 0.0 && grad_p_Y_SIA(i_y,i_x) > 0.0)
                    angle_SIA(i_y,i_x) = atan(grad_p_Y_SIA(i_y,i_x)/grad_p_X_SIA(i_y,i_x));
                end
                
                if (grad_p_X_SIA(i_y,i_x) > 0.0 && grad_p_Y_SIA(i_y,i_x) <= 0.0)
                    angle_SIA(i_y,i_x) = 2.0*Pi+atan(grad_p_Y_SIA(i_y,i_x)/grad_p_X_SIA(i_y,i_x));
                end
                
                if (grad_p_X_SIA(i_y,i_x) < 0.0)
                    angle_SIA(i_y,i_x) = Pi+atan(grad_p_Y_SIA(i_y,i_x)/grad_p_X_SIA(i_y,i_x));
                end
                
                %   Vac
                
                if (grad_p_X_Vac(i_y,i_x) == 0.0 && grad_p_Y_Vac(i_y,i_x) > 0.0)
                    angle_Vac(i_y,i_x) = 0.5*Pi;
                end
                
                if (grad_p_X_Vac(i_y,i_x) == 0.0 && grad_p_Y_Vac(i_y,i_x) <= 0.0)
                    angle_Vac(i_y,i_x) = -0.5*Pi;
                end
                
                if (grad_p_X_Vac(i_y,i_x) > 0.0 && grad_p_Y_Vac(i_y,i_x) > 0.0)
                    angle_Vac(i_y,i_x) = atan(grad_p_Y_Vac(i_y,i_x)/grad_p_X_Vac(i_y,i_x));
                end
                
                if (grad_p_X_Vac(i_y,i_x) > 0.0 && grad_p_Y_Vac(i_y,i_x) <= 0.0)
                    angle_Vac(i_y,i_x) = 2.0*Pi+atan(grad_p_Y_Vac(i_y,i_x)/grad_p_X_Vac(i_y,i_x));
                end
                
                if (grad_p_X_Vac(i_y,i_x) < 0.0)
                    angle_Vac(i_y,i_x) = Pi+atan(grad_p_Y_Vac(i_y,i_x)/grad_p_X_Vac(i_y,i_x));
                end
            end
        end
        
        for i_y = 1:NY
            for i_x = 1:NX
                
                %   SIA
                
                epsilon_SIA(i_y,i_x) = EPS_SIA*(1.0 + DELTA_SIA*cos(ANISO_SIA*(angle_SIA(i_y,i_x)-ANGLEO_SIA)));
                epsilon_prime_SIA(i_y,i_x) = -EPS_SIA*ANISO_SIA*DELTA_SIA*sin(ANISO_SIA*(angle_SIA(i_y,i_x)-ANGLEO_SIA));
                
                %   Vac
                
                epsilon_Vac(i_y,i_x) = EPS_Vac*(1.0 + DELTA_Vac*cos(ANISO_Vac*(angle_Vac(i_y,i_x)-ANGLEO_Vac)));
                epsilon_prime_Vac(i_y,i_x) = -EPS_Vac*ANISO_Vac*DELTA_Vac*sin(ANISO_Vac*(angle_Vac(i_y,i_x)-ANGLEO_Vac));
            end
        end
        
        for i_y = 1:NY
            for i_x = 1:NX
                
                %   SIA
                
                aY_SIA(i_y,i_x) = -epsilon_SIA(i_y,i_x)* epsilon_prime_SIA(i_y,i_x) * grad_p_Y_SIA(i_y,i_x);
                aX_SIA(i_y,i_x) = epsilon_SIA(i_y,i_x) * epsilon_prime_SIA(i_y,i_x) * grad_p_X_SIA(i_y,i_x);
                eps2_SIA(i_y,i_x) = epsilon_SIA(i_y,i_x) * epsilon_SIA(i_y,i_x);
              
                %   Vac
                
                aY_Vac(i_y,i_x) = -epsilon_Vac(i_y,i_x)* epsilon_prime_Vac(i_y,i_x) * grad_p_Y_Vac(i_y,i_x);
                aX_Vac(i_y,i_x) = epsilon_Vac(i_y,i_x) * epsilon_prime_Vac(i_y,i_x) * grad_p_X_Vac(i_y,i_x);
                eps2_Vac(i_y,i_x) = epsilon_Vac(i_y,i_x) * epsilon_Vac(i_y,i_x);
            end
        end
        
        for i_y = 1:NY
            for i_x = 1:NX
                
                %   SIA
                
                ip_SIA = mod(i_x,NX)+1;
                im_SIA = mod((NX+i_x-2),NX)+1;
                jp_SIA = mod(i_y,NY)+1;
                jm_SIA = mod((NY+i_y-2),NY)+1;
                dXdY_SIA(i_y,i_x) = (aY_SIA(i_y,ip_SIA)-aY_SIA(i_y,im_SIA))/H;
                dYdX_SIA(i_y,i_x) = (aX_SIA(jp_SIA,i_x)-aX_SIA(jm_SIA,i_x))/H;
                grad_eps2_X_SIA(i_y,i_x) = (eps2_SIA(i_y,ip_SIA)-eps2_SIA(i_y,im_SIA))/H;
                grad_eps2_Y_SIA(i_y,i_x) = (eps2_SIA(jp_SIA,i_x)-eps2_SIA(jm_SIA,i_x))/H;
               
                %   Vac
                
                ip_Vac = mod(i_x,NX)+1;
                im_Vac = mod((NX+i_x-2),NX)+1;
                jp_Vac = mod(i_y,NY)+1;
                jm_Vac = mod((NY+i_y-2),NY)+1;
                dXdY_Vac(i_y,i_x) = (aY_Vac(i_y,ip_Vac)-aY_Vac(i_y,im_Vac))/H;
                dYdX_Vac(i_y,i_x) = (aX_Vac(jp_Vac,i_x)-aX_Vac(jm_Vac,i_x))/H;
                grad_eps2_X_Vac(i_y,i_x) = (eps2_Vac(i_y,ip_Vac)-eps2_Vac(i_y,im_Vac))/H;
                grad_eps2_Y_Vac(i_y,i_x) = (eps2_Vac(jp_Vac,i_x)-eps2_Vac(jm_Vac,i_x))/H;
            end
        end
        
        for i_y = 1:NY
            for i_x = 1:NX
                
                %   SIA
                
                scal_SIA = grad_eps2_X_SIA(i_y,i_x)*grad_p_X_SIA(i_y,i_x)+grad_eps2_Y_SIA(i_y,i_x)*grad_p_Y_SIA(i_y,i_x);
                
                %   Evolution of the SIA concentration
                
                C_SIA(i_y,i_x) = C_SIA(i_y,i_x)+((dXdY_SIA(i_y,i_x)+dYdX_SIA(i_y,i_x)+eps2_SIA(i_y,i_x)*lap_p_SIA(i_y,i_x)+scal_SIA - K_Annhilation*C_Vac(i_y,i_x)*C_SIA(i_y,i_x))*DT/TAU_SIA);
               
                %   Vac
                
                scal_Vac = grad_eps2_X_Vac(i_y,i_x)*grad_p_X_Vac(i_y,i_x)+grad_eps2_Y_Vac(i_y,i_x)*grad_p_Y_Vac(i_y,i_x);
               
                %   Evolution of the Vacancy concentration
                
                C_Vac(i_y,i_x) = C_Vac(i_y,i_x)+((dXdY_Vac(i_y,i_x)+dYdX_Vac(i_y,i_x)+eps2_Vac(i_y,i_x)*lap_p_Vac(i_y,i_x)+scal_Vac - K_Annhilation*C_Vac(i_y,i_x)*C_SIA(i_y,i_x))*DT/TAU_Vac);
               
                %   Calculating the combined simulation
                
                C_Total(i_y,i_x) = C_SIA(i_y,i_x) + C_Vac(i_y,i_x);
            end
        end
    end
    
    figure(1)
        
    subplot(2,2,1)
    image(C_Total*50)
    colormap('Hot')
    set(gca,'Ydir','Normal')    %   Corrects the y-axis.
    title('Heat Map of C Total')
    
    subplot(2,2,2)
    image(C_Vac*50)
    set(gca,'Ydir','Normal')    %   Corrects the y-axis.
    title('Plot of C Vac')
    
    subplot(2,2,3)
    image(C_SIA*50)
    set(gca,'Ydir','Normal')    %   Corrects the y-axis.
    title('Plot of C SIA')
    
    drawnow
       
end