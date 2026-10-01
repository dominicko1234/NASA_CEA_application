import numpy as np
from engine import Engine
from nasa_cea import NASA_CEA
from plotter import Plotter

class EnginePerformance:
    def __init__(self, engine: Engine) -> None:
        '''
        engine: Engine object
        '''
        self.engine = engine

    def calc_isp(self, effective_exhaust_velocity: float) -> float:
        '''
        calculate isp from effective exhaust velocity
        effective_exhaust_velocity: effective exhaust velocity c in m/s
        '''
        return effective_exhaust_velocity / 9.80665

    def calc_mdot(self, target_thrust: float, effective_exhaust_velocity: float) -> float:
        '''
        calculate total mass flow rate from target thrust and effective exhaust velocity
        target_thrust: target thrust in N
        effective_exhaust_velocity: effective exhaust velocity c in m/s
        '''
        return target_thrust / effective_exhaust_velocity

    def _():
        ...

def main() -> None:
    pass

if __name__ == "__main__":
    main()