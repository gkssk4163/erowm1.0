from accounting.models import Subdivision

def getSubdivisionList(business = "", item = "", codeYN = 'N'):
    subdivision = Subdivision.objects.all()
    if business is not "":
        subdivision = subdivision.filter(business = business)
    if item is not "":
        subdivision = subdivision.filter(item = item)
    # code 0 배제여부
    if codeYN is 'N':
        subdivision = subdivision.exclude(code = 0)
    return subdivision