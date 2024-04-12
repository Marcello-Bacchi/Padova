# library from https://github.com/antonl/pyWinSpec
from winspec import SpeFile
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter import filedialog as fd

root = Tk()
root.withdraw()
fnames = fd.askopenfilenames(defaultextension='.SPE',parent=root)

for fname in fnames:   
    a = SpeFile(fname)
    wavel, spectrum = a.xaxis, np.array(a.data)
    np.savetxt(fname[:-4]+".csv",np.array([wavel, spectrum.flatten().T]), delimiter = ",")
