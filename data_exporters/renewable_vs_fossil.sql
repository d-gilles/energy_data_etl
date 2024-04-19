Select
    "date",
    "fossil_brown_coal" + "fossil_gas" + "fossil_hard_coal" + "fossil_oil" + "other" + "waste" AS "Non-Renewable",
	"geothermal" + "hydro_pumped_storage" + "hydro_run_of_river" + "hydro_water_reservoir"  + "other_renewable" + "solar" + "wind_offshore" + "wind_onshore" AS "Renewable"
from {{ df_1 }}