from rest_framework import serializers
from .models import Poem

class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = [
            'uuid',
            'number',
            'poem',
            'interpretation',
            'is_active',
            'created_at',
            'updated_at',
        ]
