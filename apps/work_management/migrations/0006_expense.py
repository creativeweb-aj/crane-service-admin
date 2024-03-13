# Generated by Django 3.2.18 on 2024-03-13 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work_management', '0005_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('payment_type', models.CharField(blank=True, choices=[('cash', 'Cash'), ('bank_transfer', 'Bank Transfer'), ('online', 'Online')], max_length=13, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='work_management.staff')),
            ],
            options={
                'db_table': 'expense',
            },
        ),
    ]