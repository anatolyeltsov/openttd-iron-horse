from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="sbb_gp_3",
        base_numeric_id=8910,
        name="Ae 4/6",
        role="super_heavy_express",
        role_child_branch_num=2,
        power=5160,
        random_reverse=True,
        gen=3,
        pantograph_type="diamond-double",
        #intro_date_offset=5,  # introduce later than gen epoch by design
        force_default_pax_mail_livery=2,  # pax/mail cars default to second livery with this engine
        default_livery_extra_docs_examples=[
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_DARK_GREEN", "COLOUR_WHITE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
        ],
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=105, vehicle_length=8, spriterow_num=0
    )

    consist.description = (
        """ """
    )
    consist.foamer_facts = """SBB Ae 4/6"""

    return consist