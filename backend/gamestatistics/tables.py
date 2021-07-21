import django_tables2 as tables
from django_tables2 import TemplateColumn, RelatedLinkColumn
from django.db.models import F, Case, When


class Rank_awpTable(tables.Table):
    name = tables.Column(accessor='name',
         verbose_name='Name')
    steam = tables.Column(accessor='steam',
         verbose_name='Steam ID')
    score = tables.Column(accessor='score',
         verbose_name='Score')
    KD = tables.Column(accessor='KDcalculator',
         verbose_name='K/D')
    ADR = tables.Column(accessor='ADRcalculator',
         verbose_name='ADR')
    link = tables.Column(accessor='steamid_to_profile',
         verbose_name='Profile', orderable=False)
    time = tables.Column(verbose_name='Playtime', order_by="connected")

    class Meta:
        #template_name = "django_tables2/bootstrap4.html"
        fields = ("name", 'steam', 'score', 'KD', 'ADR', 'time', 'link')
        order_by = ('-score')
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

    def order_KD(self, queryset, is_descending):
        queryset = queryset.annotate(
            amount = Case(When(deaths=0, then=F("kills")),
            default = F("kills") / F("deaths"))
        ).order_by(("-" if is_descending else "") + "amount")
        return (queryset, True)
    
    def order_ADR(self, queryset, is_descending):
        queryset = queryset.annotate(
            amount = F("damage") / (F("rounds_ct")+F("rounds_tr"))
        ).order_by(("-" if is_descending else "") + "amount")
        return (queryset, True)

class Rank_retakeTable(tables.Table):
    name = tables.Column(accessor='name',
         verbose_name='Name')
    steam = tables.Column(accessor='steam',
         verbose_name='Steam ID')
    score = tables.Column(accessor='score',
         verbose_name='Score')
    KD = tables.Column(accessor='KDcalculator',
         verbose_name='K/D')
    ADR = tables.Column(accessor='ADRcalculator',
         verbose_name='ADR')
    link = tables.Column(accessor='steamid_to_profile',
         verbose_name='Profile', orderable=False)
    time = tables.Column(verbose_name='Playtime', order_by="connected")

    class Meta:
        #template_name = "django_tables2/bootstrap4.html"
        fields = ("name", 'steam', 'score', 'KD', 'ADR', 'time', 'link')
        order_by = ('-score')
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

    def order_KD(self, queryset, is_descending):
        queryset = queryset.annotate(
            amount = Case(When(deaths=0, then=F("kills")),
            default = F("kills") / F("deaths"))
        ).order_by(("-" if is_descending else "") + "amount")
        return (queryset, True)
    
    def order_ADR(self, queryset, is_descending):
        queryset = queryset.annotate(
            amount = F("damage") / (F("rounds_ct")+F("rounds_tr"))
        ).order_by(("-" if is_descending else "") + "amount")
        return (queryset, True)