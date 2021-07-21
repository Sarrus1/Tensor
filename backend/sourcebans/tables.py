import django_tables2 as tables


class SbBans_Table(tables.Table):
    name = tables.Column(accessor='name',
                         verbose_name='Name', orderable=False)
    authid = tables.Column(accessor='authid',
                           verbose_name='Steam ID', orderable=False)
    # length = tables.Column(accessor='length',
    # verbose_name='Duration', orderable=False)
    date = tables.Column(accessor='date', order_by="created")
    admin_name = tables.Column(accessor='admin_name', order_by="aid")
    reason = tables.Column(accessor='reason',
                           verbose_name='Reason', orderable=False)
    percent = tables.Column(
        accessor="percent", verbose_name="Remaining Progress", orderable=False),
    duration = tables.Column(
        accessor="duration", verbose_name="Length", orderable=False)

    class Meta:
        #template_name = "django_tables2/bootstrap4.html"
        fields = ('date', "name", 'authid', 'admin_name',
                  'duration', 'reason')
        order_by = ('-created')
        attrs = {"class": "table table-bordered table-hover dataTable dtr-inline",
                 "id": "example2",
                 "th": {
                     "_ordering": {
                         "orderable": "sorting",  # Instead of `orderable`
                         "ascending": "sorting_asc",   # Instead of `asc`
                         "descending": "sorting_desc"  # Instead of `desc`
                     }
                 },
                 "td": {
                     "style": "text-align:center !important"
                 }
                 }
        per_page = 10
