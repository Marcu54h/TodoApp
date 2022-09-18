from rest_framework import serializers
from todo.models import Todo

# ectend DRF's ModelSerializer into a TodoSerializer class.
# ModelSerializer provides an API to create serializers from created models.
class TodoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()

    # Soecify database model Todo and the fields to expose
    class Meta:
        model = Todo
        fields = ['id', 'title', 'memo', 'created', 'completed']

class TodoToggleCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id"]
        read_only_fields = ["title", "memo", "created", "completed"]