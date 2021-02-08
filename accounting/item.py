from .models import Item

def getItemList(paragraph = "", codeYN = 'N'):
    item = Item.objects.all()
    if paragraph is not "":
        item = item.filter(paragraph = paragraph)
    # code 0 배제여부
    if codeYN is 'N':
        item = item.exclude(code = 0)
    return item