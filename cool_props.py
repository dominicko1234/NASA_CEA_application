import CoolProp.CoolProp as coolprop

def get_nitrous_density(temp: int | float) -> float:
    '''
    get nitrous oxide density from temperature assuming it is in liquid phase
    temp: nitrous oxide temperature in K
    '''
    # Q = mol based vapour quality, 0 = saturated liquid
    return coolprop.PropsSI("D", "T", temp, "Q", 0, "N2O")

def main() -> None:
    print(get_nitrous_density(298.15))

if __name__ == "__main__":
    main()
    