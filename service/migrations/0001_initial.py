# Generated by Django 4.1.3 on 2023-03-21 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0003_alter_patient_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('injection', 'Injection'), ('solution', 'Solution'), ('wound_dressing', 'Wound Dressing')], max_length=100)),
                ('time', models.DateTimeField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
    ]
