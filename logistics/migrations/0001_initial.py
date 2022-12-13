# Generated by Django 4.1.1 on 2022-10-01 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MIS',
            fields=[
                ('transportername', models.TextField(blank=True, db_column='Transporter Name', null=True)),
                ('activity_frommanual_vinsummis_field', models.TextField(blank=True, db_column='Activity (from manual-Vinsum MIS)', null=True)),
                ('paymenttype_frommaster_field', models.TextField(blank=True, db_column='PAYMENT TYPE (from master)', null=True)),
                ('activitystatus', models.TextField(blank=True, db_column='Activity Status', null=True)),
                ('location', models.TextField(blank=True, db_column='Location', null=True)),
                ('deliverydate', models.TextField(blank=True, db_column='Delivery Date', null=True)),
                ('grnnumber', models.TextField(blank=True, db_column='Grn Number', null=True)),
                ('lrno_field', models.IntegerField(blank=True, db_column='LR no.', null=True)),
                ('lrdt_field', models.TextField(blank=True, db_column='LR dt.', null=True)),
                ('lrtime', models.TextField(blank=True, db_column='LR Time', null=True)),
                ('consignor', models.TextField(blank=True, db_column='Consignor', null=True)),
                ('consignee', models.TextField(blank=True, db_column='Consignee', null=True)),
                ('consignorlocation', models.TextField(blank=True, db_column='Consignor Location', null=True)),
                ('locationcode', models.TextField(blank=True, db_column='Location Code', null=True)),
                ('state', models.TextField(blank=True, db_column='State', null=True)),
                ('invoiceno_field', models.TextField(db_column='Invoice No.', primary_key=True, serialize=False)),
                ('invoicedate', models.TextField(blank=True, db_column='Invoice Date', null=True)),
                ('vendorpono', models.TextField(blank=True, db_column='Vendor PO No', null=True)),
                ('partno_field', models.FloatField(blank=True, db_column='Part No.', null=True)),
                ('pkg', models.IntegerField(blank=True, db_column='PKG', null=True)),
                ('pkgtype', models.TextField(blank=True, db_column='PKG TYPE', null=True)),
                ('qty_field', models.IntegerField(blank=True, db_column='Qty.', null=True)),
                ('actualwt_kg_field', models.IntegerField(blank=True, db_column='Actual Wt. (KG)', null=True)),
            ],
            options={
                'db_table': 'MIS',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='VC_NO',
            fields=[
                ('VC_No', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Level', models.CharField(max_length=50, null=True)),
                ('Component_number', models.CharField(max_length=50, null=True)),
                ('Object_description', models.CharField(max_length=50, null=True)),
                ('Item_Number', models.CharField(max_length=50, null=True)),
                ('Component_quantity', models.CharField(max_length=20, null=True)),
                ('Component_unit', models.CharField(max_length=50, null=True)),
                ('Change_Number', models.CharField(max_length=50, null=True)),
                ('Product_store_location', models.CharField(max_length=50, null=True)),
                ('BOM_number', models.CharField(max_length=50, null=True)),
                ('Plant', models.CharField(max_length=50, null=True)),
                ('Valid_from', models.DateField(null=True)),
                ('Valid_to', models.DateField(null=True)),
                ('Special_procurement', models.CharField(max_length=50, null=True)),
                ('Bulk_material_item_material', models.CharField(max_length=50, null=True)),
                ('VC_number_description', models.CharField(max_length=255, null=True)),
                ('First', models.CharField(max_length=255, null=True)),
                ('Second', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'VC_NO',
            },
        ),
    ]
