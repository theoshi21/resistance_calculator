class Resistance:
    def __init__(self, banddigit, multiplier, tolerance):
        self.banddigit = banddigit
        self.multiplier = multiplier
        self.tolerance = tolerance

    def displayinfo(self):
        print("FINAL VALUES: ")
        print(f"Band Digit: {self.banddigit}")
        print(f"Multiplier: {self.multiplier}")

        print(f"Tolerance: +-{self.tolerance}")
        ptolerance = round(float(self.multiplier + self.tolerance),2)
        mtolerance = round(float(self.multiplier - self.tolerance),2)
        print(f"+ Tolerance: {ptolerance}")
        print(f"- Tolerance: {mtolerance}")

