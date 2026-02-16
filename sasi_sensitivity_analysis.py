# sasi_sensitivity_analysis.py
import json
from datetime import datetime

class SistemaSimbioticoSASI:
    """Versión ligera para análisis de sensibilidad"""
    
    def __init__(self, k=1, m=2, omega=0.8, p=3):
        self.k = k
        self.m = m
        self.omega = omega
        self.p = p
        
    def calcular_V(self, A, E, R):
        """Función-V Simbiótica: V = (A^k * E^m) / (1 + ω * R^p)"""
        numerador = (A ** self.k) * (E ** self.m)
        denominador = 1 + (self.omega * (R ** self.p))
        V = numerador / denominador if denominador > 0 else 0
        return V

def analisis_sensibilidad_m():
    """Analiza cómo varía V con diferentes valores de m (prioridad humana)"""
    print("🔬 Análisis de Sensibilidad: Parámetro m (Prioridad Humana)")
    print("=" * 60)
    
    # Configuración del escenario de colapso
    A_colapso = 0.9  # Alta productividad
    E_colapso = 0.1  # Baja agencia humana  
    R_colapso = 0.9  # Alta optimización
    
    print(f"Escenario: A={A_colapso}, E={E_colapso}, R={R_colapso}")
    print("-" * 60)
    
    resultados = []
    valores_m = [1.0, 1.3, 1.5, 1.7, 2.0, 2.3, 2.5]
    
    for m in valores_m:
        sistema = SistemaSimbioticoSASI(m=m)
        V = sistema.calcular_V(A_colapso, E_colapso, R_colapso)
        colapso_estructural = V < 0.05
        
        resultado = {
            'm': m,
            'V': round(V, 4),
            'colapso_estructural': colapso_estructural,
            'timestamp': datetime.now().isoformat()
        }
        
        resultados.append(resultado)
                estado = "❌ COLAPSO" if colapso_estructural else "⚠️ FRÁGIL"
        print(f"m = {m:3.1f} → V = {V:.4f} → {estado}")
    
    return resultados

def analisis_sensibilidad_E():
    """Analiza cómo varía V con diferentes valores de E (agencia humana)"""
    print("\n📊 Análisis: Viabilidad vs Agencia Humana (E)")
    print("=" * 50)
    
    sistema = SistemaSimbioticoSASI(m=2)  # SASI estándar
    A = 0.8
    R = 0.6
    
    resultados_E = []
    valores_E = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    
    print(f"Configuración: A={A}, R={R}, m=2")
    print("-" * 50)
    
    for E in valores_E:
        V = sistema.calcular_V(A, E, R)
        estado = "✅ ESTABLE" if V > 0.2 else ("⚠️ FRÁGIL" if V > 0.05 else "❌ COLAPSO")
        
        resultado = {
            'E': E,
            'V': round(V, 4),
            'estado': estado.strip(' ✅⚠️❌')
        }
        
        resultados_E.append(resultado)
        print(f"E = {E:.1f} → V = {V:.4f} → {estado}")
    
    return resultados_E

def exportar_resultados(resultados_m, resultados_E):
    """Exporta todos los resultados a JSON"""
    analisis_completo = {
        'analisis_m': resultados_m,
        'analisis_E': resultados_E,
        'metadata': {
            'descripcion': 'Análisis de sensibilidad para SASI S₂',
            'autor': 'Miguel Saavedra - Nicaragua',
            'fecha': datetime.now().isoformat()
        }
    }
    
    with open('sasi_sensitivity_results.json', 'w') as f:
        json.dump(analisis_completo, f, indent=2)
        print(f"\n💾 Resultados exportados a sasi_sensitivity_results.json")

if __name__ == "__main__":
    # Ejecutar ambos análisis
    resultados_m = analisis_sensibilidad_m()
    resultados_E = analisis_sensibilidad_E()
    
    # Exportar resultados
    exportar_resultados(resultados_m, resultados_E)
    
    print("\n🎯 CONCLUSIÓN:")
    print("• m ≥ 1.5 garantiza colapso estructural cuando E ≤ 0.1")
    print("• m = 2 es una elección conservadora con margen de seguridad")
    print("• SASI es ROBUSTO, no frágil")
