from accounting.models import Transaction

def getTransactionList(param):
    transaction = Transaction.objects.filter(business = param['business']).select_related('item')

    if 'start_date' in param.keys() and param['start_date'] != "":
        transaction = transaction.filter(Bkdate__gte = param['start_date'])
    if 'end_date' in param.keys() and param['end_date'] != "":
        transaction = transaction.filter(Bkdate__lte = param['end_date'])
    if 'keyword' in param.keys() and param['keyword'] != "":
        transaction = transaction.filter(Bkjukyo__contains = param['keyword'])
    if 'type' in param.keys() and param['type'] != "":
        transaction = transaction.filter(item__paragraph__subsection__type = param['type'])
    if 'subsection' in param.keys() and param['subsection'] != "":
        transaction = transaction.filter(item__paragraph__subsection = int(param['subsection']))
    if 'paragraph' in param.keys() and param['paragraph'] != "":
        transaction = transaction.filter(item__paragraph = int(param['paragraph']))
    if 'item' in param.keys() and param['item'] != "":
        transaction = transaction.filter(item = int(param['item']))

    if 'codeYN' in param.keys() and param['codeYN'] == "N":
        transaction = transaction.exclude(item__paragraph__subsection__code = 0)

    return transaction