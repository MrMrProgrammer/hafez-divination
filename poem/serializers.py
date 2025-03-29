from rest_framework import serializers
from .models import Poem

class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = [
            'number',
            'poem',
            'interpretation',
            # 'uuid',
            # 'is_active',
            # 'created_at',
            # 'updated_at',
        ]
