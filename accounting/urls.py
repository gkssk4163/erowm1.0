from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^home$', views.home, name='home'),
    url(r'^business/list/$', views.business_list, name='business_list'),
    url(r'^business/create/$', views.business_create, name='business_create'),
    url(r'^business/edit/(?P<pk>\d+)/$', views.business_edit, name='business_edit'),
    #url(r'^business/info/(?P<pk>\d+)/$', views.business_info, name='business_info'),
    url(r'^business/info/$', views.business_info, name='business_info'),
    url(r'^transform/business/(?P<pk>\d+)/$', views.transform_business, name='transform_business'),
    url(r'^retransform/business/$', views.retransform_business, name='retransform_business'),
    url(r'^user/list/$', views.user_list, name="user_list"),
    url(r'^user/delete/$', views.user_delete, name="user_delete"),
    url(r'^user/transform/$', views.user_transform, name="user_transform"),
    url(r'^transform/(?P<pk>\d+)/$', views.transform, name="transform"),
    url(r'^retransform/$', views.retransform, name="retransform"),
    url(r'^sales/list/$', views.sales_list, name="sales_list"),
    url(r'^sales/create/$', views.sales_create, name='sales_create'),
    url(r'^sales/edit/(?P<pk>\d+)/$', views.sales_edit, name='sales_edit'),
    url(r'^sales/delete/(?P<pk>\d+)/$', views.sales_delete, name='sales_delete'),
    url(r'^sales/change/$', views.sales_change, name='sales_change'),
    url(r'^agency/list/$', views.agency_list, name="agency_list"),
    url(r'^agency/create/$', views.agency_create, name='agency_create'),
    url(r'^agency/edit/(?P<pk>\d+)/$', views.agency_edit, name='agency_edit'),
    url(r'^agency/change/$', views.agency_change, name='agency_change'),
    url(r'^mypage/$', views.mypage, name='mypage'),
    url(r'^mypage/edit/$', views.mypage_edit, name='mypage_edit'),
    url(r'^agency/delete/(?P<pk>\d+)/$', views.agency_delete, name='agency_delete'),
    url(r'^bankda/join/$', views.bankda_join, name='bankda_join'),
    url(r'^bankda/account/$', views.bankda_account, name='bankda_account'),
    url(r'^erowm/account/$', views.erowm_account, name='erowm_account'),
    url(r'^bankda/account/delete$', views.bankda_account_delete, name='bankda_account_delete'),
    url(r'^account/list/$', views.account_list, name='account_list'),
    url(r'^account/create/$', views.account_create, name='account_create'),
    url(r'^account/edit/(?P<pk>\d+)/$', views.account_edit, name='account_edit'),
    url(r'^account/delete/(?P<pk>\d+)/$', views.account_delete, name='account_delete'),
    url(r'^transaction/history/$', views.transaction_history, name='transaction_history'),
    url(r'^transaction/list/$', views.transaction_list, name='transaction_list'),

    url(r'^spi/list/$', views.spi_list, name='spi_list'),
    url(r'^subsection/create/$', views.subsection_create, name='subsection_create'),
    url(r'^subsection/edit/(?P<pk>\d+)/$', views.subsection_edit, name='subsection_edit'),
    url(r'^paragraph/create/$', views.paragraph_create, name='paragraph_create'),
    url(r'^paragraph/edit/(?P<pk>\d+)/$', views.paragraph_edit, name='paragraph_edit'),
    url(r'^item/create/$', views.item_create, name='item_create'),
    url(r'^item/edit/(?P<pk>\d+)/$', views.item_edit, name='item_edit'),
    url(r'^subdivision/list/$', views.subdivision_list, name='subdivision_list'),
    url(r'^subdivision/create/$', views.subdivision_create, name='subdivision_create'),
    #url(r'^premonth/transfer/price/$', views.premonth_transfer_price, name='premonth_transfer_price'),
    url(r'^regist_transaction/$', views.regist_transaction, name='regist_transaction'),
    url(r'^popup_transaction_direct/$', views.popup_transaction_direct, name='popup_transaction_direct'),
    url(r'^regist_transaction_direct/$', views.regist_transaction_direct, name='regist_transaction_direct'),
    url(r'^popup_transaction_edit/$', views.popup_transaction_edit, name='popup_transaction_edit'),
    url(r'^edit_transaction/$', views.edit_transaction, name='edit_transaction'),
    url(r'^other/settings/$', views.other_settings, name='other_settings'),
    url(r'^database/syn/$', views.database_syn, name='database_syn'),
    url(r'^transaction/delete/$', views.transaction_delete, name='transaction_delete'),
    url(r'^popup_change_main_account/$', views.popup_change_main_account, name='popup_change_main_account'),
    url(r'^change/main/account/$', views.change_main_account, name='change_main_account'),
    url(r'^popup_transaction_division_(?P<Bkid>\d+)/$', views.popup_transaction_division, name='popup_transaction_division'),
    url(r'^add_row/$', views.add_row, name='add_row'),
    url(r'^delete_row/$', views.delete_row, name='delete_row'),
    #url(r'^extract_subdivision/$', views.extract_subdivision, name='extract_subdivision'),
    url(r'^popup_select_item/$', views.popup_select_item, name='popup_select_item'),
    url(r'^regist/division/$', views.regist_division, name='regist_division'),
    url(r'^budget/(?P<budget_type>[a-z_]\w+)/$', views.annual_budget, name='annual_budget'),
    url(r'^print/yearly/(?P<budget_type>[a-z_]\w+)/$', views.print_yearly_budget, name='print_yearly_budget'),
    url(r'^regist/annual/budget/$', views.regist_annual_budget, name='regist_annual_budget'),
    url(r'^budget/settlement/(?P<budget_type>[a-z]\w+)/$', views.budget_settlement, name='budget_settlement'),
    url(r'^trial/balance$', views.trial_balance, name='trial_balance'),
    url(r'^print/trial/balance$', views.print_trial_balance, name='print_trial_balance'),
    url(r'^annual/trial/balance$', views.annual_trial_balance, name='annual_trial_balance'),
    url(r'^print/annual/trial/balance$', views.print_annual_trial_balance, name='print_annual_trial_balance'),

    url(r'^print/settlement/$', views.print_settlement, name='print_settlement'),
    url(r'^print/settlement/all$', views.print_settlement_all, name='print_settlement_all'),
    url(r'^print/budget/$', views.print_budget, name='print_budget'),
    url(r'^print/(?P<budget_type>[a-z]\w+)_settlement/$', views.print_budget_settlement, name='print_budget_settlement'),
    url(r'^print/(?P<budget_type>[a-z]\w+)_settlement2/$', views.print_budget_settlement2, name='print_budget_settlement2'),
    url(r'^print/transaction/$', views.print_transaction, name='print_transaction'),
    url(r'^print/general_ledger/$', views.print_general_ledger, name='print_general_ledger'),
    url(r'^print/voucher/$', views.print_voucher2, name='print_voucher2'),
    url(r'^print/(?P<voucher_type>[a-z]\w+)_voucher/$', views.print_voucher, name='print_voucher'),
    url(r'^popup_returned_transaction/$', views.popup_returned_transaction, name='popup_returned_transaction'),
    url(r'^regist/returned_transaction$', views.regist_returned_transaction, name='regist_returned_transaction'),
    url(r'^print/return/(?P<voucher_type>[a-z]\w+)_voucher/$', views.print_returned_voucher, name='print_returned_voucher'),
    url(r'^monthly/print/$', views.monthly_print, name='monthly_print'),
    url(r'^monthly/print/all$', views.monthly_print_all, name='monthly_print_all'),
    url(r'^print/budget/all$', views.print_budget_all, name='print_budget_all'),
    url(r'^check_date/$', views.check_date, name='check_date'),

    url(r'^file/download/$', views.file_download, name='file_download'),
    url(r'^popup_upload/$', views.popup_upload, name='popup_upload'),
    url(r'^upload/transaction/$', views.upload_transaction, name='upload_transaction'),
    url(r'^upload/transaction2/$', views.upload_transaction2, name='upload_transaction2'),
    url(r'^upload/voucher/$', views.upload_voucher, name='upload_voucher'),

    url(r'^close/list/$', views.close_list, name='close_list'),
    url(r'^regist/close/$', views.regist_close, name='regist_close'),
    url(r'^undo/close/$', views.undo_close, name='undo_close'),

    url(r'^account_check/$', views.account_check, name='account_check'),
    url(r'^change_item_option/$', views.change_item_option, name='change_item_option'),

    url(r'^authkey_list/$', views.authkey_list, name='authkey_list'),
    url(r'^authkey_edit/$', views.authkey_edit, name='authkey_edit'),
    
    url(r'^set_proofnum/$', views.set_proofnum, name='set_proofnum'),
    url(r'^tr_syn/$', views.tr_syn, name='tr_syn'),

    url(r'^select/subdivision/$', views.select_subdivision, name='select_subdivision'),
    url(r'^select/item/$', views.select_item, name='select_item'),

    #url(r'^/$', views., name=''),
    url(r'^test/$', views.test, name='test'),
    url(r'^design_test/$', views.design_test, name='design_test'),

    #ajax function
    url(r'^budget/spi/total/$', views.budget_spi_total, name='budget_spi_total'),

    url(r'^subsection/list/$', views.subsection_list, name='subsection_list'),
    url(r'^paragraph/list/$', views.paragraph_list, name='paragraph_list'),
    url(r'^item/list/$', views.item_list, name='item_list'),
]
