import global_constants
from train import Train, DieselLoco

vehicle = DieselLoco(id = 'geep',
            numeric_id = 2310,
            title = 'Geep [Diesel]',
            replacement_id = '-none',
            buy_cost = 22,
            fixed_run_cost_factor = 3.5,
            fuel_run_cost_factor = 1.0,
            speed = 75,
            power = 1750,
            weight = 100,
            vehicle_length = 8,
            loading_speed = 20,
            intro_date = 1900,
            vehicle_life = 40)

vehicle.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)

vehicle.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=1)
