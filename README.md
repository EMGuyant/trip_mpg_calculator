# Multi-Leg Trip MPG Calculations

Program that takes an input CSV file (Leg, Odometer (mi), Gas (gal used)) and calculates the miles traveled each leg, total trip miles, MPG for each leg, and MPG for the total trip. The program reads and processes the input data and provides the user an option to print results to the screen or generate an output CSV with results. If a output file is generated there is the additional option to open the file if desired after it has been created. This project was completed as
part of a Python course and is not maintained (Archived 10/15/21).

## USAGE
### Program uses python libraries: 
 * csv - read and write CSV file 
 * os.startfile - optional opening of outputfile
 * tkinter (Tk and .filedialog) - Open file and Save As file Dialog boxes

### Steps to Run:
1) Import MPGCalculator
2) Call the multi_leg_mpg() function from MPGCalulator
3) When prompted select the input file
4) When prompted choose whether to print results to screen ('n') or to an output file ('y')
5) If printed to screen you will see:
   * For Each Leg
     >During \<LEG NAME> of your trip you travled \<MILES TRAVELED> miles using /\<GALLONS USED> gallons of gas. Your fuel efficiency was \<MPG> MPG."
    * Final Total Trip
    >"You traveled a total of \<MILES TRAVELED> miles using \<GALLONS USED> gallons of gas on your mulit-leg trip. Your overall fuel efficiency was \<MPG> MPG."
6) If printed to output file (nothing will be printed to screen)
    * All result data will be printed to the output file you selected. After creation of the file you will be prompted to whether you would like to open ('y') the file or not ('n').

## INPUT FILE:
Program reads an input CSV file with the Leg, Odometer (mi), and Gas (gal used).
* Leg - Defines the Name of the Leg on the Multi-Leg Trip
* Odometer (mi) - Odometer reading at the end of each leg (first record is Starting Odometer reading)
* Gas (gal used) - Gallons of gas used to travel that leg (first record is 0 - Starting)
  >Leg,Odometer (mi), Gas (gal used)   
  Starting,######,0.0   
  Leg 1,#####,###
  .....
* Example file Input_RoadTripData.csv provided

## OPTIONAL OUTPUT FILE:
Program has the option to create an output file with the Leg name, miles traveld, gallons used, and MPG or print results to the screen.
* If an Output file is generated the user has the option to select an already exsisting file or in the dialog box enter a name for a newly created file (or keep default naming).
  * Leg - Defines the name of the Leg on the Multi-Leg Trip
  * Miles Traveled - Calculated difference of leg ending odometer reading and the previous reading
  * Gallons Used - Amount of gas used to travel that laeg
  * MPG - (End Odometer Miles - Start Odometer Miles)/Gallons of Gas Used
  >Leg,Miles Traveled,Gallons Used, MPG   
  Leg 1,###,##.##,##.#  
  Leg 2,###,##.##,##.#
  .....