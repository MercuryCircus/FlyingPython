#  Gegeben: Temp. in Grad Celsius (C)
#  Gegeben: Temp. in Kelvin (K)
#  K = C + 273.15
#  K minimum = 0


# class InvalidValue(Exception):
#    def __init__(self, message):
#        self.message = message


def get_temp():
    while True:
        c = input("Welche Temperatur möchtest du von C in K umrechnen? ")
        try:
            c = float(c)
            return c
        except ValueError:
            print("Bitte gib eine Ganz- oder Kommazahl ein.")
    #    except (c < -273.15):
        #    print("Temperatur liegt unter absolut 0.")


def convert_to_kelvin(c):
    k = c + 273.15
    return k


if __name__ == "__main__":
    c = get_temp()
    print("Die Antwort ist " + str(convert_to_kelvin(c)) + " K.")
