from utils import functionType
from utils import Interval

def integralArea(f: functionType, interval: Interval, Δx = 1) -> float:
    def trapeziumArea(f: functionType, x: float, Δx: float) -> float:
        return (Δx*(f(x + Δx) + f(x))) / 2
    
    if interval.size < Δx:
        raise Exception("b - a < Δx")

    trapeziumsNumbers = int(interval.size / Δx)
    trapeziumsAreas = [trapeziumArea(f, i*Δx + interval.a, Δx) for i in range(trapeziumsNumbers)]

    return sum(trapeziumsAreas)

if __name__ == "__main__":
    from math import e
    from math import log
    from math import pow

    def y(x: float) -> float:
        return log(x, e) * pow(x, 2)
    
    print(integralArea(y, Interval(1, 10), 1e-1))
    print(integralArea(y, Interval(1, 10), 1e-5))
    print("-"*9)

    print(integralArea(y, Interval(20, 30), 1e-1))
    print(integralArea(y, Interval(20, 30), 1e-5))
    print("-"*9)
    
    print(integralArea(y, Interval(30, 40), 1e-1))
    print(integralArea(y, Interval(30, 40), 1e-5))
    print("-"*9)

