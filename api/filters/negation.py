class NegationFilterMixin:
	@staticmethod
	def is_not(queryset, field_name, value):
		lookup = '{}__in'.format(field_name)
		return queryset.exclude(**{lookup: value.split(',')})
