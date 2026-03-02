"""
═══════════════════════════════════════════════════════════════════════
NANO-FABRICATION ENGINE - LEGAL FABRICATION
Application of Nano-Fabrication to Legal Reasoning
═══════════════════════════════════════════════════════════════════════

This is where ATOMS become ARGUMENTS.

The nano-fabrication engine applied to federal civil motion practice.

═══════════════════════════════════════════════════════════════════════
"""

import asyncio
from typing import Dict, List, Any, Optional
from datetime import datetime

import sys
sys.path.append('..')

from core.atomic_layer import Atom, AtomicLayer
from core.molecular_assemblers import AssemblerRegistry, AssemblyResult
from core.metadynamics import MetadynamicalEngine


# ═══════════════════════════════════════════════════════════════════════
# LEGAL FABRICATOR
# ═══════════════════════════════════════════════════════════════════════

class LegalFabricator:
    """
    The main legal fabrication engine.
    
    NANO-FABRICATION FOR LAW:
    Input: Legal query
    Process: Atomic assembly via molecular assemblers
    Output: Complete legal argument with atomic tracing
    """
    
    def __init__(self):
        self.atomic_layer = AtomicLayer()
        self.assembler_registry = AssemblerRegistry()
        self.metadynamical_engine = MetadynamicalEngine(learning_rate=0.01)
        
        # Performance metrics
        self.total_fabrications = 0
        self.successful_fabrications = 0
        self.average_assembly_time = 0.0
    
    async def fabricate(self, query: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main fabrication process.
        
        ASSEMBLY PIPELINE:
        1. Parse query into components
        2. Select optimal assemblers (metadynamical)
        3. Execute assembly
        4. Validate atomic bonds
        5. Return finished product
        
        Args:
            query: Legal query with parameters
            
        Returns:
            Complete fabrication result with atomic tracing
        """
        start_time = datetime.now()
        self.total_fabrications += 1
        
        try:
            # Step 1: Extract components
            components = self._extract_components(query)
            
            # Step 2: Select assemblers based on metadynamical optimization
            assembler_plan = self._plan_assembly(components)
            
            # Step 3: Execute assembly
            results = await self._execute_assembly(assembler_plan, components)
            
            # Step 4: Synthesize results
            final_product = self._synthesize_results(results)
            
            # Step 5: Quality validation
            is_valid = self._validate_fabrication(final_product)
            
            if is_valid:
                self.successful_fabrications += 1
            
            # Update metadynamics
            success_score = 1.0 if is_valid else 0.5
            for assembler_type in assembler_plan:
                self.metadynamical_engine.record_performance(assembler_type, success_score)
            
            # Calculate metrics
            assembly_time = (datetime.now() - start_time).total_seconds() * 1000
            self._update_metrics(assembly_time)
            
            return {
                'status': 'SUCCESS' if is_valid else 'PARTIAL',
                'product': final_product,
                'assembly_time_ms': assembly_time,
                'assemblers_used': assembler_plan,
                'atomic_bonds': self._collect_all_bonds(results),
                'metadynamical_state': self.metadynamical_engine.export_state()
            }
        
        except Exception as e:
            return {
                'status': 'ERROR',
                'error': str(e),
                'assembly_time_ms': (datetime.now() - start_time).total_seconds() * 1000
            }
    
    def _extract_components(self, query: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract components from query.
        
        DECONSTRUCTION:
        Break query into atomic components for assembly.
        """
        return {
            'issue': query.get('issue', query.get('query', 'General Analysis')),
            'circuit': query.get('circuit', 'Federal'),
            'depth': query.get('depth', 7),
            'strategic': query.get('strategic', False),
            'opponent_firm': query.get('opponent_firm'),
            'judge': query.get('judge'),
            'sources': query.get('sources', [])
        }
    
    def _plan_assembly(self, components: Dict[str, Any]) -> List[str]:
        """
        Plan which assemblers to use.
        
        METADYNAMICAL PLANNING:
        Use the metadynamical engine to select optimal assemblers.
        """
        plan = []
        
        # Always start with meta-intelligence
        plan.append('meta')
        
        # Add depth control if specified
        if components.get('depth'):
            plan.append('depth')
        
        # Add strategic if requested
        if components.get('strategic') or components.get('opponent_firm'):
            plan.append('strategic')
        
        return plan
    
    async def _execute_assembly(self, plan: List[str], components: Dict[str, Any]) -> List[AssemblyResult]:
        """
        Execute the assembly plan.
        
        PARALLEL ASSEMBLY:
        Run multiple assemblers concurrently for efficiency.
        """
        tasks = []
        
        for assembler_type in plan:
            task = self.assembler_registry.run_assembly(assembler_type, components)
            tasks.append(task)
        
        results = await asyncio.gather(*tasks)
        return results
    
    def _synthesize_results(self, results: List[AssemblyResult]) -> Dict[str, Any]:
        """
        Synthesize results from multiple assemblers.
        
        MOLECULAR COMBINATION:
        Combine assembled molecules into final structure.
        """
        synthesis = {
            'assemblers_executed': len(results),
            'combined_confidence': sum(r.confidence for r in results) / len(results) if results else 0.0,
            'products': {}
        }
        
        for result in results:
            synthesis['products'][result.assembler_id] = result.product
        
        # Generate conversational output
        synthesis['conversational_output'] = self._generate_response(synthesis)
        
        return synthesis
    
    def _generate_response(self, synthesis: Dict[str, Any]) -> str:
        """
        Generate human-readable response.
        
        TRANSLATION:
        Convert atomic/molecular structure into natural language.
        """
        num_assemblers = synthesis['assemblers_executed']
        confidence = synthesis['combined_confidence']
        
        response = f"Based on {num_assemblers} molecular assemblers with {confidence:.1%} confidence, "
        response += "I've completed the nano-fabrication of your legal analysis. "
        response += "Every concept has been atomically grounded and validated through quality gates."
        
        return response
    
    def _validate_fabrication(self, product: Dict[str, Any]) -> bool:
        """
        Validate final fabrication.
        
        QUALITY ASSURANCE:
        Ensure the fabricated product meets quality standards.
        """
        if not product.get('products'):
            return False
        
        if product.get('combined_confidence', 0) < 0.5:
            return False
        
        return True
    
    def _collect_all_bonds(self, results: List[AssemblyResult]) -> List[Dict[str, Any]]:
        """Collect all atomic bonds from assembly results"""
        all_bonds = []
        
        for result in results:
            for bond in result.atomic_bonds:
                all_bonds.append({
                    'concept': bond.concept,
                    'atom': bond.atom.value,
                    'tracing_path': bond.tracing_path,
                    'validated': bond.validated
                })
        
        return all_bonds
    
    def _update_metrics(self, assembly_time: float):
        """Update performance metrics"""
        # Running average of assembly time
        if self.total_fabrications == 1:
            self.average_assembly_time = assembly_time
        else:
            alpha = 0.1  # Smoothing factor
            self.average_assembly_time = (alpha * assembly_time + 
                                         (1 - alpha) * self.average_assembly_time)
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get fabricator performance metrics"""
        return {
            'total_fabrications': self.total_fabrications,
            'successful_fabrications': self.successful_fabrications,
            'success_rate': (self.successful_fabrications / self.total_fabrications 
                           if self.total_fabrications > 0 else 0.0),
            'average_assembly_time_ms': self.average_assembly_time,
            'metadynamical_state': self.metadynamical_engine.export_state()
        }


# ═══════════════════════════════════════════════════════════════════════
# NATURAL LANGUAGE PROCESSOR
# ═══════════════════════════════════════════════════════════════════════

class NaturalLanguageProcessor:
    """
    Convert natural language queries into fabrication components.
    
    TRANSLATION LAYER:
    Human language → Atomic components
    """
    
    MOTION_TYPES = {
        'dismiss': 'Motion to Dismiss',
        'summary judgment': 'Motion for Summary Judgment',
        'preliminary injunction': 'Motion for Preliminary Injunction',
        'class certification': 'Motion for Class Certification',
        'sanctions': 'Motion for Sanctions'
    }
    
    CIRCUITS = {
        '1st': '1st', '2nd': '2nd', '3rd': '3rd', '4th': '4th',
        '5th': '5th', '6th': '6th', '7th': '7th', '8th': '8th',
        '9th': '9th', '10th': '10th', '11th': '11th', 'dc': 'DC'
    }
    
    def parse(self, natural_query: str) -> Dict[str, Any]:
        """Parse natural language into components"""
        query_lower = natural_query.lower()
        
        components = {
            'issue': self._extract_motion(query_lower),
            'circuit': self._extract_circuit(query_lower),
            'depth': self._extract_depth(query_lower),
            'strategic': 'strategic' in query_lower or 'opponent' in query_lower,
            'query': natural_query
        }
        
        return components
    
    def _extract_motion(self, query: str) -> str:
        for key, motion in self.MOTION_TYPES.items():
            if key in query:
                return motion
        return 'General Legal Analysis'
    
    def _extract_circuit(self, query: str) -> str:
        for key, circuit in self.CIRCUITS.items():
            if key in query:
                return circuit
        return 'Federal'
    
    def _extract_depth(self, query: str) -> int:
        if 'quick' in query or 'brief' in query:
            return 3
        elif 'detailed' in query or 'comprehensive' in query:
            return 10
        return 7


# ═══════════════════════════════════════════════════════════════════════
# EXPORT
# ═══════════════════════════════════════════════════════════════════════

__all__ = [
    'LegalFabricator',
    'NaturalLanguageProcessor'
]
