# Generated by Django 4.1.2 on 2022-10-07 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_user_gender_alter_user_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobPost', to='api.jobpost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='api.user')),
            ],
        ),
    ]