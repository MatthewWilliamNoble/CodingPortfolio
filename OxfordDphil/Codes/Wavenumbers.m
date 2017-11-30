%%%%++++%%%%++++%%%%
%
%   Name:
%   Matthew W. Noble
%
%   Purpose:
%   Solve the determinant for its roots and turns and generate tables of the scenarios to
%   display that information.
%
%%%%++++%%%%++++%%%%

%%%%    Preamble

clc;    clear;  format long g;

%%%%    Initial conditions and parameters

% % General Testing
% Du = 2.5E1;  Dv = 1;  gamma_v = 1;  gamma_u = 1;    a = 0.005;

% % He into Cu @ 300 [K]
% Du = 1.45E17;  Dv = 4.85E5;  gamma_v = 1;  gamma_u = 1;    a = 2.5E0;

% % n into Mo @ 1193 [K]
% Du = 9.76E15;  Dv = 2.67E5;  gamma_v = 1;  gamma_u = 1;    a = 8E3;

% He into Au @ 293 [K]
Du = 1.45E17;  Dv = 4.48E4;  gamma_v = 1;  gamma_u = 1;    a = 5E2;

TableRawData = [];

Beginning_u = 0;  Ending_u = 1;  Stepping_u = 0.01;
Beginning_v = 0;  Ending_v = 1;  Stepping_v = 0.01;

%%%%    Solving the determinant

for ubar = Beginning_u:Stepping_u:Ending_u
    for vbar = Beginning_v:Stepping_v:Ending_v
        
        c = vbar*ubar*a;
        
        gv = 12*vbar*(vbar-1)+2;
        gu = 12*ubar*(ubar-1)+2;
        
        A = Dv*Du*gamma_u*gamma_v;
        B = Dv*Du*(gu*gamma_v + gv*gamma_u);
        C = Dv*Du*gv*gu + 2*a*(Dv*gamma_v*vbar + Du*gamma_u*ubar);
        D = 2*a*(Dv*vbar*gv + Du*ubar*gu);
        
        det = [A    B    C    D    0];
        ROOTS = roots(det);
        ROOTS = sort(ROOTS);
        Root1 = double(ROOTS(1));
        Root2 = double(ROOTS(2));
        Root3 = double(ROOTS(3));
        Root4 = double(ROOTS(4));
        
        dif_det = [4*A    3*B    2*C    D];
        TURNS = roots(dif_det);
        TURNS = sort(TURNS);
        Turn1 = double(TURNS(1));
        Turn2 = double(TURNS(2));
        Turn3 = double(TURNS(3));
        
        %   Temporary to populate the table
        
        Scenario = 0;
        
        Wavenumber_i = 0;
        Wavenumber_ii = 0;
        
        TableRawData = [TableRawData; table(ubar, vbar, Scenario, Wavenumber_i, Wavenumber_ii, Root1, Root2, Root3, Root4, Turn1, Turn2, Turn3)];
    end
end

%%%%    Defining Scenarios

for FilterTempVarA = 1:height(TableRawData)
    
    if TableRawData.Root1(FilterTempVarA)<0 && TableRawData.Root2(FilterTempVarA)<0 && TableRawData.Root3(FilterTempVarA)<0 && TableRawData.Root4(FilterTempVarA)==0 && isreal(TableRawData.Root1(FilterTempVarA))==1 && isreal(TableRawData.Root2(FilterTempVarA))==1 && isreal(TableRawData.Root3(FilterTempVarA))==1 && isreal(TableRawData.Root4(FilterTempVarA))==1
        TableRawData.Scenario(FilterTempVarA) = 1;
        
    elseif TableRawData.Root1(FilterTempVarA)<0 && TableRawData.Root2(FilterTempVarA)<0 && TableRawData.Root3(FilterTempVarA)==0 && TableRawData.Root4(FilterTempVarA)>0 && isreal(TableRawData.Root1(FilterTempVarA))==1 && isreal(TableRawData.Root2(FilterTempVarA))==1 && isreal(TableRawData.Root3(FilterTempVarA))==1 && isreal(TableRawData.Root4(FilterTempVarA))==1
        TableRawData.Scenario(FilterTempVarA) = 2;
        
    elseif TableRawData.Root1(FilterTempVarA)<0 && TableRawData.Root2(FilterTempVarA)==0 && TableRawData.Root3(FilterTempVarA)>0 && TableRawData.Root4(FilterTempVarA)>0 && isreal(TableRawData.Root1(FilterTempVarA))==1 && isreal(TableRawData.Root2(FilterTempVarA))==1 && isreal(TableRawData.Root3(FilterTempVarA))==1 && isreal(TableRawData.Root4(FilterTempVarA))==1
        TableRawData.Scenario(FilterTempVarA) = 3;
        
    elseif TableRawData.Root1(FilterTempVarA)==0 && TableRawData.Root2(FilterTempVarA)>0 && TableRawData.Root3(FilterTempVarA)>0 && TableRawData.Root4(FilterTempVarA)>0 && isreal(TableRawData.Root1(FilterTempVarA))==1 && isreal(TableRawData.Root2(FilterTempVarA))==1 && isreal(TableRawData.Root3(FilterTempVarA))==1 && isreal(TableRawData.Root4(FilterTempVarA))==1
        TableRawData.Scenario(FilterTempVarA) = 4;
        
    else
        TableRawData.Scenario(FilterTempVarA) = 0;
        
    end
    
end

%%%%    Calculate Wavelengths

for FilterTempVarB = 1:height(TableRawData)
    
    Turn1 = TableRawData.Turn1(FilterTempVarB);
    Turn2 = TableRawData.Turn2(FilterTempVarB);
    Turn3 = TableRawData.Turn3(FilterTempVarB);
    
    TableRawData.Wavenumber_i(FilterTempVarB) = (2*pi)/(Turn1^0.5);
    TableRawData.Wavenumber_ii(FilterTempVarB) = (2*pi)/(Turn3^0.5);
    
end

%%%%	Generate scenario tables

%%%%    Scenario 0
TableScenario0 = TableRawData;
TempTableB = [];
for FilterTempVarC = 1:height(TableScenario0)
    
    if TableScenario0.Scenario(FilterTempVarC) ~= 0
        TempTableB = [TempTableB;FilterTempVarC];
    end
    
end
TableScenario0(TempTableB,:) = [];

%%%%    Scenario 1
TableScenario1 = TableRawData;
TempTableB = [];
for FilterTempVarC = 1:height(TableScenario1)
    
    if TableScenario1.Scenario(FilterTempVarC) ~= 1
        TempTableB = [TempTableB;FilterTempVarC];
    end
    
end
TableScenario1(TempTableB,:) = [];

%%%%    Scenario2
TableScenario2 = TableRawData;
TempTableB = [];
for FilterTempVarC = 1:height(TableScenario2)
    
    if TableScenario2.Scenario(FilterTempVarC) ~= 2
        TempTableB = [TempTableB;FilterTempVarC];
    end
    
end
TableScenario2(TempTableB,:) = [];

%%%%    Scenario 3
TableScenario3 = TableRawData;
TempTableB = [];
for FilterTempVarC = 1:height(TableScenario3)
    
    if TableScenario3.Scenario(FilterTempVarC) ~= 3
        TempTableB = [TempTableB;FilterTempVarC];
    end
    
end
TableScenario3(TempTableB,:) = [];

%%%%    Scenario 4
TableScenario4 = TableRawData;
TempTableB = [];
for FilterTempVarC = 1:height(TableScenario4)
    
    if TableScenario4.Scenario(FilterTempVarC) ~= 4
        TempTableB = [TempTableB;FilterTempVarC];
    end
    
end
TableScenario4(TempTableB,:) = [];


% %%%%    Sorting the raw data for the other scenarios
% TableScenarioX = TableRawData;
% TempTableB = [];
% for FilterTempVarC = 1:height(TableScenarioX)
%     
%     if isreal(TableScenarioX.Root1(FilterTempVarC))==0 || isreal(TableScenarioX.Root2(FilterTempVarC))==0
%         TempTableB = [TempTableB;FilterTempVarC];
%     end
%     
% end
% TableScenarioX(TempTableB,:) = [];
% 
% TempTableB = [];
% for FilterTempVarC = 1:height(TableScenarioX)
%     
%     if isreal(TableScenarioX.Wavenumber_i(FilterTempVarC))==0
%         TempTableB = [TempTableB;FilterTempVarC];
%     end
%     
% end
% TableScenarioX(TempTableB,:) = [];
% 
% WavelengthRecall(TableScenarioX)
%%%%    Sorting the raw data for the other scenarios

TableScenarioX = TableScenario0;
TempTableB = [];
for FilterTempVarC = 1:height(TableScenarioX)
    
    if isreal(TableScenarioX.Root1(FilterTempVarC))==0 || isreal(TableScenarioX.Root2(FilterTempVarC))==0
        TempTableB = [TempTableB;FilterTempVarC];
    end
    
end
TableScenarioX(TempTableB,:) = [];

TempTableB = [];
for FilterTempVarC = 1:height(TableScenarioX)
    
    if isreal(TableScenarioX.Wavenumber_i(FilterTempVarC))==0
        TempTableB = [TempTableB;FilterTempVarC];
    end
    
end
TableScenarioX(TempTableB,:) = [];

% WavelengthRecall(TableScenario2)
% WavelengthRecall(TableScenario3)
% WavelengthRecall(TableScenarioX)

TableScenarioY = TableScenario0;
TempTableB = [];
for FilterTempVarC = 1:height(TableScenarioY)
    
    if isreal(TableScenarioY.Turn1(FilterTempVarC))==0 || isreal(TableScenarioY.Turn2(FilterTempVarC))==0 || isreal(TableScenarioY.Turn3(FilterTempVarC))==0
        TempTableB = [TempTableB;FilterTempVarC];
    end
    
end
TableScenarioY(TempTableB,:) = [];

TempTableB = [];
for FilterTempVarC = 1:height(TableScenarioY)
    
    if isreal(TableScenarioY.Root1(FilterTempVarC))==0 || isreal(TableScenarioY.Root2(FilterTempVarC))==0
        TempTableB = [TempTableB;FilterTempVarC];
    end
    
end
TableScenarioY(TempTableB,:) = [];

TempTableB = [];
for FilterTempVarC = 1:height(TableScenarioY)
    
    if TableScenarioY.Turn1(FilterTempVarC)<0 || TableScenarioY.Turn2(FilterTempVarC)<0 || TableScenarioY.Turn3(FilterTempVarC)<0
        TempTableB = [TempTableB;FilterTempVarC];
    end
    
end
TableScenarioY(TempTableB,:) = [];

% TempTableB = [];
% for FilterTempVarC = 1:height(TableScenarioY)
%     
%     if isreal(TableScenarioY.Wavenumber_i(FilterTempVarC))==0
%         TempTableB = [TempTableB;FilterTempVarC];
%     end
%     
% end
% TableScenarioY(TempTableB,:) = [];

TableScenarioY

