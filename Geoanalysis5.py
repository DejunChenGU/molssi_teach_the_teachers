#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
Geometry Analysis for bond length

"""
import numpy
import os
import sys # function to convert code to execute on file name, return a list

def open_xyz(filename):
    """
    Write a function that read in and process an xyz file: open_xyz
    Input: filename
    Output: symbol and coordinate
    
    """
    xyzfile = numpy.genfromtxt(fname=filename, dtype='unicode', skip_header=2)
    symbol = xyzfile[:, 0]
    coordinate = xyzfile[:,1:]
    coordinate = coordinate.astype(numpy.float)
    #print(symbols)
    #print(coordinates)
    
    return symbol, coordinate

def bond_check(distance, minimum_length=0, maximum_length=1.5):
    """
    check and see if the distance(input) is between minmum_length(input, default=0) and maximum_length(input, default=1.5) 
    in Anstroms. Return True or False
    
    """
    if distance <= 0:
        raise ValueError('bond length of {distance} must not be 0 or negative value. Check your input.')
        
    if distance > minimum_length and distance < maximum_length:
        return True
    else: 
        return False

def calculate_distance(atom1_coord, atom2_coord): 
    """
    
    Add help file here: This function takes the coordinates of two atoms(Input) and calculate the distance of these two 
    atoms: atom1_coord, atom2_coord
    return: distance
    
    """
    x_distance = atom1_coord[0] - atom2_coord[0] # must use the input
    y_distance = atom1_coord[1] - atom2_coord[1]
    z_distance = atom1_coord[2] - atom2_coord[2]
    distance = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return distance # may return sth you calculated 

if __name__=="__main__":

    #file_location = os.path.join('water.xyz')
    if len(sys.argv) < 2:
        raise NameError("Incorrect Input, please specify a xyz file to be analysis!") #raise is going to break the whole code

    print(F'Running {sys.argv[0]}.')
    file_location = sys.argv[1] # python name.py file.xyz: name.py=sys.argv[0], file.xyz=sys.argv[1]

    symbols, coord = open_xyz(file_location)
    num_atoms = len(symbols)

    for num1 in range(0, num_atoms): # range(start, end) ___ not include end
        for num2 in range(0, num_atoms):
            if num1<num2:
                bond_length_12 = calculate_distance(coord[num1], coord[num2])
                if bond_check(bond_length_12) is True: # exclude the atom to the same atom by >0
                    print(F'{symbols[num1]} to {symbols[num2]} : {bond_length_12:.3f}')


# In[ ]:




