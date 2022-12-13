from django.urls import path
from django.contrib import admin
from . import views



urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('', views.tables, name='tables'),
    path('vc_no',views.Vc_no,name='Vc_no'),
    path('Inco-Terms',views.inco_terms,name='inco_terms'),
    path('origin-state',views.origin_state,name='origin_state'),
    path('mis',views.Mis,name='Mis'),
    path('distance-range',views.distance_range,name='distance_range'),
    path('rate',views.rate,name='rate'),
    path('chartJSON', views.line_chart_json, name='line_chart_json'),
    path('chartJSON2', views.line_chart2_json, name='line_chart2_json'),
    path('chartJSON3', views.line_chart3_json, name='line_chart3_json'),
    path('recovery-condition',views.recovery_condition,name='recovery_condition'),
    path('pf-mis',views.pf_mis,name='pf_mis'),
    path('rate-master',views.rate_master,name='rate_master'),
    path('Weight-Master',views.weight_master,name='weight_master'),
    path('cbm-cft',views.cbm_cft,name='cbm_cft'),
    path('svps-remark',views.svps_remark,name='svps_remark'),
    path('transporter-master',views.transporter_master,name='transporter_master'),
    path('mis-full',views.Mis_Full,name='Mis_Full'),
    path('po',views.po,name='po'),
    path('ses',views.ses,name='ses'),
    path('svps',views.svps,name='svps'),
    path('lr-bill',views.lr_bill,name='lr_bill'),
    path('inbound-shipment',views.inbound_shipment,name='inbound_shipment'),
    path('leci',views.Leci,name='Leci'),
    path('grn',views.Grn,name='Grn'),
    path('part',views.Part,name='Part'),
    path('vendor',views.Vendor,name='Vendor'),
    path('fast-dump',views.fast_dump,name="fast_dump"),
    path('pf-lsp-mis',views.pf_lsp_mis,name="pf_lsp_mis"),
    path('chart',views.line_chart,name="line_chart"),
    #path('forms/mis_form',views.manage_mis,name='Manage_mis'),
    path('update/<int:lrno_field>', views.update, name='update'),
    path('update/updaterecord/<str:invoiceno_field>', views.updaterecord, name='updaterecord'),
    path('show_leci/<int:grn_number>', views.show_leci, name='show_leci'),
    #path('mis-full?<int:searchdata>', views.show_leci, name='show_leci'),
    path('excel/',views.download,name="download"),
    
]
    