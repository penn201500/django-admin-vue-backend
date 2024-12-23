# Generated by Django 5.1.3 on 2024-12-11 07:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("role", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SysMenu",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "name",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="Menu Name"
                    ),
                ),
                (
                    "icon",
                    models.CharField(
                        max_length=100, null=True, verbose_name="Menu Icon"
                    ),
                ),
                (
                    "parent_id",
                    models.IntegerField(null=True, verbose_name="Parent Menu ID"),
                ),
                ("order_num", models.IntegerField(null=True, verbose_name="Order")),
                (
                    "path",
                    models.CharField(max_length=200, null=True, verbose_name="Router"),
                ),
                (
                    "component",
                    models.CharField(max_length=255, null=True, verbose_name="Path"),
                ),
                (
                    "menu_type",
                    models.CharField(
                        max_length=1,
                        null=True,
                        verbose_name="Menu Type（Category Menu Button）",
                    ),
                ),
                (
                    "perms",
                    models.CharField(
                        max_length=100, null=True, verbose_name="Permission"
                    ),
                ),
                (
                    "create_time",
                    models.DateField(null=True, verbose_name="Created Time"),
                ),
                (
                    "update_time",
                    models.DateField(null=True, verbose_name="Updated Time"),
                ),
                (
                    "remark",
                    models.CharField(max_length=500, null=True, verbose_name="Comment"),
                ),
            ],
            options={
                "db_table": "sys_menu",
            },
        ),
        migrations.CreateModel(
            name="SysRoleMenu",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "menu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="menu.sysmenu"
                    ),
                ),
                (
                    "role",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="role.sysrole"
                    ),
                ),
            ],
            options={
                "db_table": "sys_role_menu",
            },
        ),
    ]
