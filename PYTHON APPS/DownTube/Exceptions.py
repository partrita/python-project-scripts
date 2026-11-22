class Downtube_Error(Exception):
    """ This is the base exception class for all other user defined exception(classes) """

class Link_Error(Downtube_Error):
    """ When there is no Link is given as input """
    
class InvalidLink(Downtube_Error):
    """ When the ink URL isn't a youtube link """

class DirectoryError(Downtube_Error):
    """ when No directory is given """
class ResolutionError(Downtube_Error):
    """ when no resolution is givenn """
