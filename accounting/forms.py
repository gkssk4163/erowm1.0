# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import NON_FIELD_ERRORS

from .models import Profile, Owner, Business, Sales, Agency, Account
from .models import Subsection, Paragraph, Item, Subdivision
from .models import TBLBANK, Transaction

class SignupForm(UserCreationForm):
    email = forms.EmailField(
        label="이메일",
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }
        )
    )

    username = forms.RegexField(
        label="아이디",
        max_length=30,
        min_length=8,
        regex=r'^[a-zA-Z0-9.@+_-]+$',
        help_text="Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.",
        error_messages = {
            'invalid': "아이디는 영문 대,소문자, 숫자 및 " "@/./+/-/_ 문자만 포함될 수 있습니다.",
            'unique': "이미 존재하는 아이디입니다.",
        },
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'ID',
        })
    )

    password1 = forms.CharField(
        label="비밀번호",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
        })
    )

    password2 = forms.CharField(
        label="비밀번호 확인",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password confirmation',
        })
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email',)


class OwnerForm(forms.ModelForm):
    name = forms.CharField(
        label="이름",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
        })
    )

    phone = forms.RegexField(
        label="전화번호",
        regex=r'^\d{2,3}-\d{3,4}-\d{4}$',
        max_length=13,
        help_text="'-'로 구분하여 적어주세요.",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
        })
    )

    cellphone = forms.RegexField(
        label="핸드폰번호",
        regex=r'^\d{3}-\d{3,4}-\d{4}$',
        max_length=13,
        help_text="'-'로 구분하여 적어주세요.",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
        })
    )

    place_name = forms.CharField(
        label="사업장명",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
        })
    )

    reg_number = forms.RegexField(
        regex=r'^\d{3}-\d{2}-\d{5}$',
        label='사업자등록번호',
        max_length=12,
        error_messages = {
            'invalid': "'-'로 구분하여 적어주세요.",
        },
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
        })
    )

    class Meta:
        model = Owner
        fields = ('name', 'phone', 'cellphone', 'place_name', 'reg_number',)

    def __init__(self, *args, **kwargs):
        super(OwnerForm, self).__init__(*args, **kwargs)
        self.fields['phone'].required = False


class BusinessForm(forms.ModelForm):
    reg_number = forms.RegexField(
        regex=r'^\d{3}-\d{2}-\d{5}$',
        label='사업자등록번호',
        max_length=12,
        error_messages = {
            'invalid': "'-'로 구분하여 적어주세요.",
        },
    )

    owner_reg_number1 = forms.RegexField(
        regex=r'^(?:[0-9]{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[1,2][0-9]|3[0,1]))$',
        label='주민번호 앞자리',
        max_length=6,
        error_messages = {
            'invalid': "생년월일을 정확하게 입력해주세요.",
        },
    )

    owner_reg_number2 = forms.RegexField(
        regex=r'^[1-4][0-9]{6}$',
        label='주민번호 뒷자리',
        max_length=7,
        error_messages = {
            'invalid': "주민번호뒷자리를 정확하게 입력해주세요.",
        },
    )

    cellphone = forms.RegexField(
        regex=r'^\d{3}-\d{3,4}-\d{4}$',
        label='핸드폰번호',
        max_length=13,
        error_messages = {
            'invalid': "'-'로 구분하여 적어주세요.",
        },
    )

    phone = forms.RegexField(
        regex=r'^\d{2,3}-\d{3,4}-\d{4}$',
        label='전화번호',
        max_length=13,
        error_messages = {
            'invalid': "'-'로 구분하여 적어주세요.",
        },
    )

    fax = forms.RegexField(
        regex=r'^\d{3}-\d{3,4}-\d{4}$',
        label='팩스번호',
        max_length=13,
        error_messages = {
            'invalid': "'-'로 구분하여 적어주세요.",
        },
    )

    zip_number = forms.RegexField(
        regex=r'^[0-9]{5}$',
        label="우편번호",
        max_length=5,
    )

    class Meta:
        model = Business
        fields = ('name', 'place_name', 'reg_number', 'owner_name', 'owner_reg_number1', 'owner_reg_number2', 'type1', 'type2', 'type3','cellphone', 'phone', 'fax', 'email', 'zip_number', 'address', 'detailed_address')
        labels = {
                'name': '사업명',
                'place_name': '사업장명',
                'owner_name': '대표자성명',
                'type1': '업태',
                'type2': '업종',
                'type3': '사업종류',
                'email': '이메일',
                'address': '주소',
                'detailed_address': '상세주소',
        }
    def __init__(self, *args, **kwargs):
        super(BusinessForm, self).__init__(*args, **kwargs)
        self.fields['phone'].required = False
        self.fields['fax'].required = False
        self.fields['zip_number'].widget.attrs['readonly'] = True
        self.fields['address'].widget.attrs['readonly'] = True


class EditOwnerForm(OwnerForm, BusinessForm):
    class Meta:
        model = Owner
        fields = ('place_name', 'reg_number', 'type1', 'type2', 'name', 'owner_reg_number1', 'owner_reg_number2', 'email', 'cellphone', 'phone', 'fax', 'zip_number', 'address', 'detailed_address',)


class UserForm(UserCreationForm):
    email = forms.EmailField(
        label="이메일",
        required=True,
    )

    username = forms.RegexField(
        label="아이디",
        max_length=30,
        min_length=8,
        regex=r'^[a-zA-Z0-9.@+_-]+$',
        help_text="Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.",
        error_messages = {
            'invalid': "아이디는 영문 대,소문자, 숫자 및 " "@/./+/-/_ 문자만 포함될 수 있습니다.",
            'unique': "이미 존재하는 아이디입니다.",
        },
    )

    password1 = forms.CharField(
        label="비밀번호",
        strip=False,
        widget=forms.PasswordInput(attrs={})
    )

    password2 = forms.CharField(
        label="비밀번호 확인",
        strip=False,
        widget=forms.PasswordInput(attrs={})
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email',)


class SalesForm(forms.ModelForm):
    jdate = forms.DateField(
        label="입사일자",
        widget = forms.DateInput(attrs={'class': 'vDateField'})
    )
    reg_number1 = forms.RegexField(
        regex=r'^(?:[0-9]{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[1,2][0-9]|3[0,1]))$',
        label='주민번호 앞자리',
        max_length=6,
        error_messages = {
            'invalid': "생년월일을 정확하게 입력해주세요.",
        },
    )

    reg_number2 = forms.RegexField(
        regex=r'^[1-4][0-9]{6}$',
        label='주민번호 뒷자리',
        max_length=7,
        error_messages = {
            'invalid': "주민번호뒷자리를 정확하게 입력해주세요.",
        },
    )

    cellphone = forms.RegexField(
        label="핸드폰번호",
        regex=r'^\d{3}-\d{3,4}-\d{4}$',
        help_text="'-'로 구분하여 적어주세요.",
    )

    zip_number = forms.RegexField(
        regex=r'^[0-9]{5}$',
        label="우편번호",
        max_length=5,
    )

    account_number = forms.RegexField(
        regex=r'^\d+-\d+-?\d+-?\d+$',
        label="계좌번호",
        max_length=20,
    )

    class Meta:
        model = Sales
        fields = ('name', 'jdate', 'reg_number1', 'reg_number2', 'cellphone', 'zip_number', 'address', 'detailed_address', 'agency', 'bank', 'account_number')
        labels = {
            'name': '이름',
            'jdate': '입사일자',
            'address': '주소',
            'detailed_address': '상세주소',
            'agency': '대리점',
            'bank': '은행',
        }

    def __init__(self, *args, **kwargs):
        super(SalesForm, self).__init__(*args, **kwargs)
        self.fields['jdate'].widget.attrs['readonly'] = True
        self.fields['zip_number'].widget.attrs['readonly'] = True
        self.fields['address'].widget.attrs['readonly'] = True


class AgencyForm(forms.ModelForm):
    reg_number = forms.RegexField(
        regex=r'^\d{3}-\d{2}-\d{5}$',
        label='사업자등록번호',
        max_length=12,
        error_messages = {
            'invalid': "'-'로 구분하여 적어주세요.",
        },
    )

    owner_reg_number1 = forms.RegexField(
        regex=r'^(?:[0-9]{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[1,2][0-9]|3[0,1]))$',
        label='주민번호 앞자리',
        max_length=6,
        error_messages = {
            'invalid': "생년월일을 정확하게 입력해주세요.",
        },
    )

    owner_reg_number2 = forms.RegexField(
        regex=r'^[1-4][0-9]{6}$',
        label='주민번호 뒷자리',
        max_length=7,
        error_messages = {
            'invalid': "주민번호뒷자리를 정확하게 입력해주세요.",
        },
    )

    cellphone = forms.RegexField(
        label="핸드폰번호",
        regex=r'^\d{3}-\d{3,4}-\d{4}$',
        help_text="'-'로 구분하여 적어주세요.",
    )

    zip_number = forms.RegexField(
        regex=r'^[0-9]{5}$',
        label="우편번호",
        max_length=5,
    )

    account_number = forms.RegexField(
        regex=r'^\d+-\d+-?\d+-?\d+$',
        label="계좌번호",
        max_length=20,
    )

    class Meta:
        model = Agency
        fields = ('name', 'reg_number', 'owner_name', 'reg_date', 'owner_reg_number1', 'owner_reg_number2', 'cellphone', 'zip_number', 'address', 'detailed_address', 'bank', 'account_number', 'phone', 'fax')
        labels = {
            'name': '상호',
            'owner_name': '대표자명',
            'reg_date': '등록일자',
            'address': '주소',
            'detailed_address': '상세주소',
        }

    def __init__(self, *args, **kwargs):
        super(AgencyForm, self).__init__(*args, **kwargs)
        self.fields['reg_date'].widget.attrs['readonly'] = True
        self.fields['zip_number'].widget.attrs['readonly'] = True
        self.fields['address'].widget.attrs['readonly'] = True


class AccountForm(forms.ModelForm):
    business = forms.ModelChoiceField(
        queryset=Business.objects.all(),
        widget=forms.HiddenInput()
    )

    account_number = forms.RegexField(
        regex=r'^\d+$',
        label="계좌번호",
        max_length=64,
    )

    account_pw = forms.CharField(
        label="비밀번호",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
        })
    )

    bkdiv = forms.ChoiceField(
        label="구분",
        widget=forms.RadioSelect(
            attrs = {
                'class': 'select-ul',
            }
        ),
        choices = ([('C','법인'), ('P','개인')]), initial='C', required = True,
    )

    class Meta:
        model = Account
        fields = ('business', 'renames', 'bank', 'account_number', 'account_pw', 'bkdiv', 'webid', 'webpw')
        labels = {
            'renames': '계좌별명',
            'bank': '은행선택',
            'bkdiv': '계좌구분',
            'webid': '간편조회ID',
            'webpw': '간편조회PW',
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "이미 등록된 계좌입니다. 확인하고 다시 등록해주세요.",
            }
        }

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.fields['webpw'].widget = forms.PasswordInput()
        self.fields['webpw'].strip = False


class SubsectionForm(forms.ModelForm):
    type = forms.ChoiceField(
        label="수입/지출",
        widget=forms.RadioSelect(
            attrs={
                'class': 'select-ul',
            }
        ),
        choices = ([('수입','수입'), ('지출','지출')]), initial='수입', required = True,
    )

    class Meta:
        model = Subsection
        fields = ('year', 'institution', 'type', 'code', 'context')
        labels = {
            'year': '회계년도',
            'institution': '기관',
            'code': '관번호',
            'context': '내용',
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "이미 등록된 관번호입니다. 확인하고 다시 등록해주세요.",
            }
        }


class ParagraphForm(forms.ModelForm):
    class Meta:
        model = Paragraph
        fields = ('subsection', 'code', 'context')
        labels = {
            'subsection': '관번호',
            'code': '항번호',
            'context': '내용',
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "이미 등록된 항번호입니다. 확인하고 다시 등록해주세요.",
            }
        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('paragraph', 'code', 'context', 'text')
        labels = {
            'paragraph': '항번호',
            'code': '목번호',
            'context': '내용',
            'text': '내역',
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "이미 등록된 목번호입니다. 확인하고 다시 등록해주세요.",
            }
        }


class SubdivisionForm(forms.ModelForm):
    class Meta:
        model = Subdivision
        fields = ('item', 'code', 'context')
        labels = {
            'item': '목번호',
            'code': '세목번호',
            'context': '내용',
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "이미 등록된 세목번호입니다. 확인하고 다시 등록해주세요.",
            }
        }


class TblbankDirectForm(forms.ModelForm):
    Bkdate = forms.DateField(
        label="거래일자",
        widget = forms.DateInput(attrs={'class': 'vDateField'})
    )

    class Meta:
        model = TBLBANK
        fields = ('Bkdate', 'item', 'Bkjukyo', 'Bkinput', 'Bkoutput')
        labels = {
            'item': '계정',
            'Bkjukyo': '적요',
            'Bkinput': '수입',
            'Bkoutput': '지출',
        }

    def __init__(self, *args, **kwargs):
        super(TblbankDirectForm, self).__init__(*args, **kwargs)
        self.fields['Bkdate'].widget.attrs['readonly'] = True
        self.fields['Bkoutput'].widget.attrs['style'] = 'display:none'
        self.fields['Bkoutput'].widget.attrs['value'] = 0

class TransactionEditForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('Bkdate', 'item', 'Bkjukyo', 'Bkinput', 'Bkoutput')
        labels = {
            'Bkdate': '거래일자',
            'item': '계정',
            'Bkjukyo': '적요',
            'Bkinput': '수입',
            'Bkoutput': '지출',
        }

    def __init__(self, *args, **kwargs):
        super(TransactionEditForm, self).__init__(*args, **kwargs)
        self.fields['Bkdate'].widget.attrs['readonly'] = True
        self.fields['Bkinput'].widget.attrs['readonly'] = True
        self.fields['Bkoutput'].widget.attrs['readonly'] = True
        self.fields['Bkdate'].widget.attrs['style'] = "background-color:#ddd"
        self.fields['Bkinput'].widget.attrs['style'] = "background-color:#ddd"
        self.fields['Bkoutput'].widget.attrs['style'] = "background-color:#ddd"

class AuthKeyForm(forms.ModelForm):
    s_auth_key = forms.RegexField(
        regex=r'^[A-Z0-9]{32}$',
        label='인증키',
        max_length=32,
        error_messages = {
            'invalid': "인증키를 다시 확인해주세요.",
        },
        widget=forms.TextInput(
            attrs={
                'size': '35',
            }
        )
    )
    class Meta:
        model = Business
        fields = ('s_auth_key',)
