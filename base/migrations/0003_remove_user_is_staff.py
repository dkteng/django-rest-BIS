# Generated by Django 4.2.6 on 2023-11-02 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_user_alter_book_borrow_date_alter_book_due_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]
