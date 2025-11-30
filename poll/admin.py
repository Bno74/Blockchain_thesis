from django.contrib import admin
from . import models

# Register your models here.

class VoteAdmin(admin.ModelAdmin):
    """Read-only admin for Vote model to prevent manual vote manipulation"""
    list_display = ('id', 'vote', 'timestamp', 'block_id')
    list_filter = ('block_id', 'vote')
    search_fields = ('id',)
    readonly_fields = ('id', 'vote', 'timestamp', 'block_id')
    
    def has_add_permission(self, request):
        """Prevent adding votes through admin"""
        return False
    
    def has_change_permission(self, request, obj=None):
        """Prevent editing votes through admin"""
        return False
    
    def has_delete_permission(self, request, obj=None):
        """Prevent deleting votes through admin"""
        return False

class BlockAdmin(admin.ModelAdmin):
    """Read-only admin for Block model to prevent blockchain manipulation"""
    list_display = ('id', 'prev_hash', 'self_hash', 'merkle_hash', 'nonce', 'timestamp')
    list_filter = ('id',)
    search_fields = ('id', 'self_hash', 'prev_hash')
    readonly_fields = ('id', 'prev_hash', 'self_hash', 'merkle_hash', 'nonce', 'timestamp')
    
    def has_add_permission(self, request):
        """Prevent adding blocks through admin"""
        return False
    
    def has_change_permission(self, request, obj=None):
        """Prevent editing blocks through admin"""
        return False
    
    def has_delete_permission(self, request, obj=None):
        """Prevent deleting blocks through admin"""
        return False

admin.site.register(models.Candidate)
admin.site.register(models.Voter)
admin.site.register(models.Vote, VoteAdmin)
admin.site.register(models.Block, BlockAdmin)
admin.site.register(models.VoterList)
admin.site.register(models.VoterPvt)
admin.site.register(models.VoteAuth)