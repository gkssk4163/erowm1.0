from .models import Subsection

def getSubsectionList(institution = "", year = "", type = "", codeYN = 'N'):
    subsection = Subsection.objects.all()
    if institution is not "":
        subsection = subsection.filter(institution = institution)
    if year is not "":
        subsection = subsection.filter(year = year)
    if type is not "":
        subsection = subsection.filter(type = type)
    # code 0 배제여부
    if codeYN is 'N':
        subsection = subsection.exclude(code = 0)
    return subsection