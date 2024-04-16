Select
    date(date) AS "date",
    sum("biomass") AS "biomass",
	sum("fossil_brown_coal") AS "fossil_brown_coal", 
	sum("fossil_gas") AS "fossil_gas", 
	sum("fossil_hard_coal") AS "fossil_hard_coal", 
	sum("fossil_oil") AS "fossil_oil",
	sum("geothermal") AS "geothermal",
	sum("hydro_pumped_storage") AS "hydro_pumped_storage",
	sum("hydro_run_of_river") AS "hydro_run_of_river", 
	sum("hydro_water_reservoir") AS "hydro_water_reservoir",
	sum("other") AS "other", 
	sum("other_renewable") AS "other_renewable", 
	sum("solar") AS "solar", 
	sum("waste") AS "waste", 
	sum("wind_offshore") AS "wind_offshore", 
	sum("wind_onshore") AS "wind_onshore" 
from {{ df_2 }}
group by date(date)

