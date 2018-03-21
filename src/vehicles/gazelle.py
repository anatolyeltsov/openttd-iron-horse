from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='gazelle',
                        base_numeric_id=2030,
                        name='Gazelle',
                        power=1800,
                        track_type='NG',
                        speed=85,
                        intro_date=1975)

consist.add_unit(type=DieselEngineUnit,
                 weight=90,
                 vehicle_length=7,
                 spriterow_num=0)

