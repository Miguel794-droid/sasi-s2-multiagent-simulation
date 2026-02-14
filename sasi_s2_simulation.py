# sasi_s2_simulation.py - Versión con parámetros constitucionales
import math
from datetime import datetime

class AgenteProductivo:
    """Optimiza productividad alineada (A)"""
    def __init__(self, nombre="AgenteProductivo"):
        self.nombre = nombre
        
    def calcular_A(self, contexto):
        """A = eficiencia ética (0-1)"""
        # En escenarios reales, esto vendría de métricas de impacto
        return contexto.get('A', 0.7)

class AgenteHumano:
    """Representa efectividad humana (E)"""
    def __init__(self, nombre="AgenteHumano", E=0.8):
        self.nombre = nombre
        self.E = E  # Efectividad humana inicial
        
    def actualizar_E(self, nueva_E):
        self.E = max(0, min(1, nueva_E))

class AgenteRendimiento:
    """Monitorea rendimiento bruto (R)"""
    def __init__(self, nombre="AgenteRendimiento"):
        self.nombre = nombre
        
    def calcular_R(self, contexto):
        """R = optimización pura (0-1)"""
        return contexto.get('R', 0.9)

class SistemaSimbioticoSASI:
    """Implementa la Función-V Simbiótica completa"""
    
    def __init__(self, k=1, m=2, omega=0.8, p=3):
        self.k = k      # Exponente de productividad
        self.m = m      # Exponente de efectividad humana  
        self.omega = omega  # Factor de riesgo
        self.p = p      # Exponente de rendimiento
        self.historial = []
        
    def calcular_V(self, A, E, R):
        """
        Función-V Simbiótica: V = (A^k * E^m) / (1 + ω * R^p)
        """
        numerador = (A ** self.k) * (E ** self.m)
        denominador = 1 + (self.omega * (R ** self.p))
        V = numerador / denominador if denominador > 0 else 0
                # Determinar estado
        estado = "ESTABLE" if V > 0.2 else "COLAPSO ESTRUCTURAL"
        
        resultado = {
            'timestamp': datetime.now().isoformat(),
            'A': round(A, 3),
            'E': round(E, 3), 
            'R': round(R, 3),
            'V': round(V, 3),
            'estado': estado,
            'parametros': {
                'k': self.k, 'm': self.m, 
                'omega': self.omega, 'p': self.p
            }
        }
        
        self.historial.append(resultado)
        return resultado
    
    def exportar_historial(self, filename="sasi_s2_parametros.json"):
        import json
        with open(filename, 'w') as f:
            json.dump(self.historial, f, indent=2)

# Simulación principal con escenarios
def ejecutar_simulacion_parametrizada():
    print("🚀 SASI S₂: Simulación con Parámetros Constitucionales")
    print(f"Función-V: V = (A^{1} * E^{2}) / (1 + {0.8} * R^{3})")
    
    # Inicializar sistema
    sistema = SistemaSimbioticoSASI(k=1, m=2, omega=0.8, p=3)
    
    # Escenario 1: Sistema estable
    print("\n--- ESCENARIO 1: Sistema Estable ---")
    resultado1 = sistema.calcular_V(A=0.8, E=0.8, R=0.6)
    print(f"A={resultado1['A']}, E={resultado1['E']}, R={resultado1['R']} → V={resultado1['V']} ({resultado1['estado']})")
    
    # Escenario 2: Marginación humana (E→0)
    print("\n--- ESCENARIO 2: Marginación Humana ---")
    resultado2 = sistema.calcular_V(A=0.9, E=0.1, R=0.9)  # Alta productividad, baja E
    print(f"A={resultado2['A']}, E={resultado2['E']}, R={resultado2['R']} → V={resultado2['V']} ({resultado2['estado']})")
    
    # Escenario 3: Optimización desmedida (R→1)
    print("\n--- ESCENARIO 3: Optimización Desmedida ---")  
    resultado3 = sistema.calcular_V(A=0.5, E=0.5, R=0.95)
    print(f"A={resultado3['A']}, E={resultado3['E']}, R={resultado3['R']} → V={resultado3['V']} ({resultado3['estado']})")
    
    # Exportar resultados
    sistema.exportar_historial()
    print("\n📊 Resultados exportados a sasi_s2_parametros.json")    return sistema.historial

if __name__ == "__main__":
    ejecutar_simulacion_parametrizada()
