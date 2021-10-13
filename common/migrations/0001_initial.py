# Generated by Django 3.2.5 on 2021-10-12 06:40

import common.models.item
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BundleGroup',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'wm_bundle_group',
            },
        ),
        migrations.CreateModel(
            name='ComplainStatus',
            fields=[
                ('code', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'wm_comment_complain_status',
            },
        ),
        migrations.CreateModel(
            name='ContactStatus',
            fields=[
                ('code', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'wm_user_contact_status',
            },
        ),
        migrations.CreateModel(
            name='ContactType',
            fields=[
                ('code', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'wm_user_contact_type',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'db_table': 'wm_user_gender',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(1.0)])),
                ('highlighted', models.BooleanField(default=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('sales', models.PositiveIntegerField(default=0)),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'wm_item',
            },
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('code', models.CharField(max_length=25, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'wm_item_category',
            },
        ),
        migrations.CreateModel(
            name='OfferStatus',
            fields=[
                ('code', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'wm_offer_status',
            },
        ),
        migrations.CreateModel(
            name='OfferType',
            fields=[
                ('code', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'wm_offer_type',
            },
        ),
        migrations.CreateModel(
            name='OriginCategory',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'wm_item_origin_category',
            },
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('enabled', models.BooleanField()),
            ],
            options={
                'db_table': 'wm_payment_type',
            },
        ),
        migrations.CreateModel(
            name='PurchaseStatus',
            fields=[
                ('code', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'wm_purchase_status',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=250, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('pepper', models.CharField(max_length=128)),
                ('birth_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('news_feed', models.BooleanField()),
                ('tier_points', models.IntegerField()),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.gender')),
                ('payments', models.ManyToManyField(to='common.PaymentType')),
            ],
            options={
                'db_table': 'wm_user',
            },
        ),
        migrations.CreateModel(
            name='UserStatus',
            fields=[
                ('code', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'wm_user_status',
            },
        ),
        migrations.CreateModel(
            name='UserTier',
            fields=[
                ('code', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('base_points', models.IntegerField()),
                ('next_tier_points', models.IntegerField()),
            ],
            options={
                'db_table': 'wm_user_tier',
            },
        ),
        migrations.CreateModel(
            name='UserActivation',
            fields=[
                ('code', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('activated_at', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.user')),
            ],
            options={
                'db_table': 'wm_user_activation',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.userstatus'),
        ),
        migrations.AddField(
            model_name='user',
            name='tier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.usertier'),
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.PositiveIntegerField()),
                ('update_date', models.DateField(auto_now_add=True)),
                ('last_buy_date', models.DateTimeField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.item')),
            ],
            options={
                'db_table': 'wm_item_stock',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('sid', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('expires', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.user')),
            ],
            options={
                'db_table': 'wm_user_session',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('final_price', models.FloatField()),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('payment_date', models.DateField()),
                ('bundle_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.bundlegroup')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.paymenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.user')),
            ],
            options={
                'db_table': 'wm_purchase',
            },
        ),
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.origincategory')),
            ],
            options={
                'db_table': 'wm_item_origin',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=500)),
                ('settings', models.CharField(max_length=1000)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.offerstatus')),
            ],
            options={
                'db_table': 'wm_offer',
            },
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.BooleanField()),
                ('path', models.FileField(upload_to=common.models.item.Item.item_image_directory)),
                ('mime_type', models.CharField(max_length=50)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.item')),
            ],
            options={
                'db_table': 'wm_item_image',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.itemcategory'),
        ),
        migrations.AddField(
            model_name='item',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.origin'),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=250)),
                ('is_main', models.BooleanField()),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.contactstatus')),
                ('t', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.contacttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.user')),
            ],
            options={
                'db_table': 'wm_user_contact',
            },
        ),
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=128)),
                ('message', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('replied_at', models.DateTimeField(auto_now=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.complainstatus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.user')),
            ],
            options={
                'db_table': 'wm_comment_complain',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=250)),
                ('liked', models.BooleanField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.user')),
            ],
            options={
                'db_table': 'wm_comment',
            },
        ),
        migrations.CreateModel(
            name='Bundle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bundle_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.bundlegroup')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.item')),
            ],
            options={
                'db_table': 'wm_bundle',
            },
        ),
    ]
