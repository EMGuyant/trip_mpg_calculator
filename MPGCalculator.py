#Description of Program - Multi Leg Trip MPG Calculations
#-------------------------------------------------------------------------------------#
#Program that takes an input CSV file (Leg, Odometer (mi), Gas (gal used)) and
#   calculates the miles traveled each leg, total trip miles, MPG for each leg, and
#   MPG for the total trip. The program reads and processes the input data and provides the 
#   user an option to print results to the screen or generate an output CSV with results.
#   If a output file is generated there is the additional option to open the file if desired
#   after it has been created.
#
#INPUT FILE:
#Program reads an input CSV file with the Leg, Odometer (mi), and Gas (gal used).
#   Leg - Defines the Name of the Leg on the Multi-Leg Trip
#   Odometer (mi) - Odometer reading at the end of each leg (first record is Starting Odometer reading)
#   Gas (gal used) - Gallons of gas used to travel that leg (first record is 0 - Starting)
#       Leg,Odometer (mi), Gas (gal used)
#       Starting,######,0.0
#       Leg 1,#####,###
#       .....
#   Example file Input_RoadTripData.csv provided
#
#OPTIONAL OUTPUT FILE:
#Program has the option to create an output file with the Leg name, miles traveld, gallons used, and MPG or print results to the screen.
#   If an Output file is generated the user has the option to select an already exsisting file or
#   in the dialog box enter a name for a newly created file (or keep default naming).
#
#   Leg - Defines the name of the Leg on the Multi-Leg Trip
#   Miles Traveled - Calculated difference of leg ending odometer reading and the previous reading
#   Gallons Used - Amount of gas used to travel that laeg
#   MPG - (End Odometer Miles - Start Odometer Miles)/Gallons of Gas Used
#       Leg,Miles Traveled,Gallons Used, MPG
#       Leg 1,###,##.##,##.#
#       Leg 2,###,##.##,##.#
#       .....
#
#RUN THE PROGRAM
#Program uses python libraries: 
#   csv - read and write CSV file 
#   os.startfile - optional opening of outputfile
#   tkinter (Tk and .filedialog) - Open file and Save As file Dialog boxes
#Steps to Run:
#  1) Import MPGCalculator
#  2) Call the multi_leg_mpg() function from MPGCalulator
#  3) When prompted select the input file
#  4) When prompted choose whether to print results to screen ('n') or to an output file ('y')
#  5a) If printed to screen you will see:
#       For Each Leg
#           "During <LEG NAME> of your trip you travled <MILES TRAVELED> miles using 
#           <GALLONS USED> gallons of gas. Your fuel efficiency was <MPG> MPG."
#       Final Total Trip
#           "You traveled a total of <MILES TRAVELED> miles using <GALLONS USED> gallons
#           of gas on your mulit-leg trip. Your overall fuel efficiency was <MPG> MPG."
#   5b)If printed to output file (nothing will be printed to screen)
#       All result data will be printed to the output file you selected. After creation
#       of the file you will be prompted to whether you would like to open ('y') the file or not ('n').
#-------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------#
import csv #Input/Output Files are CSV files
from os import startfile #Handles option of open Output CSV file
#import tkinter dialogs for selecting input and creating output files
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
#hide tkinter.Tk main window
Tk().wm_withdraw()

#-------------------------------------------------------------------------------------#
def multi_leg_mpg():
    print('ESTIMATE FUEL EFFICIENCY FOR A MULTI-LEG ROADTRIP')

    # Selection of Required Input File
    print('\nNavigate to and Select the Input file.')
    infileName = askopenfilename(title='Select the Input File', 
                                filetypes=(('CVS Files', '*.csv'),))
    #Verify a File was Selected
    if infileName == '':
        print('User Canceled.')
        quit() #Program cannot be ran with out an input file

    # Optional Output File -- if No results will print to Screen
    print('\nWould you like to save the fuel efficiency estimates to an Output File? \n  If No, results will be printed to the screen.')
    #Decision structure dependent on user input being 'y' or 'n' to correctly function
    #Verify the user input is one of these options
    outputFile_YN = verifyAnswer()
    #Sets outputfileName if the creation of and Output file is chosen
    if outputFile_YN == 'y':
        outfileName = outputSelection()

        if outfileName == '':
            print('User Canceled')
            quit() #If output to file selected program requires a output file to be created or selected

        #Process input for Output File Generation
        outData = processInput(infileName, outfileName=outfileName)
        #Write the output file
        writeOutput(outfileName, outData)
        #Option to open output file
        print('\nThe output file  has been created do you wish to open it?')
        openFile_YN = verifyAnswer()
        if openFile_YN == 'y':
            startfile(outfileName)

    elif outputFile_YN == 'n':
               
        #Process input for Screen Output of Results
        processInput(infileName)

#-----------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------#
# Read and Process Input File        
def processInput(infileName, outfileName=''):
    #Open and read Input CSV to tripData variable
    with open(infileName) as in_csv:
        infile = csv.reader(in_csv, delimiter = ',')
        tripData = list(infile)
    #Input file requires at minimum 4 rows (1:headers, 2:starting information, 3-n:at least two destinations)
    if len(tripData) < 4:
        print('\nThe input file must contain a starting mileage and at least 2 other entries to be a multi-leg trip.')
        quit()

    #Initiate MPGData List to append to if Creation of Output file is selected
    if outfileName != '':
        MPGData = [['Leg', 'Miles Traveled', 'Gallons Used', 'MPG']]
    else: 
        MPGData = []

    #Iterate through tripData to calculate
    #   Each leg Miles Traveled, Gallons of Gas used, and MGP
    #   Total Trip Miles Traveled, Gallons of Gas used, and MPG
    tripStartMiles = 0.0
    tripEndMiles = 0.0
    totalgals = 0.0

    #start = 1 do not need to process header row (=0)
    #current_row range to Length tripData - 1 so ahead_row does not go out of range
    for current_row in range (1, len(tripData)-1): 
        #Set ahead_row variable to get the odometer reading and gallons used to get
        #   to next destination
        ahead_row = current_row + 1

        #Deine trip Starting/Ending miles (used for total miles & MPG)
        if current_row == 1:
            tripStartMiles = float(tripData[current_row][1])
        elif ahead_row == len(tripData) - 1: 
            tripEndMiles = float(tripData[ahead_row][1])
       
        #Leg starting miles
        startMiles = float(tripData[current_row][1])
        #Leg ending miles
        endMiles = float(tripData[ahead_row][1])
        #Leg gallons used
        galUsed = float(tripData[ahead_row][2])
        #Leg Name
        endLocation = tripData[ahead_row][0]

        #Call to MPGCalc Function
        MPGCalc(startMiles, endMiles, galUsed, MPGData, outfileName, endloc = endLocation)
        
        #Accumluate total gallons used
        totalgals = round(totalgals + galUsed, 2)
    
    #Call to MPGCalc Function set tripTotal = True
    listMPG = MPGCalc(tripStartMiles, tripEndMiles, totalgals, MPGData, outfileName, tripTotal=True)

    return listMPG
#------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------#
# Ensure the User Input 'y' or 'n' to avoid errounous determinations
def verifyAnswer(YN_verify=False):
    userInput_YN = input ('    Enter (y) for Yes or (n) for No: ')

    while YN_verify == False:
        if userInput_YN == 'y' or userInput_YN == 'n':
            YN_verify = True
        else:
            userInput_YN = input('    Enter (y) for Yes or (n) for No: ')
            continue
    
    return userInput_YN
#------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------#
# If User opts to generate output file open dialog box for seletion or create of outfile
def outputSelection():
    print('\nNavigate to where you would like the output saved and enter or keep default name for the new file, then Save.')
    outfileSelected = asksaveasfilename(title='Create Output File', 
                                        filetypes=(('CSV Files', '*.csv'),),
                                        defaultextension='.csv',
                                        initialfile='DefaultOutputFileName')
    return outfileSelected
#------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------#
#MPG Calculation
#Positional Arguments
#   start - Starting Odometer reading 
#   end - Ending Odometer reading
#   gal - Gallons used to get from start to end
#Keywork/Optional Arguments
#   output - Default = '' IF Output generation is needed pass outputfileName
#   endloc - Default = 'Trip Total' If location other than Total pass location name
#   tripTotal - Default = False If no Output file is generaated set to True to get 
#       Trip Total  message to print to scree
def MPGCalc(start, end, gal, MPGData, output, endloc='Trip Total', tripTotal=False):
    MPG = round((end - start)/gal,1)

    if output != '':
        MPGData.append([endloc, end-start, gal, MPG])
    elif tripTotal == False and output == '':
        print('\nDuring ' + endloc + ' of your trip you traveled ' + str(end - start) 
            + ' miles using ' + str(gal) + ' gallons of gas. \n  Your fuel efficiency was ' 
            + str(MPG) + ' MPG.')    
    elif tripTotal == True and output == '':
        print('\nYou traveled a total of ' + str(end - start) + ' miles using ' + str(gal) 
            + ' gallons of gas on your multi-leg trip. \n  Your overall fuel efficiency was ' 
            + str(MPG) + ' MPG.')

    return MPGData
#------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------#
# Write Output File if User chose to output to file
def writeOutput(outfile, data):
    with open(outfile, 'w', newline='') as out_file:
        outfile = csv.writer(out_file, delimiter=',')
        for row in range(len(data)):
            outfile.writerow(data[row])
#------------------------------------------------------------------------------------#

multi_leg_mpg()