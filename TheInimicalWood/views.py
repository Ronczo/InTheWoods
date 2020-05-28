from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, CharacterForm
from .models import Character, Item
from django.contrib.auth.decorators import login_required
from . import logic
import json


def home(request):
    """
    home page
    """
    return render(request, 'home.html')


def signup(request):
    """
    user registration
    """
    something_went_wrong = False
    if request.method == "POST":
        form_signup = RegisterForm(request.POST)
        if form_signup.is_valid():
            form_signup.save()
            return redirect('login')
        else:
            something_went_wrong = True
    else:
        form_signup = RegisterForm()

    return render(request, 'registration/signup.html', {'form_signup': form_signup,
                                                        'something_went_wrong': something_went_wrong})


def aboutme(request):
    """
    about me page
    """
    return render(request, 'aboutme.html')


@login_required
def contact(request):
    """
    sending e-mail
    """
    something_went_wrong = False
    if request.method == 'POST':
        try:
            logic.contact_logic(request.POST.get('username'), request.POST.get('usermail'),
                                request.POST.get('usersubject'), request.POST.get('usertext'), request.user)
        except:
            something_went_wrong = True

    return render(request, 'contact.html', {'something_went_wrong': something_went_wrong})


@login_required
def game(request):
    """
    selecting character
    """
    user_characters = Character.objects.filter(belongs_to=request.user)
    len_user_characters = len(user_characters)

    context = {
        'user_characters': user_characters,
        'len_user_characters': len_user_characters
    }

    return render(request, 'character_select.html', context)


@login_required
def create_character(request):
    """
    creating new character in database
    """
    new_character_form = CharacterForm(request.POST or None)

    if new_character_form.is_valid():
        hero = new_character_form.save(commit=False)
        hero.belongs_to = request.user
        logic.create_character_logic(hero)
        return redirect(game)

    return render(request, 'create_character.html', {'New_character_form': new_character_form})


@login_required
def delete_character(request, id):
    """
    deletes character from database
    """
    character = get_object_or_404(Character, pk=id)

    if request.method == "POST":
        character.delete()
        return redirect(game)

    return render(request, 'confirmation.html', {'character': character})


def specialthanks(request):
    """
Special thanks for help and copyrights
    """
    return render(request, 'specialthanks.html')


@login_required
def overview(request, id):
    """
    character overview
    """
    character = get_object_or_404(Character, pk=id)
    hero_backpack = json.loads(character.backpack)
    hero_inventory = json.loads(character.inventory)

    # Creating backpack from JSON string
    backpack = {}
    for item in hero_backpack:
        if hero_backpack[item] > 0:
            item_to_add = get_object_or_404(Item, name=item)
            backpack[item_to_add] = hero_backpack[item]


    # Creating inventory from JSON string
    inventory = {}
    for item in hero_inventory:
        item_to_add_to_inventory = get_object_or_404(Item, name=hero_inventory[item])
        inventory[item] = item_to_add_to_inventory

    if 'sell' in request.POST:
        if request.method == "POST":
            logic.Overview.sell(request, character, hero_backpack)
            return redirect(overview, id=character.id)

    if request.method == "POST":
        if 'equip' in request.POST:
            logic.Overview.equip_item(request, character, hero_backpack, hero_inventory)
            return redirect(overview, id=character.id)

    if request.method == "POST":
        if 'takeoff' in request.POST:
            logic.Overview.take_off_item(request, character, hero_backpack, hero_inventory)
            return redirect(overview, id=character.id)

    # Variables needed for template
    loop_index_raw = [i for i in range(1000)][1::3]
    progress_bar_hp = int(character.current_hp / character.hp * 100) if (
                                                                                character.current_hp / character.hp * 100) >= 25 else 25
    progress_bar_mana = int(character.current_mana / character.mana * 100) if (
                                                                                      character.current_mana / character.mana * 100) >= 25 else 25
    progress_bar_stamina = int(character.current_stamina / character.stamina * 100) if (
                                                                                               character.current_stamina / character.stamina * 100) >= 25 else 25
    context = {
        'character': character, 'backpack': backpack,
        'loop_index_raw': loop_index_raw, 'inventory': inventory,
        'progress_bar_hp': progress_bar_hp,
        'progress_bar_mana': progress_bar_mana,
        'progress_bar_stamina': progress_bar_stamina
    }

    return render(request, 'overview.html', context)
