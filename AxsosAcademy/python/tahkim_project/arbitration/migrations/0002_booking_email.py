from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("arbitration", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="email",
            field=models.EmailField(blank=True, default="", max_length=254, verbose_name="البريد الإلكتروني"),
        ),
    ]
