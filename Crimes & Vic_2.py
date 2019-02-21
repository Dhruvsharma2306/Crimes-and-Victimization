'''COSC 480 Project - Demographic Analysis for Crimes and Victimisations in New Zealand 

Use cases discussed - Crimes classified by Offenders Sex, Ethnicity, Crime Type and Age Group, grouped by Year and Months.
                    - Victimisations (number of people affected by the crime) classified by Crime Type, Area unit, Territorial Authority,
                      Occurence hour of the day, Occurence day of the week, grouped by Year and Months.

Author - Dhruv Sharma
Last Updated Date - May 27,2018
'''

import pandas as pd # Data management Library
import numpy # For Numerical functions


def colstats(data_file, column1):
    """ Function to display column statistics"""
    print("***********************************************")
    print("Column Statistics for : " + str(column1))
    print("=============================================") 
    return data_file[column1].describe()

       
def crosstab(data_file, column1, column2):
    """Crosstable"""
    print("***********************************************")
    print("Cross table between "+ column1+" and "+ column2)
    print("=============================================") 
    return data_file.groupby([column1])[column2].count()


def barplots(data_file, column1, column2):
    """Creates Bar Plots"""
    print("***********************************************")
    print("Bar Plot analysis for "+column1+ "for count of "+column2)
    print("=============================================")    
    print("Note - Only Top 10 values displayed")
    data_file.groupby(column1).sum().sort_values(column2, ascending=False).head(10).plot(y=column2, kind='bar',rot=25, grid=False)

        
def piecharts(data_file, column1, column2):
    """Function to creating factor plot"""
    print("***********************************************")
    print("Pie chart analysis for "+column1+ "for count of "+column2)
    print("=============================================") 
    print("Note - Only Top 10 values displayed")
    data_file.groupby(column1).sum().sort_values(column2, ascending=False).head(10).plot(y=column2, kind='pie', fontsize=8 , shadow=False)
    
    
def offender_stats():
    """ Retrieves analysis for offender Demographics """
    data_file1 = pd.read_csv('Offender_Demographics.csv')
    data_file1.groupby(['Ethnic Group']).sum().plot(y='Number of Crime', kind='bar', fontsize=8 ,rot=45, grid=False,title="Crimes by Ethnic Group")
    data_file1.groupby(['Year', 'SEX']).sum().unstack().plot(y='Number of Crime', kind='bar',rot=45, grid=False,title="Crimes by Year and Sex")
    data_file1.groupby(['Age Group']).sum().plot(y='Number of Crime', kind='pie', fontsize=8 ,title="Crimes by Age Group" )
    
    
def victimisations_stats():
    """ Retrieves analysis for Victimisations Time and Place """
    data_file = pd.read_csv('Victimisation Time and Place.csv')
    data_file.groupby('Locn Type Division').sum().plot(y='Victimisations', kind='bar',rot=0, grid=False,title="Victimisations by Location type division")
    data_file.groupby('Occurrence Hour Of Day').sum().plot(y='Victimisations', kind='bar',rot=0, grid=False,title="Victimisations by Occurence hour of the day")
    data_file.groupby('Occurrence Day Of Week').sum().plot(y='Victimisations', kind='bar',rot=0, grid=False,title="Victimisations by Occurence day of the Week")
    data_file.groupby('Year Month').sum().plot(y='Victimisations', kind='bar',rot=45, grid=False,title="Victimisations by Year Month")    
    data_file.groupby('Location Type').sum().sort_values('Victimisations', ascending=False).head(10).plot(y='Victimisations', kind='bar',rot=10, grid=False,title="Top by Victimisations by Location Type") 
    data_file.groupby('Territorial Authority').sum().sort_values('Victimisations', ascending=False).head(10).plot(y='Victimisations', kind='pie', fontsize=8 , shadow=False,title="Top 10 Victimisations by Territorial Authority")
    
    
def adhoc_function_call(filename):
    """ Retrieves information for Adhoc User requests """
    try:
        print("\nFor analysis of Offender Demographics - X variables could be any one of the following - \nAge Group,Ethnic Group, Mop Division, Mop Group, SEX, ANZSOC Division, Year Month \nY Variables could be any one of the following - \nNumber of Crime, Proceedings")
        print("\nFor analysis of Victimisations Time and Place - X variables could be any one of the following -\nAnzsoc Division, Area Unit, Locn Type Division, Occurrence Day Of Week, Occurrence Hour Of Day, Territorial Authority, Year Month \nY Variables could be- Victimisations\n")        
        column1 = input("Enter X variable: ")
        column2 = input("Enter Y variable: ")    
        data_file = pd.read_csv(filename)
        colstats_output= colstats(data_file, column1)
        print(colstats_output)
        crosstab_output = crosstab(data_file,column1, column2)
        print(crosstab_output)
        barplots(data_file, column1, column2)
        piecharts(data_file, column1, column2)
    except KeyError:
        print("Please enter valid X and Y variable entry")


def main():
    """main function to call other functions"""
    while True:
        print("=============================================")
        print("Enter 1 to see Offender Demographics Analysis \nEnter 2 to see Victimizations Time and Place Analysis \nEnter 3 to do Adhoc Analysis \nEnter q to exit")
        print("=============================================")
        step_number = input("Your Option - ") 
        if step_number == str(3):
            try:
                print("Adhoc Analysis ")
                print("=============================================")
                print("Enter the File Name Number to Read from the below options: \n1. Victimisation Time and Place.csv \n2. Offender_Demographics.csv ")
                filename_input = input("Your Option: ")
                if filename_input == str(1):
                    filename = 'Victimisation Time and Place.csv'
                elif filename_input == str(2):
                    filename = 'Offender_Demographics.csv'
                adhoc_function_call(filename)
            except UnboundLocalError:
                print(" Enter either of 1 or 2 only")
        elif step_number == str(1):
            print("Analysis for Offender Demographics ")
            print("=============================================")
            offender_stats()
        elif step_number == str(2):
            print("Analysis for Victimizations Time and Place")
            print("=============================================")
            victimisations_stats()
        elif  step_number == 'q':
            break
        else:
            print("Enter 1, 2 or 3 only")

 
main()   
        
    








    
    
