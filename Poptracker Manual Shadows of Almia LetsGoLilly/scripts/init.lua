
local variant = Tracker.ActiveVariantUID

-- Logic
ScriptHost:LoadScript("scripts/logic.lua")

-- Utility Script for helper functions etc.
ScriptHost:LoadScript("scripts/utils.lua")


-- Items
Tracker:AddItems("items/items.json")
Tracker:AddItems("items/options.jsonc")

if not IS_ITEMS_ONLY then -- <--- use variant info to optimize loading
    Tracker:AddMaps("maps/maps.json")
    ScriptHost:LoadScript("scripts/locations_import.lua")
    ScriptHost:LoadScript("scripts/logic/base_logic.lua")
    ScriptHost:LoadScript("scripts/logic/more_logic.lua")
    ScriptHost:LoadScript("scripts/logic/even_more_logic.lua")
end

-- Layout
Tracker:AddLayouts("layouts/broadcast.json")
Tracker:AddLayouts("layouts/items.json")
Tracker:AddLayouts("layouts/options.jsonc")
Tracker:AddLayouts("layouts/tabs.jsonc")
Tracker:AddLayouts("layouts/tracker.json")

-- AutoTracking for Poptracker
if PopVersion and PopVersion >= "0.26.0" then
    require("scripts/autotracking")
end

function OnFrameHandler()
    ScriptHost:RemoveOnFrameHandler("load handler")
    -- stuff
    ScriptHost:AddWatchForCode("StateChanged", "*", StateChanged)
    ScriptHost:AddOnLocationSectionChangedHandler("location_section_change_handler", LocationHandler)
    CreateLuaManualStorageItem("manual_location_storage")
    ForceUpdate()
end
require("scripts/luaitems")
require("scripts/watches")
ScriptHost:AddOnFrameHandler("load handler", OnFrameHandler)
