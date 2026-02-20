ENABLE_DEBUG_LOG = true
-- get current variant
local variant = Tracker.ActiveVariantUID
-- check variant info
IS_ITEMS_ONLY = variant:find("itemsonly")

print("-- Manual Shadows of Almia Tracker --")
print("Loaded variant: ", variant)
if ENABLE_DEBUG_LOG then
    print("Debug logging is enabled!")
end
-- Logic
ScriptHost:LoadScript("scripts/logic.lua")

-- Utility Script for helper functions etc.
ScriptHost:LoadScript("scripts/utils.lua")


-- Items
Tracker:AddItems("items/items.json")
Tracker:AddItems("items/options.jsonc")

if not IS_ITEMS_ONLY then -- <--- use variant info to optimize loading
    Tracker:AddMaps("maps/maps.json")
    ScriptHost:LoadScript("scripts/locations.lua")
end

-- Layout
Tracker:AddLayouts("layouts/broadcast.json")
Tracker:AddLayouts("layouts/items.json")
Tracker:AddLayouts("layouts/options.jsonc")
Tracker:AddLayouts("layouts/tabs.jsonc")
Tracker:AddLayouts("layouts/tracker.json")

-- AutoTracking for Poptracker
if PopVersion and PopVersion >= "0.18.0" then
    ScriptHost:LoadScript("scripts/autotracking.lua")
end