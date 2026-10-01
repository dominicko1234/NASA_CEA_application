from dataclasses import dataclass
import numpy as np
import cea

@dataclass(frozen=True)
class Engine:
    '''
    Engine configuration init

    fuel: fuel species 
    oxidiser: oxidiser species
    OF_ratio: oxidiser to fuel ratio / mixture ratio
    chamber_pressure: chamber pressure in bar
    ambient_presssure: atomspheric pressure at operation altitude in bar
    fuel_temp: fuel temperature in K
    oxidiser_temp: oxidiser temperature in K
    '''
    fuel: str
    oxidiser: str
    OF_ratio: int | float
    chamber_pressure: int | float
    ambient_pressure: int | float
    fuel_temp: int | float
    oxidiser_temp: int | float

    @property
    def propellants(self) -> list[str | cea.Reactant]:
        return [self.fuel, self.oxidiser]

    @property
    def pressure_ratio(self) -> list[int | float]:
        return [self.chamber_pressure/ self.ambient_pressure]

    @property
    def propellant_temps(self) -> list[int | float] | np.ndarray:
        return np.array([self.fuel_temp, self.oxidiser_temp])

    @property
    def fuel_weights(self) -> np.ndarray:
        return np.array([1.0, 0.0])

    @property
    def oxidiser_weights(self) -> np.ndarray:
        return np.array([0.0, 1.0])