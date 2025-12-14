from django.db import models


class UserServiceAssignment(models.Model):
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='service_assignments',
    )
    service = models.ForeignKey(
        'service.Service',
        on_delete=models.CASCADE,
        related_name='user_assignments',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        'user.User',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='created_assignments',
    )

    class Meta:
        unique_together = ('user', 'service')
