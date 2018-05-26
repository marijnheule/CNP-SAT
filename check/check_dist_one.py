# Checking distance one proofs
# Daniela Ritirc
# 17.04.2018

# usage: python3 check_dist_one.py x.vtx x.edge 
# returns: x.singular
 
import os, sys
import string


command_line_args = sys.argv

# input files
if (len(command_line_args) != 3) :
  raise AttributeError("Two input files shall be given")

inputfile_vtx = command_line_args[1]
inputfile_edg = command_line_args[2]

# name output file
if inputfile_vtx.find('.')!= -1 :
  outputfile = inputfile_vtx[:inputfile_vtx.find('.')]

outputfile = outputfile + ".singular"

# read .vtx
f_read = open(inputfile_vtx,"r")
contents = f_read.read()

# Replace "Sqrt[x]" by variables 
contents = contents.replace('Sqrt[11/3]'   ,'s11*r3')
contents = contents.replace('/(2*Sqrt[3])' ,'/2*r3')
contents = contents.replace('/(3*Sqrt[3])' ,'/3*r3')
contents = contents.replace('/(4*Sqrt[3])' ,'/4*r3')
contents = contents.replace('/(6*Sqrt[3])' ,'/6*r3')
contents = contents.replace('/(8*Sqrt[3])' ,'/8*r3')
contents = contents.replace('/(12*Sqrt[3])','/12*r3')
contents = contents.replace('/(16*Sqrt[3])','/16*r3')
contents = contents.replace('/(18*Sqrt[3])','/18*r3')
contents = contents.replace('/(32*Sqrt[3])','/32*r3')
contents = contents.replace('/(36*Sqrt[3])','/36*r3')
contents = contents.replace('/(48*Sqrt[3])','/48*r3')
contents = contents.replace('/(96*Sqrt[3])','/96*r3')
contents = contents.replace('/Sqrt[3]'     ,'*r3')

contents = contents.replace('Sqrt[165]', 'Sqrt[3]*Sqrt[55]')
contents = contents.replace('Sqrt[33]' , 'Sqrt[3]*Sqrt[11]')
contents = contents.replace('Sqrt[55]' , 'Sqrt[5]*Sqrt[11]')
contents = contents.replace('Sqrt[15]' , 'Sqrt[3]*Sqrt[5]')
contents = contents.replace('Sqrt[3]'  , 's3')
contents = contents.replace('Sqrt[5]'  , 's5')
contents = contents.replace('Sqrt[11]' , 's11')
contents = contents.replace('\n' , '')
contents = contents.replace('{','')
contents = contents.replace(' ','')
contents = contents.replace('"','')

# store vertices in 2D list
vertices = contents.split('}')
coordinates = []
i=0
for line in vertices:
  coordinates.append([])
  coordinates[i] = [n for n in line.split(',')]
  i += 1

# write header of singular file
f_out = open(outputfile,"w")
f_out.write("monitor(\"results.out\",\"o\");\n")
f_out.write("ring R = 0, (r3,s11,s5,s3), lp;\n\n")
f_out.write(
  "ideal I = \n"
  "  s3 * r3 -1, \n "
  "  s11^2 - 11, \n "
  "  s5^2  -  5, \n "
  "  s3^2  -  3  \n "
  ";\n\n")

f_out.write("ideal J = groebner(I);\n\n") 

# print vertices as polynomials
for i in range(len(vertices)-1):
  f_out.write("poly p" + str(i+1) + "_x = " +  coordinates[i][0] + ";\n")
  f_out.write("poly p" + str(i+1) + "_y = " +  coordinates[i][1] + ";\n\n")

# read .edg as lines
f_read_edge = open(inputfile_edg,"r")
contents_edge = f_read_edge.readlines()
contents_edge = [x.strip() for x in contents_edge] 
del(contents_edge[0])

# print reduce command for each line
for line in contents_edge:
  f_out.write("// " + str(line) +"\n")
  # uncomment following line, then "e x y" is written in output file 
  # f_out.write("print(\" " + str(line) +"\");\n") 
  line = line.split(" ")
  f_out.write("reduce ( -1 + (p" + str(line[1]) + "_x "
              "- (p" + str(line[2]) + "_x))^2 "
              "+ (p" + str(line[1]) + "_y "
              "- (p" + str(line[2]) + "_y))^2, J);\n\n")
              

f_out.write("quit;")
f_out.close()

