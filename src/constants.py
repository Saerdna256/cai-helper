# Enable Loging for pure dev builds
LOGGING = True

# current version
VERSION = "0.0.0.1"

# author
AUTHOR = "Andreas Bonenkamp"

# extension for the individual assessment files
ASSESSMENT_EXT = ".caf"

# static general filenames
OPTIONS_FILENAME = "options.xml"
LOGFILE = "dev.log"
MODS_FOLDER = "bausteine"

# filnames for text modules
MODS_EXTERNAL = "fremdbefunde.mod"
MODS_GIVEN = "anamnese.mod"
MODS_FINDINGS = "befund.mod"
MODS_SITUATION = "versorgungssituation.mod"
MODS_LIVING = "wohnsituation.mod"
MODS_REASONING = "begruendung.mod"
MODS_OUTLOOK = "prognose.mod"

# Modes for the main program
class INSERTMODE:
    CHRONOLOGICAL = "CHRON" # chronological
    PLACEHOLDER = "PLACE" # placeholder

# Possible export modes
class EXPORTMODE:
    TXT_SINGLE = "txtsingle"
    TXT_MULTI = "txtmulti"
    PDF_SINGLE = "pdfsingle"
    PDF_MULTI = "pdfmulti"

# Defaults for first run / corrupted options file
class DEFAULT_OPTIONS:
    INSERTMODE = INSERTMODE.PLACEHOLDER
    EXPORTMODE = EXPORTMODE.TXT_SINGLE
    LAST_SAVE_PATH = ""
    LAST_WINDOW_SIZE = "800x600"

