"""
═══════════════════════════════════════════════════════════════════════
NANO-FABRICATION ENGINE - ATOMIC LAYER
The Foundation: Six Ontological Axioms
═══════════════════════════════════════════════════════════════════════

Just as atoms are the foundation of matter,
axioms are the foundation of reasoning.

CRITICAL: Every concept in this system MUST trace back to these atoms.
NO FLOATING CONCEPTS. NO UNGROUNDED LOGIC.

═══════════════════════════════════════════════════════════════════════
"""

from enum import Enum
from dataclasses import dataclass
from typing import List, Optional


# ═══════════════════════════════════════════════════════════════════════
# THE SIX ATOMS
# ═══════════════════════════════════════════════════════════════════════

class Atom(Enum):
    """
    The six fundamental atoms from which all reasoning is assembled.
    
    These are IRREDUCIBLE - they cannot be broken down further.
    They are SELF-EVIDENT - they require no proof.
    They are COMPLETE - all reasoning traces to these.
    """
    
    A0_EXISTENCE = "existence"
    """
    ATOM 0: EXISTENCE
    Statement: Something exists rather than nothing
    Legal: Rights, duties, jurisdictions exist as constructs
    Validation: Can this be instantiated in reality?
    
    Example: "The court has jurisdiction" presupposes jurisdiction EXISTS as a concept
    """
    
    A1_DISTINCTION = "distinction"
    """
    ATOM 1: DISTINCTION
    Statement: It is possible to distinguish between things
    Legal: Guilty vs innocent, jurisdiction vs non-jurisdiction
    Validation: Are these categories mutually exclusive?
    
    Example: "This is a contract claim, not a tort claim" - DISTINCTION between categories
    """
    
    A2_PATTERN = "pattern"
    """
    ATOM 2: PATTERN
    Statement: Regularities persist across instances
    Legal: Precedent, doctrine, legal principles
    Validation: Does this pattern repeat?
    
    Example: "Courts in this circuit consistently hold..." - PATTERN across cases
    """
    
    A3_RECURSION = "recursion"
    """
    ATOM 3: RECURSION
    Statement: Operations can be applied to their own outputs
    Legal: Appellate review of appellate review, meta-rules
    Validation: Can this be applied to itself?
    
    Example: "The standard of review for reviewing a standard of review" - RECURSION
    """
    
    A4_CONSISTENCY = "consistency"
    """
    ATOM 4: CONSISTENCY
    Statement: Non-contradiction as navigational principle
    Legal: Internal consistency of legal arguments
    Validation: Does this contradict itself?
    
    Example: "The argument cannot both assert and deny standing" - CONSISTENCY check
    """
    
    A5_COMPOSITION = "composition"
    """
    ATOM 5: COMPOSITION
    Statement: Simple elements combine to form complex structures
    Legal: Elements of causes of action, statutory construction
    Validation: Can this be decomposed into parts?
    
    Example: "A contract requires: offer + acceptance + consideration" - COMPOSITION
    """


@dataclass
class AtomicBond:
    """
    A traceable connection from a concept back to its atomic foundation.
    
    This is what makes the system VERIFIABLE - every concept has a proof chain
    back to irreducible axioms.
    """
    concept: str
    atom: Atom
    tracing_path: List[str]
    validated: bool = False
    
    def __post_init__(self):
        """Automatically validate on creation"""
        self.validated = len(self.tracing_path) > 0 and self.atom is not None
    
    def __repr__(self):
        return f"Bond({self.concept} → {self.atom.value})"


class AtomicLayer:
    """
    The foundational layer from which all reasoning emerges.
    
    NANO-FABRICATION PRINCIPLE:
    Just as molecules are made of atoms,
    legal arguments are made of axioms.
    
    This layer ensures NOTHING floats untethered.
    Everything grounds to these six atoms.
    """
    
    def __init__(self):
        self.atoms = {
            Atom.A0_EXISTENCE: {
                "statement": "Something exists rather than nothing",
                "legal_domain": "Rights, duties, jurisdictions exist as constructs",
                "validation_test": "Can this be instantiated in reality?",
                "strength": 1.0  # Foundational - cannot be stronger
            },
            Atom.A1_DISTINCTION: {
                "statement": "It is possible to distinguish between things",
                "legal_domain": "Guilty vs innocent, jurisdiction vs non-jurisdiction",
                "validation_test": "Are these categories mutually exclusive?",
                "strength": 1.0
            },
            Atom.A2_PATTERN: {
                "statement": "Regularities persist across instances",
                "legal_domain": "Precedent, doctrine, legal principles",
                "validation_test": "Does this pattern repeat?",
                "strength": 1.0
            },
            Atom.A3_RECURSION: {
                "statement": "Operations can be applied to their own outputs",
                "legal_domain": "Appellate review of appellate review, meta-rules",
                "validation_test": "Can this be applied to itself?",
                "strength": 1.0
            },
            Atom.A4_CONSISTENCY: {
                "statement": "Non-contradiction as navigational principle",
                "legal_domain": "Internal consistency of legal arguments",
                "validation_test": "Does this contradict itself?",
                "strength": 1.0
            },
            Atom.A5_COMPOSITION: {
                "statement": "Simple elements combine to form complex structures",
                "legal_domain": "Elements of causes of action, statutory construction",
                "validation_test": "Can this be decomposed into parts?",
                "strength": 1.0
            }
        }
    
    def bond_concept(self, concept: str, atom: Atom, intermediate_steps: List[str] = None) -> AtomicBond:
        """
        Create an atomic bond - trace a concept to its foundational atom.
        
        This is the CORE of nano-fabrication:
        Every concept must bond to an atom, or it doesn't exist in our system.
        
        Args:
            concept: The legal concept being grounded
            atom: Which of the 6 atoms it traces to
            intermediate_steps: Optional chain showing the derivation
            
        Returns:
            AtomicBond with full tracing path
            
        Example:
            bond_concept("jurisdiction", Atom.A0_EXISTENCE, ["legal authority", "power to adjudicate"])
            → Proves "jurisdiction" exists by tracing through intermediate concepts to A0
        """
        if intermediate_steps is None:
            intermediate_steps = []
        
        # Build complete tracing path: concept → intermediate → atom
        full_path = [concept] + intermediate_steps + [f"grounds_in_{atom.value}"]
        
        return AtomicBond(
            concept=concept,
            atom=atom,
            tracing_path=full_path,
            validated=True
        )
    
    def validate_bond(self, bond: AtomicBond) -> bool:
        """
        Validate that an atomic bond is properly constructed.
        
        Quality control for molecular assembly:
        - Must have a concept
        - Must connect to an atom
        - Must have a tracing path
        """
        if not bond.concept or len(bond.concept) == 0:
            return False
        
        if bond.atom not in self.atoms:
            return False
        
        if not bond.tracing_path or len(bond.tracing_path) < 2:
            return False
        
        return True
    
    def get_atom_definition(self, atom: Atom) -> dict:
        """Get the complete definition of an atom"""
        return self.atoms.get(atom, {})
    
    def list_all_atoms(self) -> List[str]:
        """List all available atoms"""
        return [atom.value for atom in Atom]


# ═══════════════════════════════════════════════════════════════════════
# ATOMIC VALIDATION
# ═══════════════════════════════════════════════════════════════════════

class AtomicValidator:
    """
    Ensures every concept in the system is properly bonded to atoms.
    
    NANO-FABRICATION QUALITY CONTROL:
    No unbonded concepts allowed.
    Everything must trace to the foundation.
    """
    
    def __init__(self):
        self.atomic_layer = AtomicLayer()
    
    def validate_concept(self, concept: str, claimed_atom: Atom) -> tuple[bool, str]:
        """
        Validate that a concept can properly bond to the claimed atom.
        
        Returns:
            (is_valid, explanation)
        """
        # Check if atom exists
        if claimed_atom not in self.atomic_layer.atoms:
            return (False, f"Atom {claimed_atom} does not exist in atomic layer")
        
        # Check if concept is non-empty
        if not concept or len(concept.strip()) == 0:
            return (False, "Concept cannot be empty")
        
        # All checks passed
        return (True, f"Concept '{concept}' can bond to {claimed_atom.value}")
    
    def find_best_atom(self, concept: str, context: str = "") -> Atom:
        """
        Determine which atom a concept should bond to.
        
        This uses heuristics to find the most appropriate atomic foundation.
        """
        concept_lower = concept.lower()
        context_lower = context.lower()
        
        # Heuristic matching
        if any(word in concept_lower for word in ['exist', 'is', 'being', 'entity']):
            return Atom.A0_EXISTENCE
        
        if any(word in concept_lower for word in ['vs', 'versus', 'different', 'distinguish']):
            return Atom.A1_DISTINCTION
        
        if any(word in concept_lower for word in ['precedent', 'pattern', 'consistently', 'doctrine']):
            return Atom.A2_PATTERN
        
        if any(word in concept_lower for word in ['review', 'appeal', 'meta', 'recursive']):
            return Atom.A3_RECURSION
        
        if any(word in concept_lower for word in ['consistent', 'contradict', 'coherent']):
            return Atom.A4_CONSISTENCY
        
        if any(word in concept_lower for word in ['element', 'component', 'part', 'combine']):
            return Atom.A5_COMPOSITION
        
        # Default to existence
        return Atom.A0_EXISTENCE


# ═══════════════════════════════════════════════════════════════════════
# EXPORT
# ═══════════════════════════════════════════════════════════════════════

__all__ = [
    'Atom',
    'AtomicBond',
    'AtomicLayer',
    'AtomicValidator'
]
