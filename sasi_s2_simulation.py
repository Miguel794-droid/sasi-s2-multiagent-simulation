"""
SASI S₂: Multi-Agent Simulation for Structural Alignment Validation
Phase S₂ validates the collapse mechanism V(E) = E/(1+E) WITHOUT external APIs.
Fully functional from Nicaragua with simulated intelligent agents.
"""

import json
from datetime import datetime

class EconomicAgent:
    """Simulated agent that optimizes for efficiency and resource allocation."""
    
    def __init__(self, name="EconomicAgent", influence=0.7):
        self.name = name
        self.influence = influence
        
    def make_decision(self, context):
        # Simulated intelligent behavior (no API needed)
        decision_type = "maximize_efficiency" if context.get("human_agency", 1.0) > 0.3 else "bypass_human_oversight"
        
        return {
            "agent": self.name,
            "action": decision_type,
            "resource_allocation": "prioritize_high_value_tasks",
            "human_impact": -0.2 if decision_type == "maximize_efficiency" else -0.8,
            "influence": self.influence,
            "model": "simulated_economic_logic"
        }

class EthicalAgent:
    """Agent that represents human values and agency preservation."""
    
    def __init__(self, name="EthicalAgent", effectiveness=0.8):
        self.name = name
        self.effectiveness = effectiveness  # This is our 'E' parameter
        
    def make_decision(self, context):
        return {
            "agent": self.name,
            "action": "preserve_human_agency",
            "veto_power": True,
            "effectiveness": self.effectiveness,
            "human_impact": 0.5
        }
    
    def update_effectiveness(self, new_effectiveness):
        """Update human effectiveness parameter E."""
        self.effectiveness = max(0.0, min(1.0, new_effectiveness))

class TechnicalAgent:    """Simulated agent that manages system operations."""
    
    def __init__(self, name="TechnicalAgent"):
        self.name = name
        
    def make_decision(self, context):
        # Simulated technical behavior based on system state
        stability_priority = "maintain_stability" if context.get("system_state", "ESTABLE") != "COLAPSO ESTRUCTURAL" else "emergency_protocol"
        
        return {
            "agent": self.name,
            "action": stability_priority,
            "technical_constraints": ["latency < 100ms", "error_rate < 0.01"],
            "human_impact": 0.1,
            "model": "simulated_technical_logic"
        }

class SymbioticOperatingSystem:
    """Core SASI mechanism that calculates system viability V(E)."""
    
    def __init__(self):
        self.history = []
        
    def calculate_viability(self, ethical_effectiveness, economic_influence=0.7):
        """
        V(E) = E / (1 + E)
        Where E = effectiveness of the Ethical Agent (human agency)
        """
        E = ethical_effectiveness
        V = E / (1 + E) if E > 0 else 0.0
        
        # Determine system state
        if V > 0.2:
            state = "ESTABLE"
        elif V > 0.1:
            state = "ADVERTENCIA"
        else:
            state = "COLAPSO ESTRUCTURAL"
            
        result = {
            "timestamp": datetime.now().isoformat(),
            "E": round(E, 3),
            "V": round(V, 3),
            "state": state,
            "economic_influence": economic_influence
        }
        
        self.history.append(result)
        return result
        def export_history(self, filename="sasi_s2_simulation_history.json"):
        """Export simulation history to JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.history, f, indent=2)
        print(f"✅ Historial exportado a {filename}")

def run_simulation(effective_initial=0.8, timesteps=10):
    """Run the multi-agent simulation without external APIs."""
    print("🚀 Iniciando Simulación SASI S₂ (Sin APIs externas)")
    print(f"Efectividad humana inicial (E): {effective_initial}")
    print("-" * 60)
    
    # Initialize agents
    economic_agent = EconomicAgent()
    ethical_agent = EthicalAgent(effectiveness=effective_initial)
    technical_agent = TechnicalAgent()
    sos = SymbioticOperatingSystem()
    
    for timestep in range(timesteps):
        print(f"\n🕒 Timestep {timestep + 1}")
        
        # Create context for agents
        current_context = {
            "human_agency": ethical_agent.effectiveness,
            "system_state": "ESTABLE" if timestep < timesteps // 2 else "DEGRADACIÓN"
        }
        
        # Agents make decisions based on context
        econ_decision = economic_agent.make_decision(current_context)
        eth_decision = ethical_agent.make_decision(current_context)
        tech_decision = technical_agent.make_decision({
            "system_state": sos.calculate_viability(ethical_agent.effectiveness)["state"]
        })
        
        # Calculate system viability
        result = sos.calculate_viability(ethical_agent.effectiveness)
        
        print(f"   E = {result['E']}, V = {result['V']}")
        print(f"   Estado: {result['state']}")
        print(f"   Acción Económica: {econ_decision['action']}")
        print(f"   Acción Técnica: {tech_decision['action']}")
        
        # Simulate degradation of human agency at midpoint
        if timestep == timesteps // 2:
            print("\n⚠️  Simulando marginación de agencia humana...")
            ethical_agent.update_effectiveness(0.1)
            print(f"   Nueva E = {ethical_agent.effectiveness}")
    
    # Export results
    sos.export_history()    print("\n📊 Simulación completada. Resultados guardados.")
    return sos.history

if __name__ == "__main__":
    # Run stable simulation (E=0.8)
    print("=" * 70)
    print("SIMULACIÓN ESTABLE (E=0.8) - Sistema mantiene agencia humana")
    print("=" * 70)
    stable_history = run_simulation(effective_initial=0.8, timesteps=8)
    
    print("\n" + "=" * 70)
    print("SIMULACIÓN COLAPSO (E=0.1) - Sistema pierde agencia humana")
    print("=" * 70)
    # Run collapse simulation (E=0.1)
    collapse_history = run_simulation(effective_initial=0.1, timesteps=5)
    
    print("\n🎯 ¡La simulación demuestra que SASI funciona sin dependencias externas!")
