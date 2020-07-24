from train import EngineConsist, SteamEngineUnit, SteamEngineTenderUnit


def main(roster_id):
    consist = EngineConsist(roster_id=roster_id,
                            id='thunderer',
                            base_numeric_id=4830,
                            name='4-6-0 Thunderer', # shorter 2-6-0 version was tried, but doesn't fit a power band gap in the mixed traffic roster
                            role='heavy_express',
                            role_child_branch_num=-1,
                            replacement_consist_id='wyvern', # this Joker ends with Wyvern, long-lived
                            power=1500, # slightly less than the Swift (and lighter engine)
                            tractive_effort_coefficient=0.2,
                            gen=2,
                            fixed_run_cost_points=140, # give a bonus so this can be a genuine mixed-traffic engine
                            intro_date_offset=10, # introduce later than gen epoch by design
                            sprites_complete=False)

    consist.add_unit(type=SteamEngineUnit,
                     weight=82,
                     vehicle_length=6,
                     spriterow_num=0)

    consist.add_unit(type=SteamEngineTenderUnit,
                     weight=30,
                     vehicle_length=4,
                     spriterow_num=1)

    return consist