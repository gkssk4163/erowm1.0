from .models import Paragraph

def getParagraphList(subsection = "", codeYN = 'N'):
    paragraph = Paragraph.objects.all()
    if subsection is not "":
        paragraph = paragraph.filter(subsection = subsection)
    # code 0 배제여부
    if codeYN is 'N':
        paragraph = paragraph.exclude(code = 0)
    return paragraph