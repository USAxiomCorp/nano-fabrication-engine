#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════
NANO-FABRICATION ENGINE - WEB APPLICATION
Atomic Assembly for Legal Intelligence
═══════════════════════════════════════════════════════════════════════
"""

from flask import Flask, request, jsonify, render_template, session
from flask_cors import CORS
import asyncio
import os
import secrets
from datetime import datetime

import sys
sys.path.append('..')

from legal.fabricator import LegalFabricator, NaturalLanguageProcessor

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', secrets.token_hex(32))
CORS(app)

# Initialize fabricator
fabricator = None
nlp = NaturalLanguageProcessor()

def initialize_fabricator():
    """Initialize the nano-fabrication engine"""
    global fabricator
    
    try:
        print("🔬 Initializing Nano-Fabrication Engine...")
        fabricator = LegalFabricator()
        print("✅ Nano-Fabrication Engine online")
        print("⚛️  Atomic Layer: Active")
        print("🧬 Molecular Assemblers: Ready")
        print("📊 Metadynamical Engine: Optimizing")
        return True
    except Exception as e:
        print(f"❌ Initialization failed: {e}")
        import traceback
        traceback.print_exc()
        return False


# ═══════════════════════════════════════════════════════════════════════
# WEB ROUTES
# ═══════════════════════════════════════════════════════════════════════

@app.route('/')
def home():
    """Serve the fabricator interface"""
    return render_template('fabricator.html')


@app.route('/api/fabricate', methods=['POST'])
def fabricate():
    """
    Main fabrication endpoint.
    
    Accepts natural language legal queries and returns
    atomically-assembled legal analysis.
    """
    if fabricator is None:
        return jsonify({
            'error': 'Fabricator not initialized',
            'response': 'The nano-fabrication engine is offline. Please check server logs.'
        }), 503
    
    try:
        data = request.get_json()
        message = data.get('message', '')
        
        if not message:
            return jsonify({'error': 'Message required'}), 400
        
        # Session management
        if 'session_id' not in session:
            session['session_id'] = secrets.token_hex(16)
        
        # Parse natural language to components
        components = nlp.parse(message)
        
        # Execute fabrication
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(fabricator.fabricate(components))
        loop.close()
        
        # Format response
        response = {
            'response': result.get('product', {}).get('conversational_output', 'Fabrication complete.'),
            'metadata': {
                'assemblers_used': result.get('assemblers_used', []),
                'assembly_time_ms': result.get('assembly_time_ms', 0),
                'confidence': result.get('product', {}).get('combined_confidence', 0),
                'atomic_bonds': len(result.get('atomic_bonds', [])),
                'timestamp': datetime.now().isoformat()
            },
            'full_result': result,
            'status': result.get('status', 'SUCCESS')
        }
        
        return jsonify(response)
    
    except Exception as e:
        print(f"Fabrication error: {e}")
        import traceback
        traceback.print_exc()
        
        return jsonify({
            'error': str(e),
            'status': 'ERROR',
            'response': 'Fabrication error. Please try again.'
        }), 500


@app.route('/health')
def health():
    """Health check"""
    return jsonify({
        'status': 'healthy',
        'fabricator_online': fabricator is not None,
        'system': 'Nano-Fabrication Engine v1.0'
    }), 200


@app.route('/metrics')
def metrics():
    """Get fabricator metrics"""
    if fabricator is None:
        return jsonify({'error': 'Fabricator offline'}), 503
    
    return jsonify(fabricator.get_metrics())


@app.route('/api/capabilities')
def capabilities():
    """System capabilities"""
    return jsonify({
        'system': 'Nano-Fabrication Engine',
        'version': '1.0',
        'achievement_value': '$600M per milestone',
        'status': fabricator is not None,
        'capabilities': {
            'atomic_foundation': ['A0:Existence', 'A1:Distinction', 'A2:Pattern', 
                                'A3:Recursion', 'A4:Consistency', 'A5:Composition'],
            'molecular_assemblers': ['Meta-Intelligence', 'Depth-Control', 'Strategic'],
            'metadynamical_optimization': True,
            'quality_validation': '100% error prevention (M8 gates)',
            'atomic_tracing': 'Every concept grounded to axioms'
        },
        'domains': ['Legal Reasoning', 'Federal Civil Motions'],
        'features': [
            'Atomic precision assembly',
            'Self-optimizing pathways',
            'Zero-defect fabrication',
            'Transparent reasoning',
            'Metadynamical learning'
        ]
    })


# ═══════════════════════════════════════════════════════════════════════
# ERROR HANDLERS
# ═══════════════════════════════════════════════════════════════════════

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': 'Internal server error'}), 500


# ═══════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print("═" * 80)
    print("🔬 NANO-FABRICATION ENGINE")
    print("   Molecular Assembly for Legal Superintelligence")
    print("═" * 80)
    
    if initialize_fabricator():
        print("\n✅ All systems operational")
        print("🌐 Web interface: http://localhost:PORT/")
        print("⚛️  Building arguments atom-by-atom...")
    else:
        print("\n⚠️  Fabricator initialization failed")
    
    port = int(os.getenv('PORT', 10000))
    print(f"\n🚀 Starting on port {port}")
    print("═" * 80)
    app.run(host='0.0.0.0', port=port, debug=False)
