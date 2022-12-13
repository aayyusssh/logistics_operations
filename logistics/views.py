from django.db import connection
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.template import loader
from django.urls import reverse
from django.views.generic import TemplateView
from .models import *
from django.views import View  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from logistics.management.commands.add_data import Command
from io import BytesIO
import pandas as pd
from sqlalchemy import create_engine
from chartjs.views.lines import BaseLineChartView,HighchartPlotLineChartView


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        
        return 

    def get_providers(self):
        """Return names of datasets."""
        
        return ["Consider Weight",'Billing Weight']

    def get_data(self):
        """Return 3 datasets to plot."""
        eng = create_engine('sqlite:///db.sqlite3')
        df = pd.read_sql_query('''select SUM("Consider Weight (Provision)"),SUM("Billing Weight") from "Mis Full" group by "Invoice Date" Like '%Apr%';''',con = eng)
        return df.values.tolist()

class LineChartJSONView2(BaseLineChartView):
  def get_labels(self):
    return

  def get_providers(self):
    return['Consider Value', 'Billing Value']

  def get_data(self):
    eng = create_engine('sqlite:///db.sqlite3')
    df = pd.read_sql_query('''select SUM("Consider Value (Provision)"),SUM("Billing Value") from "Mis Full" group by "Invoice Date" Like '%Apr%';''',con = eng)
    return df.values.tolist()

class LineChartJSONView3(BaseLineChartView):
  def get_labels(self):
    eng = create_engine('sqlite:///db.sqlite3')
    df = pd.read_sql_query('''SELECT "PART No." FROM "MIS FULL" limit 10;''',con = eng)
    print(df.values.tolist())
    return df.values.tolist()

  def get_providers(self):
    return["Qty.","PKG"]

  def get_data(self):
    eng = create_engine('sqlite:///db.sqlite3')
    df = pd.read_sql_query('''SELECT "qty.","pkg","qty.","mb02 Qty.","pkg","qty.","actual wt. (KG)","pkg","billing weight","billing value" FROM "MIS FULL" limit 2;''',con = eng)
    return df.values.tolist()

line_chart = TemplateView.as_view(template_name='home/index.html')
line_chart_json = LineChartJSONView.as_view()
line_chart2_json = LineChartJSONView2.as_view()
line_chart3_json = LineChartJSONView3.as_view()

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('tables')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('tables')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('tables')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/logi.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def tables(request):
  template = loader.get_template('home/tables.html')
  return HttpResponse(template.render({}, request))

def Mis(request):
 if request.method == 'POST':
  excel = request.FILES.get('excel').read()
  if(request.POST.get('re_upload')):
   msg = Command.re_mis(excel)
   print(msg)
   if msg == 'Error Occurred Correct Your Data':
       messages.error(request,msg)
       excel = None
       
   #Command.query(excel)
  if (request.POST.get('upload')):
   msg = Command.mis(excel)
   print(msg)
   if msg == 'Error Occurred Correct Your Data':
      messages.error(request,msg)
      excel = None
     
 mis = MIS.objects.all()
 paginator = Paginator(mis,500)
 page = request.GET.get('page')
 p = paginator.get_page(page)
 try:
  numbers = paginator.page(page)
 except PageNotAnInteger:
  numbers = paginator.page(1)
 except EmptyPage:
  numbers = paginator.page(paginator.num_pages)
 col = [f.name for f in MIS._meta.get_fields()]
 template = loader.get_template('home/tables/mis.html')
 context = {
   'mis': numbers,
   'col': col,
  }
 
 return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def Mis_Full(request):
  eng = create_engine('sqlite:///db.sqlite3')
  if(request.GET.get('update_btn')):
    df = pd.read_sql_query('''select * from mis as x left join "Grn Dump" as y on x."Invoice No." = y."Grn Reference" and x."Part No." = y.Material and x."Qty." = y."GR Qty.";''', con = eng)
    #df.drop([],axis=1,inplace=True)
    df["Grn Number"] = pd.to_numeric(df['Grn Number'], errors='coerce').astype('Int64')
    df["MB02 Qty."] = pd.to_numeric(df['MB02 Qty.'], errors='coerce').astype('Int64')
    df['Part No.'] = df['Part No.'].astype(str).apply(lambda x: x.replace('.0',''))
    df.to_sql(MisFull._meta.db_table,if_exists='replace',con=eng,index=False)
    #df2 = pd.read_sql_query('''SELECT "Material Document", "VENDOR DESCRIPTION" FROM "Grn Dump" as x left join "Vendor Master" as y on x.Vendor = y.Vendor;''',con=eng)
    #df2.to_sql("grnvendor",if_exists='replace',con= eng,index=False)
    df2 = pd.read_sql_query('''SELECT * FROM "MIS FULL" as x left join "LECI DUMP" as y on x.LECI = y."LECI No";''',con=eng)
    #df2.rename(columns={"Material Document": "MD"},inplace=True)
    #df2.to_sql("grnleci",if_exists='replace',con= eng,index=False)
    #df2 = pd.read_sql_query('''SELECT * FROM grnvendor as x left join grnleci as y on x."Material Document" = y.MD;''',con=eng)
    #df2.drop("MD",axis=1,inplace=True)
    df2.insert(23,"Transporter",'')
    df2.to_sql(MisFull._meta.db_table,if_exists='replace',con= eng,index=False)
    
    #df3 = pd.read_sql_query('''SELECT * FROM "MIS FULL" as x left join grnvendor as y on x."Grn Number" = y."Material Document";''',con=eng)
    
    #df3.drop(["Material Document","Vendor Name"],axis = 1, inplace = True)
    #df3.rename(columns={"VENDOR DESCRIPTION":"Vendor Name"},inplace=True)

    #df3.to_sql(MisFull._meta.db_table,if_exists='replace',con=eng,index=False)
    try:
      pd.read_sql_query('''UPDATE "MIS FULL" SET Transporter = CASE WHEN "LECI LSP NAME" = "" THEN "TEXT FOR LOADING" ELSE "LECI LSP NAME"  END;''',con= eng)
    except Exception as e:
      print(e)
    df3 = pd.read_sql_query('''SELECT * FROM "MIS FULL" as x left join "inco terms" as y on x."Purchase Order" = y."PO No";''',con= eng)
    df3.insert(28,"Rate",'')
    df3.to_sql(MisFull._meta.db_table,if_exists='replace',con=eng,index=False)
    df3 = pd.read_sql_query('''SELECT * FROM "MIS FULL" as x left join "Origin State" as y on x."Location Code" = y."ORIGIN";''',con= eng)
    df3.to_sql(MisFull._meta.db_table,if_exists='replace',con=eng,index=False)
    df3 = pd.read_sql_query('''SELECT * FROM "MIS FULL" as x left join "Rate Master" as y on x."Origin State Name" = y."State Description";''',con= eng)
    #df3['LR dt.'] = df3['LR dt.'].dt.strftime('%d-%b-%Y')
    df3.to_sql(MisFull._meta.db_table,if_exists='replace',con=eng,index=False)
    try:
      pd.read_sql_query('''update "MIS FULL" SET Rate = CASE WHEN "Lr dt." LIKE "%Apr%" THEN "Apr-22" WHEN "Lr dt." LIKE "%May%" THEN "MAy-22" WHEN "Lr dt." LIKE "%Jun%" THEN "Jun-22" WHEN "Lr dt." LIKE "%Jul%" THEN "Jul-22" WHEN "Lr dt." LIKE "%Aug%" THEN "Aug-22" WHEN "Lr dt." LIKE "%Sep%" THEN "Sep-22" WHEN "Lr dt." LIKE "%Oct%" THEN "Oct-22" WHEN "Lr dt." LIKE "%Nov%" THEN "Nov-22" WHEN "Lr dt." LIKE "%Dec%" THEN "Dec-22" ELSE NULL END;''',con= eng)
    except Exception as e:
      print(e)
    df3 = pd.read_sql_query('''SELECT * FROM "MIS FULL" as x left join "transporter Master" as y on x."Transporter Name" = y."LSP Short Name";''',con=eng)
    df3.to_sql(MisFull._meta.db_table,if_exists='replace',con=eng,index=False)
    df3 = pd.read_sql_query('''SELECT * FROM "MIS FULL" as x left join "Weight Master" as y on x."Part No." = y."Wt Part No." and x.vendor = y."Supplier Code";''',con= eng)
    df3.to_sql(MisFull._meta.db_table,if_exists='replace',con=eng,index=False)
    df3 = pd.read_sql_query('''SELECT * FROM "MIS FULL" as x left join "CBM/CFT" as y on x."LSP Code" = y."LSP Code" and y."Activity CBM CFT" = "PTL";''',con= eng)
    df3.to_sql(MisFull._meta.db_table,if_exists='replace',con=eng,index=False)
    df3 = pd.read_sql_query('''SELECT * FROM "MIS FULL";''',con=eng)
    df3["Weight/Part"] = pd.to_numeric('',errors='coerce').astype('float')
    df3["Consider Weight (Provision)"] = pd.to_numeric('',errors='coerce').astype('float')
    df3["Billing Weight"]  = pd.to_numeric('',errors='coerce').astype('float')
    df3["Consider Value (Provision)"] = pd.to_numeric('',errors='coerce').astype('float')
    df3["Billing Value"] = pd.to_numeric('',errors='coerce').astype('float')
    df3["Actual Wt. (KG)"] = pd.to_numeric(df3['Actual Wt. (KG)'], errors='coerce').astype('float')
    df3["LR dt."] = pd.to_datetime(df3["LR dt."],format='%d-%b-%Y')
    df3.to_sql(MisFull._meta.db_table,if_exists='replace',con=eng,index=False)
    df3 = pd.read_sql_query('''SELECT * FROM "MIS FULL" ORDER BY "LR No.", "LR dt." ASC;''',con=eng)
    df3.to_sql(MisFull._meta.db_table,if_exists='replace',con=eng,index=False)
    try:
        pd.read_sql_query('''UPDATE "MIS FULL" SET "Wt/CFT volumetric PTL" = ROUND((("L (mm)"/304.8) * ("W (mm)"/304.8) * ("H (mm)"/304.8))*"CFT/CBM",5);''',con=eng)
    except Exception as e:
      print(e)
    try:
        pd.read_sql_query('''UPDATE "MIS FULL" SET "Wt/CFT against gross wt PTL" = "Gross Wt.";''',con=eng)
    except Exception as e:
      print(e)
    try:
        pd.read_sql_query('''UPDATE "MIS FULL" SET "Chargeable CFT for PTL" = MAX("Wt/CFT volumetric PTL","Wt/CFT against gross wt PTL");''',con=eng)
    except Exception as e:
      print(e)
    try:
        pd.read_sql_query('''UPDATE "MIS FULL" SET "Wt./Part PTL" = ROUND("Chargeable CFT for PTL"/"Qty./Box",5);''',con=eng)
    except Exception as e:
      print(e)
    try:
        pd.read_sql_query('''UPDATE "MIS FULL" SET "Weight/Part" = ROUND("Chargeable CFT for PTL"/"Qty./Box",5);''',con=eng)
    except Exception as e:
      print(e)
    
    try:
      pd.read_sql_query('''UPDATE "MIS FULL" SET "Consider Weight (Provision)" = CASE WHEN "Weight/Part">0 THEN MAX("Weight/Part" * Rate,50) ELSE MAX("Actual Wt. (KG)",50)END WHERE "Invoice No." in (SELECT "Invoice No." FROM "MIS FULL" GROUP BY "LR No.");''',con= eng)
    except Exception as e:
      print(e)
    try:
      pd.read_sql_query('''UPDATE "MIS FULL" SET "Billing Weight" = CASE WHEN "Weight/Part">0 THEN "Consider Weight (Provision)" ELSE 50 END WHERE "Invoice No." in (SELECT "Invoice No." FROM "MIS FULL" GROUP BY "LR No.");''',con= eng)
    except Exception as e:
      print(e)
    try:
       pd.read_sql_query('''UPDATE "MIS FULL" SET "Consider Value (Provision)" = "Rate"*"Consider Weight (Provision)";''',con= eng)
    except Exception as e:
       print(e)
    try:
       pd.read_sql_query('''UPDATE "MIS FULL" SET "Billing Value" = "Rate"*"Billing Weight";''',con= eng)
    except Exception as e:
       print(e)
    df3 = pd.read_sql_query('''SELECT * FROM "MIS FULL";''',con = eng)
    #df3.drop(["Text for Loading","LSP Name","Apr-22","May-22","Jun-22","Jul-22","Aug-22","Sep-22","Oct-22","Nov-22","Dec-22","Jan-23","Feb-23","Mar-23","ORIGIN","Origin Full Name","Origin State Name","Material Document","Material Description","Inv. Dt.","GR Qty.","Mov","Str Loc.","LECI","Purchase Order","Vendor","LECI No","RFID No","Check Point","Chkin Date","Chk Time","Truck's/Car's License Plate No.","First Name","Last Name","NO","RI","Rel Date","Rel Time","Release by","Out date","Out time","Out by","TAT(HRS)","Weight","Text for Loading","LSP Name","Posting Date","Plant","GRN Amount","Part No","V_Code","PO No","Vendor Name"],axis = 1, inplace = True)
    df3["Grn Number"] = pd.to_numeric(df3['Grn Number'], errors='coerce').astype('Int64')
    df3["MB02 Qty."] = pd.to_numeric(df3['MB02 Qty.'], errors='coerce').astype('Int64')
    #df3["LR dt."] = pd.to_datetime(df3["LR dt."],format='%d-%b-%Y')
    #df3['Consider Weight'] = df3['Consider Weight'].astype(str).apply(lambda x: x.replace('.0',''))
    df3.to_sql(MisFull._meta.db_table,if_exists='replace',con=eng,index=False)
    df3 = pd.read_sql_query('''SELECT * FROM "Mis FULL" as x left join "LR BILL" as y on x."Lr No." = y."LR No";''',con = eng)
    df3["Bill No"] = pd.to_numeric(df3['Bill No'], errors='coerce').astype('Int64')
    df3.to_sql(MisFull._meta.db_table,if_exists='replace',con=eng,index=False)
    df2 = pd.read_sql_query('''SELECT * FROM "SVPS" Group By "InvoiceNo";''',con=eng)
    df2.to_sql('SVPSGrp',if_exists='replace',con=eng,index=False)
    df3 = pd.read_sql_query('''SELECT * FROM "MIS FULL" as x left join "SVPSGrp" as y on x."LSP Code" = y."VendorCode" and x."Bill No" = y."InvoiceNo";''',con=eng)
    df3["Bill Status"] = df3["Remark"]
    #df3.drop(["Remark"],axis=1,inplace=True)
    df3["Bill No"] = pd.to_numeric(df3['Bill No'], errors='coerce').astype('Int64')
    df3.to_sql(MisFull._meta.db_table,if_exists='replace',con=eng,index=False)
    df3 = pd.read_sql_query('''SELECT * FROM "MIS FULL" as x left join SES as y on x."LSP Code" = y."V_Code" and x."Bill No" = y."SES Reference";''',con=eng)
    df3["Delivery Date"] = pd.to_datetime(df3["Delivery Date"])
    df3["Delivery Date"] = df3['Delivery Date'].dt.strftime("%d-%b-%Y")
    df3["Invoice Date"] = pd.to_datetime(df3["Invoice Date"])
    df3["Invoice Date"] = df3['Invoice Date'].dt.strftime("%d-%b-%Y")
    df3["Created on"] = pd.to_datetime(df3["Created on"])
    df3["Created on"] = df3['Created on'].dt.strftime("%d-%b-%Y")
    df3["Changed on"] = pd.to_datetime(df3["Changed on"])
    df3["Changed on"] = df3['Changed on'].dt.strftime("%d-%b-%Y")
    df3["LR dt."] = pd.to_datetime(df3["LR dt."])
    df3['LR dt.'] = df3['LR dt.'].dt.strftime('%d-%b-%Y')
    df3["Grn Number"] = pd.to_numeric(df3['Grn Number'], errors='coerce').astype('Int64')
    df3["MB02 Qty."] = pd.to_numeric(df3['MB02 Qty.'], errors='coerce').astype('Int64')
    df3['Part No.'] = df3['Part No.'].astype(str).apply(lambda x: x.replace('.0',''))
    df3["Bill No"] = pd.to_numeric(df3['Bill No'], errors='coerce').astype('Int64')
    #df3["Weight/Part"] = pd.to_numeric(df3['Weight/Part'],errors='coerce').astype('float')
    #df3["Consider Weight"] = pd.to_numeric(df3['Consider Weight'],errors='coerce').astype('float')
    #df3["Value"] = pd.to_numeric(df3['Value'],errors='coerce').astype('float')
    df3["Entry Sheet"] = pd.to_numeric(df3["Entry Sheet"],errors='coerce').astype('Int64')
    df3["Actual Wt. (KG)"] = pd.to_numeric(df3['Actual Wt. (KG)'], errors='coerce').astype('float')
    df4 = df3[['LSP Code','Transporter Name','Activity (from manual-Vinsum MIS)','PAYMENT TYPE (from master)','Activity Status','Location','Delivery Date','Grn Number','LR no.','LR dt.','LR Time','Consignor','Consignee','Consignor Location','Location Code','State','Invoice No.','Invoice Date','Vendor PO No','Part No.','PKG','PKG TYPE','Qty.','Actual Wt. (KG)','Transporter','Material','Grn Reference','MB02 Qty.','Inco-Terms','State Description','Weight/Part','Rate','Consider Weight (Provision)','Billing Weight','Consider Value (Provision)','Billing Value','Bill No','Bill Status','Entry Sheet','Created on','Changed on','AccIn']]
    df4.rename(columns={'LSP Code': 'Transporter Code', 'Entry Sheet': 'SES No',"Created on":"SES Date","Changed on":"2nd Ref","AccIn":"SES Status"}, inplace=True)
    df4.to_sql(MisFull._meta.db_table,if_exists = 'replace', con=eng,index=False) 
  if(request.GET.get('match')):
     df = pd.read_sql_query('''select * from mis as x left join "Grn Dump" as y on x."Invoice No." = y."Grn Reference" and x."Part No." = y.Material and x."Qty." = y."GR Qty.";''', con = eng)
     df.to_sql(MisFull._meta.db_table,if_exists='replace',con=eng,index=False)
     try:
         eng = create_engine('sqlite:///db.sqlite3')
         pd.read_sql_query('''update "MIS FULL" SET "Grn Number" = "Material Document";''',con= eng)
        
     except Exception as e:
         print(e)
     #print(pd.read_sql_query('''SELECT "Grn Number" FROM "MIS FULL" LIMIT 10;''',con= eng))
     df = pd.read_sql_query('''SELECT * FROM "MIS FULL" as x left join "inco terms" as y on x."Purchase Order" = y."PO No";''',con= eng)
     df.to_sql(MisFull._meta.db_table,if_exists='replace',con=eng,index=False)
     #df2 = pd.read_sql_query('''SELECT "Material Document", "VENDOR DESCRIPTION" FROM "Grn Dump" as x left join "Vendor Master" as y on x.Vendor = y.Vendor;''',con=eng)
     #df2.to_sql("grnvendor",if_exists='replace',con= eng,index=False)
     
     df2 = pd.read_sql_query('''SELECT * FROM "MIS FULL" as x left join "LECI DUMP" as y on x.LECI = y."LECI No";''',con=eng)
     #df2.rename(columns={"Material Document": "MD"},inplace=True)
     #df2.to_sql("grnleci",if_exists='replace',con= eng,index=False)
     #df2 = pd.read_sql_query('''SELECT * FROM "MIS FULL" as x left join grnleci as y on x."Grn Number" = y.MD;''',con=eng)
     #df2.drop("MD",axis=1,inplace=True)
     df2.insert(23,"Transporter",'')
     df2.to_sql(MisFull._meta.db_table,if_exists='replace',con= eng,index=False)
     
     #df3 = pd.read_sql_query('''SELECT * FROM "MIS FULL" as x left join grnvendor as y on x."Grn Number" = y."Material Document";''',con=eng)
     
     #df3.drop(["Material Document","Vendor Name"],axis = 1, inplace = True)
     #df3.rename(columns={"VENDOR DESCRIPTION":"Vendor Name"},inplace=True)
     

     #df3.to_sql(MisFull._meta.db_table,if_exists='replace',con=eng,index=False)
     try:
       pd.read_sql_query('''UPDATE "MIS FULL" SET Transporter = CASE WHEN "LECI LSP NAME" = "" THEN "TEXT FOR LOADING" ELSE "LECI LSP NAME"  END;''',con= eng)
     except Exception as e:
       print(e)

     df3 = pd.read_sql_query('''SELECT * FROM "MIS FULL" as x left join "Origin State" as y on x."Location Code" = y."ORIGIN";''',con= eng)
     df3.to_sql(MisFull._meta.db_table,if_exists='replace',con=eng,index=False)
     df3 = pd.read_sql_query('''SELECT * FROM "MIS FULL" as x left join "Rate Master" as y on x."Origin State Name" = y."State Description";''',con= eng)
    #df3['LR dt.'] = df3['LR dt.'].dt.strftime('%d-%b-%Y')
     df3.insert(28,"Rate",'')
     df3.to_sql(MisFull._meta.db_table,if_exists='replace',con=eng,index=False)
     try:
       pd.read_sql_query('''update "MIS FULL" SET Rate = CASE WHEN "Lr dt." LIKE "%Apr%" THEN "Apr-22" WHEN "Lr dt." LIKE "%May%" THEN "MAy-22" WHEN "Lr dt." LIKE "%Jun%" THEN "Jun-22" WHEN "Lr dt." LIKE "%Jul%" THEN "Jul-22" WHEN "Lr dt." LIKE "%Aug%" THEN "Aug-22" WHEN "Lr dt." LIKE "%Sep%" THEN "Sep-22" WHEN "Lr dt." LIKE "%Oct%" THEN "Oct-22" WHEN "Lr dt." LIKE "%Nov%" THEN "Nov-22" WHEN "Lr dt." LIKE "%Dec%" THEN "Dec-22" ELSE NULL END;''',con= eng)
     except Exception as e:
       print(e)
     df3 = pd.read_sql_query('''SELECT * FROM "MIS FULL" as x left join "transporter Master" as y on x."Transporter Name" = y."LSP Short Name";''',con=eng)
     df3.to_sql(MisFull._meta.db_table,if_exists='replace',con=eng,index=False)
     df3 = pd.read_sql_query('''SELECT * FROM "MIS FULL" as x left join "Weight Master" as y on x.material = y."Wt Part No." and x.vendor = y."Supplier Code";''',con= eng)
     df3.to_sql(MisFull._meta.db_table,if_exists='replace',con=eng,index=False)
     df3 = pd.read_sql_query('''SELECT * FROM "MIS FULL" as x left join "CBM/CFT" as y on x."LSP Code" = y."LSP Code" and y."Activity CBM CFT" = "PTL";''',con= eng)
     df3["Weight/Part"] = pd.to_numeric('',errors='coerce').astype('float')
     df3["Consider Weight (Provision)"] = pd.to_numeric('',errors='coerce').astype('float')
     df3["Billing Weight"]  = pd.to_numeric('',errors='coerce').astype('float')
     df3["Consider Value (Provision)"] = pd.to_numeric('',errors='coerce').astype('float')
     df3["Billing Value"] = pd.to_numeric('',errors='coerce').astype('float')
     df3["Value"] = pd.to_numeric('',errors='coerce').astype('float')
     df3["Actual Wt. (KG)"] = pd.to_numeric(df3['Actual Wt. (KG)'], errors='coerce').astype('float')
     df3["LR dt."] = pd.to_datetime(df3["LR dt."],format='%d-%b-%Y')
     df3.to_sql(MisFull._meta.db_table,if_exists='replace',con=eng,index=False)
     try:
         pd.read_sql_query('''UPDATE "MIS FULL" SET "Wt/CFT volumetric PTL" = ROUND((("L (mm)"/304.8) * ("W (mm)"/304.8) * ("H (mm)"/304.8))*"CFT/CBM",5);''',con=eng)
     except Exception as e:
       print(e)
     try:
         pd.read_sql_query('''UPDATE "MIS FULL" SET "Wt/CFT against gross wt PTL" = "Gross Wt.";''',con=eng)
     except Exception as e:
       print(e)
     try:
         pd.read_sql_query('''UPDATE "MIS FULL" SET "Chargeable CFT for PTL" = MAX("Wt/CFT volumetric PTL","Wt/CFT against gross wt PTL");''',con=eng)
     except Exception as e:
       print(e)
     try:
         pd.read_sql_query('''UPDATE "MIS FULL" SET "Wt./Part PTL" = ROUND("Chargeable CFT for PTL"/"Qty./Box",5);''',con=eng)
     except Exception as e:
       print(e)
     try:
         pd.read_sql_query('''UPDATE "MIS FULL" SET "Weight/Part" = ROUND("Chargeable CFT for PTL"/"Qty./Box",5);''',con=eng)
     except Exception as e:
       print(e)
     try:
        pd.read_sql_query('''UPDATE "MIS FULL" SET "Consider Weight (Provision)" = CASE WHEN "Weight/Part">0 THEN MAX("Weight/Part" * Rate,50) ELSE MAX("Actual Wt. (KG)",50)END WHERE "Invoice No." in (SELECT "Invoice No." FROM "MIS FULL" GROUP BY "LR No.");''',con= eng)
     except Exception as e:
       print(e)
     try:
      pd.read_sql_query('''UPDATE "MIS FULL" SET "Billing Weight" = CASE WHEN "Weight/Part">0 THEN "Consider Weight (Provision)" ELSE 50 END WHERE "Invoice No." in (SELECT "Invoice No." FROM "MIS FULL" GROUP BY "LR No.");''',con= eng)
     except Exception as e:
       print(e)
     try:
       pd.read_sql_query('''UPDATE "MIS FULL" SET "Consider Value (Provision)" = "Rate"*"Consider Weight (Provision)";''',con= eng)
     except Exception as e:
       print(e)
     try:
       pd.read_sql_query('''UPDATE "MIS FULL" SET "Billing Value" = "Rate"*"Billing Weight";''',con= eng)
     except Exception as e:
       print(e)
     #df3.to_sql("MISS",if_exists='replace',con=eng,index=False)
     df3 = pd.read_sql_query('''SELECT * FROM "MIS FULL";''',con = eng)
     #df3.drop(["Text for Loading","LSP Name","Apr-22","May-22","Jun-22","Jul-22","Aug-22","Sep-22","Oct-22","Nov-22","Dec-22","Jan-23","Feb-23","Mar-23","ORIGIN","Origin Full Name","Origin State Name","Material Document","Material Description","Inv. Dt.","GR Qty.","Mov","Str Loc.","LECI","Purchase Order","Vendor","LECI No","RFID No","Check Point","Chkin Date","Chk Time","Truck's/Car's License Plate No.","First Name","Last Name","NO","RI","Rel Date","Rel Time","Release by","Out date","Out time","Out by","TAT(HRS)","Weight","Text for Loading","LSP Name","Posting Date","Plant","GRN Amount","Part No","V_Code","PO No","Vendor Name"],axis = 1, inplace = True)
     df3["Grn Number"] = pd.to_numeric(df3['Grn Number'], errors='coerce').astype('Int64')
     df3["MB02 Qty."] = pd.to_numeric(df3['MB02 Qty.'], errors='coerce').astype('Int64')
     df3["Actual Wt. (KG)"] = pd.to_numeric(df3['Actual Wt. (KG)'], errors='coerce').astype('float')
     #df3['Consider Weight'] = df3['Consider Weight'].astype(str).apply(lambda x: x.replace('.0',''))
     #df3["LR dt."] = pd.to_datetime(df3["LR dt."],format='%d-%b-%Y')
     df3.to_sql(MisFull._meta.db_table,if_exists='replace',con=eng,index=False)
     df3 = pd.read_sql_query('''SELECT * FROM "Mis FULL" as x left join "LR BILL" as y on x."Lr No." = y."LR No";''',con = eng)
     df3["Bill No"] = pd.to_numeric(df3['Bill No'], errors='coerce').astype('Int64')
     df3.to_sql(MisFull._meta.db_table,if_exists='replace',con=eng,index=False)
     df2 = pd.read_sql_query('''SELECT * FROM "SVPS" Group By "InvoiceNo";''',con=eng)
     df2.to_sql('SVPSGrp',if_exists='replace',con=eng,index=False)
     df3 = pd.read_sql_query('''SELECT * FROM "MIS FULL" as x left join "SVPSGrp" as y on x."LSP Code" = y."VendorCode" and x."Bill No" = y."InvoiceNo";''',con=eng)
     df3["Bill Status"] = df3["Remark"]
     df3.drop(["Remark"],axis=1,inplace=True)
     df3["Bill No"] = pd.to_numeric(df3['Bill No'], errors='coerce').astype('Int64')
     df3.to_sql(MisFull._meta.db_table,if_exists='replace',con=eng,index=False)
     df3 = pd.read_sql_query('''SELECT * FROM "MIS FULL" as x left join "SVPSGrp" as y on x."LSP Code" = y."VendorCode" and x."Bill No" = y."InvoiceNo";''',con=eng)
     
     df3.to_sql(MisFull._meta.db_table,if_exists='replace',con=eng,index=False)
     df3 = pd.read_sql_query('''SELECT * FROM "MIS FULL" as x left join SES as y on x."LSP Code" = y."V_Code" and x."Bill No" = y."SES Reference";''',con=eng)
     df3["Delivery Date"] = pd.to_datetime(df3["Delivery Date"])
     df3["Delivery Date"] = df3['Delivery Date'].dt.strftime("%d-%b-%Y")
     df3["Invoice Date"] = pd.to_datetime(df3["Invoice Date"])
     df3["Invoice Date"] = df3['Invoice Date'].dt.strftime("%d-%b-%Y")
     df3["Created on"] = pd.to_datetime(df3["Created on"])
     df3["Created on"] = df3['Created on'].dt.strftime("%d-%b-%Y")
     df3["Changed on"] = pd.to_datetime(df3["Changed on"])
     df3["Changed on"] = df3['Changed on'].dt.strftime("%d-%b-%Y")
     df3["LR dt."] = pd.to_datetime(df3["LR dt."])
     df3['LR dt.'] = df3['LR dt.'].dt.strftime('%d-%b-%Y')
     df3["Grn Number"] = pd.to_numeric(df3['Grn Number'], errors='coerce').astype('Int64')
     df3["MB02 Qty."] = pd.to_numeric(df3['MB02 Qty.'], errors='coerce').astype('Int64')
     df3['Part No.'] = df3['Part No.'].astype(str).apply(lambda x: x.replace('.0',''))
     df3["Bill No"] = df3['Bill No'].astype(str).apply(lambda x: x.replace('.0',''))
     #df3["Weight/Part"] = pd.to_numeric(df3["Weight/Part"],errors='coerce').astype('float')
     #df3["Consider Weight"] = pd.to_numeric(df3["Consider Weight"],errors='coerce').astype('float')
     #df3["Value"] = pd.to_numeric(df3["Value"],errors='coerce').astype('float')
     df3["Entry Sheet"] = pd.to_numeric(df3["Entry Sheet"],errors='coerce').astype('Int64')
     #df3["Reference"] = pd.to_numeric(df3["Reference"],errors='coerce').astype('Int64')
     df3["Actual Wt. (KG)"] = pd.to_numeric(df3['Actual Wt. (KG)'], errors='coerce').astype('float')
     df4 = df3[['LSP Code','Transporter Name','Activity (from manual-Vinsum MIS)','PAYMENT TYPE (from master)','Activity Status','Location','Delivery Date','Grn Number','LR no.','LR dt.','LR Time','Consignor','Consignee','Consignor Location','Location Code','State','Invoice No.','Invoice Date','Vendor PO No','Part No.','PKG','PKG TYPE','Qty.','Actual Wt. (KG)','Transporter','Material','Grn Reference','MB02 Qty.','Inco-Terms','State Description','Weight/Part','Rate','Consider Weight (Provision)','Billing Weight','Consider Value (Provision)','Billing Value','Bill No','Bill Status','Entry Sheet','Created on','Changed on','AccIn']]
     df4.rename(columns={'LSP Code': 'Transporter Code', 'Entry Sheet': 'SES No',"Created on":"SES Date","Changed on":"2nd Ref","AccIn":"SES Status"}, inplace=True)
     df4.to_sql(MisFull._meta.db_table,if_exists = 'replace', con=eng,index=False) 
     #df3.drop(["Material Document","Material Description","Inv. Dt.","GR Qty.","Mov","Str Loc.","LECI","Purchase Order","Vendor","Posting Date","Plant","GRN Amount","Part No","V_Code","PO No"],axis=1,inplace=True)
     updated_mis = pd.read_sql_query('''select "Transporter Name", "Activity (from manual-Vinsum MIS)","PAYMENT TYPE (from master)","Activity Status", "Location", "Delivery Date", "Grn Number", "LR no.", "LR dt.", "LR Time", "Consignor", "Consignee","Consignor Location", "Location Code", "State", "Invoice No.", "Invoice Date", "Vendor PO No", "Part No.", "PKG", "PKG TYPE", "Qty.", "Actual Wt. (KG)" from "MIS FULL";''',con=eng)
     updated_mis["Grn Number"] = pd.to_numeric(updated_mis['Grn Number'], errors='coerce').astype('Int64')
     updated_mis.to_sql(MIS._meta.db_table,if_exists='replace',con=eng,index=False)
  if request.GET.get('billno'):
    search = request.GET.get('searchdata')
    print(search)
    misfull = MisFull.objects.filter(bill_no_field=search)
    col = [f.name for f in MisFull._meta.get_fields()]
    template = loader.get_template('home/tables/mis_full.html')
    context = {
   'mis': misfull,
   'col':col,
  }
    return HttpResponse(template.render(context, request))
  if request.GET.get('lrno'):
    search = request.GET.get('searchdata')
    print(search)
    misfull = MisFull.objects.filter(lr_no_field=search)
    col = [f.name for f in MisFull._meta.get_fields()]
    template = loader.get_template('home/tables/mis_full.html')
    context = {
   'mis': misfull,
   'col':col,
  }
    return HttpResponse(template.render(context, request))
  if request.GET.get('partno'):
    search = request.GET.get('searchdata')
    print(search)
    misfull = MisFull.objects.filter(part_no_field=search)
    col = [f.name for f in MisFull._meta.get_fields()]
    template = loader.get_template('home/tables/mis_full.html')
    context = {
   'mis': misfull,
   'col':col,
  }
    return HttpResponse(template.render(context, request))
  if request.GET.get('invno'):
    search = request.GET.get('searchdata')
    print(search)
    misfull = MisFull.objects.filter(invoice_no_field=search)
    col = [f.name for f in MisFull._meta.get_fields()]
    template = loader.get_template('home/tables/mis_full.html')
    context = {
   'mis': misfull,
   'col':col,
  }
    return HttpResponse(template.render(context, request))

  misfull = MisFull.objects.all()
  col = [f.name for f in MisFull._meta.get_fields()]
  template = loader.get_template('home/tables/mis_full.html')
  paginator = Paginator(misfull,400)
  page = request.GET.get('page')
  p = paginator.get_page(page)
  try:
   numbers = paginator.page(page)
  except PageNotAnInteger:
   numbers = paginator.page(1)
  except EmptyPage:
   numbers = paginator.page(paginator.num_pages)
  context = {
   'mis': numbers,
   'col':col,
  }
  return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def Vc_no(request):
  vc_no = VC_NO.objects.all().values()
  template = loader.get_template('home/tables/vc_no.html')
  context = {
    'vc_no': vc_no,
  }
  return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def origin_state(request):
  if request.method == 'POST':
    excel = request.FILES.get('excel').read()
    Command.origin(excel)
  origin = OriginState.objects.all()
  col = [f.name for f in OriginState._meta.get_fields()]
  template = loader.get_template('home/tables/origin_state.html')
  context = {
    'origin': origin,
    'col':col,
   }
  
  return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def lr_bill(request):
  if request.method == 'POST':
    excel = request.FILES.get('excel').read()
    Command.lr_bill(excel)
  lrbill = LrBill.objects.all()
  col = [f.name for f in LrBill._meta.get_fields()]
  template = loader.get_template('home/tables/lr_bill.html')
  context = {
    'lrbill': lrbill,
    'col':col,
   }
  
  return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def transporter_master(request):
  if request.method == 'POST':
    excel = request.FILES.get('excel').read()
    Command.transporter(excel)
  transporter = TransporterMaster.objects.all()
  col = [f.name for f in TransporterMaster._meta.get_fields()]
  template = loader.get_template('home/tables/transporter_master.html')
  context = {
    'transporter': transporter,
    'col':col,
   }
  
  return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def po(request):
  if request.method == 'POST':
    excel = request.FILES.get('excel').read()
    Command.po(excel)
  po = Po.objects.all()
  col = [f.name for f in Po._meta.get_fields()]
  template = loader.get_template('home/tables/po.html')
  context = {
    'po': po,
    'col':col,
   }
  
  return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def ses(request):
  if request.method == 'POST':
    excel = request.FILES.get('excel').read()
    Command.ses(excel)
  ses = Ses.objects.all()
  col = [f.name for f in Ses._meta.get_fields()]
  template = loader.get_template('home/tables/ses.html')
  paginator = Paginator(ses,500)
  page = request.GET.get('page')
  p = paginator.get_page(page)
  try:
   numbers = paginator.page(page)
  except PageNotAnInteger:
   numbers = paginator.page(1)
  except EmptyPage:
   numbers = paginator.page(paginator.num_pages)
  context = {
    'ses': numbers,
    'col':col,
   }
  
  return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def fast_dump(request):
  if request.method == 'POST':
    excel = request.FILES.get('excel').read()
    Command.fast_dump(excel)
  fastDump = FastDump.objects.all()
  col = [f.name for f in FastDump._meta.get_fields()]
  template = loader.get_template('home/tables/fast_dump.html')
  paginator = Paginator(fastDump,500)
  page = request.GET.get('page')
  p = paginator.get_page(page)
  try:
   numbers = paginator.page(page)
  except PageNotAnInteger:
   numbers = paginator.page(1)
  except EmptyPage:
   numbers = paginator.page(paginator.num_pages)
  context = {
    'fastDump': numbers,
    'col':col,
   }
  
  return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def pf_lsp_mis(request):
  if request.method == 'POST':
    excel = request.FILES.get('excel').read()
    Command.pf_lsp_mis(excel)
  pflspmis = PfLspMis.objects.all()
  col = [f.name for f in PfLspMis._meta.get_fields()]
  template = loader.get_template('home/tables/Pf_Lsp_Mis.html')
  paginator = Paginator(pflspmis,500)
  page = request.GET.get('page')
  p = paginator.get_page(page)
  try:
   numbers = paginator.page(page)
  except PageNotAnInteger:
   numbers = paginator.page(1)
  except EmptyPage:
   numbers = paginator.page(paginator.num_pages)
  context = {
    'pflspmis': numbers,
    'col': col,
   }
  
  return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def pf_mis(request):
  eng = create_engine('sqlite:///db.sqlite3')
  if request.GET.get('match'):

    df = pd.read_sql_query('''SELECT * FROM 'PF LSP MIS' as x left join 'Fast Dump' as y on x.'Indent No.' = y.'Dump Indent No.';''',con = eng)
    df.to_sql(PfMis._meta.db_table,if_exists='replace',con=eng,index=False)
    df.insert(0,"Consider Pick-up Month",df['Pickup Date'])
    df.insert(1,"Indent Request Month",df['Request Date'])
    df.insert(2,"S. No",'')
    df['S. No'] = df['Indent No.'].ne(df['Indent No.'].shift()).cumsum()
    df["Consider Pick-up Month"] = pd.to_datetime(df["Consider Pick-up Month"])
    df["Consider Pick-up Month"] = df['Consider Pick-up Month'].dt.strftime("%b-%Y")
    df["Indent Request Month"] = pd.to_datetime(df["Indent Request Month"])
    df["Indent Request Month"] = df['Indent Request Month'].dt.strftime("%b-%Y")
    df["Indent Request date "] = pd.to_datetime(df["Indent Request date "])
    df["Indent Request date "] = df['Indent Request date '].dt.strftime("%d-%b-%Y")
    df["Pickup Date"] = pd.to_datetime(df["Pickup Date"])
    df["Pickup Date"] = df['Pickup Date'].dt.strftime("%d-%b-%Y")
    df.to_sql(PfMis._meta.db_table,if_exists='replace',con=eng,index=False)
    df = pd.read_sql_query('''SELECT * FROM "PF Mis" as x left join "Distance Range" as y on x."Vendor Code" = y."Vendor Code ";''',con=eng)
    df["Zone"] = df["Zone for Air/Train"]
    df.to_sql(PfMis._meta.db_table,if_exists='replace',con=eng,index=False)
    df = pd.read_sql_query('''SELECT * FROM "PF Mis" as x left join "Weight Master" as y on x."part number" = y."Wt part no." and x."vendor code" = y."supplier code";''',con=eng)
    df.to_sql(PfMis._meta.db_table,if_exists='replace',con=eng,index=False)
  

  pfmis = PfMis.objects.all()
  col = [f.name for f in PfMis._meta.get_fields()]
  template = loader.get_template('home/tables/pf_mis.html')
  paginator = Paginator(pfmis,500)
  page = request.GET.get('page')
  p = paginator.get_page(page)
  try:
   numbers = paginator.page(page)
  except PageNotAnInteger:
   numbers = paginator.page(1)
  except EmptyPage:
   numbers = paginator.page(paginator.num_pages)
  context = {
    'pfmis': numbers,
    'col': col,
   }
  
  return HttpResponse(template.render(context, request))

@user_passes_test(lambda u: u.is_superuser,login_url='logout')
def distance_range(request):
  if request.method == 'POST':
    excel = request.FILES.get('excel').read()
    Command.distance_range(excel)
  distancerange = DistanceRange.objects.all()
  col = [f.name for f in DistanceRange._meta.get_fields()]
  template = loader.get_template('home/tables/distance_range.html')
  paginator = Paginator(distancerange,500)
  page = request.GET.get('page')
  p = paginator.get_page(page)
  try:
   numbers = paginator.page(page)
  except PageNotAnInteger:
   numbers = paginator.page(1)
  except EmptyPage:
   numbers = paginator.page(paginator.num_pages)
  context = {
    'distancerange': numbers,
    'col':col,
   }
  
  return HttpResponse(template.render(context, request))

@user_passes_test(lambda u: u.is_superuser,login_url='logout')
def rate(request):
  if request.method == 'POST':
    excel = request.FILES.get('excel').read()
    Command.rate(excel)
  Leci = LeciDump.objects.all()
  col = [f.name for f in LeciDump._meta.get_fields()]
  template = loader.get_template('home/tables/rate.html')
  paginator = Paginator(Leci,500)
  page = request.GET.get('page')
  p = paginator.get_page(page)
  try:
   numbers = paginator.page(page)
  except PageNotAnInteger:
   numbers = paginator.page(1)
  except EmptyPage:
   numbers = paginator.page(paginator.num_pages)
  context = {
    'Leci': numbers,
    'col':col,
   }
  
  return HttpResponse(template.render({}, request))

@user_passes_test(lambda u: u.is_superuser,login_url='logout')
def recovery_condition(request):
  if request.method == 'POST':
    excel = request.FILES.get('excel').read()
    Command.recovery_condition(excel)
  Leci = LeciDump.objects.all()
  col = [f.name for f in LeciDump._meta.get_fields()]
  template = loader.get_template('home/tables/recovery_condition.html')
  paginator = Paginator(Leci,500)
  page = request.GET.get('page')
  p = paginator.get_page(page)
  try:
   numbers = paginator.page(page)
  except PageNotAnInteger:
   numbers = paginator.page(1)
  except EmptyPage:
   numbers = paginator.page(paginator.num_pages)
  context = {
    'Leci': numbers,
    'col':col,
   }
  
  return HttpResponse(template.render({}, request))

@user_passes_test(lambda u: u.is_superuser,login_url='logout')
def Leci(request):
  if request.method == 'POST':
    excel = request.FILES.get('excel').read()
    Command.leci(excel)
  Leci = LeciDump.objects.all()
  col = [f.name for f in LeciDump._meta.get_fields()]
  template = loader.get_template('home/tables/Leci.html')
  paginator = Paginator(Leci,500)
  page = request.GET.get('page')
  p = paginator.get_page(page)
  try:
   numbers = paginator.page(page)
  except PageNotAnInteger:
   numbers = paginator.page(1)
  except EmptyPage:
   numbers = paginator.page(paginator.num_pages)
  context = {
    'Leci': numbers,
    'col':col,
   }
  
  return HttpResponse(template.render(context, request))

@user_passes_test(lambda u: u.is_superuser,login_url='logout')
def Grn(request):
  if request.method == 'POST':
    excel = request.FILES.get('excel').read()
    if request.POST.get('append'):
     Command.grn(excel,'append')
     
    if request.POST.get('replace'):
     Command.grn(excel,'replace')
  Grn = GrnDump.objects.all()
  col = [f.name for f in GrnDump._meta.get_fields()]
 
  template = loader.get_template('home/tables/Grn.html')

  paginator = Paginator(Grn,1000)
  page = request.GET.get('page')
  p = paginator.get_page(page)
 
  try:
   numbers = paginator.page(page)
  except PageNotAnInteger:
   numbers = paginator.page(1)
  except EmptyPage:
   numbers = paginator.page(paginator.num_pages)
  context = {
    'Grn': numbers,
    'col':col,
   }

  return HttpResponse(template.render(context, request))


@user_passes_test(lambda u: u.is_superuser,login_url='logout')
def Vendor(request):
  if request.method == 'POST':
    excel = request.FILES.get('excel').read()
    Command.vendor(excel)
  vendor = VendorMaster.objects.all().values()
  col = [f.name for f in VendorMaster._meta.get_fields()]
  template = loader.get_template('home/tables/vendor.html')
  paginator = Paginator(vendor,500)
  page = request.GET.get('page')
  p = paginator.get_page(page)
  try:
   numbers = paginator.page(page)
  except PageNotAnInteger:
   numbers = paginator.page(1)
  except EmptyPage:
   numbers = paginator.page(paginator.num_pages)
  context = {
    'vendor': numbers,
    'col':col,
   }
  return HttpResponse(template.render(context, request))

@user_passes_test(lambda u: u.is_superuser,login_url='login')
def Part(request):
  part = PartMaster.objects.all().values()
  col = [f.name for f in PartMaster._meta.get_fields()]
  excel = None
  excel = request.POST.get('excel')
  template = loader.get_template('home/tables/part.html')
  context = {
    'part': part,
    'col':col,
   }
  if excel != None:
   Command.part(excel)
   excel = None
  return HttpResponse(template.render(context, request))  

@user_passes_test(lambda u: u.is_superuser,login_url='logout')
def update(request,lrno_field):
  mymis = MIS.objects.filter(lrno_field = lrno_field).values()
  
  template = loader.get_template('home/tables/update_table.html')
  context = {'mymis': mymis}
  return HttpResponse(template.render(context,request))

@user_passes_test(lambda u: u.is_superuser,login_url='logout')
def updaterecord(request,invoiceno_field):
  transportername = request.POST['transportername']
  activity_frommanual_vinsummis_field = request.POST['activity_frommanual_vinsummis_field']
  paymenttype_frommaster_field = request.POST['paymenttype_frommaster_field']
  activitystatus = request.POST['activitystatus']
  location = request.POST['location']
  deliverydate = request.POST['deliverydate']
  grnnumber = request.POST['grnnumber']
  lrno_field = request.POST['lrno_field']
  lrdt_field = request.POST['lrdt_field']
  lrtime = request.POST['lrtime']
  consignor = request.POST['consignor']
  consignee = request.POST['consignee']
  consignorlocation = request.POST['consignorlocation']
  locationcode = request.POST['locationcode']
  state = request.POST['state']
  invoiceno = request.POST['invoiceno_field']
  invoicedate = request.POST['invoicedate']
  vendorpono = request.POST['vendorpono']
  partno_field = request.POST['partno_field']
  pkg = request.POST['pkg']
  pkgtype = request.POST['pkgtype']
  qty_field = request.POST['qty_field']
  actualwt_kg_field = request.POST['actualwt_kg_field']
  mis = MIS.objects.get(invoiceno_field=invoiceno_field)
  mis.transportername = transportername
  mis.activity_frommanual_vinsummis_field = activity_frommanual_vinsummis_field
  mis.paymenttype_frommaster_field = paymenttype_frommaster_field
  mis.activitystatus = activitystatus
  mis.location = location
  mis.deliverydate = deliverydate
  mis.grnnumber = grnnumber
  mis.lrno_field = lrno_field
  mis.lrdt_field = lrdt_field
  mis.lrtime = lrtime
  mis.consignor = consignor
  mis.consignee = consignee 
  mis.consignorlocation = consignorlocation
  mis.locationcode = locationcode
  mis.state = state
  mis.invoiceno_field = invoiceno
  mis.invoicedate = invoicedate
  mis.vendorpono = vendorpono
  mis.partno_field = partno_field
  mis.pkg = pkg
  mis.pkgtype = pkgtype
  mis.qty_field = qty_field
  mis.actualwt_kg_field = actualwt_kg_field 
  mis.save()
  return HttpResponseRedirect(reverse('update',args=(lrno_field,)))

@user_passes_test(lambda u: u.is_superuser, login_url= 'logout')
def inco_terms(request):
  if request.method == 'POST':
    excel = request.FILES.get('excel').read()
    Command.inco_terms(excel)
  inco = IncoTerms.objects.all()
  col = [f.name for f in IncoTerms._meta.get_fields()]
  paginator = Paginator(inco,500)
  page = request.GET.get('page')
  p = paginator.get_page(page)
  try:
   numbers = paginator.page(page)
  except PageNotAnInteger:
   numbers = paginator.page(1)
  except EmptyPage:
   numbers = paginator.page(paginator.num_pages)
  context = {"inco": numbers,
             "col": col
                       }
  template = loader.get_template('home/tables/inco_terms.html')
  
  return HttpResponse(template.render(context, request))

@user_passes_test(lambda u: u.is_superuser,login_url='logout')
def rate_master(request):
  if request.method == 'POST':
    excel = request.FILES.get('excel').read()
    Command.rate_master(excel)
  inco = IncoTerms.objects.all()
  col = [f.name for f in IncoTerms._meta.get_fields()]
  context = {"inco": inco,
             "col": col
                       }
  template = loader.get_template('home/tables/rate_master.html')
  
  return HttpResponse(template.render({}, request))

@user_passes_test(lambda u: u.is_superuser,login_url='logout')
def inbound_shipment(request):
  if request.method == 'POST':
    excel = request.FILES.get('excel').read()
    Command.inbound_shipment(excel)
  inbound = InboundShipment.objects.all()
  col = [f.name for f in InboundShipment._meta.get_fields()]
  context = {"inbound": inbound,
             "col": col
                       }
  template = loader.get_template('home/tables/inbound_shipment.html')
  
  return HttpResponse(template.render(context, request))

@user_passes_test(lambda u: u.is_superuser,login_url='logout')
def svps(request):
  if request.method == 'POST':
    excel = request.FILES.get('excel').read()
    Command.svps(excel)
  svps = Svps.objects.all()
  col = [f.name for f in Svps._meta.get_fields()]
  paginator = Paginator(svps,500)
  page = request.GET.get('page')
  p = paginator.get_page(page)
  try:
   numbers = paginator.page(page)
  except PageNotAnInteger:
   numbers = paginator.page(1)
  except EmptyPage:
   numbers = paginator.page(paginator.num_pages)
  context = {"svps": numbers,
             "col": col
                       }
  template = loader.get_template('home/tables/svps.html')
  
  return HttpResponse(template.render(context, request))

@user_passes_test(lambda u: u.is_superuser,login_url='logout')
def svps_remark(request):
  if request.method == 'POST':
    excel = request.FILES.get('excel').read()
    Command.svps_remark(excel)
  svps_remark = SvpsRemark.objects.all()
  col = [f.name for f in SvpsRemark._meta.get_fields()]
  context = {"svps_remark": svps_remark,
             "col": col
                       }
  template = loader.get_template('home/tables/svps_remark.html')
  
  return HttpResponse(template.render(context, request))

@user_passes_test(lambda u: u.is_superuser,login_url='logout')
def cbm_cft(request):
  if request.method == 'POST':
    excel = request.FILES.get('excel').read()
    Command.cbm_cft(excel)
  cbm = CbmCft.objects.all()
  col = [f.name for f in CbmCft._meta.get_fields()]
  context = {"cbm": cbm,
             "col": col
                       }
  template = loader.get_template('home/tables/cbm_cft.html')
  
  return HttpResponse(template.render(context, request))

@user_passes_test(lambda u: u.is_superuser,login_url='logout')
def weight_master(request):
  eng = create_engine('sqlite:///db.sqlite3')
  if request.method == 'POST':
    excel = request.FILES.get('excel').read()
    Command.weight_master(excel)

    df = pd.read_sql_query('''SELECT * FROM "Weight Master";''',con = eng)
    df["CBM volumetric"] = pd.to_numeric('', errors='coerce').astype('float')
    df["CBM against gross wt"] = pd.to_numeric('',errors='coerce').astype('float')
    df["Chargeable CBM for CC"] = pd.to_numeric('',errors='coerce').astype('float')
    df["CBM/Part"] = pd.to_numeric('',errors='coerce').astype('float')
    df["Wt/CFT volumetric PTL"] = pd.to_numeric('',errors='coerce').astype('float')
    df["Wt/CFT against gross wt PTL"] = pd.to_numeric('',errors='coerce').astype('float')
    df["Chargeable CFT for PTL"] = pd.to_numeric('',errors='coerce').astype('float')
    df["Wt./Part PTL"] = pd.to_numeric('',errors='coerce').astype('float')
    df["Wt/CFT volumetric Express Road"] = pd.to_numeric('',errors='coerce').astype('float')
    df["Wt/CFT against gross wt Express Road"] = pd.to_numeric('',errors='coerce').astype('float')
    df["Chargeable CFT for Express Road"] = pd.to_numeric('',errors='coerce').astype('float')
    df["Wt./Part Express Road"] = pd.to_numeric('',errors='coerce').astype('float')
    df["volumetric Wt. Air"] = pd.to_numeric('',errors='coerce').astype('float')
    df["gross wt Air"] = pd.to_numeric('',errors='coerce').astype('float')
    df["Chargeable CFT for Air"] = pd.to_numeric('',errors='coerce').astype('float')
    df["Wt./Part Air"] = pd.to_numeric('',errors='coerce').astype('float')
    df["volumetric Wt. Train"] = pd.to_numeric('',errors='coerce').astype('float')
    df["gross wt Train"] = pd.to_numeric('',errors='coerce').astype('float')
    df["Chargeable CFT for Train"] = pd.to_numeric('',errors='coerce').astype('float')
    df["Wt./Part Train"] = pd.to_numeric('',errors='coerce').astype('float')
    df.to_sql(WeightMaster._meta.db_table,if_exists='replace',con=eng,index=False)
    try:
        pd.read_sql_query('''UPDATE "Weight Master" SET "CBM volumetric" = ROUND((("L (mm)"/304.8) * ("W (mm)"/304.8) * ("H (mm)"/304.8))*7,5);''',con=eng)
    except Exception as e:
      print(e)
    try:
        pd.read_sql_query('''UPDATE "Weight Master" SET "CBM against gross wt" = ROUND("Gross Wt.",5);''',con=eng)
    except Exception as e:
      print(e)
    try:
        pd.read_sql_query('''UPDATE "Weight Master" SET "Chargeable CBM for CC" = MAX("CBM volumetric","CBM against gross wt");''',con=eng)
    except Exception as e:
      print(e)
    try:
        pd.read_sql_query('''UPDATE "Weight Master" SET "CBM/Part" = ROUND("Chargeable CBM for CC"/"Qty./Box",5);''',con=eng)
    except Exception as e:
      print(e)
    try:
        pd.read_sql_query('''UPDATE "Weight Master" SET "Wt/CFT volumetric PTL" = ROUND((("L (mm)"/304.8) * ("W (mm)"/304.8) * ("H (mm)"/304.8))*7,5);''',con=eng)
    except Exception as e:
      print(e)
    try:
        pd.read_sql_query('''UPDATE "Weight Master" SET "Wt/CFT against gross wt PTL" = "Gross Wt.";''',con=eng)
    except Exception as e:
      print(e)
    try:
        pd.read_sql_query('''UPDATE "Weight Master" SET "Chargeable CFT for PTL" = MAX("Wt/CFT volumetric PTL","Wt/CFT against gross wt PTL");''',con=eng)
    except Exception as e:
      print(e)
    try:
        pd.read_sql_query('''UPDATE "Weight Master" SET "Wt./Part PTL" = ROUND("Chargeable CFT for PTL"/"Qty./Box",5);''',con=eng)
    except Exception as e:
      print(e)
    try:
        pd.read_sql_query('''UPDATE "Weight Master" SET "Wt/CFT volumetric Express Road" = ROUND((("L (mm)"/304.8) * ("W (mm)"/304.8) * ("H (mm)"/304.8))*8,5);''',con=eng)
    except Exception as e:
      print(e)
    try:
        pd.read_sql_query('''UPDATE "Weight Master" SET "Wt/CFT against gross wt Express Road" = "Gross Wt.";''',con=eng)
    except Exception as e:
      print(e)
    try:
        pd.read_sql_query('''UPDATE "Weight Master" SET "Chargeable CFT for Express Road" = MAX("Wt/CFT volumetric Express Road","Wt/CFT against gross wt Express Road") ;''',con=eng)
    except Exception as e:
      print(e)
    try:
        pd.read_sql_query('''UPDATE "Weight Master" SET "Wt./Part Express Road" = ROUND("Chargeable CFT for Express Road"/"Qty./Box",5);''',con=eng)
    except Exception as e:
      print(e)
    try:
        pd.read_sql_query('''UPDATE "Weight Master" SET "volumetric Wt. Air" = ROUND((("L (mm)"/10) * ("W (mm)"/10) * ("H (mm)"/10))/6000,5);''',con=eng)
    except Exception as e:
      print(e)
    try:
        pd.read_sql_query('''UPDATE "Weight Master" SET "gross wt Air" = "Gross Wt.";''',con=eng)
    except Exception as e:
      print(e)
    try:
        pd.read_sql_query('''UPDATE "Weight Master" SET "Chargeable CFT for Air" = MAX("volumetric Wt. Air","gross wt Air");''',con=eng)
    except Exception as e:
      print(e)
    try:
        pd.read_sql_query('''UPDATE "Weight Master" SET "Wt./Part Air" = ROUND("Chargeable CFT for Air"/"Qty./Box",5);''',con=eng)
    except Exception as e:
      print(e)
    try:
        pd.read_sql_query('''UPDATE "Weight Master" SET "volumetric Wt. Train" = ROUND((("L (mm)"/10) * ("W (mm)"/10) * ("H (mm)"/10))/5000,5);''',con=eng)
    except Exception as e:
      print(e)
    try:
        pd.read_sql_query('''UPDATE "Weight Master" SET "gross wt Train" = "Gross Wt.";''',con=eng)
    except Exception as e:
      print(e)
    try:
        pd.read_sql_query('''UPDATE "Weight Master" SET "Chargeable CFT for Train" = MAX("volumetric Wt. Train","gross wt Train");''',con=eng)
    except Exception as e:
      print(e)
    try:
        pd.read_sql_query('''UPDATE "Weight Master" SET "Wt./Part Train" = ROUND("Chargeable CFT for Train"/"Qty./Box",5);''',con=eng)
    except Exception as e:
      print(e)
  

  weight = WeightMaster.objects.all()
  col = [f.name for f in WeightMaster._meta.get_fields()]
  paginator = Paginator(weight,500)
  page = request.GET.get('page')
  p = paginator.get_page(page)
  try:
   numbers = paginator.page(page)
  except PageNotAnInteger:
   numbers = paginator.page(1)
  except EmptyPage:
   numbers = paginator.page(paginator.num_pages)
  context = {"weight": numbers,
             "col": col
                       }
  template = loader.get_template('home/tables/weight_master.html')
  
  return HttpResponse(template.render(context, request))


  
@login_required(login_url='login') 
def show_leci(request, grn_number):
  eng = create_engine('sqlite:///db.sqlite3')
  #leci = pd.read_sql_query('''SELECT leci FROM "Grn Dump" WHERE "Material Document" = '''+str(grn_number)+''';''',con = eng)
  leci = GrnDump.objects.get(materialdocument=grn_number)
  print(leci.leci)
  lec = LeciDump.objects.filter(lecino = leci.leci).values()
  col = [f.name for f in LeciDump._meta.get_fields()]
  print(lec)
  context = {"lec": lec,
             "col": col
                       }
  template = loader.get_template('home/tables/show_leci.html')
  
  return HttpResponse(template.render(context,request))

@login_required(login_url='login')
def download(request):
  with BytesIO() as b:
        writer = pd.ExcelWriter(b, engine='xlsxwriter')
        eng = create_engine('sqlite:///db.sqlite3')
        table = request.POST.get('data')
        df = pd.read_sql_query('''select * from "MIS FULL";''', con = eng)
        if table == 'MIS':
          df['Grn Number'] = pd.to_numeric(df['Grn Number'])
        df.to_excel(writer, sheet_name='MIS',index=False)
        print(df.dtypes)
        writer.save()
        filename = table+".xlsx"
        response = HttpResponse(
            b.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        return response
  
 

