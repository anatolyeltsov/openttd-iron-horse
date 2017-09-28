import global_constants
from train import TankConsist, Wagon

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = TankConsist(title = '[Tank Car]',
                      roster = 'pony',
                      base_numeric_id = 630,
                      vehicle_generation = 1,
                      vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            vehicle_length = 4))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = TankConsist(title = '[Tank Car]',
                      roster = 'pony',
                      base_numeric_id = 640,
                      vehicle_generation = 3,
                      vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 30,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = TankConsist(title = '[Tank Car]',
                      roster = 'pony',
                      base_numeric_id = 960,
                      vehicle_generation = 4,
                      vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 40,
                            vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = TankConsist(title = '[Tank Car]',
                      roster = 'pony',
                      base_numeric_id = 650,
                      vehicle_generation = 1,
                      vehicle_life = 40,
                      track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 12,
                            vehicle_length = 4))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- llama ----------------------------------------------------------------------
    consist = TankConsist(title = '[Tank Car]',
                      roster = 'llama',
                      base_numeric_id = 660,
                      vehicle_generation = 1,
                      vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 25,
                            vehicle_length = 5))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = TankConsist(title = '[Tank Car]',
                      roster = 'llama',
                      base_numeric_id = 670,
                      vehicle_generation = 2,
                      vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 50,
                            vehicle_length = 5))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = TankConsist(title = '[Tank Car]',
                      roster = 'llama',
                      base_numeric_id = 680,
                      vehicle_generation = 3,
                      vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 75,
                            vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = TankConsist(title = '[Tank Car]',
                      roster = 'llama',
                      base_numeric_id = 690,
                      vehicle_generation = 1,
                      vehicle_life = 40,
                      track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 20,
                            vehicle_length = 4))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = TankConsist(title = '[Tank Car]',
                      roster = 'llama',
                      base_numeric_id = 1360,
                      vehicle_generation = 2,
                      vehicle_life = 40,
                      track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 40,
                            vehicle_length = 4))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    #--------------- antelope ----------------------------------------------------------------------
    consist = TankConsist(title = '[Tank Car]',
                      roster = 'antelope',
                      base_numeric_id = 1670,
                      vehicle_generation = 1,
                      vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 55,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = TankConsist(title = '[Tank Car]',
                      roster = 'antelope',
                      base_numeric_id = 1680,
                      vehicle_generation = 2,
                      vehicle_life = 40)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 70,
                            vehicle_length = 8))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = TankConsist(title = '[Tank Car]',
                      roster = 'antelope',
                      base_numeric_id = 1910,
                      vehicle_generation = 1,
                      vehicle_life = 40,
                      track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 25,
                            vehicle_length = 5))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


    consist = TankConsist(title = '[Tank Car]',
                      roster = 'antelope',
                      base_numeric_id = 1920,
                      vehicle_generation = 2,
                      vehicle_life = 40,
                      track_type = 'NG')

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 35,
                            vehicle_length = 6))

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['pass_through'])

    consist.add_model_variant(start_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor=consist.graphics_processors['swap_company_colours'])


# gen 3 at 1980 or so
