class CustomLogger:    
    __isActive:bool = False
    __logfile:str = ""
    
    @classmethod
    def init(cls, filename:str) -> None:
        cls.__isActive = True
        # continue logfile initialisation

    @classmethod
    def log_line(cls, line:str) -> None:
        if(cls.__isActive):
            pass
        pass