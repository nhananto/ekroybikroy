# Generated by Django 3.1.1 on 2020-11-16 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0011_product_condition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='district',
            name='division',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='short_desc',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='location',
            name='area',
        ),
        migrations.RemoveField(
            model_name='location',
            name='district',
        ),
        migrations.RemoveField(
            model_name='product',
            name='address',
        ),
        migrations.RemoveField(
            model_name='product',
            name='desc',
        ),
        migrations.AddField(
            model_name='location',
            name='name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.location'),
        ),
        migrations.AddField(
            model_name='location',
            name='type',
            field=models.CharField(choices=[('division', 'Division'), ('district', 'District'), ('thana', 'Thana'), ('city', 'City')], default=None, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.location'),
        ),
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Area',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='District',
        ),
        migrations.DeleteModel(
            name='Division',
        ),
    ]
