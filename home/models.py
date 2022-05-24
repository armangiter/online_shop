from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    parent = models.ForeignKey(to='self', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, verbose_name=_('is active'),
                                    help_text=_('to not showing this category disable this field'))
    is_root = models.BooleanField(default=False, verbose_name=_('is root category'),
                                  help_text=_('if this is root category mark this field'))


class OffCode(models.Model):
    is_active = models.BooleanField(default=True, verbose_name=_('is active'),
                                    help_text=_('to disable this off code disable this field'))
    type = models.CharField(max_length=10, choices=(('p', _('percent')),
                                                    ('a', _('amount'))), verbose_name=_('off code type'))
    amount = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.amount} {self.type}'


serve_type = (
    ('s', _('single')),
    ('o_t', _('one and two person')),
    ('s_b', _('big and small'))
)


class Food(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name=_('category'))
    name = models.CharField(max_lengt=255, verbose_name=_('name'))
    description = models.TextField(verbose_name=_('description'),
                                   help_text=_('write like example (meet 150g, chicken 250g)'))
    serve_type = models.CharField(choices=serve_type, verbose_name=_('serve type'))
    first_price = models.IntegerField(verbose_name=_('price one person'))
    second_price = models.IntegerField(verbose_name=_('price for two person'),
                                    help_text=_('if this food is for two serve type fill this field'), null=True,
                                    blank=True)
    off_code_for_first_price = models.ForeignKey(to=OffCode, on_delete=models.SET_NULL, null=True, blank=True)
    off_code_for_second_price = models.ForeignKey(to=OffCode, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name=_('is active'),
                                    help_text=_('to not showing this food disable this field'))

    def price_return(self):
        if self.serve_type == 's':
            if self.off_code_for_first_price:
                ...

    def first_price_calculate(self):
        off_code = self.off_code_for_first_price
        if off_code:
            if off_code.type == 'p':
                return self.first_price * off_code.amount / 100
            return self.first_price - off_code.amount

    def second_price_calculate(self):
        off_code = self.off_code_for_second_price
        if off_code.type == 'p':
            return self.second_price * off_code.amount / 100
        return self.second_price - off_code.amount

    def __str__(self):
        return self.name
