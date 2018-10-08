###############################################################################
# Progrom Discription :A simple machine-learning algorithm that uses a        #
# rule-based classifier to predict whether or not a particular patient has a  #
# coronary heart disease                                                      #
#                                                                             #
# Program written by : Thomas                                                 #
# Program written date: 06/07/2018                                            #
# Program Compatibility : Python 3.x                                          #
###############################################################################

############################## START  OF PROGRAM ##############################
from decimal import Decimal
import csv
import logging
import os

###############################################################################
#                          Variable Definitions
###############################################################################

patient_okcnt = 0
patient_tokcnt = 0
patient_illcnt = 0
patient_tillcnt = 0
patient_ok = list()
patient_tok = list()
patient_ill = list()
patient_till = list()
separator = list()
patient_flo_atr = []
test_patient = []
patient_cnt = 0
tstpat_illcnt = 0
eachlstcnt = 0
myoutput_data = []
trainname = "Training set: "
testname = "Test set: "

###################### End of Variable Definitions ############################

###############################################################################
#                            My Functions
###############################################################################

##################### Function to check file-open and validate ################

def openfilchk(filname):

    while True:
        fname = input(filname)
        if len(fname) < 1:
            print ("No File chosen. Please enter valid file name again")
            continue
        try:
            fh = open(fname)
        except IOError as e:
            logging.error(e)
            continue
        if os.path.getsize(fname) <= 2:
            print ("File is empty. Enter different file name")
            continue
        else:
            if os.path.getsize(fname) < 41:
                print ("File does not contain all attributes of patient")
                continue
        break
    return (fh)

##################### Function to Add all Patients attributes #################

def common(patient,count,patlist):
    count = count + 1
    if '?' in patlist:
        indx = patlist.index('?')
        patlist[indx] = 0
        i = 0
        for atr in patlist:
            patient[i] = round(((atr + patient[i])), 2)
            i = i + 1
    else:
        if count != 1:
            i = 0
            for atr in patlist:
                patient[i] = round(((atr + patient[i])), 2)
                i = i + 1
        else:
            for atr in patlist:
                patient.append(atr/count)

    return (patient,count)

##################### Function to Find Averages of Patients attributes ########

def avg(patients,cnt):
    i = 0
    for atr in patients:
        patients[i] = (atr/cnt)
        patients[i] = format((patients[i]), '.2f')
        i = i + 1
    return (patients,cnt)

##################### Function to calculate Separator values ##################

def separ(patnt1,patnt2):
    patavg = list()
    patnt1 = list(map(float, patnt1))
    patnt2 = list(map(float, patnt2))
    i = 0
    for itm in patnt1:
        patavg.append((patnt1[i] + patnt2[i])/2)
        patavg[i] = format((patavg[i]), '.2f')
        i = i + 1
    return (patavg)

##################### Function to read and handle file ########################

def filefunc(filena,cnts):
    for line in filena:
        line = line.strip()
        cnts= cnts + 1
        patient_str_atr = list(line.split(","))
        try:
            patient_flo_atr.append(list(map(float,patient_str_atr)))
            test_patient.append(list(map(float,patient_str_atr)))
        except ValueError:
            for item in patient_str_atr:
                if item == '?':
                    patient_flo_atr[cnts - 1].append(item)
                    test_patient[cnts - 1].append(item)
                else:
                    #patient_flo_atr.append(float(item))
                    if len(test_patient) != cnts:
                        test_patient.append([])
                        patient_flo_atr.append([])
                    patient_flo_atr[cnts - 1].append(float(item))
                    test_patient[cnts - 1].append(float(item))
    return(patient_flo_atr,test_patient)

######################## End of Functions #####################################

###############################################################################
############ Training Program to understand diagnosis of patients #############
###############################################################################

fh = openfilchk(trainname)
patient_flo_atr,test_patient = filefunc(fh,patient_cnt)

for eachlst in patient_flo_atr:
    if eachlst[13] == 0:
        patient_ok, patient_okcnt = common(patient_ok,patient_okcnt,eachlst)
    else:
        patient_ill, patient_illcnt = common(patient_ill,patient_illcnt,eachlst)

patient_ok.pop()
patient_ill.pop()
patient_ok,patient_okcnt = avg(patient_ok,patient_okcnt)
patient_ill,patient_illcnt = avg(patient_ill,patient_illcnt)

###############################################################################
############ Display the averages of Healthy and Ill Patients #################
###############################################################################

print ("Healthy Patient averages:")
print (','.join(patient_ok))
print ("Ill Patient averages:")
print (','.join(patient_ill))
separator = separ(patient_ok,patient_ill)
print ("Separator values:")
print (','.join(separator))

###############################################################################
############ Obtain Accuracy of results from diagonised patients ##############
###############################################################################

for eachlst in test_patient:
    eachlst.pop()
    i = 0
    tstpatatr = 0
    for eachitm in eachlst:
        if eachitm == '?':
            continue
        else:
            if eachitm > float(separator[i]) :
                tstpatatr = tstpatatr + 1
        i = i + 1
    if tstpatatr > 6:
        tstpat_illcnt = tstpat_illcnt + 1
    else:
        eachlstcnt = test_patient.index(eachlst) + 1

acur = tstpat_illcnt/patient_illcnt
print ("Accuracy: ", end="")
print (format((acur), '.2f'))

###############################################################################
## Use obtained diagnosis on another Test file containing patients attributes #
## and create an output file containing results of diagnosis                  #
###############################################################################

fh = openfilchk(testname)
del patient_flo_atr[:]
del test_patient[:]
patient_flo_atr = filefunc(fh,patient_cnt)

eachlstcnt = 0
for eachlst in test_patient:
    i = 0
    tstpatatr = 0
    for eachitm in eachlst:
        if eachitm == '?':
            continue
        else:
            if eachlst.index(eachitm) == 0:
                continue
            if eachitm > float(separator[i]) :
                tstpatatr = tstpatatr + 1
            i = i + 1
    if eachlstcnt == 0:
        myoutput_data.append(['id', 'disease?'])
    if tstpatatr > 6:
        tstpat_illcnt = tstpat_illcnt + 1
        myoutput_data.append([eachlst[0], 'yes'])
    else:
        myoutput_data.append([eachlst[0], 'no'])
    eachlstcnt = test_patient.index(eachlst) + 1

##################### Write all the saved values into Output File #############

with open('testout.csv', 'w', newline='') as csvfile:
    #fieldnames = ['first_name', 'last_name']
    writer = csv.writer(csvfile)
    writer.writerows(myoutput_data)

############################## END OF PROGRAM #################################
