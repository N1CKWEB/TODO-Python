


# Convertidor de temperaturas

class ConvertidorTemperaturas:
    
    MAX_CELSIUS=100
    MAX_FAHRENHEIT=213
    
    
    @classmethod
    def c_f(cls,celcius):
        if celcius > cls.MAX_CELSIUS:
            raise ValueError(f'Temperatura de grado celcius demasiada alta: {celcius}')
        return celcius * 9/5 + 32
    
    
    @classmethod
    def f_c(cls,fahrenheit):
        if fahrenheit > cls.MAX_FAHRENHEIT:
            raise ValueError(f"Temperatura de grado fehrenheit demasiada alta: {fahrenheit}")
        return (fahrenheit-32)*5/9
 




if __name__ == "__main__":
    resultado=ConvertidorTemperaturas.c_f(230)
    print(f"23 C a F: {resultado:.2f}")
    
    resultado=ConvertidorTemperaturas.f_c(130)
    print(f"13 F a C: {resultado:.2f}")
    
    
    
    
    
    
    