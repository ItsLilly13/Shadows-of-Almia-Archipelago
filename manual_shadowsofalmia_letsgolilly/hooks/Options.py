# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith

class AddMissions(Toggle):
    """Add the Ranger Net Missions to the itempool."""
    display_name = "Add Ranger Net Missions"
    default = True

class AddCelebi (Toggle):
    """Adds Celebi to the Item Pool. (If added needs to be collected to win the Legendary and Catch 'em All Goals)"""
    display_name = "Add Celebi"
    default = True

#class GemsLocal(Toggle):
#    """Force the Gems needed to beat Darkrai to be found in your game"""
#    display_name = "Gems are Local"
#    default = True

class StartingLocation(Choice):
    """Choose your starting location."""
    display_name = "Starting Location"
    option_random = 1
    option_chicole_path = 2
    option_ranger_school = 3
    option_pueltown = 4
    option_chroma_highlands = 5
    option_union_road = 6
    option_hia_valley = 7
    option_puel_sea = 8
    option_sea_of_wailord = 9
    option_volcano_cave = 10
    option_haruba_desert = 11
    option_oil_field_hideout = 12
    default = 1


# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["add_missions"] = AddMissions
    options["add_celebi"] = AddCelebi
    #options["gems_local"] = GemsLocal
    options["starting_location"] = StartingLocation
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options

    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups