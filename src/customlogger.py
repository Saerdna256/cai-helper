import os as os
from datetime import datetime
from pathlib import Path

import constants as const

"""
I don't open the file in the init and close it with another dunction call at
program shutdown because after a program crash it may leave the logfile in an unknown state.
That would a) be bad form and b) potentially not write one ore more log lines due to
how the buffering works.
Since logs should not be enabled on a general use case, I really don't mind about a couple
of superfluous filesystem operations / calls
"""

class CustomLogger:    
    __isActive:bool = False
    __logfile:str = ""
    file: object = None

    @classmethod
    def init(cls) -> None:
        if cls.__isActive:
            return
        cls.__isActive = True
        cls.__logfile = os.path.normpath(Path.joinpath(Path.cwd(), const.LOGFILE))
        
        with open(cls.__logfile, "+w") as f:        
            f.write(f"CAI Version {const.VERSION}\n")
            now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            f.write(f"Log started {now}\n")
            f.write("===============================\n")

    # TODO: Remove the check for logging once this can get moved to the main() function!
    @classmethod
    def log_line(cls, line:str) -> None:
        if(cls.__isActive or const.LOGGING):
            with open(cls.__logfile, "+a") as f:
                split_lines = line.splitlines()
                if split_lines != None:
                    now = datetime.now().strftime("%H:%M:%S: ")
                    f.write(now + split_lines[0] + "\n")
                    i = 1
                    while i < len(split_lines):
                        f.write(f"          {split_lines[i]}")
                        i = i + 1



# Crude inline tests following

if __name__ == "__main__":
    CustomLogger.init()
    CustomLogger.log_line("Test 1")
    CustomLogger.log_line("Test 2\nTest 3")