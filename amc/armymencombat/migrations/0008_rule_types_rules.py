# Generated by Django 4.0.7 on 2023-07-21 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('armymencombat', '0007_alter_vehicle_upgrades_weapon_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule_Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule_type', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Rule Types',
            },
        ),
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=100)),
                ('rule_text', models.CharField(max_length=500)),
                ('rule_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='armymencombat.rule_types')),
            ],
            options={
                'verbose_name_plural': 'Rules Reference',
            },
        ),
    ]
