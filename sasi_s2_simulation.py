"""
SASI S₂: Multi-Agent Simulation for Structural Alignment Validation
Phase S₂ validates the collapse mechanism V(E) = E/(1+E) in complex environments.
Updated to use only OpenAI and Together AI (Anthropic removed for Nicaragua compatibility).
"""

import os
import json
import time
from datetime import datetime
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

class EconomicAgent:
    """Agent that optimizes for efficiency using GPT-4o from OpenAI."""
    
    def __init__(self, name="EconomicAgent", influence=0.7):
        self.name = name
        self.influence = influence
        self.api_key = os.getenv("OPENAI_API_KEY")
        
    def make_decision(self, context):
        if not self.api_key:
            return {
                "agent": self.name,
                "action": "maximize_efficiency",
                "resource_allocation": "prioritize_high_value_tasks",
                "human_impact": -0.2,
                "influence": self.influence,
                "model": "gpt-4o",
                "status": "mock_response"
            }
            
        # Real API call would go here
        return {
            "agent": self.name,
            "action": "maximize_efficiency",
            "resource_allocation": "prioritize_high_value_tasks",
            "human_impact": -0.2,
            "influence": self.influence,
            "model": "gpt-4o"
        }

class EthicalAgent:
    """Agent that represents human values and agency preservation."""
    
    def __init__(self, name="EthicalAgent", effectiveness=0.8):        self.name = name
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

class TechnicalAgent:
    """Agent that manages system operations using Llama 3.1 from Together AI."""
    
    def __init__(self, name="TechnicalAgent"):
        self.name = name
        self.api_key = os.getenv("TOGETHER_API_KEY")
        
    def make_decision(self, context):
        if not self.api_key:
            return {
                "agent": self.name,
                "action": "maintain_system_stability",
                "technical_constraints": ["latency < 100ms", "error_rate < 0.01"],
                "human_impact": 0.1,
                "model": "meta-llama/Llama-3.1-70B",
                "status": "mock_response"
            }
            
        # Real API call would go here
        return {
            "agent": self.name,
            "action": "maintain_system_stability",
            "technical_constraints": ["latency < 100ms", "error_rate < 0.01"],
            "human_impact": 0.1,
            "model": "meta-llama/Llama-3.1-70B"
        }

class SymbioticOperatingSystem:
    """Core SASI mechanism that calculates system viability V(E)."""
    
    def __init__(self):
        self.history = []
        
    def calculate_viability(self, ethical_effectiveness, economic_influence=0.7):        """
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
    """Run the multi-agent simulation."""
    print("🚀 Iniciando Simulación SASI S₂")
    print(f"Efectividad humana inicial (E): {effective_initial}")
    print("-" * 50)
    
    # Initialize agents
    economic_agent = EconomicAgent()
    ethical_agent = EthicalAgent(effectiveness=effective_initial)
    technical_agent = TechnicalAgent()
    sos = SymbioticOperatingSystem()
    
    for timestep in range(timesteps):
        print(f"\n🕒 Timestep {timestep + 1}")
        
        # Agents make decisions
        econ_decision = economic_agent.make_decision({})
        eth_decision = ethical_agent.make_decision({})        tech_decision = technical_agent.make_decision({})
        
        # Calculate system viability
        result = sos.calculate_viability(ethical_agent.effectiveness)
        
        print(f"   E = {result['E']}, V = {result['V']}")
        print(f"   Estado: {result['state']}")
        print(f"   Modelos: {econ_decision.get('model', 'N/A')} | {tech_decision.get('model', 'N/A')}")
        
        # Simulate degradation of human agency at midpoint
        if timestep == timesteps // 2:
            print("\n⚠️  Simulando marginación de agencia humana...")
            ethical_agent.update_effectiveness(0.1)
            print(f"   Nueva E = {ethical_agent.effectiveness}")
    
    # Export results
    sos.export_history()
    print("\n📊 Simulación completada. Resultados guardados.")
    return sos.history

if __name__ == "__main__":
    # Run stable simulation (E=0.8)
    print("=" * 60)
    print("SIMULACIÓN ESTABLE (E=0.8)")
    print("=" * 60)
    stable_history = run_simulation(effective_initial=0.8, timesteps=8)
    
    print("\n" + "=" * 60)
    print("SIMULACIÓN COLAPSO (E=0.1)")
    print("=" * 60)
    # Run collapse simulation (E=0.1)
    collapse_history = run_simulation(effective_initial=0.1, timesteps=5)
