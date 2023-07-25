from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly, SAFE_METHODS


class IsOwnerOrAdminOrReadOnly(BasePermission):
	def has_object_permission(self, request, view, obj):
		return request.method in SAFE_METHODS or obj.author == request.user or request.user.is_superuser


class IsAuthenticatedAndNotOwner(BasePermission):
	def has_object_permission(self, request, view, obj):
		return request.user.is_authenticated and obj.author != request.user


class ViewSetPermission(BasePermission):
	def has_permission(self, request, view):
		return IsAuthenticatedOrReadOnly().has_permission(request, view)

	def has_object_permission(self, request, view, obj):
		return IsOwnerOrAdminOrReadOnly().has_object_permission(request, view, obj)
