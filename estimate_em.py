#!usr/bin/env python3

import os
#import glob
import pprint
import astropy.io.fits
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import openpyxl

df = pd.read_excel('/Users/u_tsubasa/Dropbox/T_Umetani_work/for_doctor/doctor_target.xlsx',sheet_name="light_curve")
