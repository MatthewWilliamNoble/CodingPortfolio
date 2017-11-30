function NewTable = WavelengthRecallDouble(TABLE, Max, Min)

TableScenario = TABLE;

%%%%    Filtering for LARGE wavelength
TempTableA = [];
for FilterTempVarA = 1:height(TableScenario)
    
    if TableScenario.Wavenumber_i(FilterTempVarA) <= Max*0.975
        TempTableA = [TempTableA;FilterTempVarA];
    elseif TableScenario.Wavenumber_i(FilterTempVarA) >= Max*1.025
        TempTableA = [TempTableA;FilterTempVarA];
    end
    
end
TableScenario(TempTableA,:) = [];

Min = 20;

%%%%    Cross-filtering for SMALL wavelength
TempTableB = [];
TableScenario = TableScenario4;
for FilterTempVarB = 1:height(TableScenario)
    
    if TableScenario.Wavenumber_ii(FilterTempVarB) <= Min*0.975
        TempTableB = [TempTableB;FilterTempVarB];
    elseif TableScenario.Wavenumber_ii(FilterTempVarB) >= Min*1.025
        TempTableB = [TempTableB;FilterTempVarB];
    end
    
end
TableScenario(TempTableB,:) = [];

[col_val_Max,row_Max] = max(TableScenario.Wavenumber_i);

TempTableA = TableScenario{row_Max,:}

NewTable = TableScenario;

end