import numpy as np
from skfuzzy import control as ctrl
from fuzzy_algo.trimf import trimf
from fuzzy_algo.trapmf import trapmf
import matplotlib.pyplot as plt

# Khởi tạo Universe (đầu vào và đầu ra)
capital_efficiency_ratio = ctrl.Antecedent(np.arange(0, 101, 1), 'Capital_Efficiency_Ratio')  # unit %
ROI = ctrl.Antecedent(np.arange(0, 101, 1), 'ROI') # unit %
IRR = ctrl.Antecedent(np.arange(0, 101, 1), 'IRR') # unit %

Efficiency = ctrl.Consequent(np.arange(0, 101, 1), 'Efficiency')

# Xác định các tập mờ và hàm thành viên cho Capital Efficiency Ratio
capital_efficiency_ratio['Low'] = trimf(capital_efficiency_ratio.universe, [0, 20, 40])
capital_efficiency_ratio['Medium'] = trimf(capital_efficiency_ratio.universe, [20, 40, 60])
capital_efficiency_ratio['High'] = trimf(capital_efficiency_ratio.universe, [40, 60, 100])

# Xác định các tập mờ và hàm thành viên cho ROI và IRR
ROI['Low'] = trapmf(ROI.universe, [0, 0, 5, 7])
ROI['Medium'] = trapmf(ROI.universe, [5, 7, 13, 15])
ROI['High'] = trapmf(ROI.universe, [13, 15, 20, 20])

IRR['Low'] = trimf(IRR.universe, [0, 25, 50])
IRR['Medium'] = trimf(IRR.universe, [25, 50, 75])
IRR['High'] = trimf(IRR.universe, [50, 75, 100])

# Xác định các tập mờ và hàm thành viên cho Efficiency
Efficiency['VeryLow'] = trimf(Efficiency.universe, [0, 20, 40])
Efficiency['Low'] = trimf(Efficiency.universe, [20, 40, 60])
Efficiency['Medium'] = trimf(Efficiency.universe, [40, 60, 80])
Efficiency['High'] = trimf(Efficiency.universe, [60, 80, 100])
Efficiency['VeryHigh'] = trimf(Efficiency.universe, [80, 100, 100])

# Xác định các quy tắc (IF-THEN) mờ
rule1 = ctrl.Rule(capital_efficiency_ratio['Low'] & ROI['Low'] & IRR['Low'], Efficiency['VeryLow'])
rule2 = ctrl.Rule(capital_efficiency_ratio['Low'] & ROI['Low'] & IRR['Medium'], Efficiency['VeryLow'])
rule3 = ctrl.Rule(capital_efficiency_ratio['Low'] & ROI['Low'] & IRR['High'], Efficiency['Low'])

rule4 = ctrl.Rule(capital_efficiency_ratio['Low'] & ROI['Medium'] & IRR['Low'], Efficiency['VeryLow'])
rule5 = ctrl.Rule(capital_efficiency_ratio['Low'] & ROI['Medium'] & IRR['Medium'], Efficiency['Medium'])
rule6 = ctrl.Rule(capital_efficiency_ratio['Low'] & ROI['Medium'] & IRR['High'], Efficiency['Medium'])

rule7 = ctrl.Rule(capital_efficiency_ratio['Low'] & ROI['High'] & IRR['Low'], Efficiency['Low'])
rule8 = ctrl.Rule(capital_efficiency_ratio['Low'] & ROI['High'] & IRR['Medium'], Efficiency['Medium'])
rule9 = ctrl.Rule(capital_efficiency_ratio['Low'] & ROI['High'] & IRR['High'], Efficiency['High'])

rule10 = ctrl.Rule(capital_efficiency_ratio['Medium'] & ROI['Low'] & IRR['Low'], Efficiency['VeryLow'])
rule11 = ctrl.Rule(capital_efficiency_ratio['Medium'] & ROI['Low'] & IRR['Medium'], Efficiency['Medium'])
rule12 = ctrl.Rule(capital_efficiency_ratio['Medium'] & ROI['Low'] & IRR['High'], Efficiency['Medium'])

rule13 = ctrl.Rule(capital_efficiency_ratio['Medium'] & ROI['Medium'] & IRR['Low'], Efficiency['Medium'])
rule14 = ctrl.Rule(capital_efficiency_ratio['Medium'] & ROI['Medium'] & IRR['Medium'], Efficiency['Medium'])
rule15 = ctrl.Rule(capital_efficiency_ratio['Medium'] & ROI['Medium'] & IRR['High'], Efficiency['High'])

rule16 = ctrl.Rule(capital_efficiency_ratio['Medium'] & ROI['High'] & IRR['Low'], Efficiency['Medium'])
rule17 = ctrl.Rule(capital_efficiency_ratio['Medium'] & ROI['High'] & IRR['Medium'], Efficiency['High'])
rule18 = ctrl.Rule(capital_efficiency_ratio['Medium'] & ROI['High'] & IRR['High'], Efficiency['VeryHigh'])

rule19 = ctrl.Rule(capital_efficiency_ratio['High'] & ROI['Low'] & IRR['Low'], Efficiency['Low'])
rule20 = ctrl.Rule(capital_efficiency_ratio['High'] & ROI['Low'] & IRR['Medium'], Efficiency['Medium'])
rule21 = ctrl.Rule(capital_efficiency_ratio['High'] & ROI['Low'] & IRR['High'], Efficiency['High'])

rule22 = ctrl.Rule(capital_efficiency_ratio['High'] & ROI['Medium'] & IRR['Low'], Efficiency['Medium'])
rule23 = ctrl.Rule(capital_efficiency_ratio['High'] & ROI['Medium'] & IRR['Medium'], Efficiency['High'])
rule24 = ctrl.Rule(capital_efficiency_ratio['High'] & ROI['Medium'] & IRR['High'], Efficiency['VeryHigh'])

rule25 = ctrl.Rule(capital_efficiency_ratio['High'] & ROI['High'] & IRR['Low'], Efficiency['High'])
rule26 = ctrl.Rule(capital_efficiency_ratio['High'] & ROI['High'] & IRR['Medium'], Efficiency['VeryHigh'])
rule27 = ctrl.Rule(capital_efficiency_ratio['High'] & ROI['High'] & IRR['High'], Efficiency['VeryHigh'])

# Tạo Control System và thêm các quy tắc vào đó
system = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
                             rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17,
                             rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25,
                             rule26, rule27])
evaluation = ctrl.ControlSystemSimulation(system)

# Gán giá trị đầu vào và tính toán
evaluation.input['Capital_Efficiency_Ratio'] = 25  # Giá trị của Capital Efficiency Ratio đầu vào (thay đổi giá trị này)
evaluation.input['ROI'] = 10  # Giá trị của ROI đầu vào (thay đổi giá trị này)
evaluation.input['IRR'] = 70  # Giá trị của IRR đầu vào (thay đổi giá trị này)

evaluation.compute()

# Hiển thị kết quả và biểu đồ
print("Efficiency:", evaluation.output['Efficiency'])

if (evaluation.output['Efficiency'] < 30):
    print('VeryLow')
elif (evaluation.output['Efficiency'] < 50):
    print('Low')
elif (evaluation.output['Efficiency'] < 70):
    print('Medium')
elif (evaluation.output['Efficiency'] < 90):
    print('High')
else:
    print('VeryHigh')

Efficiency.view(sim=evaluation)
capital_efficiency_ratio.view()
ROI.view()
IRR.view()
plt.show()
