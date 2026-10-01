import cea
from engine import Engine
import numpy as np

class NASA_CEA:
    '''
    nasa cea application
    '''
    def cea_rocket_solver(self, engine_config: Engine) -> cea.RocketSolution:
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

    def cea_print_full(self, solution: cea.RocketSolution) -> None:
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

if __name__ == "__main__":
    pass