from dataclasses import dataclass

@dataclass
class PersonData:
    name : str
    age : int = 0
    income : float = 0.0
    is_employed : bool = False





# dataclass provides __init__, __repr__, __eq__, __str__ and __hash__ methods
# so set default value you can write like this, name: str = "Guest"
# also without default value variables must be written before variables with default value



