## Задание 5

# Вам дана **JSON** структура:
# {
#  "name": "x-men",
#  "team": [
# 				 {"name": "Wolverine", "gender": "male", "ability": "regeneration"},
# 				 {"name": "Cyclops", "gender": "female", "ability": "laser-eyes"}, 
# 				 {"name": "Storm", "gender": "female", "ability": "weather-manipulation"}
# 					], 
#  "name": "avengers",
#  "team": [
# 				 {"name": "Hulk", "gender": "male", "ability": "super-strength"},
# 				 {"name": "Captain Amerika", "gender": "male", "ability": "shield-bearer"}, 
# 				 {"name": "Iron Man", "gender": "male", "ability": "money"}
# 				 ]
# }
# Напишите модели и сериализаторы, которые могут выдать такую структуру

#models.py
from django.db import models

class Heroes(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=50)
    ability = models.CharField(max_length=250)
    team = models.ForeignKey('person.Type', models.CASCADE, 'team')


class Type(models.Model):
    name = models.CharField(max_length=100)


# serializers.py
class TypeSerializer(serializers.ModelSerializer):
    team = HeroesSerializer(many=True, read_only=True)

    class Meta:
        model = Type
        fields = ('name', 'team')


class HeroesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Heroes
        fields = ('name', 'gender', 'ability')