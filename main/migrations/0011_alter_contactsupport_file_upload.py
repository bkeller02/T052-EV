# Generated by Django 4.2.6 on 2023-11-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_contactsupport_file_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactsupport',
            name='file_upload',
            field=models.FileField(help_text='max. 42 megabytes', null=True, upload_to='contact/submissions/documents/'),
        ),
    ]
