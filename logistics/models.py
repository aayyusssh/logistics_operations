from django.db import models

class MIS(models.Model):
    transportername = models.TextField(db_column='Transporter Name', blank=True, null=True)  # Field name made lowercase.
    activity_frommanual_vinsummis_field = models.TextField(db_column='Activity (from manual-Vinsum MIS)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    paymenttype_frommaster_field = models.TextField(db_column='PAYMENT TYPE (from master)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    activitystatus = models.TextField(db_column='Activity Status', blank=True, null=True)  # Field name made lowercase.
    location = models.TextField(db_column='Location', blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.TextField(db_column='Delivery Date', blank=True, null=True)  # Field name made lowercase.
    grnnumber = models.TextField(db_column='Grn Number', blank=True, null=True)  # Field name made lowercase.
    lrno_field = models.IntegerField(db_column='LR no.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lrdt_field = models.TextField(db_column='LR dt.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lrtime = models.TextField(db_column='LR Time', blank=True, null=True)  # Field name made lowercase.
    consignor = models.TextField(db_column='Consignor', blank=True, null=True)  # Field name made lowercase.
    consignee = models.TextField(db_column='Consignee', blank=True, null=True)  # Field name made lowercase.
    consignorlocation = models.TextField(db_column='Consignor Location', blank=True, null=True)  # Field name made lowercase.
    locationcode = models.TextField(db_column='Location Code', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    invoiceno_field = models.TextField(db_column='Invoice No.', primary_key = True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    invoicedate = models.TextField(db_column='Invoice Date', blank=True, null=True)  # Field name made lowercase.
    vendorpono = models.TextField(db_column='Vendor PO No', blank=True, null=True)  # Field name made lowercase.
    partno_field = models.FloatField(db_column='Part No.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    pkg = models.IntegerField(db_column='PKG', blank=True, null=True)  # Field name made lowercase.
    pkgtype = models.TextField(db_column='PKG TYPE', blank=True, null=True)  # Field name made lowercase.
    qty_field = models.IntegerField(db_column='Qty.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    actualwt_kg_field = models.IntegerField(db_column='Actual Wt. (KG)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    class Meta:
        managed = True
        db_table = 'MIS'
    
class VC_NO(models.Model):
    VC_No = models.CharField(max_length=50, primary_key = True)
    Level = models.CharField(max_length=50,null=True)
    Component_number = models.CharField(max_length=50,null=True)
    Object_description = models.CharField(max_length=50,null=True)
    Item_Number = models.CharField(max_length=50,null=True)
    Component_quantity = models.CharField(max_length=20,null=True)
    Component_unit = models.CharField(max_length=50, null=True)
    Change_Number = models.CharField(max_length=50,null=True)
    Product_store_location = models.CharField(max_length=50, null=True)
    BOM_number = models.CharField(max_length=50,null=True)
    Plant = models.CharField(max_length=50,null=True)
    Valid_from = models.DateField(null=True)
    Valid_to = models.DateField(null=True)
    Special_procurement = models.CharField(max_length=50,null=True)
    Bulk_material_item_material = models.CharField(max_length=50, null=True)
    VC_number_description = models.CharField(max_length=255, null=True)
    First = models.CharField(max_length=255, null=True)
    Second = models.CharField(max_length=255, null=True)
    class Meta:
        db_table = 'VC_NO'

class LeciDump(models.Model):
    lecino = models.IntegerField(db_column='LECI No', primary_key = True, default = 1)  # Field name made lowercase.
    rfidno = models.IntegerField(db_column='RFID No', blank=True, null=True)  # Field name made lowercase.
    checkpoint = models.TextField(db_column='Check Point', blank=True, null=True)  # Field name made lowercase.
    chkindate = models.TextField(db_column='Chkin Date', blank=True, null=True)  # Field name made lowercase.
    chktime = models.TextField(db_column='Chk Time', blank=True, null=True)  # Field name made lowercase.
    trucks_carslicenseplateno_field = models.TextField(db_column="Truck's/Car's License Plate No.", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    firstname = models.TextField(db_column='First Name', blank=True, null=True)  # Field name made lowercase.
    lastname = models.TextField(db_column='Last Name', blank=True, null=True)  # Field name made lowercase.
    no = models.IntegerField(db_column='NO', blank=True, null=True)  # Field name made lowercase.
    ri = models.TextField(db_column='RI', blank=True, null=True)  # Field name made lowercase.
    reldate = models.TextField(db_column='Rel Date', blank=True, null=True)  # Field name made lowercase.
    reltime = models.TextField(db_column='Rel Time', blank=True, null=True)  # Field name made lowercase.
    releaseby = models.TextField(db_column='Release by', blank=True, null=True)  # Field name made lowercase.
    outdate = models.TextField(db_column='Out date', blank=True, null=True)  # Field name made lowercase.
    outtime = models.TextField(db_column='Out time', blank=True, null=True)  # Field name made lowercase.
    outby = models.TextField(db_column='Out by', blank=True, null=True)  # Field name made lowercase.
    tat_hrs_field = models.IntegerField(db_column='TAT(HRS)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    weight = models.TextField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    textforloading = models.TextField(db_column='Text for Loading', blank=True, null=True)  # Field name made lowercase.
    lspname = models.TextField(db_column='LECI LSP Name', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = True
        db_table = 'LECI Dump'

class IncoTerms(models.Model):
    po_no = models.BigIntegerField(db_column='PO No', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_no = models.TextField(db_column='Inco Part No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    v_code = models.TextField(db_column='V_Code', blank=True, null=True)  # Field name made lowercase.
    inco_terms = models.TextField(db_column='Inco-Terms', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'inco terms'

class GrnDump(models.Model):
    materialdocument = models.IntegerField(db_column='Material Document', primary_key=True)  # Field name made lowercase.
    material = models.IntegerField(db_column='Material', blank=True, null=True)  # Field name made lowercase.
    materialdescription = models.TextField(db_column='Material Description', blank=True, null=True)  # Field name made lowercase.
    reference = models.TextField(db_column='Grn Reference', blank=True, null=True)  # Field name made lowercase.
    inv_dt_field = models.TextField(db_column='Inv. Dt.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    grqty_field = models.IntegerField(db_column='GR Qty.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    mb02qty_field = models.IntegerField(db_column='MB02 Qty.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    mov = models.IntegerField(db_column='Mov', blank=True, null=True)  # Field name made lowercase.
    strloc_field = models.TextField(db_column='Str Loc.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    leci = models.IntegerField(db_column='LECI', blank=True, null=True)  # Field name made lowercase.
    purchaseorder = models.IntegerField(db_column='Purchase Order', blank=True, null=True)  # Field name made lowercase.
    vendor = models.TextField(db_column='Vendor', blank=True, null=True)  # Field name made lowercase.
    postingdate = models.TextField(db_column='Posting Date', blank=True, null=True)  # Field name made lowercase.
    plant = models.IntegerField(db_column='Plant', blank=True, null=True)  # Field name made lowercase.
    grnamount = models.IntegerField(db_column='GRN Amount', blank=True, null=True)  # Field name made lowercase.
    vendorname = models.TextField(db_column='Vendor Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Grn Dump'

class MisFull(models.Model):
    lsp_code = models.TextField(db_column='Transporter Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    transporter_name = models.TextField(db_column='Transporter Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    activity_from_manual_vinsum_mis_field = models.TextField(db_column='Activity (from manual-Vinsum MIS)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    payment_type_from_master_field = models.TextField(db_column='PAYMENT TYPE (from master)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    activity_status = models.TextField(db_column='Activity Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location = models.TextField(db_column='Location', blank=True, null=True)  # Field name made lowercase.
    delivery_date = models.TextField(db_column='Delivery Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.    
    grn_number = models.BigIntegerField(db_column='Grn Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.    
    lr_no_field = models.BigIntegerField(db_column='LR no.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lr_dt_field = models.TextField(db_column='LR dt.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lr_time = models.TextField(db_column='LR Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    consignor = models.TextField(db_column='Consignor', blank=True, null=True)  # Field name made lowercase.
    consignee = models.TextField(db_column='Consignee', blank=True, null=True)  # Field name made lowercase.
    consignor_location = models.TextField(db_column='Consignor Location', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_code = models.TextField(db_column='Location Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.    
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    invoice_no_field = models.TextField(db_column='Invoice No.', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    invoice_date = models.TextField(db_column='Invoice Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.      
    vendor_po_no = models.TextField(db_column='Vendor PO No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.      
    part_no_field = models.TextField(db_column='Part No.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    pkg = models.BigIntegerField(db_column='PKG', blank=True, null=True)  # Field name made lowercase.
    pkg_type = models.TextField(db_column='PKG TYPE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    qty_field = models.BigIntegerField(db_column='Qty.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    actual_wt_kg_field = models.TextField(db_column='Actual Wt. (KG)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    transporter = models.TextField(db_column='Transporter', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    material = models.TextField(db_column='Material', blank=True, null=True)  # Field name made lowercase.
    reference = models.TextField(db_column='Grn Reference', blank=True, null=True)  # Field name made lowercase.
    mb02_qty_field = models.TextField(db_column='MB02 Qty.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    inco_terms = models.TextField(db_column='Inco-Terms', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    weight_part = models.TextField(db_column='Weight/Part', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    rate = models.TextField(db_column='Rate', blank=True, null=True)
    state_description = models.TextField(db_column='State Description', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    consider_weight = models.TextField(db_column='Consider Weight (Provision)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    billing_weight = models.TextField(db_column='Billing Weight', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    consider_value = models.TextField(db_column='Consider Value (Provision)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    billing_value = models.TextField(db_column='Billing Value', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bill_no_field = models.BigIntegerField(db_column='Bill No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    bill_status = models.TextField(db_column='Bill Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    entry_sheet = models.TextField(db_column='SES No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    created_on = models.TextField(db_column='SES Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    changed_on = models.TextField(db_column='2nd Ref', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    accin = models.TextField(db_column='SES Status', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'MIS FULL'
        
class VendorMaster(models.Model):
    vendor = models.TextField(db_column='Vendor', primary_key = True)  # Field name made lowercase.
    vendordescription = models.TextField(db_column='VENDOR DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    name3 = models.TextField(db_column='Name 3', blank=True, null=True)  # Field name made lowercase.
    name4 = models.TextField(db_column='Name 4', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    postalcode = models.IntegerField(db_column='Postal Code', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    recovery = models.TextField(db_column='Recovery', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Vendor Master'

class PartMaster(models.Model):
    material = models.IntegerField(db_column='Material', primary_key = True, default = 1)  # Field name made lowercase.
    materialdescription = models.TextField(db_column='Material description', blank=True, null=True)  # Field name made lowercase.
    vendorcode = models.TextField(db_column='Vendor Code', blank=True, null=True)  # Field name made lowercase.
    vendordescription = models.TextField(db_column='Vendor Description', blank=True, null=True)  # Field name made lowercase.
    quotavalidfrom = models.TextField(db_column='Quota Valid from', blank=True, null=True)  # Field name made lowercase.
    quotavalidto = models.TextField(db_column='Quota Valid to', blank=True, null=True)  # Field name made lowercase.
    quota_field = models.IntegerField(db_column='Quota %', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    quotanumber = models.IntegerField(db_column='Quota Number', blank=True, null=True)  # Field name made lowercase.
    proctype = models.TextField(db_column='Proc Type', blank=True, null=True)  # Field name made lowercase.
    splproctype = models.TextField(db_column='Spl Proc Type', blank=True, null=True)  # Field name made lowercase.
    bulkind = models.TextField(db_column='Bulk Ind', blank=True, null=True)  # Field name made lowercase.
    mrpcntrl = models.IntegerField(db_column='MRP Cntrl', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Part Master'

class OriginState(models.Model):
    origin = models.TextField(db_column='ORIGIN', primary_key=True)  # Field name made lowercase.
    origin_full_name = models.TextField(db_column='Origin Full Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    origin_state_name = models.TextField(db_column='Origin State Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Origin State'

class RateMaster(models.Model):
    state_description = models.TextField(db_column='State Description', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    apr_22 = models.TextField(db_column='Apr-22', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    may_22 = models.TextField(db_column='May-22', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    jun_22 = models.TextField(db_column='Jun-22', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    jul_22 = models.TextField(db_column='Jul-22', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    aug_22 = models.TextField(db_column='Aug-22', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    sep_22 = models.TextField(db_column='Sep-22', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    oct_22 = models.TextField(db_column='Oct-22', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    nov_22 = models.TextField(db_column='Nov-22', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    dec_22 = models.BigIntegerField(db_column='Dec-22', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jan_23 = models.BigIntegerField(db_column='Jan-23', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    feb_23 = models.BigIntegerField(db_column='Feb-23', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mar_23 = models.BigIntegerField(db_column='Mar-23', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Rate Master'

class WeightMaster(models.Model):
    activity = models.TextField(db_column='Activity', blank=True, null=True)  # Field name made lowercase.
    part_no_field = models.TextField(db_column='Wt Part No.', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    part_description = models.TextField(db_column='Part Description', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    supplier_code = models.TextField(db_column='Supplier Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.    
    supplier_name = models.TextField(db_column='Supplier Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.    
    approved_packging = models.TextField(db_column='Approved Packging', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    actual_packging = models.TextField(db_column='Actual Packging', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    indivudual_part_s_wt_field = models.TextField(db_column="Indivudual Part's Wt.", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    indivudual_box_s_wt_field = models.TextField(db_column="Indivudual Box's Wt.", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    qty_box = models.BigIntegerField(db_column='Qty./Box', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gross_wt_field = models.TextField(db_column='Gross Wt.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    wt_part = models.TextField(db_column='Wt./Part', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    l_mm_field = models.TextField(db_column='L (mm)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    w_mm_field = models.TextField(db_column='W (mm)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    h_mm_field = models.TextField(db_column='H (mm)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    cbm_volumetric = models.TextField(db_column='CBM volumetric', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    cbm_against_gross_wt = models.TextField(db_column='CBM against gross wt', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    chargeable_cbm_for_cc = models.TextField(db_column='Chargeable CBM for CC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    cbm_part = models.TextField(db_column='CBM/Part', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    wt_cft_volumetric_ptl = models.TextField(db_column='Wt/CFT volumetric PTL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    wt_cft_against_gross_wt_ptl = models.TextField(db_column='Wt/CFT against gross wt PTL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    chargeable_cft_for_ptl = models.TextField(db_column='Chargeable CFT for PTL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    wt_part_ptl = models.TextField(db_column='Wt./Part PTL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    wt_cft_volumetric_express_road = models.TextField(db_column='Wt/CFT volumetric Express Road', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    wt_cft_against_gross_wt_express_road = models.TextField(db_column='Wt/CFT against gross wt Express Road', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    chargeable_cft_for_express_road = models.TextField(db_column='Chargeable CFT for Express Road', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    wt_part_express_road = models.TextField(db_column='Wt./Part Express Road', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    volumetric_wt_air = models.TextField(db_column='volumetric Wt. Air', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    gross_wt_air = models.TextField(db_column='gross wt Air', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    chargeable_cft_for_air = models.TextField(db_column='Chargeable CFT for Air', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    wt_part_air = models.TextField(db_column='Wt./Part Air', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    volumetric_wt_train = models.TextField(db_column='volumetric Wt. Train', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    gross_wt_train = models.TextField(db_column='gross wt Train', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    chargeable_cft_for_train = models.TextField(db_column='Chargeable CFT for Train', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    wt_part_train = models.TextField(db_column='Wt./Part Train', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = True
        db_table = 'Weight Master'

class CbmCft(models.Model):
    activity = models.TextField(db_column='Activity CBM CFT', blank=True, null=True)  # Field name made lowercase.
    lsp_code = models.TextField(db_column='LSP Code', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lsp_short_name = models.TextField(db_column='LSP Short Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.  
    cft_cbm = models.BigIntegerField(db_column='CFT/CBM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'CBM/CFT'

class TransporterMaster(models.Model):
    lsp_code = models.TextField(db_column='LSP Code', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.   
    lsp_name = models.TextField(db_column='LSP Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.   
    lsp_short_name = models.TextField(db_column='LSP Short Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contact_name_1 = models.TextField(db_column='Contact Name - 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contact_nos_1 = models.TextField(db_column='Contact Nos - 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mail_id_1 = models.TextField(db_column='Mail Id - 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contact_name_2 = models.TextField(db_column='Contact Name - 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contact_nos_2 = models.TextField(db_column='Contact Nos - 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mail_id_2 = models.TextField(db_column='Mail Id - 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contact_name_3 = models.TextField(db_column='Contact Name - 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contact_nos_3 = models.TextField(db_column='Contact Nos - 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mail_id_3 = models.TextField(db_column='Mail Id - 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'Transporter Master'

class SvpsRemark(models.Model):
    stage_wise_status_field = models.TextField(db_column='Stage wise Status ', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    status_meaning = models.TextField(db_column='Status Meaning', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    actual_status = models.TextField(db_column='Actual Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'SVPS Remark'

class Po(models.Model):
    po_no_field = models.BigIntegerField(db_column='PO No.', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    contract_validity = models.TextField(db_column='Contract Validity', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    extention = models.TextField(db_column='Extention', blank=True, null=True)  # Field name made lowercase.
    po_creation_date = models.TextField(db_column='PO Creation Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    po_start_validity = models.TextField(db_column='PO Start Validity', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    po_end_validity = models.TextField(db_column='PO End Validity', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vendor_code = models.TextField(db_column='Vendor Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vendor_name = models.TextField(db_column='Vendor Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    activity = models.TextField(db_column='Activity', blank=True, null=True)  # Field name made lowercase.
    user_for_bill_clearance = models.TextField(db_column='User for bill clearance', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    po_for = models.TextField(db_column='PO for', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.       
    main_activity = models.TextField(db_column='Main Activity', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mode = models.TextField(db_column='Mode', blank=True, null=True)  # Field name made lowercase.
    io_no = models.TextField(db_column='IO No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gl_no = models.TextField(db_column='GL No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cost_centre = models.TextField(db_column='Cost Centre', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'PO'

class Ses(models.Model):
    v_code = models.TextField(db_column='V_Code', primary_key=True)  # Field name made lowercase.
    v_name = models.TextField(db_column='V_Name', blank=True, null=True)  # Field name made lowercase.
    po_no_field = models.BigIntegerField(db_column='PO No.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    reference = models.TextField(db_column='SES Reference', blank=True, null=True)  # Field name made lowercase.
    document_date = models.TextField(db_column='Document Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    entry_sheet = models.BigIntegerField(db_column='Entry Sheet', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    created_on = models.TextField(db_column='Created on', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    changed_on = models.DateTimeField(db_column='Changed on', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    accin = models.TextField(db_column='AccIn', blank=True, null=True)  # Field name made lowercase.
    basic_amount = models.TextField(db_column='Basic Amount', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    ses_qty_field = models.TextField(db_column='SES Qty.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    gl_a_c = models.BigIntegerField(db_column='GL A/c', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. 
    cost_centre = models.TextField(db_column='Cost Centre', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rate = models.TextField(db_column='Rate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    service_no_field = models.TextField(db_column='Service No.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    service_description = models.TextField(db_column='Service Description', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fin_doc_no_field = models.TextField(db_column='Fin Doc. No.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = True
        db_table = 'SES'

class InboundShipment(models.Model):
    invoiceid = models.BigIntegerField(db_column='InvoiceId', primary_key=True)  # Field name made lowercase.
    invoiceno = models.TextField(db_column='InvoiceNo', blank=True, null=True)  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
    uploadeddate = models.DateTimeField(db_column='UploadedDate', blank=True, null=True)  # Field name made lowercase.
    vendorcode = models.TextField(db_column='VendorCode', blank=True, null=True)  # Field name made lowercase.
    vendorname = models.TextField(db_column='VendorName', blank=True, null=True)  # Field name made lowercase.
    currentstatus = models.TextField(db_column='CurrentStatus', blank=True, null=True)  # Field name made lowercase.
    ponumber = models.BigIntegerField(db_column='PONumber', blank=True, null=True)  # Field name made lowercase.
    signedby = models.TextField(db_column='SignedBy', blank=True, null=True)  # Field name made lowercase.
    isverified = models.TextField(db_column='IsVerified', blank=True, null=True)  # Field name made lowercase.
    signtimestamp = models.TextField(db_column='SignTimestamp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    plantcode = models.BigIntegerField(db_column='PlantCode', blank=True, null=True)  # Field name made lowercase.
    plantname = models.TextField(db_column='PlantName', blank=True, null=True)  # Field name made lowercase.
    shipmentcode = models.TextField(db_column='ShipmentCode', blank=True, null=True)  # Field name made lowercase.
    rmsrefnumber = models.TextField(db_column='RMSRefNumber', blank=True, null=True)  # Field name made lowercase.
    invoiceamount = models.TextField(db_column='InvoiceAmount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    uaremark = models.TextField(db_column='UARemark', blank=True, null=True)  # Field name made lowercase.
    gdcremark = models.TextField(db_column='GDCRemark', blank=True, null=True)  # Field name made lowercase.
    rejectedbygdc = models.TextField(db_column='RejectedByGDC', blank=True, null=True)  # Field name made lowercase.
    shipmentno = models.TextField(db_column='ShipmentNo', blank=True, null=True)  # Field name made lowercase.
    sesno = models.BigIntegerField(db_column='SESNO', blank=True, null=True)  # Field name made lowercase.
    shipmentcostingno = models.TextField(db_column='ShipmentCostingNo', blank=True, null=True)  # Field name made lowercase.
    shipmentdate = models.TextField(db_column='ShipmentDate', blank=True, null=True)  # Field name made lowercase.
    shipmentstatus = models.TextField(db_column='ShipmentStatus', blank=True, null=True)  # Field name made lowercase.
    shipmentcostingstatus = models.TextField(db_column='ShipmentCostingStatus', blank=True, null=True)  # Field name made lowercase.
    mrrlrunstatus = models.TextField(db_column='MRRLRUNSTATUS', blank=True, null=True)  # Field name made lowercase.
    basicfreightcharges = models.TextField(db_column='BasicFreightCharges', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    discountamount = models.TextField(db_column='DiscountAmount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    gstamount = models.TextField(db_column='GSTAmount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Inbound Shipment'

class Svps(models.Model):
    invoiceid = models.BigIntegerField(db_column='InvoiceId', primary_key=True)  # Field name made lowercase.
    signtimestamp = models.DateTimeField(db_column='SignTimestamp', blank=True, null=True)  # Field name made lowercase.
    ponumber = models.BigIntegerField(db_column='PONumber', blank=True, null=True)  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate', blank=True, null=True)  # Field name made lowercase.
    invoiceno = models.TextField(db_column='InvoiceNo', blank=True, null=True)  # Field name made lowercase.
    agencyname = models.TextField(db_column='AgencyName', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    vendorcode = models.TextField(db_column='VendorCode', blank=True, null=True)  # Field name made lowercase.
    vendorname = models.TextField(db_column='VendorName', blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='Remark', blank=True, null=True)  # Field name made lowercase.
    uploadeddate = models.DateTimeField(db_column='UploadedDate', blank=True, null=True)  # Field name made lowercase.
    sap_isrejected = models.BigIntegerField(db_column='SAP_IsRejected', blank=True, null=True)  # Field name made lowercase.
    sap_text = models.TextField(db_column='SAP_TEXT', blank=True, null=True)  # Field name made lowercase.
    sap_fi_document_number = models.TextField(db_column='SAP_FI_DOCUMENT_NUMBER', blank=True, null=True)  # Field name made lowercase.
    sap_batch_creation_date = models.DateTimeField(db_column='SAP_BATCH_CREATION_DATE', blank=True, null=True)  # Field name made lowercase.
    sap_rejection_date = models.TextField(db_column='SAP_REJECTION_DATE', blank=True, null=True)  # Field name made lowercase.
    sap_inv_verification_date = models.DateTimeField(db_column='SAP_INV_VERIFICATION_DATE', blank=True, null=True)  # Field name made lowercase.
    number_2nd_rel_field = models.DateTimeField(db_column='2nd Rel.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    sap_parking_date = models.DateTimeField(db_column='SAP_PARKING_DATE', blank=True, null=True)  # Field name made lowercase.
    sap_posting_date = models.DateTimeField(db_column='SAP_POSTING_DATE', blank=True, null=True)  # Field name made lowercase.
    sap_entry_date_can_be_consider_as_ses_creation_date_field = models.DateTimeField(db_column='SAP_ENTRY_DATE (Can be consider as SES creation date)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sap_due_date = models.DateTimeField(db_column='SAP_DUE_DATE', blank=True, null=True)  # Field name made lowercase.
    sap_business_location = models.TextField(db_column='SAP_BUSINESS_LOCATION', blank=True, null=True)  # Field name made lowercase.
    sap_buyer_group = models.TextField(db_column='SAP_BUYER_GROUP', blank=True, null=True)  # Field name made lowercase.
    sap_payment_date = models.DateTimeField(db_column='SAP_Payment_Date', blank=True, null=True)  # Field name made lowercase.
    sap_clearing_doc_no = models.TextField(db_column='SAP_Clearing_Doc_No', blank=True, null=True)  # Field name made lowercase.
    sap_cheque_no = models.TextField(db_column='SAP_Cheque_No', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'SVPS'

class LrBill(models.Model):
    lr_no_field = models.BigIntegerField(db_column='LR No', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    bill_no_field = models.BigIntegerField(db_column='Bill No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    basic_bill_value = models.TextField(db_column='Basic Bill Value', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.     

    class Meta:
        managed = True
        db_table = 'LR BILL'

class FastDump(models.Model):
    indent_no_field = models.TextField(db_column='Dump Indent No.', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    request_date = models.DateTimeField(db_column='Request Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mode_of_premium_freight = models.TextField(db_column='Mode Of Premium Freight', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    incoterm = models.TextField(db_column='INCOTERM', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    pending_with = models.TextField(db_column='Pending with', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    indenter_name = models.TextField(db_column='Indenter Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    indenter_t_no = models.BigIntegerField(db_column='Indenter T No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vendor_name = models.TextField(db_column='Vendor Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vendor_code = models.TextField(db_column='Vendor Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vendor_location_state = models.TextField(db_column='Vendor Location State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vendor_location_city = models.TextField(db_column='Vendor Location City', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pickup_state = models.TextField(db_column='Pickup State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pickup_city = models.TextField(db_column='Pickup City', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pickup_date = models.DateTimeField(db_column='Pickup Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    destination_state = models.TextField(db_column='Destination State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    destination_city = models.TextField(db_column='Destination City', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_no = models.TextField(db_column='Part No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.      
    part_description = models.TextField(db_column='Part Description', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    indent_weight_kg_field = models.TextField(db_column='Indent Weight (Kg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cost_to_be_borne_by = models.TextField(db_column='Cost To be Borne By', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cost_center = models.BigIntegerField(db_column='Cost Center', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    description_of_cc_entered = models.TextField(db_column='Description Of CC Entered', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    if_shared_any_other_agreed_with_vender_for_recovery_field = models.TextField(db_column='If Shared (Any other % agreed with vender for recovery)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    indent_qty_field = models.TextField(db_column='Indent Qty-', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    indent_issue_to_lsp = models.TextField(db_column='Indent issue to LSP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'Fast Dump'

class PfLspMis(models.Model):
    lsp = models.TextField(db_column='LSP', primary_key=True)  # Field name made lowercase.
    mode = models.TextField(db_column='MODE', blank=True, null=True)  # Field name made lowercase.
    indent_no_field = models.TextField(db_column='Indent No.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    indent_request_date_field = models.DateTimeField(db_column='Indent Request date ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lr_no_field = models.BigIntegerField(db_column='LR NO.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lr_date = models.TextField(db_column='LR DATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.      
    pickup_time_field = models.TimeField(db_column='Pickup Time  ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    flight_no = models.TextField(db_column='Flight No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.  
    flight_date = models.TextField(db_column='Flight Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    flight_time = models.TextField(db_column='Flight Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    invoice_no = models.TextField(db_column='Invoice No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_number = models.TextField(db_column='PART NUMBER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pkg = models.TextField(db_column='PKG', blank=True, null=True)  # Field name made lowercase.
    quantity = models.TextField(db_column='QUANTITY', blank=True, null=True)  # Field name made lowercase.
    indent_wt = models.TextField(db_column='INDENT WT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.  
    chrg_wt = models.TextField(db_column='Chrg.WT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.      
    consignor = models.TextField(db_column='CONSIGNOR', blank=True, null=True)  # Field name made lowercase.
    consignor_state = models.TextField(db_column='CONSIGNOR STATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cnr_location = models.TextField(db_column='CNR. LOCATION', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    consignee = models.TextField(db_column='CONSIGNEE', blank=True, null=True)  # Field name made lowercase.
    status_w_h_in_transit_field = models.TextField(db_column='STATUS(W/H, IN TRANSIT)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    edd = models.TextField(db_column='EDD', blank=True, null=True)  # Field name made lowercase.
    delivery_date = models.DateTimeField(db_column='Delivery Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    remarks_field = models.TextField(db_column='REMARKS ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    leci_no = models.TextField(db_column='LECI No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.      
    grn_no = models.TextField(db_column='GRN No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.        

    class Meta:
        managed = True
        db_table = 'PF LSP MIS'
 
class PfMis(models.Model):
    consider_pick_up_month = models.TextField(db_column='Consider Pick-up Month', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    indent_request_month = models.TextField(db_column='Indent Request Month', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    s_no = models.BigIntegerField(db_column='S. No', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.     
    lsp = models.TextField(db_column='LSP', blank=True, null=True)  # Field name made lowercase.
    mode = models.TextField(db_column='MODE', blank=True, null=True)  # Field name made lowercase.
    indent_no_field = models.TextField(db_column='Indent No.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    indent_request_date_field = models.TextField(db_column='Indent Request date ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lr_no_field = models.BigIntegerField(db_column='LR NO.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    lr_date = models.TextField(db_column='LR DATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.      
    pickup_time_field = models.TextField(db_column='Pickup Time  ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    flight_no = models.TextField(db_column='Flight No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.  
    flight_date = models.TextField(db_column='Flight Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    flight_time = models.TextField(db_column='Flight Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    invoice_no = models.TextField(db_column='Invoice No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_number = models.TextField(db_column='PART NUMBER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pkg = models.TextField(db_column='PKG', blank=True, null=True)  # Field name made lowercase.
    quantity = models.TextField(db_column='QUANTITY', blank=True, null=True)  # Field name made lowercase.
    indent_wt = models.TextField(db_column='INDENT WT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.  
    chrg_wt = models.TextField(db_column='Chrg.WT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.      
    consignor = models.TextField(db_column='CONSIGNOR', blank=True, null=True)  # Field name made lowercase.
    consignor_state = models.TextField(db_column='CONSIGNOR STATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cnr_location = models.TextField(db_column='CNR. LOCATION', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    consignee = models.TextField(db_column='CONSIGNEE', blank=True, null=True)  # Field name made lowercase.
    status_w_h_in_transit_field = models.TextField(db_column='STATUS(W/H, IN TRANSIT)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    edd = models.TextField(db_column='EDD', blank=True, null=True)  # Field name made lowercase.
    delivery_date = models.TextField(db_column='Delivery Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    remarks_field = models.TextField(db_column='REMARKS ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    leci_no = models.TextField(db_column='LECI No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.      
    grn_no = models.TextField(db_column='GRN No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.        
    dump_indent_no_field = models.TextField(db_column='Dump Indent No.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    request_date = models.TextField(db_column='Request Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mode_of_premium_freight = models.TextField(db_column='Mode Of Premium Freight', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    incoterm = models.TextField(db_column='INCOTERM', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    pending_with = models.TextField(db_column='Pending with', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    indenter_name = models.TextField(db_column='Indenter Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    indenter_t_no = models.TextField(db_column='Indenter T No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    vendor_name = models.TextField(db_column='Vendor Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vendor_code = models.TextField(db_column='Vendor Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vendor_location_state = models.TextField(db_column='Vendor Location State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vendor_location_city = models.TextField(db_column='Vendor Location City', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pickup_state = models.TextField(db_column='Pickup State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pickup_city = models.TextField(db_column='Pickup City', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pickup_date = models.TextField(db_column='Pickup Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    destination_state = models.TextField(db_column='Destination State', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    destination_city = models.TextField(db_column='Destination City', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    part_no = models.TextField(db_column='Part No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.      
    part_description = models.TextField(db_column='Part Description', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    indent_weight_kg_field = models.TextField(db_column='Indent Weight (Kg)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cost_to_be_borne_by = models.TextField(db_column='Cost To be Borne By', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cost_center = models.TextField(db_column='Cost Center', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    description_of_cc_entered = models.TextField(db_column='Description Of CC Entered', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    if_shared_any_other_agreed_with_vender_for_recovery_field = models.TextField(db_column='If Shared (Any other % agreed with vender for recovery)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    indent_qty_field = models.TextField(db_column='Indent Qty-', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    indent_issue_to_lsp = models.TextField(db_column='Indent issue to LSP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vendor_code_field = models.TextField(db_column='Vendor Code ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    vendor = models.TextField(db_column='Vendor', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    consider_city = models.TextField(db_column='Consider City', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    zone_for_air_train = models.TextField(db_column='Zone for Air/Train', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    distance_from_utk_to_vendor_consider_city_distance_check_from_google_field = models.TextField(db_column='Distance from UTK to Vendor consider City (distance check from google)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    distance_for_speed_truck = models.TextField(db_column='Distance for Speed Truck', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nearest_airport = models.TextField(db_column='Nearest Airport', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    distance_from_pick_up_location_to_airport = models.TextField(db_column='Distance from Pick-up location to Airport', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nearest_railway_station = models.TextField(db_column='Nearest Railway station', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    distance_from_pick_up_location_to_railway_station = models.TextField(db_column='Distance from Pick-up location to Railway Station', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    zone = models.TextField(db_column='Zone', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PF MIS'

class DistanceRange(models.Model):
    vendor_code_field = models.TextField(db_column='Vendor Code ', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    vendor = models.TextField(db_column='Vendor', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    consider_city = models.TextField(db_column='Consider City', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    zone_for_air_train = models.TextField(db_column='Zone for Air/Train', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    distance_from_utk_to_vendor_consider_city_distance_check_from_google_field = models.TextField(db_column='Distance from UTK to Vendor consider City (distance check from google)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    distance_for_speed_truck = models.TextField(db_column='Distance for Speed Truck', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nearest_airport = models.TextField(db_column='Nearest Airport', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    distance_from_pick_up_location_to_airport = models.TextField(db_column='Distance from Pick-up location to Airport', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nearest_railway_station = models.TextField(db_column='Nearest Railway station', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    distance_from_pick_up_location_to_railway_station = models.TextField(db_column='Distance from Pick-up location to Railway Station', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = True
        db_table = 'Distance Range'