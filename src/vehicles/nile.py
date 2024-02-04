from train import EngineConsist, SteamEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="nile",
        base_numeric_id=14140,
        name="2-6-0+0-6-2 Nile",
        role="universal",
        role_child_branch_num=-5,
        base_track_type_name="NG",
        power_by_power_source={
            "STEAM": 900,
        },
        tractive_effort_coefficient=0.3,
        gen=2,
        intro_year_offset=10, # introduce a bit later
        extended_vehicle_life=True,  # extended vehicle life for all this generation of NG eh
        random_reverse=True,
        # note that livery names are metadata only and can repeat for different spriterows
        additional_liveries=["INDUSTRIAL_YELLOW"],
        sprites_complete=False,
    )

    consist.add_unit(
        type=SteamEngineUnit,
        weight=80,
        vehicle_length=8,
        effect_offsets=[(-3, 0), (1, 0)],  # double the smoke eh?
        effect_z_offset=10,  # reduce smoke z position to suit NG engine height
        spriterow_num=0,
    )

    consist.description = (
        """"""
    )
    consist.foamer_facts = """Victorian Railways G class Garratt locomotives"""

    return consist
