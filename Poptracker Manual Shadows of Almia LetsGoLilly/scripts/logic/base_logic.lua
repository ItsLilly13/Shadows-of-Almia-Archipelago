function Mainland_Start() 
	if (has("Chicole Path Start") 
    or has("Ranger School Start") 
    or has("Pueltown Start") 
    or has("Chroma Highlands Start") 
    or has("Union Road Start")) then
		return 1
	else
		return 0
	end 
end

function Mainland_Fly_Point() 
	if (has("Chicole Village Fly Point") 
    or has("Vientown Fly Point") 
    or has("Ranger School Fly Point") 
    or has("Pueltown Fly Point") 
    or has("Altru Building Fly Point") 
    or has("Altru Tower Fly Point") 
    or has("Chroma Highlands Fly Point") 
    or has("Chroma Ruins Fly Point") 
    or has("Ranger Union Fly Point")) then
		return 1
	else
		return 0
	end 
end

function Haruba_Fly_Point() 
	if (has("Haruba Village Fly Point") 
    or has("Hippowdon Temple Fly Point")) then
		return 1
	else
		return 0
	end 
end

function Flight() 
	if (has("Staraptor") and has("Fly")) then
		return 1
	else
		return 0
	end 
end

function River() 
	if (has("Floatzel") and has("River Flow 1")) then
		return 1
	else
		return 0
	end 
end

function Rapids() 
	if (has("Empoleon") and has("River Flow 2")) then
		return 1
	else
		return 0
	end 
end

function Deep_Water() 
	if (has("Mantine") and has("Swim")) then
		return 1
	else
		return 0
	end 
end

function Lava() 
	if (has("Torkoal") and has("Magma Flow")) then
		return 1
	else
		return 0
	end 
end

function Speed() 
	if (has("Doduo") and has("Agility")) then
		return 1
	else
		return 0
	end 
end

function Steam() 
	if (has("Drifloon") and has("Airlift")) then
		return 1
	else
		return 0
	end 
end

function Light() 
	if (has("Drifblim") and has("Elevate")) then
		return 1
	else
		return 0
	end 
end

function Mainland_Area() 
	if ((function_Cached("Mainland_Start")==1) 
    or (function_Cached("Mainland_Fly_Point")==1 and function_Cached("Flight")==1) 
    or (has("Puel Sea Start") and has("Light Blue Boat Key")) 
    or (has("Sea of Wailord Start") and has("Dark Blue Boat Key")) 
    or (has("Volcano Cave Start") and has("Green Boat Key")) 
    or (has("Boyleland Fly Point") and function_Cached("Flight")==1 and has("Green Boat Key"))
    or (has("Haruba Desert Start") and has("Green Boat Key"))
    or (function_Cached("Haruba_Fly_Point")==1 and function_Cached("Flight")==1 and has("Green Boat Key"))
    or (has("Hia Valley Start") and function_Cached("River")==1)
    or (has("Shiver Camp Fly Point") and function_Cached("Flight")==1 and function_Cached("River")==1)
    or (has("Almia Castle Fly Point") and function_Cached("Flight")==1 and function_Cached("Rapids")==1 and function_Cached("River")==1)
    or (has("Capture Arena Fly Point") and function_Cached("Flight")==1 and has("Wailord") and has("Green Boat Key"))) then
		return 1
	else
		return 0
	end 
end

function Hia_Area() 
	if ((function_Cached("Mainland_Start")==1 and function_Cached("River")==1)
    or (function_Cached("Mainlad_Fly_Point")==1 and function_Cached("Flight")==1 and function_Cached("River")==1)
    or (has("Puel Sea Start") and has("Light Blue Boat Key") and function_Cached("River")==1)
    or (has("Sea of Wailord Start") and has("Dark Blue Boat Key") and function_Cached("River")==1)
    or (has("Volcano Cave Start") and has("Green Boat Key") and function_Cached("River")==1)
    or (has("Boyleland Fly Point") and function_Cached("Flight")==1 and has("Green Boat Key") and function_Cached("River")==1)
    or (has("Haruba Desert Start") and has("Green Boat Key") and function_Cached("River")==1)
    or (function_Cached("Haruba_Fly_Point")==1 and function_Cached("Flight")==1 and has("Green Boat Key") and function_Cached("River")==1)
    or (has("Hia Valley Start"))
    or (has("Shiver Camp Fly Point") and function_Cached("Flight")==1)
    or (has("Almia Castle Fly Point") and function_Cached("Flight")==1 and function_Cached("Rapids")==1)
    or (has("Capture Arena Fly Point") and function_Cached("Flight")==1 and has("Wailord") and has("Green Boat Key") and function_Cached("River")==1)) then
		return 1
	else
		return 0
	end 
end

function Almia_Castle_Area() 
	if ((function_Cached("Mainland_Start")==1 and function_Cached("River")==1 and function_Cached("Rapids")==1)
    or (function_Cached("Mainland_Fly_Point")==1 and function_Cached("Flight")==1 and function_Cached("River")==1 and function_Cached("Rapids")==1)
    or (has("Puel Sea Start") and has("Light Blue Boat Key") and function_Cached("River")==1 and function_Cached("Rapids")==1)
    or (has("Sea of Wailord Start") and has("Dark Blue Boat Key") and function_Cached("River")==1 and function_Cached("Rapids")==1)
    or (has("Volcano Cave Start") and has("Green Boat Key") and function_Cached("River")==1 and function_Cached("Rapids")==1)
    or (has("Boyleland Fly Point") and function_Cached("Flight")==1 and has("Green Boat Key") and function_Cached("River")==1 and function_Cached("Rapids")==1)
    or (has("Haruba Desert Start") and has("Green Boat Key") and function_Cached("River")==1 and function_Cached("Rapids")==1)
    or (function_Cached("Haruba_Fly_Point")==1 and function_Cached("Flight")==1 and has("Green Boat Key") and function_Cached("River")==1 and function_Cached("Rapids")==1)
    or (has("Hia Valley Start") and function_Cached("Rapids")==1)
    or (has("Shiver Camp Fly Point") and function_Cached("Flight")==1 and function_Cached("Rapids")==1)
    or (has("Almia Castle Fly Point") and function_Cached("Flight")==1)
    or (has("Capture Arena Fly Point") and function_Cached("Flight")==1 and has("Wailord") and has("Green Boat Key") and function_Cached("River")==1 and function_Cached("Rapids")==1)) then
		return 1
	else
		return 0
	end 
end

function Boyleland_Area() 
	if ((function_Cached("Mainland_Start")==1 and has("Red Boat Key")) 
    or (function_Cached("Mainland_Fly_Point")==1 and function_Cached("Flight")==1 and has("Red Boat Key")) 
    or (has("Puel Sea Start") and has("Light Blue Boat Key") and has("Red Boat Key")) 
    or (has("Sea of Wailord Start") and has("Dark Blue Boat Key") and has("Red Boat Key")) 
    or (has("Volcano Cave Start")) 
    or (has("Boyleland Fly Point") and function_Cached("Flight")==1)
    or (has("Haruba Desert Start") and has("Red Boat Key"))
    or (function_Cached("Haruba_Fly_Point")==1 and function_Cached("Flight")==1 and has("Red Boat Key"))
    or (has("Hia Valley Start") and function_Cached("River")==1 and has("Red Boat Key"))
    or (has("Shiver Camp Fly Point") and function_Cached("Flight")==1 and function_Cached("River")==1 and has("Red Boat Key"))
    or (has("Almia Castle Fly Point") and function_Cached("Flight")==1 and function_Cached("Rapids")==1 and function_Cached("River")==1 and has("Red Boat Key"))
    or (has("Capture Arena Fly Point") and function_Cached("Flight")==1 and has("Wailord") and has("Red Boat Key"))) then
		return 1
	else
		return 0
	end 
end

function Haruba_Area() 
	if ((function_Cached("Mainland_Start")==1 and has("Orange Boat Key")) 
    or (function_Cached("Mainland_Fly_Point")==1 and function_Cached("Flight")==1 and has("Orange Boat Key")) 
    or (has("Puel Sea Start") and has("Light Blue Boat Key") and has("Orange Boat Key")) 
    or (has("Sea of Wailord Start") and has("Dark Blue Boat Key") and has("Orange Boat Key")) 
    or (has("Volcano Cave Start") and has("Orange Boat Key")) 
    or (has("Boyleland Fly Point") and function_Cached("Flight")==1 and has("Orange Boat Key"))
    or (has("Haruba Desert Start"))
    or (function_Cached("Haruba_Fly_Point")==1 and function_Cached("Flight")==1)
    or (has("Hia Valley Start") and function_Cached("River")==1 and has("Orange Boat Key"))
    or (has("Shiver Camp Fly Point") and function_Cached("Flight")==1 and function_Cached("River")==1 and has("Orange Boat Key"))
    or (has("Almia Castle Fly Point") and function_Cached("Flight")==1 and function_Cached("Rapids")==1 and function_Cached("River")==1 and has("Orange Boat Key"))
    or (has("Capture Arena Fly Point") and function_Cached("Flight")==1 and has("Wailord"))) then
		return 1
	else
		return 0
	end 
end

function Puel_Sea_Area() 
	if ((function_Cached("Mainland_Start")==1 and has("Light Blue Boat Key")) 
    or (function_Cached("Mainland_Fly_Point")==1 and function_Cached("Flight")==1 and has("Light Blue Boat Key")) 
    or (has("Puel Sea Start")) 
    or (has("Sea of Wailord Start") and has("Dark Blue Boat Key") and has("Light Blue Boat Key")) 
    or (has("Volcano Cave Start") and has("Green Boat Key") and has("Light Blue Boat Key")) 
    or (has("Boyleland Fly Point") and function_Cached("Flight")==1 and has("Green Boat Key") and has("Light Blue Boat Key"))
    or (has("Haruba Desert Start") and has("Green Boat Key") and has("Light Blue Boat Key"))
    or (function_Cached("Haruba_Fly_Point")==1 and function_Cached("Flight")==1 and has("Green Boat Key") and has("Light Blue Boat Key"))
    or (has("Hia Valley Start") and function_Cached("River")==1 and has("Light Blue Boat Key"))
    or (has("Shiver Camp Fly Point") and function_Cached("Flight")==1 and function_Cached("River")==1 and has("Light Blue Boat Key"))
    or (has("Almia Castle Fly Point") and function_Cached("Flight")==1 and function_Cached("Rapids")==1 and function_Cached("River")==1 and has("Light Blue Boat Key"))
    or (has("Capture Arena Fly Point") and function_Cached("Flight")==1 and has("Wailord") and has("Green Boat Key") and has("Light Blue Boat Key"))) then
		return 1
	else
		return 0
	end 
end

function Sea_of_Wailord_Area() 
	if ((function_Cached("Mainland_Start")==1 and has("Dark Blue Boat Key")) 
    or (function_Cached("Mainland_Fly_Point")==1 and function_Cached("Flight")==1 and has("Dark Blue Boat Key")) 
    or (has("Puel Sea Start") and has("Light Blue Boat Key") and has("Dark Blue Boat Key")) 
    or (has("Sea of Wailord Start")) 
    or (has("Volcano Cave Start") and has("Green Boat Key") and has("Dark Blue Boat Key")) 
    or (has("Boyleland Fly Point") and function_Cached("Flight")==1 and has("Green Boat Key") and has("Dark Blue Boat Key"))
    or (has("Haruba Desert Start") and has("Green Boat Key") and has("Dark Blue Boat Key"))
    or (function_Cached("Haruba_Fly_Point")==1 and function_Cached("Flight")==1 and has("Green Boat Key") and has("Dark Blue Boat Key"))
    or (has("Hia Valley Start") and function_Cached("River")==1 and has("Dark Blue Boat Key"))
    or (has("Shiver Camp Fly Point") and function_Cached("Flight")==1 and function_Cached("River")==1 and has("Dark Blue Boat Key"))
    or (has("Almia Castle Fly Point") and function_Cached("Flight")==1 and function_Cached("Rapids")==1 and function_Cached("River")==1 and has("Dark Blue Boat Key"))
    or (has("Capture Arena Fly Point") and function_Cached("Flight")==1 and has("Wailord") and has("Green Boat Key") and has("Dark Blue Boat Key"))) then
		return 1
	else
		return 0
	end 
end

function Capture_Arena_Area() 
	if ((function_Cached("Mainland_Start")==1 and has("Orange Boat Key") and has("Wailord")) 
    or (function_Cached("Mainland_Fly_Point")==1 and function_Cached("Flight")==1 and has("Orange Boat Key") and has("Wailord")) 
    or (has("Puel Sea Start") and has("Light Blue Boat Key") and has("Orange Boat Key") and has("Wailord")) 
    or (has("Sea of Wailord Start") and has("Dark Blue Boat Key") and has("Orange Boat Key") and has("Wailord")) 
    or (has("Volcano Cave Start")  and has("Orange Boat Key") and has("Wailord")) 
    or (has("Boyleland Fly Point") and function_Cached("Flight")==1 and has("Orange Boat Key") and has("Wailord"))
    or (has("Haruba Desert Start") and has("Wailord"))
    or (function_Cached("Haruba_Fly_Point")==1 and function_Cached("Flight")==1 and has("Wailord"))
    or (has("Hia Valley Start") and function_Cached("River")==1 and has("Orange Boat Key") and has("Wailord"))
    or (has("Shiver Camp Fly Point") and function_Cached("Flight")==1 and function_Cached("River")==1 and has("Orange Boat Key") and has("Wailord"))
    or (has("Almia Castle Fly Point") and function_Cached("Flight")==1 and function_Cached("Rapids")==1 and function_Cached("River")==1 and has("Orange Boat Key") and has("Wailord"))
    or (has("Capture Arena Fly Point") and function_Cached("Flight")==1)) then
		return 1
	else
		return 0
	end 
end

function Oil_Field_Hideout_Area() 
	if ((has("Oil Field Hideout Start")) 
    or (has("Oil Field Hideout Fly Point") and function_Cached("Flight")==1)) then
		return 1
	else
		return 0
	end 
end

function Manaphy_Area() 
	if (has("Ranger Net") and has("ManaphyM")) then
		return 1
	else
		return 0
	end 
end

function Riolu_Area() 
	if (has("Ranger Net") and has("RioluM")) then
		return 1
	else
		return 0
	end 
end

function Tower_Area() 
	if (has("Ranger Net") and has("TowerM")) then
		return 1
	else
		return 0
	end 
end

function Dialga_Area() 
	if (has("Ranger Net") and has("DialgaM")) then
		return 1
	else
		return 0
	end 
end

function Palkia_Area() 
	if (has("Ranger Net") and has("PalkiaM")) then
		return 1
	else
		return 0
	end 
end

function Shaymin_Area() 
	if (has("Ranger Net") and has("ShayminM")) then
		return 1
	else
		return 0
	end 
end
