'''
DEVELOPER: julia de guzman
COLLABORATORS: 
DATE: 11/25/2024
'''

"""
Uses graphical user interface(GUI) to collect COVID 19 vaccine input. Prints the vaccine card to the console using inputs
"""


##### IMPORTS #####
from tkinter import * # gui module
#from file import MyGUI
from vaccine_record import *
  

##### MAIN PROGRAM #####
class MyGUI:
  def __init__(self):
    self.mainWindow = Tk()
    self.mainWindow.title("Vaccine Entry")
    self.mainWindow.geometry("400x400")

############################## Frames
    self.frame1 = Frame(self.mainWindow, borderwidth = 4)
    self.frame2 = Frame(self.mainWindow, borderwidth = 4)
    self.frame3 = Frame(self.mainWindow, borderwidth = 4)
    
################################### Labels'
    self.firstName = Label(self.frame1, text = "First name")
    self.lastName = Label(self.frame1, text = "Last name")
    self.dob = Label(self.frame1, text = "Date of birth: mm/dd/yyyy")
    self.firstDoseLabel = Label(self.frame1, text = "First dose information")
    self.manufacturer1 = Label(self.frame1, text = "Manufacturer")
    self.batch1 = Label(self.frame1, text = "Batch")
    self.date1 = Label(self.frame1, text = "Date (mm/dd/yyyy)")
    self.location1 = Label(self.frame1, text = "Location")
    self.secondDoseLabel = Label(self.frame1, text = "Second dose information")
    self.manufacturer2 = Label(self.frame1, text = "Manufacturer")
    self.batch2 = Label(self.frame1, text = "Batch")
    self.date2 = Label(self.frame1, text = "Date (mm/dd/yyyy)")
    self.location2 = Label(self.frame1, text = "Location")

#################################### entry
    self.enterFirstName = Entry(self.frame1, text = "Values", width = 20)
    self.enterLastName = Entry(self.frame1, text = "Values1", width = 20)
    self.enterDob = Entry(self.frame1, text = "Values2", width = 20)
    self.enterManufacturer1= Entry(self.frame1, text = "Values3", width =20)
    self.enterBatch1= Entry(self.frame1, text = "Values4", width =20)
    self.enterDate1= Entry(self.frame1, text = "Values5", width =20)
    self.enterLocation1= Entry(self.frame1, text = "Values6", width =20)
    self.enterManufacturer2= Entry(self.frame1, text = "Values7", width =20)
    self.enterBatch2= Entry(self.frame1, text = "Values8", width =20)
    self.enterDate2= Entry(self.frame1, text = "Values9", width =20)
    self.enterLocation2= Entry(self.frame1, text = "Values10", width =20)

################################### Checkbox
    self.checkBoxVariable = IntVar()
    self.secondDoseCheckBox = Checkbutton(self.frame1, text='No second dose', command=self.check_changed, variable=self.checkBoxVariable, onvalue='1', offvalue='0')

########################################## submit button
    self.submitButton = Button(self.frame1, text = "submit", command = self.process)

############################### grid frames
    self.frame1.grid(row = 0, column = 0)
    self.frame2.grid(row = 0, column = 1)       
    self.firstName.grid(row = 0, column = 0)
    self.enterFirstName.grid(row = 0, column = 1)
    self.lastName.grid(row = 1, column = 0) 
    self.enterLastName.grid(row = 1, column = 1)  
    self.dob.grid(row = 2, column = 0)
    self.enterDob.grid(row = 2, column = 1) 
    self.firstDoseLabel.grid(row = 3, column = 1)
    self.manufacturer1.grid(row = 4, column = 0)
    self.enterManufacturer1.grid(row = 4, column = 1)
    self.batch1.grid(row = 5, column = 0)
    self.enterBatch1.grid(row = 5, column = 1)
    self.date1.grid(row = 6, column = 0)
    self.enterDate1.grid(row = 6, column = 1)
    self.location1.grid(row = 7, column = 0)
    self.enterLocation1.grid(row = 7, column = 1)
    self.secondDoseLabel.grid(row = 8, column = 1)
    self.secondDoseCheckBox.grid(row = 8, column = 2)
    self.manufacturer2.grid(row = 9, column = 0)
    self.batch2.grid(row = 10, column = 0)
    self.date2.grid(row = 11, column = 0)
    self.location2.grid(row = 12, column = 0)
    self.enterManufacturer2.grid(row = 9, column = 1)
    self.enterBatch2.grid(row = 10, column = 1)
    self.enterDate2.grid(row = 11, column = 1)
    self.enterLocation2.grid(row = 12, column = 1)
    self.submitButton.grid(row = 9, column = 2)
    
    mainloop()


########################################### checkbox functions
  def check_changed(self):
    if self.checkBoxVariable.get()==1:
      self.manufacturer2.grid_forget()
      self.batch2.grid_forget()
      self.date2.grid_forget()
      self.location2.grid_forget()
      self.enterManufacturer2.grid_forget()
      self.enterBatch2.grid_forget()
      self.enterDate2.grid_forget()
      self.enterLocation2.grid_forget()

    else: 
      self.manufacturer2.grid(row = 9, column = 0)
      self.batch2.grid(row = 10, column = 0)
      self.date2.grid(row = 11, column = 0)
      self.location2.grid(row = 12, column = 0)
      self.enterManufacturer2.grid(row = 9, column = 1)
      self.enterBatch2.grid(row = 10, column = 1)
      self.enterDate2.grid(row = 11, column = 1)
      self.enterLocation2.grid(row = 12, column = 1)  


  # this method should be called when "Submit"   button is clicked
  def process(self):
    #print("submit was clicked")  
    myVaccineObject = VaccineRecord(self.enterFirstName.get(),self.enterLastName.get(),self.enterDob.get(), self.enterManufacturer1.get(), self.enterBatch1.get()  , self.enterDate1.get()  , self.enterLocation1.get() , self.enterManufacturer2.get(), self.enterBatch2.get()  , self.enterDate2.get()  , self.enterLocation2.get())
    print(myVaccineObject.printCard())  
    if self.checkBoxVariable.get()==1:
      print("\nYou should get your second dose, if appropriate within 3 weeks or more. Please check with your health care provider to verify and schedule an appointment.")

########################## Main program

def main():
  myGUIObject = MyGUI()

main()

