# Generated by Django 3.2.3 on 2021-06-09 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0008_auto_20210610_0042'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='NewsApp.customer')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='NewsApp.location')),
            ],
        ),
    ]