class computer:
    cpu = "Intel"   # Processor maker
    gpu = "AMD"     # Card maker
    ram = 8         # In GB
    case = True     # Has a case
    

class windows(computer): # Denotes that windows is a child class of computer and will add the following attributes
    os = 'Windows10'   # New windows-specific attribute
    canModify = True
    canInstall = True
    
	
class nintendoGC(computer): # nintendoGC is a child class of computer
    os = 'Nintendo GameCube'
    cd_drive = True
    controller_input = True