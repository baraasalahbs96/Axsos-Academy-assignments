from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Case",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(blank=True, default="غير محدد", max_length=150, verbose_name="الاسم")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("نزاعات تجارية", "نزاعات تجارية"),
                            ("خلافات أسرية", "خلافات أسرية"),
                            ("عقود ومعاملات", "عقود ومعاملات"),
                            ("ميراث وتركات", "ميراث وتركات"),
                            ("عام", "عام"),
                        ],
                        default="عام",
                        max_length=50,
                        verbose_name="نوع القضية",
                    ),
                ),
                ("question", models.TextField(verbose_name="تفاصيل القضية")),
                ("answer", models.TextField(blank=True, null=True, verbose_name="نص الحكم")),
                (
                    "status",
                    models.CharField(
                        choices=[("pending", "بانتظار الحكم"), ("answered", "صدر الحكم")],
                        default="pending",
                        max_length=20,
                        verbose_name="الحالة",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="تاريخ التقديم")),
                ("answered_at", models.DateTimeField(blank=True, null=True, verbose_name="تاريخ صدور الحكم")),
            ],
            options={
                "verbose_name": "قضية",
                "verbose_name_plural": "القضايا والأحكام",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=150, verbose_name="الاسم")),
                ("phone", models.CharField(max_length=30, verbose_name="رقم الهاتف")),
                ("topic", models.CharField(max_length=200, verbose_name="موضوع الاستشارة")),
                ("date", models.DateField(verbose_name="تاريخ الجلسة")),
                ("time", models.TimeField(verbose_name="وقت الجلسة")),
                (
                    "payment_method",
                    models.CharField(
                        choices=[("whatsapp", "الدفع عبر واتساب"), ("online", "الدفع الإلكتروني")],
                        default="whatsapp",
                        max_length=20,
                        verbose_name="طريقة الدفع",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "بانتظار التأكيد"),
                            ("confirmed", "مؤكد"),
                            ("cancelled", "ملغي"),
                        ],
                        default="pending",
                        max_length=20,
                        verbose_name="حالة الحجز",
                    ),
                ),
                ("paid", models.BooleanField(default=False, verbose_name="مدفوع؟")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الحجز")),
            ],
            options={
                "verbose_name": "حجز",
                "verbose_name_plural": "الحجوزات",
                "ordering": ["-created_at"],
            },
        ),
    ]
