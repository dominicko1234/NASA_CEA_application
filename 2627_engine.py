import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cea
from dataclasses import dataclass, replace

def cea_print_full(solution: cea.RocketSolution) -> None:
    '''
    Print cea solution in NASA CEA format
    solution: rocket solver solution
    '''
    num_pts = solution.num_pts
    T = solution.T
    P = solution.P
    rho = solution.density
    enthalpy = solution.enthalpy
    energy = solution.energy
    gibbs = solution.gibbs_energy
    entropy = solution.entropy
    M_1n = solution.M
    MW = solution.MW
    cp_eq = solution.cp_eq
    cp_fr = solution.cp_fr
    cv_eq = solution.cv_eq
    cv_fr = solution.cv_fr
    Mach = solution.Mach
    gamma_s = solution.gamma_s
    v_sonic = solution.sonic_velocity
    ae_at = solution.ae_at
    c_star = solution.c_star
    Cf = solution.coefficient_of_thrust
    Isp = solution.Isp
    Isp_vac = solution.Isp_vacuum

    print("P, bar         ", end=" ")
    for i in range(num_pts):
        if i < num_pts-1:
            print("{0:10.3f}".format(P[i]), end=" ")
        else:
            print("{0:10.3f}".format(P[i]))

    print("T, K           ", end=" ")
    for i in range(num_pts):
        if i < num_pts-1:
            print("{0:10.3f}".format(T[i]), end=" ")
        else:
            print("{0:10.3f}".format(T[i]))

    print("Density, kg/m^3", end=" ")
    for i in range(num_pts):
        if i < num_pts-1:
            print("{0:10.3f}".format(rho[i]), end=" ")
        else:
            print("{0:10.3f}".format(rho[i]))

    print("H, kJ/kg       ", end=" ")
    for i in range(num_pts):
        if i < num_pts-1:
            print("{0:10.2f}".format(enthalpy[i]), end=" ")
        else:
            print("{0:10.2f}".format(enthalpy[i]))

    print("U, kJ/kg       ", end=" ")
    for i in range(num_pts):
        if i < num_pts-1:
            print("{0:10.2f}".format(energy[i]), end=" ")
        else:
            print("{0:10.2f}".format(energy[i]))

    print("G, kJ/kg       ", end=" ")
    for i in range(num_pts):
        if i < num_pts-1:
            print("{0:10.1f}".format(gibbs[i]), end=" ")
        else:
            print("{0:10.1f}".format(gibbs[i]))

    print("S, kJ/kg-K     ", end=" ")
    for i in range(num_pts):
        if i < num_pts-1:
            print("{0:10.3f}".format(entropy[i]), end=" ")
        else:
            print("{0:10.3f}".format(entropy[i]))

    print("M, (1/n)       ", end=" ")
    for i in range(num_pts):
        if i < num_pts-1:
            print("{0:10.3f}".format(M_1n[i]), end=" ")
        else:
            print("{0:10.3f}".format(M_1n[i]))

    print("MW             ", end=" ")
    for i in range(num_pts):
        if i < num_pts-1:
            print("{0:10.3f}".format(MW[i]), end=" ")
        else:
            print("{0:10.3f}".format(MW[i]))

    print("Cp_eq, kJ/kg-K ", end=" ")
    for i in range(num_pts):
        if i < num_pts-1:
            print("{0:10.3f}".format(cp_eq[i]), end=" ")
        else:
            print("{0:10.3f}".format(cp_eq[i]))

    print("Cp_fr, kJ/kg-K ", end=" ")
    for i in range(num_pts):
        if i < num_pts-1:
            print("{0:10.3f}".format(cp_fr[i]), end=" ")
        else:
            print("{0:10.3f}".format(cp_fr[i]))

    print("Cv_eq, kJ/kg-K ", end=" ")
    for i in range(num_pts):
        if i < num_pts-1:
            print("{0:10.3f}".format(cv_eq[i]), end=" ")
        else:
            print("{0:10.3f}".format(cv_eq[i]))

    print("Cv_eq, kJ/kg-K ", end=" ")
    for i in range(num_pts):
        if i < num_pts-1:
            print("{0:10.3f}".format(cv_fr[i]), end=" ")
        else:
            print("{0:10.3f}".format(cv_fr[i]))

    print("Gamma_s        ", end=" ")
    for i in range(num_pts):
        if i < num_pts-1:
            print("{0:10.3f}".format(gamma_s[i]), end=" ")
        else:
            print("{0:10.3f}".format(gamma_s[i]))

    print("Son. vel., m/s ", end=" ")
    for i in range(num_pts):
        if i < num_pts-1:
            print("{0:10.2f}".format(v_sonic[i]), end=" ")
        else:
            print("{0:10.2f}".format(v_sonic[i]))

    print("Mach           ", end=" ")
    for i in range(num_pts):
        if i < num_pts-1:
            print("{0:10.3f}".format(Mach[i]), end=" ")
        else:
            print("{0:10.3f}".format(Mach[i]))

    print()
    print("PERFORMANCE PARAMETERS")
    print()

    print("Ae/At          ", end=" ")
    for i in range(num_pts):
        if i < num_pts-1:
            print("{0:10.3f}".format(ae_at[i]), end=" ")
        else:
            print("{0:10.3f}".format(ae_at[i]))

    print("C*, m/s        ", end=" ")
    for i in range(num_pts):
        if i < num_pts-1:
            print("{0:10.2f}".format(c_star[i]), end=" ")
        else:
            print("{0:10.2f}".format(c_star[i]))

    print("Cf             ", end=" ")
    for i in range(num_pts):
        if i < num_pts-1:
            print("{0:10.4f}".format(Cf[i]), end=" ")
        else:
            print("{0:10.4f}".format(Cf[i]))

    print("Isp, vac., m/s ", end=" ")
    for i in range(num_pts):
        if i < num_pts-1:
            print("{0:10.3f}".format(Isp_vac[i]), end=" ")
        else:
            print("{0:10.3f}".format(Isp_vac[i]))

    print("Isp, m/s       ", end=" ")
    for i in range(num_pts):
        if i < num_pts-1:
            print("{0:10.3f}".format(Isp[i]), end=" ")
        else:
            print("{0:10.3f}".format(Isp[i]))

    print()
    print("MOLE FRACTIONS")
    print("")
    trace_species = []
    for prod in solution.mole_fractions:
        if np.any(solution.mole_fractions[prod] > 5e-6):
            print("{0:15s}".format(prod), end=" ")
            for j in range(len(solution.mole_fractions[prod])):
                if j < len(solution.mole_fractions[prod])-1:
                    print("{0:10.5g}".format(
                        solution.mole_fractions[prod][j]), end=" ")
                else:
                    print("{0:10.5g}".format(solution.mole_fractions[prod][j]))
        else:
            trace_species.append(prod)

    print()
    print("TRACE SPECIES:")
    max_cols = 8
    nrows = (len(trace_species) + max_cols - 1) // max_cols
    for i in range(nrows):
        print(" ".join("{0:15s}".format(trace_species[j]) for j in range(
            i * max_cols, min((i + 1) * max_cols, len(trace_species)))))

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

    
@dataclass
class plot_data:
    '''
    class to pass data into plot function
    x: x axis data
    y: y axis data
    x_label: x axis label
    y_label: y axis label
    title: graph title
    '''
    x: list[int | float]
    y: list[int | float]
    x_label: str
    y_label: str
    title: str

@dataclass
class group_plot_data:
    '''
    class to pass data to plot multiple lines on the same graph/figure
    data_series: list of plot_data objects that defines the lines to be plotted
    title: title of graph
    x_label: xlabel of graph
    y_label: ylabel of graph
    '''
    data_series: list[plot_data]
    title: str
    x_label: str
    y_label: str

def cea_rocket_solver(engine_config: Engine) -> cea.RocketSolution:
    '''
    Solve CEA using RocketSolver
    engine_config: engine configuration
    '''
    propellants = engine_config.propellants

    reactants = cea.Mixture(propellants)
    products = cea.Mixture(propellants, products_from_reactants=True)
    solver = cea.RocketSolver(products, reactants=reactants)
    solution = cea.RocketSolution(solver)

    # overall weight fraction array of reactants
    weights = reactants.of_ratio_to_weights(engine_config.oxidiser_weights, engine_config.fuel_weights, engine_config.OF_ratio)
    # chamber enthalpy
    hc = reactants.calc_property(cea.ENTHALPY, weights, engine_config.propellant_temps) / cea.R
    # solve
    solver.solve(solution, weights, engine_config.chamber_pressure, pi_p=engine_config.pressure_ratio, hc=hc, iac=True)  # iac = infinite area combustor
    # return cea solution
    return solution

def calc_isp(effective_exhaust_velocity: float | int) -> float:
    '''
    Calculate isp from effective exhaust velocity
    effective_exhaust_velocity: effective exhaust velocity c in m/s
    '''
    return effective_exhaust_velocity / 9.80665

def calc_mdot(effective_exhaust_velocity: float | int, target_thrust: float | int, thrust_unit: str = "kN") -> float:
    '''
    calculate mass flow rate in kg/s from effective exhaust velocity and target thrust
    effective_exhaust_velocity: effective exhaust velocity c in m/s
    target_thrust: engine taraget thrust in kN
    thrust_unit: unit for target_thrust, can be kN or N
    '''
    if thrust_unit == "kN":
        prefix = 1000
    elif thrust_unit == "N":
        prefix = 1
    else:
        raise Exception("Invalid thrust unit")
    return (target_thrust * prefix) / effective_exhaust_velocity

def calc_individual_mdot(total_mdot: int | float, OF_ratio: float) -> tuple[float, float]:
    '''
    calculate fuel and oxidiser mass flow rate, return (fuel mdot, oxidiser mdot)
    total_mdot: total mass flow rate
    OF_ratio: oxidiser to fuel ratio
    '''
    fuel_mdot = total_mdot/(OF_ratio + 1)
    oxidiser_mdot = total_mdot * (OF_ratio/(OF_ratio + 1))
    return (fuel_mdot, oxidiser_mdot)

def get_temperature_from_Pc(chamber_pressure_array: list[int | float], engine_config: Engine) -> plot_data:
    '''
    Plot chamber combustion temperature T_1 against chamber pressure for a fixed OF ratio and ambient pressrue
    chamber_pressure_array: chamber pressure array in bar
    engine_config: engine configuration (note that chamber pressure in engine config will be overridden by chamber pressure array)
    '''

    temp_list = []
    for pc in chamber_pressure_array:
        new_config = replace(engine_config, chamber_pressure = pc)
        solution = cea_rocket_solver(new_config)
        t_1 = solution.T[0]
        temp_list.append(t_1)
    return plot_data(chamber_pressure_array, temp_list, "Chamber pressure (bar)", "Combustion temperature (K)", f"{engine_config.fuel}/{engine_config.oxidiser}, OF {engine_config.OF_ratio}")

def get_temperature_from_OF(OF_ratio_array: list[float | int], engine_config: Engine) -> plot_data:
    '''
    Plot chamber combustion temperature T_1 against OF ratio for a fixed chamber pressure
    OF_ratio_array: mixture ratio array
    engine_config: engine configuration (note that OF ratio in engine config will be overridden by chamber pressure array)
    '''
    temp_list = []
    for mr  in OF_ratio_array:
        new_config = replace(engine_config, OF_ratio=mr)
        solution = cea_rocket_solver(new_config)
        t_1 = solution.T[0]
        temp_list.append(t_1)
    return plot_data(OF_ratio_array, temp_list, "OF ratio", "Combustion temperature (K)", f"{engine_config.fuel}/{engine_config.oxidiser}, {engine_config.chamber_pressure} bar")

def get_isp_from_OF(OF_ratio_array: list[float | int], engine_config: Engine) -> plot_data:
    '''
    Plot isp against OF ratio for a fixed chamber pressure
    OF_ratio_array: mixture ratio array
    engine_config: engine configuration (note that OF ratio in engine config will be overridden by chamber pressure array)
    '''
    isp_array = []
    for mr  in OF_ratio_array:
        new_config = replace(engine_config, OF_ratio=mr)
        solution = cea_rocket_solver(new_config)
        c = solution.Isp[2]
        isp_array.append(calc_isp(c))
    return plot_data(OF_ratio_array, isp_array, "OF ratio", "Isp (s)", f"{engine_config.fuel}/{engine_config.oxidiser}, {engine_config.chamber_pressure} bar")

def get_mdot_from_OF(OF_ratio_array: list[float | int], target_thrust: float | int, engine_config: Engine) -> plot_data:
    '''
    Plot mass flow rate against OF ratio for a fixed chamber pressure
    OF_ratio_array: mixture ratio array
    target_thrust: engine target thrust in kN
    engine_config: engine configuration (note that OF ratio in engine config will be overridden by chamber pressure array)
    '''
    mdot_array = []
    for mr in OF_ratio_array:
        new_config = replace(engine_config, OF_ratio=mr)
        solution = cea_rocket_solver(new_config)
        c = solution.Isp[2]
        mdot_array.append(calc_mdot(c, target_thrust))
    return plot_data(OF_ratio_array, mdot_array, "OF ratio", "Total mass flow rate (kg/s)", f"{engine_config.fuel}/{engine_config.oxidiser}, {engine_config.chamber_pressure} bar")

def get_c_star_from_OF(OF_ratio_array: list[float | int], engine_config: Engine) -> plot_data:
    '''
    Plot c star against OF ratio for a fixed chamber pressure
    OF_ratio_array: mixture ratio array
    engine_config: engine configuration (note that OF ratio in engine config will be overridden by chamber pressure array)
    '''
    c_star_array = []
    for mr in OF_ratio_array:
        new_config = replace(engine_config, OF_ratio=mr)
        solution = cea_rocket_solver(new_config)
        c_star = solution.c_star[2]
        c_star_array.append(c_star)
    return plot_data(OF_ratio_array, c_star_array, "OF ratio", "Characteristic velocity (m/s)", f"{engine_config.fuel}/{engine_config.oxidiser}, {engine_config.chamber_pressure} bar")

def plot_graph(data: list[plot_data | group_plot_data]) -> None:
    '''
    Plot lists of data onto separate figures/ graph
    data: list of plot_data objects
    '''
    for i, series in enumerate(data):
        plt.figure(i)
        if type(series) == plot_data:
            plt.plot(series.x, series.y)
            plt.xlabel(series.x_label)
            plt.ylabel(series.y_label)
            plt.title(series.title)
            plt.grid()
        elif type(series) == group_plot_data:
            plot_on_same_graph(series)
    plt.show()

def plot_on_same_graph(data: group_plot_data) -> None:
    '''
    Plot multiple sets of array onto the same graph/figure, xlabel and ylabel are assumed to be the same as the first element in the data list
    data: list of plot_data object
    title: title of the graph
    x_label: x axis label
    y_label: y axis label
    '''

    for series in data.data_series:
        plt.plot(series.x, series.y, label=series.title)

    plt.xlabel(data.x_label)
    plt.ylabel(data.y_label)
    plt.title(data.title)
    plt.legend(loc="best")
    plt.grid()
    
def gen_graphs(engine_config: Engine, target_thrust: int | float) -> None:
    '''
    use all array gen functions to plot graphs
    engine_config: Engine class object
    target_thrust: engine target thrust in kN
    '''
    OF_ratio_array: list[int | float] = list(np.arange(1, 8.1, 0.1))
    chamber_pressure_array: list[int | float] = list(range(10, 55, 5))
    chamber_pressure_array: list[int | float] = [20, 25]

    # OF and temp 
    plot_list = []
    for pc in chamber_pressure_array:
        new_config = replace(engine_config, chamber_pressure=pc)
        plot_list.append(get_temperature_from_OF(OF_ratio_array, new_config))
    Pc_temp_group1 = group_plot_data(plot_list, "OF ratio effect on temperature for different chamber pressures", "OF ratio", "Combustion temperature (K)")

    # OF and mdot
    plot_list = []
    for pc in chamber_pressure_array:
        new_config = replace(engine_config, chamber_pressure=pc)
        plot_list.append(get_mdot_from_OF(OF_ratio_array, target_thrust, new_config))
    OF_mdot_group1 = group_plot_data(plot_list, "OF ratio effect on mdot for different chamber pressures", "OF ratio", "Total mass flow rate (kg/s)")

    # OF and isp
    plot_list = []
    for pc in chamber_pressure_array:
        new_config = replace(engine_config, chamber_pressure=pc)
        plot_list.append(get_isp_from_OF(OF_ratio_array, new_config))
    Pc_isp_group1 = group_plot_data(plot_list, "OF ratio effect on isp for different chamber pressures", "OF ratio", "Isp (s)")

    # OF and c*
    plot_list = []
    for pc in chamber_pressure_array:
        new_config = replace(engine_config, chamber_pressure = pc)
        plot_list.append(get_c_star_from_OF(OF_ratio_array, new_config))
    OF_c_star_group1 = group_plot_data(plot_list, "OF ratio effect on c* for different chamber pressures", "OF ratio", "Characteristic velocity (m/s)")

    # plot all
    plot_graph([Pc_temp_group1, OF_mdot_group1, Pc_isp_group1, OF_c_star_group1])

def max_thrust_from_max_OD(OD_array: list[int | float], OF_array: list[int | float], chamber_pressure_array: list[int | float], engine_config: Engine, plot_all_on_same_graph: bool=False) -> list[tuple[float, float]]:
    '''
    calculate max thrust using max OD
    OD_array: array of Outer Diameter in metres
    OF_array: OF ratio array 
    chamber_pressure_array: chamber pressure array in bar
    engine_config: Engine class object
    '''
    exit_area_array = np.array(OD_array)**2 * np.pi/4
    group_list = []
    output_list = []
    plot_list = []
    for pc in chamber_pressure_array:
        for i, ae in enumerate(exit_area_array):
            thrust_array = []
            for mr in OF_array:
                new_config = replace(engine_config, OF_ratio = mr, chamber_pressure=pc)
                solution = cea_rocket_solver(new_config)
                expansion_ratio = solution.ae_at[2]
                thrust_coefficient = solution.coefficient_of_thrust[2]
                throat_area = ae / expansion_ratio
                thrust = thrust_coefficient * pc * throat_area * 1e5
                thrust_array.append(thrust/1000)
                if mr > 3.5 and mr < 3.6:
                    print(thrust_coefficient)
                    print(expansion_ratio)
                    print(thrust)
            plot_list.append(plot_data(OF_array, thrust_array, "OF ratio", "Thrust (kN)", f"OD: {OD_array[i] * 1000} mm, chamber pressure: {pc} bar"))
            max_thrust = max(thrust_array)
            max_thrust_OF_index = OF_array[thrust_array.index(max_thrust)]
            output_list.append((pc, max_thrust, max_thrust_OF_index))
        if not plot_all_on_same_graph:
            group_list.append(group_plot_data(plot_list, f"Thrust against OF ratio for different max OD, chamber pressure = {pc} bar", "OF ratio", "Thrust (kN)"))
            plot_list = []
        
    # plot
    if not plot_all_on_same_graph:
        plot_graph(data=group_list)
    elif plot_all_on_same_graph:
        plot_graph(data=[group_plot_data(plot_list, f"Thrust against OF ratio for different max OD", "OF ratio", "Thrust (kN)")])
    return output_list

def main() -> None:
    fuel = "C3H8O,2propanol"
    oxidiser = "N2O"
    fuel_temp = 298.15  # K
    oxidiser_temp = 338.15  # K
    OF_ratio = 3.5
    chamber_pressure = 20  # bar
    ambient_pressure  = 1.01325  # bar
    target_thrust = 8 # kN
    G4 = Engine(fuel, oxidiser, OF_ratio, chamber_pressure, ambient_pressure, fuel_temp, oxidiser_temp)
    # gen_graphs(G4, target_thrust)
    print(G4)
    OD_array = [0.1524, 0.2032]  # 6", 8" in m
    OF_array: list[int | float] = list(np.arange(1, 8.1, 0.1))
    chamber_pressure_array: list[int | float] = [20, 25, 30, 35, 40]
    x = max_thrust_from_max_OD(OD_array, OF_array, chamber_pressure_array, G4, True)
    # cea_print_full(cea_rocket_solver(G4))
    
if __name__ == "__main__":
    main()
