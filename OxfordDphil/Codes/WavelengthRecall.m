function T = WavelengthRecall(TABLE)

TableScenario = TABLE;

[col_val_Max,row_Max] = max(TableScenario.Wavenumber_i);

TempTableA = TableScenario{row_Max,:};

Root1 = TempTableA(6);
Root2 = TempTableA(7);
Root3 = TempTableA(8);
Root4 = TempTableA(9);

Wavenumber1Max = round(col_val_Max, 1);
Wavenumber1Max_Max = round((2*pi)/(Root1^0.5), 1);
Wavenumber1Max_Min = round((2*pi)/(Root2^0.5), 1);

Minima1Max = [' The Max of Minima 1 is: ' num2str(Wavenumber1Max) ' + ' num2str(Wavenumber1Max_Max) ' and - ' num2str(Wavenumber1Max_Min)];

[col_val_Min,row_Min] = min(TableScenario.Wavenumber_i);

TempTableB = TableScenario{row_Min,:};

Root1 = TempTableB(6);
Root2 = TempTableB(7);
Root3 = TempTableB(8);
Root4 = TempTableB(9);

Wavenumber1Min = round(col_val_Min, 1);
Wavenumber1Min_Max = round((2*pi)/(Root1^0.5), 1);
Wavenumber1Min_Min = round((2*pi)/(Root2^0.5), 1);

Minima1Min = [' The Min of Minima 1 is: ', num2str(Wavenumber1Min), ' + ', num2str(Wavenumber1Min_Max), ' and - ', num2str(Wavenumber1Min_Min)];

[col_val_Max,row_Max] = max(TableScenario.Wavenumber_ii);

TempTableC = TableScenario{row_Max,:};

Root1 = TempTableC(6);
Root2 = TempTableC(7);
Root3 = TempTableC(8);
Root4 = TempTableC(9);

Wavenumber2Max = round(col_val_Max, 1);
Wavenumber2Max_Max = round((2*pi)/(Root3^0.5), 1);
Wavenumber2Max_Min = round((2*pi)/(Root4^0.5), 1);

Minima2Max = [' The Max of Minima 2 is: ', num2str(Wavenumber2Max), ' + ', num2str(Wavenumber2Max_Max), ' and - ', num2str(Wavenumber2Max_Min)];

[col_val_Min,row_Min] = min(TableScenario.Wavenumber_ii);

TempTableD = TableScenario{row_Min,:};

Root1 = TempTableD(6);
Root2 = TempTableD(7);
Root3 = TempTableD(8);
Root4 = TempTableD(9);

Wavenumber2Min = round(col_val_Min, 1);
Wavenumber2Min_Max = round((2*pi)/(Root3^0.5), 1);
Wavenumber2Min_Min = round((2*pi)/(Root4^0.5), 1);

Minima2Min = [' The Min of Minima 2 is: ', num2str(Wavenumber2Min), ' + ', num2str(Wavenumber2Min_Max), ' and - ', num2str(Wavenumber2Min_Min)];

T = table(Wavenumber1Max, Wavenumber1Max_Max, Wavenumber1Max_Min, Wavenumber1Min, Wavenumber1Min_Max, Wavenumber1Min_Min, Wavenumber2Max, Wavenumber2Max_Max, Wavenumber2Max_Min, Wavenumber2Min, Wavenumber2Min_Max, Wavenumber2Min_Min);

end