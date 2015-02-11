import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id = 'high_flyer',
              base_numeric_id = 1040,
              title = '4-4-2 High Flyer [Steam]',
              replacement_id = '-none',
              power = 1300,
              tractive_effort_coefficient = 0.10,
              speed = 80,
              buy_cost = 47,
              vehicle_life = 40,
              intro_date = 1905,
              use_legacy_spritesheet = True)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 90,
                        vehicle_length = 7,
                        spriterow_num = 0))

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 30,
                        vehicle_length = 4,
                        spriterow_num = 1))

consist.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
