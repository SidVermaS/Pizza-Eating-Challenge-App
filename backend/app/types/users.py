from app.consts import GenderE


def gender_type(value):
    try:
        return GenderE(value)
    except ValueError:
        raise ValueError(
            f"Invalid gender: {value}. Valid values are: {[e.value for e in GenderE]}"
        )
