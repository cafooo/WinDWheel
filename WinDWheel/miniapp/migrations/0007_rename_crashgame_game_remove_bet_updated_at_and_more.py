# Generated by Django 5.1.6 on 2025-03-12 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniapp', '0006_alter_crashgame_options_crashgame_is_active_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CrashGame',
            new_name='Game',
        ),
        migrations.RemoveField(
            model_name='bet',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='bet',
            name='cashout_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='bet',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='bet',
            name='cashout_multiplier',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
