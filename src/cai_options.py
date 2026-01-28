import sys
import xml.etree.ElementTree as ET
import os as os
from pathlib import Path

import cai_constants as const
from cai_customlogger import CAICustomLogger as CL

"""
Data structure for holding the general programs options, also contains the functionality to
read and save the options file.
The individual options are exposed and meant to be accessed directly. The data structure is more
the centralize all the options and for loading / saving convinience. Chcking for valid input
should be done before storing variables here.
"""

class CAIOptions:
    ROOT = 'options'
    INSERTMODE = 'INSERTMODE'
    EXPORTMODE = 'EXPORTMODE'
    LASTSAVEPATH = 'SAVEPATH'
    LASTWINDOWSIZE = 'WINDOWSIZE'

    # Path is the fully qualified filepath to the ~/CAIData path
    # Load defaults first so any variable is in a sensible state no matter 
    # if a xml file is present and / or formed correctly
    def __init__(self, path) -> None:        
        # Try to load the XML file, store the filepath for writing the options file
        self.__fullpath = os.path.normpath(Path.joinpath(path, const.OPTIONS_FILENAME))
        try:
            tree = ET.parse(self.__fullpath)
            root = tree.getroot()
        except (OSError, ET.ParseError) as e:
            # File not found / readable
            CL.log_line(f"File not found/writable: {self.__fullpath}\nCreating new options file")
            root = self.create_from_scratch()            
            tree = ET.ElementTree(root)
        # Writeback the file. If this raises an error, we should not continue
        try:
            ET.indent(tree)
            tree.write(self.__fullpath)
        except OSError as e:
            CL.log_line(f"Error writing file: {self.__fullpath}:\n{e}")
            sys.exit(1)

        # Read the variables
        im = root.find(CAIOptions.INSERTMODE)
        em = root.find(CAIOptions.EXPORTMODE)
        sp = root.find(CAIOptions.LASTSAVEPATH)
        ws = root.find(CAIOptions.LASTWINDOWSIZE)

        if (im == None) or (em == None) or (sp == None) or (ws == None):
            CL.log_line("Malformed XML in options file")
            sys.exit(1)
        self.insertmode = str(im.text)
        self.exportmode = str(em.text)
        self.last_savepath = str(sp.text)
        self.last_window_size = str(ws.text)
        
    def create_from_scratch(self) -> ET.Element:        
        root = ET.Element(CAIOptions.ROOT)
        im = ET.Element(CAIOptions.INSERTMODE)
        im.text = const.DEFAULT_OPTIONS.INSERTMODE
        root.append(im)
        em = ET.Element(CAIOptions.EXPORTMODE)
        em.text = const.DEFAULT_OPTIONS.EXPORTMODE
        root.append(em)
        sp = ET.Element(CAIOptions.LASTSAVEPATH)
        sp.text = const.DEFAULT_OPTIONS.LAST_SAVE_PATH
        root.append(sp)
        ws = ET.Element(CAIOptions.LASTWINDOWSIZE)
        ws.text = const.DEFAULT_OPTIONS.LAST_WINDOW_SIZE
        root.append(ws)
        return root
    
    def write(self) -> bool:
        root = ET.Element(CAIOptions.ROOT)
        im = ET.Element(CAIOptions.INSERTMODE)
        im.text = self.insertmode
        root.append(im)
        em = ET.Element(CAIOptions.EXPORTMODE)
        em.text = self.exportmode
        root.append(em)
        sp = ET.Element(CAIOptions.LASTSAVEPATH)
        sp.text = self.last_savepath
        root.append(sp)
        ws = ET.Element(CAIOptions.LASTWINDOWSIZE)
        ws.text = self.last_window_size
        root.append(ws)

        tree = ET.ElementTree(root)
        if(tree == None):
            CL.log_line(f"Error writing file: {self.__fullpath}")
            return False
        try:
            tree.write(self.__fullpath)
        except OSError as e:
            CL.log_line(f"Error writing file: {self.__fullpath}:\n{e}")
            return False
                    
        return True
    
# Inline Testing
if __name__ == '__main__':
    CL.init()
    tmppath = Path.cwd()
    options = CAIOptions(tmppath)
    options.last_savepath = "/bananas/"
    options.write()    
