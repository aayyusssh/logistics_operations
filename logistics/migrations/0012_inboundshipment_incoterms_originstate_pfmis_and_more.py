# Generated by Django 4.1.3 on 2022-12-03 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0011_misfull'),
    ]

    operations = [
        migrations.CreateModel(
            name='InboundShipment',
            fields=[
                ('invoiceid', models.BigIntegerField(db_column='InvoiceId', primary_key=True, serialize=False)),
                ('invoiceno', models.TextField(blank=True, db_column='InvoiceNo', null=True)),
                ('invoicedate', models.DateTimeField(blank=True, db_column='InvoiceDate', null=True)),
                ('uploadeddate', models.DateTimeField(blank=True, db_column='UploadedDate', null=True)),
                ('vendorcode', models.TextField(blank=True, db_column='VendorCode', null=True)),
                ('vendorname', models.TextField(blank=True, db_column='VendorName', null=True)),
                ('currentstatus', models.TextField(blank=True, db_column='CurrentStatus', null=True)),
                ('ponumber', models.BigIntegerField(blank=True, db_column='PONumber', null=True)),
                ('signedby', models.TextField(blank=True, db_column='SignedBy', null=True)),
                ('isverified', models.TextField(blank=True, db_column='IsVerified', null=True)),
                ('signtimestamp', models.TextField(blank=True, db_column='SignTimestamp', null=True)),
                ('email', models.TextField(blank=True, db_column='Email', null=True)),
                ('plantcode', models.BigIntegerField(blank=True, db_column='PlantCode', null=True)),
                ('plantname', models.TextField(blank=True, db_column='PlantName', null=True)),
                ('shipmentcode', models.TextField(blank=True, db_column='ShipmentCode', null=True)),
                ('rmsrefnumber', models.TextField(blank=True, db_column='RMSRefNumber', null=True)),
                ('invoiceamount', models.TextField(blank=True, db_column='InvoiceAmount', null=True)),
                ('uaremark', models.TextField(blank=True, db_column='UARemark', null=True)),
                ('gdcremark', models.TextField(blank=True, db_column='GDCRemark', null=True)),
                ('rejectedbygdc', models.TextField(blank=True, db_column='RejectedByGDC', null=True)),
                ('shipmentno', models.TextField(blank=True, db_column='ShipmentNo', null=True)),
                ('sesno', models.BigIntegerField(blank=True, db_column='SESNO', null=True)),
                ('shipmentcostingno', models.TextField(blank=True, db_column='ShipmentCostingNo', null=True)),
                ('shipmentdate', models.TextField(blank=True, db_column='ShipmentDate', null=True)),
                ('shipmentstatus', models.TextField(blank=True, db_column='ShipmentStatus', null=True)),
                ('shipmentcostingstatus', models.TextField(blank=True, db_column='ShipmentCostingStatus', null=True)),
                ('mrrlrunstatus', models.TextField(blank=True, db_column='MRRLRUNSTATUS', null=True)),
                ('basicfreightcharges', models.TextField(blank=True, db_column='BasicFreightCharges', null=True)),
                ('discountamount', models.TextField(blank=True, db_column='DiscountAmount', null=True)),
                ('gstamount', models.TextField(blank=True, db_column='GSTAmount', null=True)),
            ],
            options={
                'db_table': 'Inbound Shipment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IncoTerms',
            fields=[
                ('po_no', models.BigIntegerField(db_column='PO No', primary_key=True, serialize=False)),
                ('part_no', models.TextField(blank=True, db_column='Inco Part No', null=True)),
                ('v_code', models.TextField(blank=True, db_column='V_Code', null=True)),
                ('inco_terms', models.TextField(blank=True, db_column='Inco-Terms', null=True)),
            ],
            options={
                'db_table': 'inco terms',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OriginState',
            fields=[
                ('origin', models.TextField(db_column='ORIGIN', primary_key=True, serialize=False)),
                ('origin_full_name', models.TextField(blank=True, db_column='Origin Full Name', null=True)),
                ('origin_state_name', models.TextField(blank=True, db_column='Origin State Name', null=True)),
            ],
            options={
                'db_table': 'Origin State',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PfMis',
            fields=[
                ('consider_pick_up_month', models.TextField(blank=True, db_column='Consider Pick-up Month', null=True)),
                ('indent_request_month', models.TextField(blank=True, db_column='Indent Request Month', null=True)),
                ('s_no', models.BigIntegerField(db_column='S. No', primary_key=True, serialize=False)),
                ('lsp', models.TextField(blank=True, db_column='LSP', null=True)),
                ('mode', models.TextField(blank=True, db_column='MODE', null=True)),
                ('indent_no_field', models.TextField(blank=True, db_column='Indent No.', null=True)),
                ('indent_request_date_field', models.TextField(blank=True, db_column='Indent Request date ', null=True)),
                ('lr_no_field', models.BigIntegerField(blank=True, db_column='LR NO.', null=True)),
                ('lr_date', models.TextField(blank=True, db_column='LR DATE', null=True)),
                ('pickup_time_field', models.TextField(blank=True, db_column='Pickup Time  ', null=True)),
                ('flight_no', models.TextField(blank=True, db_column='Flight No', null=True)),
                ('flight_date', models.TextField(blank=True, db_column='Flight Date', null=True)),
                ('flight_time', models.TextField(blank=True, db_column='Flight Time', null=True)),
                ('invoice_no', models.TextField(blank=True, db_column='Invoice No', null=True)),
                ('part_number', models.TextField(blank=True, db_column='PART NUMBER', null=True)),
                ('pkg', models.TextField(blank=True, db_column='PKG', null=True)),
                ('quantity', models.TextField(blank=True, db_column='QUANTITY', null=True)),
                ('indent_wt', models.TextField(blank=True, db_column='INDENT WT', null=True)),
                ('chrg_wt', models.TextField(blank=True, db_column='Chrg.WT', null=True)),
                ('consignor', models.TextField(blank=True, db_column='CONSIGNOR', null=True)),
                ('consignor_state', models.TextField(blank=True, db_column='CONSIGNOR STATE', null=True)),
                ('cnr_location', models.TextField(blank=True, db_column='CNR. LOCATION', null=True)),
                ('consignee', models.TextField(blank=True, db_column='CONSIGNEE', null=True)),
                ('status_w_h_in_transit_field', models.TextField(blank=True, db_column='STATUS(W/H, IN TRANSIT)', null=True)),
                ('edd', models.TextField(blank=True, db_column='EDD', null=True)),
                ('delivery_date', models.TextField(blank=True, db_column='Delivery Date', null=True)),
                ('remarks_field', models.TextField(blank=True, db_column='REMARKS ', null=True)),
                ('leci_no', models.TextField(blank=True, db_column='LECI No', null=True)),
                ('grn_no', models.TextField(blank=True, db_column='GRN No', null=True)),
                ('dump_indent_no_field', models.TextField(blank=True, db_column='Dump Indent No.', null=True)),
                ('request_date', models.TextField(blank=True, db_column='Request Date', null=True)),
                ('mode_of_premium_freight', models.TextField(blank=True, db_column='Mode Of Premium Freight', null=True)),
                ('incoterm', models.TextField(blank=True, db_column='INCOTERM', null=True)),
                ('status', models.TextField(blank=True, db_column='Status', null=True)),
                ('pending_with', models.TextField(blank=True, db_column='Pending with', null=True)),
                ('indenter_name', models.TextField(blank=True, db_column='Indenter Name', null=True)),
                ('indenter_t_no', models.TextField(blank=True, db_column='Indenter T No', null=True)),
                ('vendor_name', models.TextField(blank=True, db_column='Vendor Name', null=True)),
                ('vendor_code', models.TextField(blank=True, db_column='Vendor Code', null=True)),
                ('vendor_location_state', models.TextField(blank=True, db_column='Vendor Location State', null=True)),
                ('vendor_location_city', models.TextField(blank=True, db_column='Vendor Location City', null=True)),
                ('pickup_state', models.TextField(blank=True, db_column='Pickup State', null=True)),
                ('pickup_city', models.TextField(blank=True, db_column='Pickup City', null=True)),
                ('pickup_date', models.TextField(blank=True, db_column='Pickup Date', null=True)),
                ('destination_state', models.TextField(blank=True, db_column='Destination State', null=True)),
                ('destination_city', models.TextField(blank=True, db_column='Destination City', null=True)),
                ('part_no', models.TextField(blank=True, db_column='Part No', null=True)),
                ('part_description', models.TextField(blank=True, db_column='Part Description', null=True)),
                ('indent_weight_kg_field', models.TextField(blank=True, db_column='Indent Weight (Kg)', null=True)),
                ('cost_to_be_borne_by', models.TextField(blank=True, db_column='Cost To be Borne By', null=True)),
                ('cost_center', models.TextField(blank=True, db_column='Cost Center', null=True)),
                ('description_of_cc_entered', models.TextField(blank=True, db_column='Description Of CC Entered', null=True)),
                ('if_shared_any_other_agreed_with_vender_for_recovery_field', models.TextField(blank=True, db_column='If Shared (Any other % agreed with vender for recovery)', null=True)),
                ('indent_qty_field', models.TextField(blank=True, db_column='Indent Qty-', null=True)),
                ('indent_issue_to_lsp', models.TextField(blank=True, db_column='Indent issue to LSP', null=True)),
                ('vendor_code_field', models.TextField(blank=True, db_column='Vendor Code ', null=True)),
                ('vendor', models.TextField(blank=True, db_column='Vendor', null=True)),
                ('city', models.TextField(blank=True, db_column='City', null=True)),
                ('consider_city', models.TextField(blank=True, db_column='Consider City', null=True)),
                ('state', models.TextField(blank=True, db_column='State', null=True)),
                ('zone_for_air_train', models.TextField(blank=True, db_column='Zone for Air/Train', null=True)),
                ('distance_from_utk_to_vendor_consider_city_distance_check_from_google_field', models.TextField(blank=True, db_column='Distance from UTK to Vendor consider City (distance check from google)', null=True)),
                ('distance_for_speed_truck', models.TextField(blank=True, db_column='Distance for Speed Truck', null=True)),
                ('nearest_airport', models.TextField(blank=True, db_column='Nearest Airport', null=True)),
                ('distance_from_pick_up_location_to_airport', models.TextField(blank=True, db_column='Distance from Pick-up location to Airport', null=True)),
                ('nearest_railway_station', models.TextField(blank=True, db_column='Nearest Railway station', null=True)),
                ('distance_from_pick_up_location_to_railway_station', models.TextField(blank=True, db_column='Distance from Pick-up location to Railway Station', null=True)),
                ('zone', models.TextField(blank=True, db_column='Zone', null=True)),
            ],
            options={
                'db_table': 'PF MIS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RateMaster',
            fields=[
                ('state_description', models.TextField(db_column='State Description', primary_key=True, serialize=False)),
                ('apr_22', models.TextField(blank=True, db_column='Apr-22', null=True)),
                ('may_22', models.TextField(blank=True, db_column='May-22', null=True)),
                ('jun_22', models.TextField(blank=True, db_column='Jun-22', null=True)),
                ('jul_22', models.TextField(blank=True, db_column='Jul-22', null=True)),
                ('aug_22', models.TextField(blank=True, db_column='Aug-22', null=True)),
                ('sep_22', models.TextField(blank=True, db_column='Sep-22', null=True)),
                ('oct_22', models.TextField(blank=True, db_column='Oct-22', null=True)),
                ('nov_22', models.TextField(blank=True, db_column='Nov-22', null=True)),
                ('dec_22', models.BigIntegerField(blank=True, db_column='Dec-22', null=True)),
                ('jan_23', models.BigIntegerField(blank=True, db_column='Jan-23', null=True)),
                ('feb_23', models.BigIntegerField(blank=True, db_column='Feb-23', null=True)),
                ('mar_23', models.BigIntegerField(blank=True, db_column='Mar-23', null=True)),
            ],
            options={
                'db_table': 'Rate Master',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CbmCft',
            fields=[
                ('activity', models.TextField(blank=True, db_column='Activity CBM CFT', null=True)),
                ('lsp_code', models.TextField(db_column='LSP Code', primary_key=True, serialize=False)),
                ('lsp_short_name', models.TextField(blank=True, db_column='LSP Short Name', null=True)),
                ('cft_cbm', models.BigIntegerField(blank=True, db_column='CFT/CBM', null=True)),
            ],
            options={
                'db_table': 'CBM/CFT',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DistanceRange',
            fields=[
                ('vendor_code_field', models.TextField(db_column='Vendor Code ', primary_key=True, serialize=False)),
                ('vendor', models.TextField(blank=True, db_column='Vendor', null=True)),
                ('city', models.TextField(blank=True, db_column='City', null=True)),
                ('consider_city', models.TextField(blank=True, db_column='Consider City', null=True)),
                ('state', models.TextField(blank=True, db_column='State', null=True)),
                ('zone_for_air_train', models.TextField(blank=True, db_column='Zone for Air/Train', null=True)),
                ('distance_from_utk_to_vendor_consider_city_distance_check_from_google_field', models.TextField(blank=True, db_column='Distance from UTK to Vendor consider City (distance check from google)', null=True)),
                ('distance_for_speed_truck', models.TextField(blank=True, db_column='Distance for Speed Truck', null=True)),
                ('nearest_airport', models.TextField(blank=True, db_column='Nearest Airport', null=True)),
                ('distance_from_pick_up_location_to_airport', models.TextField(blank=True, db_column='Distance from Pick-up location to Airport', null=True)),
                ('nearest_railway_station', models.TextField(blank=True, db_column='Nearest Railway station', null=True)),
                ('distance_from_pick_up_location_to_railway_station', models.TextField(blank=True, db_column='Distance from Pick-up location to Railway Station', null=True)),
            ],
            options={
                'db_table': 'Distance Range',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FastDump',
            fields=[
                ('indent_no_field', models.TextField(db_column='Dump Indent No.', primary_key=True, serialize=False)),
                ('request_date', models.DateTimeField(blank=True, db_column='Request Date', null=True)),
                ('mode_of_premium_freight', models.TextField(blank=True, db_column='Mode Of Premium Freight', null=True)),
                ('incoterm', models.TextField(blank=True, db_column='INCOTERM', null=True)),
                ('status', models.TextField(blank=True, db_column='Status', null=True)),
                ('pending_with', models.TextField(blank=True, db_column='Pending with', null=True)),
                ('indenter_name', models.TextField(blank=True, db_column='Indenter Name', null=True)),
                ('indenter_t_no', models.BigIntegerField(blank=True, db_column='Indenter T No', null=True)),
                ('vendor_name', models.TextField(blank=True, db_column='Vendor Name', null=True)),
                ('vendor_code', models.TextField(blank=True, db_column='Vendor Code', null=True)),
                ('vendor_location_state', models.TextField(blank=True, db_column='Vendor Location State', null=True)),
                ('vendor_location_city', models.TextField(blank=True, db_column='Vendor Location City', null=True)),
                ('pickup_state', models.TextField(blank=True, db_column='Pickup State', null=True)),
                ('pickup_city', models.TextField(blank=True, db_column='Pickup City', null=True)),
                ('pickup_date', models.DateTimeField(blank=True, db_column='Pickup Date', null=True)),
                ('destination_state', models.TextField(blank=True, db_column='Destination State', null=True)),
                ('destination_city', models.TextField(blank=True, db_column='Destination City', null=True)),
                ('part_no', models.TextField(blank=True, db_column='Part No', null=True)),
                ('part_description', models.TextField(blank=True, db_column='Part Description', null=True)),
                ('indent_weight_kg_field', models.TextField(blank=True, db_column='Indent Weight (Kg)', null=True)),
                ('cost_to_be_borne_by', models.TextField(blank=True, db_column='Cost To be Borne By', null=True)),
                ('cost_center', models.BigIntegerField(blank=True, db_column='Cost Center', null=True)),
                ('description_of_cc_entered', models.TextField(blank=True, db_column='Description Of CC Entered', null=True)),
                ('if_shared_any_other_agreed_with_vender_for_recovery_field', models.TextField(blank=True, db_column='If Shared (Any other % agreed with vender for recovery)', null=True)),
                ('indent_qty_field', models.TextField(blank=True, db_column='Indent Qty-', null=True)),
                ('indent_issue_to_lsp', models.TextField(blank=True, db_column='Indent issue to LSP', null=True)),
            ],
            options={
                'db_table': 'Fast Dump',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LrBill',
            fields=[
                ('lr_no_field', models.BigIntegerField(db_column='LR No', primary_key=True, serialize=False)),
                ('bill_no_field', models.BigIntegerField(blank=True, db_column='Bill No', null=True)),
                ('basic_bill_value', models.TextField(blank=True, db_column='Basic Bill Value', null=True)),
            ],
            options={
                'db_table': 'LR BILL',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PfLspMis',
            fields=[
                ('lsp', models.TextField(db_column='LSP', primary_key=True, serialize=False)),
                ('mode', models.TextField(blank=True, db_column='MODE', null=True)),
                ('indent_no_field', models.TextField(blank=True, db_column='Indent No.', null=True)),
                ('indent_request_date_field', models.DateTimeField(blank=True, db_column='Indent Request date ', null=True)),
                ('lr_no_field', models.BigIntegerField(blank=True, db_column='LR NO.', null=True)),
                ('lr_date', models.TextField(blank=True, db_column='LR DATE', null=True)),
                ('pickup_time_field', models.TimeField(blank=True, db_column='Pickup Time  ', null=True)),
                ('flight_no', models.TextField(blank=True, db_column='Flight No', null=True)),
                ('flight_date', models.TextField(blank=True, db_column='Flight Date', null=True)),
                ('flight_time', models.TextField(blank=True, db_column='Flight Time', null=True)),
                ('invoice_no', models.TextField(blank=True, db_column='Invoice No', null=True)),
                ('part_number', models.TextField(blank=True, db_column='PART NUMBER', null=True)),
                ('pkg', models.TextField(blank=True, db_column='PKG', null=True)),
                ('quantity', models.TextField(blank=True, db_column='QUANTITY', null=True)),
                ('indent_wt', models.TextField(blank=True, db_column='INDENT WT', null=True)),
                ('chrg_wt', models.TextField(blank=True, db_column='Chrg.WT', null=True)),
                ('consignor', models.TextField(blank=True, db_column='CONSIGNOR', null=True)),
                ('consignor_state', models.TextField(blank=True, db_column='CONSIGNOR STATE', null=True)),
                ('cnr_location', models.TextField(blank=True, db_column='CNR. LOCATION', null=True)),
                ('consignee', models.TextField(blank=True, db_column='CONSIGNEE', null=True)),
                ('status_w_h_in_transit_field', models.TextField(blank=True, db_column='STATUS(W/H, IN TRANSIT)', null=True)),
                ('edd', models.TextField(blank=True, db_column='EDD', null=True)),
                ('delivery_date', models.DateTimeField(blank=True, db_column='Delivery Date', null=True)),
                ('remarks_field', models.TextField(blank=True, db_column='REMARKS ', null=True)),
                ('leci_no', models.TextField(blank=True, db_column='LECI No', null=True)),
                ('grn_no', models.TextField(blank=True, db_column='GRN No', null=True)),
            ],
            options={
                'db_table': 'PF LSP MIS',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Po',
            fields=[
                ('po_no_field', models.BigIntegerField(db_column='PO No.', primary_key=True, serialize=False)),
                ('contract_validity', models.TextField(blank=True, db_column='Contract Validity', null=True)),
                ('extention', models.TextField(blank=True, db_column='Extention', null=True)),
                ('po_creation_date', models.TextField(blank=True, db_column='PO Creation Date', null=True)),
                ('po_start_validity', models.TextField(blank=True, db_column='PO Start Validity', null=True)),
                ('po_end_validity', models.TextField(blank=True, db_column='PO End Validity', null=True)),
                ('vendor_code', models.TextField(blank=True, db_column='Vendor Code', null=True)),
                ('vendor_name', models.TextField(blank=True, db_column='Vendor Name', null=True)),
                ('activity', models.TextField(blank=True, db_column='Activity', null=True)),
                ('user_for_bill_clearance', models.TextField(blank=True, db_column='User for bill clearance', null=True)),
                ('po_for', models.TextField(blank=True, db_column='PO for', null=True)),
                ('main_activity', models.TextField(blank=True, db_column='Main Activity', null=True)),
                ('mode', models.TextField(blank=True, db_column='Mode', null=True)),
                ('io_no', models.TextField(blank=True, db_column='IO No', null=True)),
                ('gl_no', models.TextField(blank=True, db_column='GL No', null=True)),
                ('cost_centre', models.TextField(blank=True, db_column='Cost Centre', null=True)),
            ],
            options={
                'db_table': 'PO',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ses',
            fields=[
                ('v_code', models.TextField(db_column='V_Code', primary_key=True, serialize=False)),
                ('v_name', models.TextField(blank=True, db_column='V_Name', null=True)),
                ('po_no_field', models.BigIntegerField(blank=True, db_column='PO No.', null=True)),
                ('reference', models.TextField(blank=True, db_column='SES Reference', null=True)),
                ('document_date', models.TextField(blank=True, db_column='Document Date', null=True)),
                ('entry_sheet', models.BigIntegerField(blank=True, db_column='Entry Sheet', null=True)),
                ('created_on', models.TextField(blank=True, db_column='Created on', null=True)),
                ('changed_on', models.DateTimeField(blank=True, db_column='Changed on', null=True)),
                ('accin', models.TextField(blank=True, db_column='AccIn', null=True)),
                ('basic_amount', models.TextField(blank=True, db_column='Basic Amount', null=True)),
                ('ses_qty_field', models.TextField(blank=True, db_column='SES Qty.', null=True)),
                ('gl_a_c', models.BigIntegerField(blank=True, db_column='GL A/c', null=True)),
                ('cost_centre', models.TextField(blank=True, db_column='Cost Centre', null=True)),
                ('rate', models.TextField(blank=True, db_column='Rate', null=True)),
                ('service_no_field', models.TextField(blank=True, db_column='Service No.', null=True)),
                ('service_description', models.TextField(blank=True, db_column='Service Description', null=True)),
                ('fin_doc_no_field', models.TextField(blank=True, db_column='Fin Doc. No.', null=True)),
            ],
            options={
                'db_table': 'SES',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Svps',
            fields=[
                ('invoiceid', models.BigIntegerField(db_column='InvoiceId', primary_key=True, serialize=False)),
                ('signtimestamp', models.DateTimeField(blank=True, db_column='SignTimestamp', null=True)),
                ('ponumber', models.BigIntegerField(blank=True, db_column='PONumber', null=True)),
                ('invoicedate', models.DateTimeField(blank=True, db_column='InvoiceDate', null=True)),
                ('invoiceno', models.TextField(blank=True, db_column='InvoiceNo', null=True)),
                ('agencyname', models.TextField(blank=True, db_column='AgencyName', null=True)),
                ('email', models.TextField(blank=True, db_column='Email', null=True)),
                ('vendorcode', models.TextField(blank=True, db_column='VendorCode', null=True)),
                ('vendorname', models.TextField(blank=True, db_column='VendorName', null=True)),
                ('remark', models.TextField(blank=True, db_column='Remark', null=True)),
                ('uploadeddate', models.DateTimeField(blank=True, db_column='UploadedDate', null=True)),
                ('sap_isrejected', models.BigIntegerField(blank=True, db_column='SAP_IsRejected', null=True)),
                ('sap_text', models.TextField(blank=True, db_column='SAP_TEXT', null=True)),
                ('sap_fi_document_number', models.TextField(blank=True, db_column='SAP_FI_DOCUMENT_NUMBER', null=True)),
                ('sap_batch_creation_date', models.DateTimeField(blank=True, db_column='SAP_BATCH_CREATION_DATE', null=True)),
                ('sap_rejection_date', models.TextField(blank=True, db_column='SAP_REJECTION_DATE', null=True)),
                ('sap_inv_verification_date', models.DateTimeField(blank=True, db_column='SAP_INV_VERIFICATION_DATE', null=True)),
                ('number_2nd_rel_field', models.DateTimeField(blank=True, db_column='2nd Rel.', null=True)),
                ('sap_parking_date', models.DateTimeField(blank=True, db_column='SAP_PARKING_DATE', null=True)),
                ('sap_posting_date', models.DateTimeField(blank=True, db_column='SAP_POSTING_DATE', null=True)),
                ('sap_entry_date_can_be_consider_as_ses_creation_date_field', models.DateTimeField(blank=True, db_column='SAP_ENTRY_DATE (Can be consider as SES creation date)', null=True)),
                ('sap_due_date', models.DateTimeField(blank=True, db_column='SAP_DUE_DATE', null=True)),
                ('sap_business_location', models.TextField(blank=True, db_column='SAP_BUSINESS_LOCATION', null=True)),
                ('sap_buyer_group', models.TextField(blank=True, db_column='SAP_BUYER_GROUP', null=True)),
                ('sap_payment_date', models.DateTimeField(blank=True, db_column='SAP_Payment_Date', null=True)),
                ('sap_clearing_doc_no', models.TextField(blank=True, db_column='SAP_Clearing_Doc_No', null=True)),
                ('sap_cheque_no', models.TextField(blank=True, db_column='SAP_Cheque_No', null=True)),
            ],
            options={
                'db_table': 'SVPS',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SvpsRemark',
            fields=[
                ('stage_wise_status_field', models.TextField(db_column='Stage wise Status ', primary_key=True, serialize=False)),
                ('status_meaning', models.TextField(blank=True, db_column='Status Meaning', null=True)),
                ('status', models.TextField(blank=True, db_column='Status', null=True)),
                ('actual_status', models.TextField(blank=True, db_column='Actual Status', null=True)),
            ],
            options={
                'db_table': 'SVPS Remark',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TransporterMaster',
            fields=[
                ('lsp_code', models.TextField(db_column='LSP Code', primary_key=True, serialize=False)),
                ('lsp_name', models.TextField(blank=True, db_column='LSP Name', null=True)),
                ('lsp_short_name', models.TextField(blank=True, db_column='LSP Short Name', null=True)),
                ('contact_name_1', models.TextField(blank=True, db_column='Contact Name - 1', null=True)),
                ('contact_nos_1', models.TextField(blank=True, db_column='Contact Nos - 1', null=True)),
                ('mail_id_1', models.TextField(blank=True, db_column='Mail Id - 1', null=True)),
                ('contact_name_2', models.TextField(blank=True, db_column='Contact Name - 2', null=True)),
                ('contact_nos_2', models.TextField(blank=True, db_column='Contact Nos - 2', null=True)),
                ('mail_id_2', models.TextField(blank=True, db_column='Mail Id - 2', null=True)),
                ('contact_name_3', models.TextField(blank=True, db_column='Contact Name - 3', null=True)),
                ('contact_nos_3', models.TextField(blank=True, db_column='Contact Nos - 3', null=True)),
                ('mail_id_3', models.TextField(blank=True, db_column='Mail Id - 3', null=True)),
            ],
            options={
                'db_table': 'Transporter Master',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WeightMaster',
            fields=[
                ('activity', models.TextField(blank=True, db_column='Activity', null=True)),
                ('part_no_field', models.TextField(db_column='Wt Part No.', primary_key=True, serialize=False)),
                ('part_description', models.TextField(blank=True, db_column='Part Description', null=True)),
                ('supplier_code', models.TextField(blank=True, db_column='Supplier Code', null=True)),
                ('supplier_name', models.TextField(blank=True, db_column='Supplier Name', null=True)),
                ('approved_packging', models.TextField(blank=True, db_column='Approved Packging', null=True)),
                ('actual_packging', models.TextField(blank=True, db_column='Actual Packging', null=True)),
                ('indivudual_part_s_wt_field', models.TextField(blank=True, db_column="Indivudual Part's Wt.", null=True)),
                ('indivudual_box_s_wt_field', models.TextField(blank=True, db_column="Indivudual Box's Wt.", null=True)),
                ('qty_box', models.BigIntegerField(blank=True, db_column='Qty./Box', null=True)),
                ('gross_wt_field', models.TextField(blank=True, db_column='Gross Wt.', null=True)),
                ('wt_part', models.TextField(blank=True, db_column='Wt./Part', null=True)),
                ('l_mm_field', models.TextField(blank=True, db_column='L (mm)', null=True)),
                ('w_mm_field', models.TextField(blank=True, db_column='W (mm)', null=True)),
                ('h_mm_field', models.TextField(blank=True, db_column='H (mm)', null=True)),
                ('cbm_volumetric', models.TextField(blank=True, db_column='CBM volumetric', null=True)),
                ('cbm_against_gross_wt', models.TextField(blank=True, db_column='CBM against gross wt', null=True)),
                ('chargeable_cbm_for_cc', models.TextField(blank=True, db_column='Chargeable CBM for CC', null=True)),
                ('cbm_part', models.TextField(blank=True, db_column='CBM/Part', null=True)),
                ('wt_cft_volumetric_ptl', models.TextField(blank=True, db_column='Wt/CFT volumetric PTL', null=True)),
                ('wt_cft_against_gross_wt_ptl', models.TextField(blank=True, db_column='Wt/CFT against gross wt PTL', null=True)),
                ('chargeable_cft_for_ptl', models.TextField(blank=True, db_column='Chargeable CFT for PTL', null=True)),
                ('wt_part_ptl', models.TextField(blank=True, db_column='Wt./Part PTL', null=True)),
                ('wt_cft_volumetric_express_road', models.TextField(blank=True, db_column='Wt/CFT volumetric Express Road', null=True)),
                ('wt_cft_against_gross_wt_express_road', models.TextField(blank=True, db_column='Wt/CFT against gross wt Express Road', null=True)),
                ('chargeable_cft_for_express_road', models.TextField(blank=True, db_column='Chargeable CFT for Express Road', null=True)),
                ('wt_part_express_road', models.TextField(blank=True, db_column='Wt./Part Express Road', null=True)),
                ('volumetric_wt_air', models.TextField(blank=True, db_column='volumetric Wt. Air', null=True)),
                ('gross_wt_air', models.TextField(blank=True, db_column='gross wt Air', null=True)),
                ('chargeable_cft_for_air', models.TextField(blank=True, db_column='Chargeable CFT for Air', null=True)),
                ('wt_part_air', models.TextField(blank=True, db_column='Wt./Part Air', null=True)),
                ('volumetric_wt_train', models.TextField(blank=True, db_column='volumetric Wt. Train', null=True)),
                ('gross_wt_train', models.TextField(blank=True, db_column='gross wt Train', null=True)),
                ('chargeable_cft_for_train', models.TextField(blank=True, db_column='Chargeable CFT for Train', null=True)),
                ('wt_part_train', models.TextField(blank=True, db_column='Wt./Part Train', null=True)),
            ],
            options={
                'db_table': 'Weight Master',
                'managed': True,
            },
        ),
        migrations.RemoveField(
            model_name='lecidump',
            name='considerlspname',
        ),
        migrations.RemoveField(
            model_name='lecidump',
            name='detention',
        ),
        migrations.AddField(
            model_name='lecidump',
            name='lspname',
            field=models.TextField(blank=True, db_column='LECI LSP Name', null=True),
        ),
        migrations.AlterField(
            model_name='grndump',
            name='reference',
            field=models.TextField(blank=True, db_column='Grn Reference', null=True),
        ),
    ]
