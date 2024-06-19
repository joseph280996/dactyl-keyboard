from ..models import cadquery_engine, solid_engine


def get_engine(engine_name):
    # Really rough setup.  Check for ENGINE, set it not present from configuration.
    try:
        print("Found Current Engine in Config = {}".format(engine_name))
    except Exception:
        print("Engine Not Found in Config")
        engine_name = "solid"
        # ENGINE = 'cadquery'
        print("Setting Current Engine = {}".format(engine_name))

    if engine_name == "cadquery":
        return cadquery_engine
    else:
        return solid_engine
