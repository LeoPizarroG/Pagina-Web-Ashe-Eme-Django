# Generated by Django 3.2.5 on 2021-07-07 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asheeme', '0002_alter_tipo_nombretipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='marca',
            field=models.CharField(max_length=100, verbose_name='Marca'),
        ),
    ]
