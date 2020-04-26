from .models import Subsection, Paragraph, Item, Subdivision
import datetime

def session_info(selected_year, selected_month, session_month):
    next_year = str(int(selected_year)+1)
    selected_start_date = datetime.datetime.strptime(selected_year+"-"+session_month+"-01", "%Y-%m-%d")
    selected_end_date = datetime.datetime.strptime(next_year+"-"+session_month+"-01", "%Y-%m-%d")
    selected_date = datetime.datetime.strptime(selected_year+"-"+selected_month+"-01", "%Y-%m-%d")

    if selected_start_date <= selected_date and selected_date < selected_end_date:
        session_year = selected_year
    else:
        session_year = str(int(selected_year)-1)

    start_date = datetime.datetime.strptime(session_year+"-"+session_month+"-01", "%Y-%m-%d")
    end_date = datetime.datetime.strptime(session_year+"-"+session_month+"-01", "%Y-%m-%d")

    return {'start_date': start_date,
            'end_date' : end_date,
            'selected_date': selected_date,
            'year': session_year}

def item_info(year, btype, iotype):
    if iotype == 'i':
        return Item.objects.filter(paragraph__subsection__year = year, paragraph__subsection__institution = btype, paragraph__subsection__type = "수입").exclude(code=0)
    elif iotype == 'o':
        return Item.objects.filter(paragraph__subsection__year = year, paragraph__subsection__institution = btype, paragraph__subsection__type = "지출").exclude(code=0)
    elif iotype == 'b': #both
        return Item.objects.filter(paragraph__subsection__year = year, paragraph__subsection__institution = btype).exclude(code=0)
    else:
        return None

def subsection_info(year, btype, iotype):
    if iotype == 'i':
        return Subsection.objects.filter(year=year, institution=btype, type="수입").exclude(code=0)
    elif iotype == 'o':
        return Subsection.objects.filter(year=year, institution=btype, type="지출").exclude(code=0)
    elif iotype == 'b': #both
        return Subsection.objects.filter(year=year, institution=btype).exclude(code=0)
    else:
        return None
