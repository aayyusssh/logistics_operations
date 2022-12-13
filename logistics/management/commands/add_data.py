import pandas as pd
import numpy as np
from django.core.management.base import BaseCommand
from logistics.models import *
from sqlalchemy import create_engine

class Command(BaseCommand):
    help = "A command to add data from an excel file to database"
    def mis(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df['Delivery Date'] = df['Delivery Date'].dt.strftime('%d-%b-%Y')
        df['LR dt.'] = df['LR dt.'].dt.strftime('%d-%b-%Y')
        df['Invoice Date'] = df['Invoice Date'].dt.strftime('%d-%b-%Y')
        df['Grn Number'] = pd.to_numeric(df['Grn Number'], errors='coerce').astype('Int64')
        df['Part No.'] = df['Part No.'].astype(str).apply(lambda x: x.replace('.0',''))
        data = df.to_dict()
        astatus = None
        grnno = None
        for key,value in data.items():
            #print(key,":",value)
            if(key == 'Activity Status'):
                astatus = value
            if(key == 'Grn Number'):
                grnno = value
            if astatus and grnno != None:
               for i in range(len(astatus)):
                  # print(astatus[i],grnno[i])
                   if astatus[i]=='In-Transit' and grnno[i] != '':
                       return 'Error Occurred Correct Your Data'
               break
        df.to_sql(MIS._meta.db_table,if_exists='replace',con=engine,index=False)
        return 'Import Successfull'
    def re_mis(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df['Delivery Date'] = df['Delivery Date'].dt.strftime('%d-%b-%Y')
        df['LR dt.'] = df['LR dt.'].dt.strftime('%d-%b-%Y')
        df['Invoice Date'] = df['Invoice Date'].dt.strftime('%d-%b-%Y')
        df['Grn Number'] = pd.to_numeric(df['Grn Number'], errors='coerce').astype('Int64')
        df['Part No.'] = df['Part No.'].astype(str).apply(lambda x: x.replace('.0',''))
        data = df.to_dict()
        
        df = df.drop(["Transporter Name","LR Time","LR dt.","PAYMENT TYPE (from master)","Consignor","Consignee","Consignor Location","Location Code","State","Invoice Date","Vendor PO No","PKG","PKG TYPE","Actual Wt. (KG)"],axis=1)
        df = df.rename(columns={"Activity (from manual-Vinsum MIS)":"act","Activity Status":"AS","Location":"LOC","Delivery Date":"DDT","Grn Number":"Grn","LR no.":"LR","Invoice No.":"Invoice","Part No.":"Part","Qty.":"Qt"})
        df.to_sql("UPD MIS",if_exists='replace',con = engine,index = False)
        join = pd.read_sql_query('''select * from mis as x left join "UPD MIS" as y on x."LR no." = y.LR and x."Invoice No." = y.Invoice and x."Qty." = y.Qt and x."Part No." = y.Part;''',con=engine )
        join["Grn Number"] = pd.to_numeric(join['Grn Number'], errors='coerce').astype('Int64')
        join["Grn"] = pd.to_numeric(join['Grn'], errors='coerce').astype('Int64')
        join.to_sql("UPD MIS JOIN",if_exists="replace",con = engine,index=False)
        try:
            pd.read_sql_query('''UPDATE "UPD MIS JOIN" SET "Grn Number" = Grn where "Grn Number" is NULL;''',con=engine)
        except Exception as e:
            print(e)
        sv = pd.read_sql_query('''SELECT "Transporter Name", "Activity (from manual-Vinsum MIS)","PAYMENT TYPE (from master)","Activity Status", "Location", "Delivery Date", "Grn Number", "LR no.", "LR dt.", "LR Time", "Consignor", "Consignee","Consignor Location", "Location Code", "State", "Invoice No.", "Invoice Date", "Vendor PO No", "Part No.", "PKG", "PKG TYPE", "Qty.", "Actual Wt. (KG)" from "UPD MIS JOIN"''',con=engine)
        sv["Grn Number"] = pd.to_numeric(sv['Grn Number'], errors='coerce').astype('Int64')
        sv.to_sql(MIS._meta.db_table,if_exists='replace',con=engine,index=False)
        
        astatus = None
        grnno = None
        for key,value in data.items():
            #print(key,":",value)
            if(key == 'Activity Status'):
                astatus = value
            if(key == 'Grn Number'):
                grnno = value
            if astatus and grnno != None:
               for i in range(len(astatus)):
                  # print(astatus[i],grnno[i])
                   if astatus[i]=='In-Transit' and grnno[i] != '':
                       return 'Error Occurred Correct Your Data'
               break
        
        df1 = MIS.objects.all().values_list()
       # print(df1)
        #df.to_sql(MIS._meta.db_table,if_exists='replace',con=engine,index=False)
        return 'Import Successfull'

    def leci(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(LeciDump._meta.db_table,if_exists='replace',con=engine,index=False)
    
    def distance_range(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql("Distance Range",if_exists='replace',con=engine,index=False)
    
    def rate(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql("Rate",if_exists='replace',con=engine,index=False)
    
    def recovery_condition(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql("Recovery Condition",if_exists='replace',con=engine,index=False)

    def svps_remark(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(SvpsRemark._meta.db_table,if_exists='replace',con=engine,index=False)
    
    def fast_dump(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(FastDump._meta.db_table,if_exists='replace',con=engine,index=False)

    def pf_lsp_mis(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(PfLspMis._meta.db_table,if_exists='replace',con=engine,index=False)


    def po(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        df["PO End Validity"] = df["PO End Validity"].astype("str")
        df["PO Creation Date"] = df["PO Creation Date"].astype("str")
        df["PO Start Validity"] = df["PO Start Validity"].astype("str")
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(Po._meta.db_table,if_exists='replace',con=engine,index=False)

    def cbm_cft(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(CbmCft._meta.db_table,if_exists='replace',con=engine,index=False)
    
    def lr_bill(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql("LR BILL",if_exists='replace',con=engine,index=False)

    def svps(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(Svps._meta.db_table,if_exists='replace',con=engine,index=False)
        df2 = pd.read_sql_query('''SELECT * FROM "SVPS" ORDER By INVOICEID DESC;''',con=engine)
        df2.to_sql(Svps._meta.db_table,if_exists='replace',con=engine,index=False)

    def inbound_shipment(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        df["ShipmentDate"] = df['ShipmentDate'].astype('str')
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(InboundShipment._meta.db_table,if_exists='replace',con=engine,index=False)

    def transporter(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(TransporterMaster._meta.db_table,if_exists='replace',con=engine,index=False)

    def origin(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(OriginState._meta.db_table,if_exists='replace',con=engine,index=False)

    def rate_master(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(RateMaster._meta.db_table,if_exists='replace',con=engine,index=False)
    
    def weight_master(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        df["Qty./Box"] = pd.to_numeric(df['Qty./Box'], errors='coerce').astype("Int64")
        df["Gross Wt."] = pd.to_numeric(df['Gross Wt.'], errors='coerce').astype("float")
        df["Wt./Part"] = pd.to_numeric(df['Wt./Part'], errors='coerce').astype("float")
        df["L (mm)"] = pd.to_numeric(df['L (mm)'], errors='coerce').astype("float")
        df["H (mm)"] = pd.to_numeric(df['H (mm)'], errors='coerce').astype("float")
        df["W (mm)"] = pd.to_numeric(df['W (mm)'], errors='coerce').astype("float")
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(WeightMaster._meta.db_table,if_exists='replace',con=engine,index=False)

    def inco_terms(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(IncoTerms._meta.db_table,if_exists='replace',con=engine,index=False)
    
    def grn(excel,option):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(GrnDump._meta.db_table,if_exists=option,con=engine,index=False)

    def vendor(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(VendorMaster._meta.db_table,if_exists='replace',con=engine,index=False)
    
    def ses(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(Ses._meta.db_table,if_exists='replace',con=engine,index=False)

    def part(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(PartMaster._meta.db_table,if_exists='replace',con=engine,index=False)

    def query(excel):
        d = pd.read_excel(excel,keep_default_na=False)
        data = d.to_dict()
        #print(data)
        engine = create_engine('sqlite:///db.sqlite3')
        column = 'Location'
        astatus = None
        grnno = None
        for key,value in data.items():
            #print(key,":",value)
            if(key == 'Activity Status'):
                astatus = value
            if(key == 'Grn Number'):
                grnno = value
            if astatus and grnno != None:
               for i in range(len(astatus)):
                   print(astatus[i],grnno[i])
                   if astatus[i]=='In-Transit' and grnno[i] != '':
                       print("Error occurred")
               break
        df = pd.read_sql_query('select '+'"'+column+'"'+' from MIS', engine)
        
        
