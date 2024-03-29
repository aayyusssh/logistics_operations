# Generated by Django 4.1.2 on 2022-10-08 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0002_alter_mis_consignorlocation_alter_mis_deliverydate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeciDump',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecino', models.IntegerField(blank=True, db_column='LECINo', null=True)),
                ('rfidno', models.IntegerField(blank=True, db_column='RFIDNo', null=True)),
                ('checkpoint', models.TextField(blank=True, db_column='CheckPoint', null=True)),
                ('chkindate', models.TextField(blank=True, db_column='ChkinDate', null=True)),
                ('chktime', models.TextField(blank=True, db_column='ChkTime', null=True)),
                ('trucks_carslicenseplateno_field', models.TextField(blank=True, db_column='Trucks/CarsLicensePlateNo.', null=True)),
                ('firstname', models.TextField(blank=True, db_column='FirstName', null=True)),
                ('lastname', models.TextField(blank=True, db_column='LastName', null=True)),
                ('no', models.IntegerField(blank=True, db_column='NO', null=True)),
                ('ri', models.TextField(blank=True, db_column='RI', null=True)),
                ('reldate', models.TextField(blank=True, db_column='RelDate', null=True)),
                ('reltime', models.TextField(blank=True, db_column='RelTime', null=True)),
                ('releaseby', models.TextField(blank=True, db_column='Releaseby', null=True)),
                ('outdate', models.TextField(blank=True, db_column='Outdate', null=True)),
                ('outtime', models.TextField(blank=True, db_column='Outtime', null=True)),
                ('outby', models.TextField(blank=True, db_column='Outby', null=True)),
                ('tat_hrs_field', models.IntegerField(blank=True, db_column='TAT(HRS)', null=True)),
                ('weight', models.TextField(blank=True, db_column='Weight', null=True)),
                ('textforloading', models.TextField(blank=True, db_column='TextforLoading', null=True)),
                ('considerlspname', models.TextField(blank=True, db_column='ConsiderLSPName', null=True)),
                ('detention', models.TextField(blank=True, db_column='Detention', null=True)),
            ],
            options={
                'db_table': 'LECI Dump',
                'managed': True,
            },
        ),
    ]
