import math as m
import numpy as np

class Diaphragm:
    
    def __init__(obj):
        obj.xdistances = np.array([])
        obj.zdistances = np.array([])
        obj.SWx = np.array([])
        obj.SWz = np.array([])
        obj.force_x = 0
        obj.force_z = 0
        obj.Lx = 0
        obj.Lz = 0
        
    def SWdistx(obj):
        size = len(obj.xdistances)-1
        obj.SWx = np.array(range(len(obj.xdistances)), dtype = 'd')
        Trib = np.array(range(len(obj.xdistances)), dtype = 'd')
        
        for i in range(len(obj.xdistances)):
            if i != 0 and i != size:
                Trib[i] =  obj.xdistances[i+1]/2 - obj.xdistances[i-1]/2
            elif i == 0:
                if obj.xdistances[i] == 0:
                    Trib[i] = (obj.xdistances[i+1])/2
                else:
                    Trib[i] = obj.xdistances[i] + (obj.xdistances[i+1] - obj.xdistances[i])/2
            else:
                Trib[i] = (obj.xdistances[i]-obj.xdistances[i-1])/2      
                if obj.xdistances[i] != obj.Lx:
                    addtrib = obj.Lx - sum(Trib)
                    Trib[i] = (obj.xdistances[i]-obj.xdistances[i-1])/2 + addtrib
                    
            obj.SWx[i] = (Trib[i]/obj.Lx)*obj.force_x
        
        sumx = sum(obj.SWx)
        sumTrib = sum(Trib)
        
        print("====== X DIRECTION RESULTS ======")
        if (sumx <= obj.force_x + 1.0 and sumx >= obj.force_x - 1) and (sumTrib <= obj.Lx + 1 and sumTrib >= obj.Lx - 1):
            print("Analysis completed successfully!")
            print("Lateral system forces are:", obj.SWx)
            print("Don't forget to add upper story and adjoining structure forces!")
        else:
            print("Fatal error occurred!")
            print("sumx=", sumx, "obj.force_x =", obj.force_x)
            print("sumTrib=", sumTrib, "obj.Lx =", obj.Lx)
        
    def SWdistz(obj):
        size = len(obj.zdistances)-1
        obj.SWz = np.array(range(len(obj.zdistances)), dtype = 'd')
        Trib = np.array(range(len(obj.zdistances)), dtype = 'd')
        
        for i in range(len(obj.zdistances)):
            if i != 0 and i != size:
                Trib[i] = obj.zdistances[i+1]/2 - obj.zdistances[i-1]/2
            elif i == 0:
                if obj.zdistances[i] == 0:
                    Trib[i] = (obj.zdistances[i+1])/2
                else:
                    Trib[i] = obj.zdistances[i] + (obj.zdistances[i+1] - obj.zdistances[i])/2
            else:
                Trib[i] = (obj.zdistances[i]-obj.zdistances[i-1])/2      
                if obj.zdistances[i] != obj.Lz:
                    addtrib = obj.Lz - sum(Trib)
                    Trib[i] = (obj.zdistances[i]-obj.zdistances[i-1])/2 + addtrib
       
            obj.SWz[i] = (Trib[i]/obj.Lz)*obj.force_z
        
        sumz = sum(obj.SWz)
        sumTrib = sum(Trib)
        
        print("====== Z DIRECTION RESULTS ======")
        if (sumz <= obj.force_z + 1.0 and sumz >= obj.force_z - 1) and (sumTrib <= obj.Lz + 1 and sumTrib >= obj.Lz - 1):
            print("Analysis completed successfully!")
            print("Lateral system forces are:", obj.SWz)
            print("Don't forget to add upper story and adjoining structure forces!")
        else:
            print("Fatal error occurred!")
            print("sumz=", sumz, "obj.force_z =", obj.force_z)
            print("sumTrib=", sumTrib, "obj.Lz =", obj.Lz)