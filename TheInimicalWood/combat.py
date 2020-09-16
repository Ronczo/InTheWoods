from django.shortcuts import get_object_or_404
from .models import Character, Monsters
from random import randint
from django.http import HttpResponse


class Attacks:
    """
    Your character's attacks
    """

    @staticmethod
    def basic_attack(id, selected_mission):
        """
        basic attack
        """
        character = get_object_or_404(Character, pk=id)
        monster = get_object_or_404(Monsters, number=selected_mission)

        miss_chance = round(randint(0, 100))
        dmg_factor = round(randint(0, 100))
        hit_dmg = character.attack_dmg + dmg_factor / 10 - monster.defence / 2
        hit_dmg = 1 if hit_dmg < 0 else hit_dmg

        if character.current_stamina >= 10:
            character.current_stamina -= 10
            if miss_chance > 10:
                message = f"{character.name} attacked {monster.name} by \"bassic attack\" for {int(round(hit_dmg, 0))}"
                if dmg_factor > 85:
                    hit_dmg * 2
                    message += " (Critical)"
                monster.current_hp -= round(hit_dmg, 0)
            else:
                message = f"{character.name} misses!"
        else:
            message = f"{character.name} doesn't have enough stamina!!"

        if monster.current_hp < 0:
            monster.current_hp = 0

        character.save()
        monster.save()

        return message


class Defends:
    """
    Heals your character
    """

    @staticmethod
    def defend(id):
        character = get_object_or_404(Character, pk=id)
        healing_value = character.hp * character.defence / 200
        if character.hp - character.current_hp < healing_value:
            character.current_hp += character.hp - character.current_hp
        else:
            character.current_hp += healing_value

        if character.stamina - character.current_stamina < 20:
            character.current_stamina += character.stamina - character.current_stamina
        else:
            character.current_stamina += 20

        character.save()
        return f"{character.name} rests, heals 10 hp and restores 20 stamina"


def monster_attack(id, selected_mission):
    """
    Monster's basic attach
    Decorator maybe?
    """
    character = get_object_or_404(Character, pk=id)
    monster = get_object_or_404(Monsters, number=selected_mission)

    monster_dmg_factor = round(randint(0, 100))
    monster_miss_chance = round(randint(0, 100))
    monster_hit_dmg = monster.attack_dmg + monster_dmg_factor / 10 - character.defence / 2
    monster_hit_dmg = 1 if monster_hit_dmg < 0 else monster_hit_dmg


    if monster_miss_chance > 20:
        monster_message = f"{monster.name} attacked {character.name} for {int(round(monster_hit_dmg, 0))}"
        if monster_dmg_factor > 85:
            monster_hit_dmg * 2
            monster_message += " (Critical)"
        character.current_hp -= round(monster_hit_dmg, 0)
    else:
        monster_message = f"{monster.name} misses!"

    if monster.current_hp < 0:
        monster.current_hp = 0

    character.save()
    monster.save()

    return monster_message


def fight_end(id, selected_mission):
    character = get_object_or_404(Character, pk=id)
    monster = get_object_or_404(Monsters, number=selected_mission)

    character.current_hp = character.hp
    character.current_mana = character.mana
    character.current_stamina = character.stamina

    monster.current_hp = monster.max_hp
    monster.current_mana = monster.max_mana

    character.mission = selected_mission

    character.save()
    monster.save()
