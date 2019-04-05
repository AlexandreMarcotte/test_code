from control import TransferFunction, zero, pole

sys = TransferFunction(1, [1, 1])
poles = pole(sys)
print(poles)


import control


control.pzmap(sys)