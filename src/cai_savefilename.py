# standard libraries
from datetime import date

# custom files
import cai_constants as const
from  cai_customlogger import CAICustomLogger as CL

"""
SaveFile is meant as a variable to store an semi-automatically created filename for each
indivdual assessment. It can either be created by the usergiving it a name in the "New Assessment" dialogue
or by the program when reading in the already saved assessments.
The current filename changes when the user gives it a new name by typing in the "Name" field in the main
window. However, the date created is fixed. 
A creation time is substituted for the name if none is given. This should produce unique filenames
with a sufficient probability.
"""

class CAISaveFileName():
    # default if newly created; with full_filename if created from existing file
    # full_filenme should not include the path, only the filename
    # if a full_filename is supplied the given_name is ignored!
    def __init__(self, given_name:str, full_filename:str = "") -> None:
        if(full_filename == ""):
            # base case
            today = date.today()
            self.__date_created :str = today.strftime("%Y%m%d")
            self.__time_created :str = today.strftime("%H%M%S")
            self._given_name :str = given_name
        else:
            if given_name != "":
                CL.log_line(f"Both filename and given_name supplied in SaveFileName():\n{given_name}\n{full_filename}")
            # check length
            if len(full_filename) < 16:
                raise ValueError(f"Filename too short: {full_filename}")
            # Check for extension
            if full_filename[-4:] != const.ASSESSMENT_EXT:
                raise ValueError(f"Invalid extension for SaveFile: {full_filename}")
            # remove extension            
            without_extension = full_filename[:-4]
            # Check for "date-time_name" format
            if(without_extension[8] != '-' or without_extension[15] != '_'):
                raise ValueError(f"Invalid filename syntax for Savefile: {full_filename}")
            # parse filename
            self.__date_created = without_extension[0:8]
            self.__time_created = without_extension[9:15]
            if len(full_filename) > 16:
                self._given_name = without_extension[16:]
            else:
                self._given_name = ""

    # return only the freely chosen name for the file
    def get_given_name(self) -> str:
        return self._given_name
    
    # return a proper filename inluding the date and time of 
    def get_full_filename_base(self) -> str:
        return self.__date_created + "-" + self.__time_created + "_" + self._given_name
    
    # return fully qualified filename inluding filytype ending
    def get_full_prop_filename(self) -> str:
        return self.get_full_filename_base() + const.ASSESSMENT_EXT
    
    def update_given_name(self, new_name:str) -> None:
        # Should NOT ever update the date / time of creation. That field is meant to remain fixed!
        self._given_name = new_name
