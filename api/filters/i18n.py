from rest_framework.filters import SearchFilter
from food.choices.lang import Lang


class I18NSearchFilter(SearchFilter):
	language_parameter = 'lang'
	language_field = 'language'
	i18n_prefix = 'i18n__'
	language = None

	def get_search_fields(self, view, request):
		prefix = self.i18n_prefix
		fields = []

		for field in getattr(view, 'search_fields', []):
			lookup_prefix = field[0]
			lookup = self.lookup_prefixes.get(lookup_prefix)

			if lookup is not None:
				field = field[1:]

			if field.startswith(prefix):
				field = field[len(prefix):]

				if lookup is not None:
					field = lookup_prefix + field

				fields.append(field)

		fields.append('=' + self.language_field)

		return fields

	def filter_queryset(self, request, queryset, view):
		language = request.query_params.get(self.language_parameter, Lang.EN)

		i18n_queryset = queryset.model.i18n.field.model.objects.all()
		i18n_queryset = i18n_queryset.filter(language=language)
		i18n_queryset = super().filter_queryset(request, i18n_queryset, view)

		ids = i18n_queryset.values_list('product_id', flat=True)

		return queryset.filter(id__in=ids)
