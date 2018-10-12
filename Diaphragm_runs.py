import numpy as np
import Flexidia as flx

####ADULT BH MAIN FLOOR RUN
##dgm = flx.Diaphragm()
##dgm.xdistances = np.array([0,93.927,145.427,150.308,164.437])
##dgm.zdistances = np.array([0,12.8962,43.104,54.4375,68.6354])
##dgm.Lx = 165
##dgm.Lz = 77.5
##dgm.force_x = 48.43
##dgm.force_z = 20.55
##
##dgm.SWdistx(0)
##dgm.SWdistz(8.802)

####ADULT BH CLERESTORY RUN
##dgm = flx.Diaphragm()
##dgm.xdistances = np.array([0,51.5])
##dgm.zdistances = np.array([0])
##dgm.Lx = 51.5
##dgm.Lz = 51.5
##dgm.force_x = 3.40
##dgm.force_z = 3.40
##
##dgm.SWdistx(0)
##dgm.SWdistz(0)

####CHILD BH MAIN FLOOR RUN
##dgm = flx.Diaphragm()
##dgm.xdistances = np.array([0, 19.2604, 51.2604, 71.5312, 82])
##dgm.zdistances = np.array([0, 45.5628, 57.25, 65.865])
##dgm.Lx = 82
##dgm.Lz = 65.865
##dgm.force_x = 25.13
##dgm.force_z = 19.82
##
##dgm.SWdistx(0)
##dgm.SWdistz(0)

####CHILD BH CLERESTORY RUN
##dgm = flx.Diaphragm()
##dgm.xdistances = np.array([0,51.5])
##dgm.zdistances = np.array([0])
##dgm.Lx = 51.5
##dgm.Lz = 51.5
##dgm.force_x = 3.40
##dgm.force_z = 3.40
##
##dgm.SWdistx(0)
##dgm.SWdistz(0)

####FCF Southwest
##dgm = flx.Diaphragm()
##dgm.xdistances = np.array([22.4, 111.4])
##dgm.zdistances = np.array([9.833, 50.25])
##dgm.Lx = 111.4
##dgm.Lz = 86.58
##dgm.force_x = 15.5
##dgm.force_z = 15.5
##
##dgm.SWdistx()
##dgm.SWdistz()

##FCF Southeast
dgm = flx.Diaphragm()
dgm.xdistances = np.array([0, 71.666])
dgm.zdistances = np.array([13, 63])
dgm.Lx = 119.666
dgm.Lz = 89
dgm.force_x = 16.1
dgm.force_z = 16.1

dgm.SWdistx()
dgm.SWdistz()
##
####FCF North
##dgm = flx.Diaphragm()
##dgm.xdistances = np.array([0, 19.2604, 51.2604, 71.5312, 82])
##dgm.zdistances = np.array([0, 45.5628, 57.25, 65.865])
##dgm.Lx = 82
##dgm.Lz = 65.865
##dgm.force_x = 25.13
##dgm.force_z = 19.82
##
##dgm.SWdistx(0)
##dgm.SWdistz(0)