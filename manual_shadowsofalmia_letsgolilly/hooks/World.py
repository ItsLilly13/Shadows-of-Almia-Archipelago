# Object classes from AP core, to represent an entire MultiWorld and this individual World that's part of it
from worlds.AutoWorld import World
from BaseClasses import MultiWorld, CollectionState, Item

# Object classes from Manual -- extending AP core -- representing items and locations that are used in generation
from ..Items import ManualItem
from ..Locations import ManualLocation

# Raw JSON data from the Manual apworld, respectively:
#          data/game.json, data/items.json, data/locations.json, data/regions.json
#
from ..Data import game_table, item_table, location_table, region_table

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value, format_state_prog_items_key, ProgItemsCat

# calling logging.info("message") anywhere below in this file will output the message to both console and log file
import logging

########################################################################################
## Order of method calls when the world generates:
##    1. create_regions - Creates regions and locations
##    2. create_items - Creates the item pool
##    3. set_rules - Creates rules for accessing regions and locations
##    4. generate_basic - Runs any post item pool options, like place item/category
##    5. pre_fill - Creates the victory location
##
## The create_item method is used by plando and start_inventory settings to create an item from an item name.
## The fill_slot_data method will be used to send data to the Manual client for later use, like deathlink.
########################################################################################



# Use this function to change the valid filler items to be created to replace item links or starting items.
# Default value is the `filler_item_name` from game.json
def hook_get_filler_item_name(world: World, multiworld: MultiWorld, player: int) -> str | bool:
    return False

# Called before regions and locations are created. Not clear why you'd want this, but it's here. Victory location is included, but Victory event is not placed yet.
def before_create_regions(world: World, multiworld: MultiWorld, player: int):
    pass

# Called after regions and locations are created, in case you want to see or modify that information. Victory location is included.
def after_create_regions(world: World, multiworld: MultiWorld, player: int):
    # Use this hook to remove locations from the world
    locationNamesToRemove: list[str] = [] # List of location names

    
    add_missions = get_option_value(multiworld, player, "add_missions") #Adds missions, ranger net and Locations for Manaphy ect.

    # Add your code here to calculate which locations to remove


    if not add_missions:
        locationNamesToRemove += ["Obtain a Manaphy Egg (1)", "Obtain a Manaphy Egg (2)", "Capture Dialga (1)", "Capture Dialga (2)", "Capture Palkia (1)", "Capture Palkia (2)", "Capture Shaymin (1)", "Capture Shaymin (2)"]

    for region in multiworld.regions:
        if region.player == player:
            for location in list(region.locations):
                if location.name in locationNamesToRemove:
                    region.locations.remove(location)

# This hook allows you to access the item names & counts before the items are created. Use this to increase/decrease the amount of a specific item in the pool
# Valid item_config key/values:
# {"Item Name": 5} <- This will create qty 5 items using all the default settings
# {"Item Name": {"useful": 7}} <- This will create qty 7 items and force them to be classified as useful
# {"Item Name": {"progression": 2, "useful": 1}} <- This will create 3 items, with 2 classified as progression and 1 as useful
# {"Item Name": {0b0110: 5}} <- If you know the special flag for the item classes, you can also define non-standard options. This setup
#       will create 5 items that are the "useful trap" class
# {"Item Name": {ItemClassification.useful: 5}} <- You can also use the classification directly
def before_create_items_all(item_config: dict[str, int|dict], world: World, multiworld: MultiWorld, player: int) -> dict[str, int|dict]:
    return item_config

# The item pool before starting items are processed, in case you want to see the raw item pool at that stage
def before_create_items_starting(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:

    #Start inventory:
    start_inventory_items = []
    DeleteList = []

    starting_location = get_option_value(multiworld, player, "starting_location")
    
    if starting_location == 1:
        StartLocation = ["Chicole Path Start", "Ranger School Start", "Pueltown Start", "Chroma Highlands Start", "Union Road Start", "Hia Valley Start", "Puel Sea Start", "Sea of Wailord Start", "Volcano Cave Start", "Haruba Desert Start", "Oil Field Hideout Start"]
        multiworld.random.shuffle(StartLocation)
        start_inventory_items += [StartLocation[0]]
    if starting_location == 2:
        start_inventory_items += ["Chicole Path Start"]
    if starting_location == 3:
        start_inventory_items += ["Ranger School Start"]
    if starting_location == 4:
        start_inventory_items += ["Pueltown Start"]
    if starting_location == 5:
        start_inventory_items += ["Chroma Highlands Start"]
    if starting_location == 6:
        start_inventory_items += ["Union Road Start"]
    if starting_location == 7:
        start_inventory_items += ["Hia Valley Start"]
    if starting_location == 8:
        start_inventory_items += ["Puel Sea Start"]
    if starting_location == 9:
        start_inventory_items += ["Sea of Wailord Start"]
    if starting_location == 10:
        start_inventory_items += ["Volcano Cave Start"]
    if starting_location == 11:
        start_inventory_items += ["Haruba Desert Start"]
    if starting_location == 12:
        start_inventory_items += ["Oil Field Hideout Start"]  

    if "Chicole Path Start" in start_inventory_items:
        start_inventory_items += ["Chicole Path Permit", "Chicole Village Fly Point", "Green Boat Key"]
        DeleteList = ["Ranger School Start", "Pueltown Start", "Chroma Highlands Start", "Union Road Start", "Hia Valley Start", "Puel Sea Start", "Sea of Wailord Start", "Volcano Cave Start", "Haruba Desert Start", "Oil Field Hideout Start"]

    if "Ranger School Start" in start_inventory_items:
        start_inventory_items += ["Ranger School Permit", "Ranger School Fly Point", "Green Boat Key"]
        DeleteList = ["Chicole Path Start", "Pueltown Start", "Chroma Highlands Start", "Union Road Start", "Hia Valley Start", "Puel Sea Start", "Sea of Wailord Start", "Volcano Cave Start", "Haruba Desert Start", "Oil Field Hideout Start"]

    if "Pueltown Start" in start_inventory_items:
        start_inventory_items += ["Pueltown Permit", "Pueltown Fly Point", "Green Boat Key"]
        DeleteList = ["Chicole Path Start", "Ranger School Start", "Chroma Highlands Start", "Union Road Start", "Hia Valley Start", "Puel Sea Start", "Sea of Wailord Start", "Volcano Cave Start", "Haruba Desert Start", "Oil Field Hideout Start"]

    if "Chroma Highlands Start" in start_inventory_items:
        start_inventory_items += ["Chroma Highlands Permit", "Chroma Highlands Fly Point", "Green Boat Key"]
        DeleteList = ["Chicole Path Start", "Ranger School Start", "Pueltown Start", "Union Road Start", "Hia Valley Start", "Puel Sea Start", "Sea of Wailord Start", "Volcano Cave Start", "Haruba Desert Start", "Oil Field Hideout Start"]

    if "Union Road Start" in start_inventory_items:
        start_inventory_items += ["Union Road Permit", "Ranger Union Fly Point", "Green Boat Key"]
        DeleteList = ["Chicole Path Start", "Ranger School Start", "Pueltown Start", "Chroma Highlands Start", "Hia Valley Start", "Puel Sea Start", "Sea of Wailord Start", "Volcano Cave Start", "Haruba Desert Start", "Oil Field Hideout Start"]

    if "Hia Valley Start" in start_inventory_items:
        start_inventory_items += ["Hia Valley Permit", "Shiver Camp Fly Point", "Green Boat Key"]
        DeleteList = ["Chicole Path Start", "Ranger School Start", "Pueltown Start", "Chroma Highlands Start", "Union Road Start", "Puel Sea Start", "Sea of Wailord Start", "Volcano Cave Start", "Haruba Desert Start", "Oil Field Hideout Start"]

    if "Puel Sea Start" in start_inventory_items:
        start_inventory_items += ["Puel Sea Permit", "Pueltown Fly Point"]
        DeleteList = ["Chicole Path Start", "Ranger School Start", "Pueltown Start", "Chroma Highlands Start", "Union Road Start", "Hia Valley Start", "Sea of Wailord Start", "Volcano Cave Start", "Haruba Desert Start", "Oil Field Hideout Start"]

    if "Sea of Wailord Start" in start_inventory_items:
        start_inventory_items += ["Sea of Wailord Permit", "Pueltown Fly Point"]
        DeleteList = ["Chicole Path Start", "Ranger School Start", "Pueltown Start", "Chroma Highlands Start", "Union Road Start", "Hia Valley Start", "Puel Sea Start", "Volcano Cave Start", "Haruba Desert Start", "Oil Field Hideout Start"]

    if "Volcano Cave Start" in start_inventory_items:
        start_inventory_items += ["Volcano Cave Permit", "Boyleland Fly Point", "Red Boat Key"]
        DeleteList = ["Chicole Path Start", "Ranger School Start", "Pueltown Start", "Chroma Highlands Start", "Union Road Start", "Hia Valley Start", "Puel Sea Start", "Sea of Wailord Start", "Haruba Desert Start", "Oil Field Hideout Start"]

    if "Haruba Desert Start" in start_inventory_items:
        start_inventory_items += ["Haruba Desert Permit", "Haruba Village Fly Point", "Orange Boat Key"]
        DeleteList = ["Chicole Path Start", "Ranger School Start", "Pueltown Start", "Chroma Highlands Start", "Union Road Start", "Hia Valley Start", "Puel Sea Start", "Sea of Wailord Start", "Volcano Cave Start", "Oil Field Hideout Start"]

    if "Oil Field Hideout Start" in start_inventory_items:
        start_inventory_items += ["Oil Field Hideout Permit", "Oil Field Hideout Fly Point"]
        DeleteList = ["Chicole Path Start", "Ranger School Start", "Pueltown Start", "Chroma Highlands Start", "Union Road Start", "Hia Valley Start", "Puel Sea Start", "Sea of Wailord Start", "Volcano Cave Start", "Haruba Desert Start"]


    Partner = ["Starly", "Munchlax", "Pachirisu", "Chimchar", "Turtwig", "Piplup", "Croagunk", "Kricketot", "Machop", "Mime Jr.", "Cranidos", "Shieldon", "Sneasel", "Snover", "Misdreavus", "Hippopotas", "Gible"]
    multiworld.random.shuffle(Partner)
    start_inventory_items += [Partner[0]]

    #logging.info(f"start_inventory_items: {start_inventory_items}")
    for itemName in start_inventory_items: #precollect items, then delete from item pool.
        start_inventory = next(item for item in item_pool if item.name == itemName)
        multiworld.push_precollected(start_inventory)
        item_pool.remove(start_inventory)
    
    for itemName in DeleteList:
        DelList = next(item for item in item_pool if item.name == itemName)
        item_pool.remove(DelList)
    
    return item_pool

# The item pool after starting items are processed but before filler is added, in case you want to see the raw item pool at that stage
def before_create_items_filler(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    # Use this hook to remove items from the item pool
    
    itemNamesToRemove: list[str] = [] # List of item names

    add_missions = get_option_value(multiworld, player, "add_missions")

    if not add_missions:
        itemNamesToRemove += ["Ranger Net", "Recover the Manaphy Egg!", "Manaphy Egg", "Rescue Kidnapped Riolu!", "Liberate the Tower!", "Dialga in Hia Valley!?", "Dialga", "Palkia in Haruba Desert!?", "Palkia", "For the Bride and Shaymin!", "Shaymin"]

#    gems_local = get_option_value(multiworld, player, "gems_local")
    
#    if gems_local:

    # Add your code here to calculate which items to remove.
    #
    # Because multiple copies of an item can exist, you need to add an item name
    # to the list multiple times if you want to remove multiple copies of it.

    for itemName in itemNamesToRemove:
        item = next(i for i in item_pool if i.name == itemName)
        item_pool.remove(item)

    return item_pool

    # Some other useful hook options:

    ## Place an item at a specific location
    # location = next(l for l in multiworld.get_unfilled_locations(player=player) if l.name == "Location Name")
    # item_to_place = next(i for i in item_pool if i.name == "Item Name")
    # location.place_locked_item(item_to_place)
    # item_pool.remove(item_to_place)

# The complete item pool prior to being set for generation is provided here, in case you want to make changes to it
def after_create_items(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool

# Called before rules for accessing regions and locations are created. Not clear why you'd want this, but it's here.
def before_set_rules(world: World, multiworld: MultiWorld, player: int):
    pass

# Called after rules for accessing regions and locations are created, in case you want to see or modify that information.
def after_set_rules(world: World, multiworld: MultiWorld, player: int):
    # Use this hook to modify the access rules for a given location

    def Example_Rule(state: CollectionState) -> bool:
        # Calculated rules take a CollectionState object and return a boolean
        # True if the player can access the location
        # CollectionState is defined in BaseClasses
        return True

    ## Common functions:
    # location = world.get_location(location_name, player)
    # location.access_rule = Example_Rule

    ## Combine rules:
    # old_rule = location.access_rule
    # location.access_rule = lambda state: old_rule(state) and Example_Rule(state)
    # OR
    # location.access_rule = lambda state: old_rule(state) or Example_Rule(state)

# The item name to create is provided before the item is created, in case you want to make changes to it
def before_create_item(item_name: str, world: World, multiworld: MultiWorld, player: int) -> str:
    return item_name

# The item that was created is provided after creation, in case you want to modify the item
def after_create_item(item: ManualItem, world: World, multiworld: MultiWorld, player: int) -> ManualItem:
    return item

# This method is run towards the end of pre-generation, before the place_item options have been handled and before AP generation occurs
def before_generate_basic(world: World, multiworld: MultiWorld, player: int):
    pass

# This method is run at the very end of pre-generation, once the place_item options have been handled and before AP generation occurs
def after_generate_basic(world: World, multiworld: MultiWorld, player: int):
    pass

# This method is run every time an item is added to the state, can be used to modify the value of an item.
# IMPORTANT! Any changes made in this hook must be cancelled/undone in after_remove_item
def after_collect_item(world: World, state: CollectionState, Changed: bool, item: Item):
    # the following let you add to the Potato Item Value count
    # if item.name == "Cooked Potato":
    #     state.prog_items[item.player][format_state_prog_items_key(ProgItemsCat.VALUE, "Potato")] += 1
    pass

# This method is run every time an item is removed from the state, can be used to modify the value of an item.
# IMPORTANT! Any changes made in this hook must be first done in after_collect_item
def after_remove_item(world: World, state: CollectionState, Changed: bool, item: Item):
    # the following let you undo the addition to the Potato Item Value count
    # if item.name == "Cooked Potato":
    #     state.prog_items[item.player][format_state_prog_items_key(ProgItemsCat.VALUE, "Potato")] -= 1
    pass


# This is called before slot data is set and provides an empty dict ({}), in case you want to modify it before Manual does
def before_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data

# This is called after slot data is set and provides the slot data at the time, in case you want to check and modify it after Manual is done with it
def after_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data

# This is called right at the end, in case you want to write stuff to the spoiler log
def before_write_spoiler(world: World, multiworld: MultiWorld, spoiler_handle) -> None:
    pass

# This is called when you want to add information to the hint text
def before_extend_hint_information(hint_data: dict[int, dict[int, str]], world: World, multiworld: MultiWorld, player: int) -> None:

    ### Example way to use this hook:
    # if player not in hint_data:
    #     hint_data.update({player: {}})
    # for location in multiworld.get_locations(player):
    #     if not location.address:
    #         continue
    #
    #     use this section to calculate the hint string
    #
    #     hint_data[player][location.address] = hint_string

    pass

def after_extend_hint_information(hint_data: dict[int, dict[int, str]], world: World, multiworld: MultiWorld, player: int) -> None:
    pass
