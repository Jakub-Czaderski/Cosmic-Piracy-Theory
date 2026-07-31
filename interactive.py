#!/usr/bin/env python3
import time
import math

def launch_ultimate_multiverse():
    print("=====================================================================")
    print("      ______   ______        _______  __    __   _______   ______ ")
    print("     /  ____| /  __  \\      |   ____||  |  |  | |   ____| /  ____|")
    print("    |  |     |  |  |  |     |  |__   |  |  |  | |  |__   |  |     ")
    print("    |  |     |  |  |  |     |   __|  |  |  |  | |   __|  |  |     ")
    print("    |  |____ |  `--'  |     |  |     |  `--'  | |  |____ |  |____ ")
    print("     \\______| \\______/      |__|      \\______/  |_______| \\______|")
    print("=====================================================================")
    print("          COSMIC PIRACY MULTIVERSE SANDBOX ENGINE - v5.4")
    print("          Dynamic Cold Spot Precursors & Causal Decoupling")
    print("=====================================================================\n")

    mode_input = input("-> Enable automated Scenario Recognition mode (0-12 & Addenda)? (y/n, Default=y): ")
    recognition_mode = False if mode_input.lower().strip() == 'n' else True

    try:
        max_aeons = input("\n-> Enter maximum number of iterations/aeons (Default=3): ")
        total_aeons = int(max_aeons) if max_aeons.strip() else 3
    except ValueError:
        total_aeons = 3

    current_aeon = 0
    observed_mass_baseline = 5000000
    aeon_generation_number = 0
    mother_ccc_postponed = False

    while current_aeon < total_aeons:
        print("\n" + "="*75)
        print(f"ITERATION {current_aeon} (GEN-ID: {aeon_generation_number}) - STOCHASTIC MATRIX ACTIVE")
        print("="*75)
        
        if mother_ccc_postponed:
            print("\n⏳ [GRAVITATIONAL LOCK] Mother aeon retaining drained rest-mass. CCC postponed.")
            time.sleep(0.4)
            mother_ccc_postponed = False

        if current_aeon == 0:
            photon_input = input("-> Trigger early quantum-geometric Photon Collapse in Aeon 0? (y/n, Default=y): ")
            photon_collapse = False if photon_input.lower().strip() == 'n' else True
        else:
            photon_collapse = True

        if not photon_collapse and current_aeon == 0:
            required_threshold = 0.0001
            example_prompt = "e.g., 13.8, infinity, 0.002"
        else:
            required_threshold = 0.001
            example_prompt = "e.g., 13.8, infinity, 0.002"

        while True:
            displacement_input = input(f"-> Enter Timeline Displacement / event value for Aeon {current_aeon} ({example_prompt}): ")
            if not displacement_input.strip():
                displacement_input = "13.8"
                
            is_infinity = displacement_input.lower() == "infinity"
            try:
                numeric_value = float(displacement_input)
                is_low_value = numeric_value < 1.0 if not is_infinity else False
                is_extremely_high = numeric_value >= 5000.0 if not is_infinity else False
            except ValueError:
                is_low_value = False
                is_extremely_high = False
                numeric_value = None
                
            break
            
        is_inter_bubble = False
        if current_aeon > 0 or photon_collapse:
            bubble_input = input("-> Does a parallel sibling bubble universe co-exist within this generation? (y/n, Default=n): ")
            is_inter_bubble = True if bubble_input.lower().strip() == 'y' else False

        if current_aeon == 0:
            if photon_collapse:
                num_black_holes = 2
                higgs_probability = 1.0
            else:
                num_black_holes = 0
                higgs_probability = 0.0
        else:
            if is_infinity:
                num_black_holes = 0
                higgs_probability = 0.0
            else:
                try:
                    bh_input = input(f"-> Enter number of non-singular core configurations (Black Holes) for this Aeon (Default=2): ")
                    num_black_holes = int(bh_input) if bh_input.strip() else 2
                except ValueError:
                    num_black_holes = 2
                    
                try:
                    higgs_input = input(f"-> Enter Higgs vacuum decay probability threshold (0.0 to 1.0, Default=0.85): ")
                    higgs_probability = float(higgs_input) if higgs_input.strip() else 0.85
                except ValueError:
                    higgs_probability = 0.85

        print(f"\n[TIMELINE] Target parameter set to: {displacement_input}")
        print(f"[METRIC] Trapping active with {num_black_holes} non-singular core configurations.")
        print(f"[HIGGS] Localized phase transition boundary initialized at p = {higgs_probability}")

        # Core Piracy & Metric Drainage Evaluation
        if is_low_value and num_black_holes > 0:
            print("\n[ALERT] Low temporal event parameter detected. Instant interception sequence active.")
            stolen_mass = 1500000 * num_black_holes
            observed_mass_baseline -= stolen_mass
            print(f"[CORE PIRACY] {stolen_mass:,} M_sun evacuated through topological perforation.")
        else:
            print("\n[STABILITY] Metric insulated. No active core-theft possible at this boundary.")

        # DYNAMISCHE COLD SPOT EVALUIERUNG NACH JAKUB CZADERSKI
        cold_spot_triggered = False
        cold_spot_cause = ""

        if current_aeon == 0 and not photon_collapse and is_low_value:
            cold_spot_triggered = True
            cold_spot_cause = "Scenario 1 Metric Drainage (Plasma evacuation into old-aeon giant void)"
            mother_ccc_postponed = True
        elif is_inter_bubble:
            cold_spot_triggered = True
            cold_spot_cause = "Addendum 1b Trans-Cosmic Collision (Shockwave signature between sibling bubble domains)"
        elif higgs_probability >= 0.5 and num_black_holes >= 2:
            cold_spot_triggered = True
            cold_spot_cause = "Pathway 3 Higgs Conformal Phase Transition (Thermodynamic vacuum anomaly void)"

        if higgs_probability >= 0.5:
            print("[PATHWAY 3] Higgs conformal phase transition ignited. Radiative shockwave expanding.")
        else:
            print("[SUPPRESSION] Thermal barrier stable. Higgs expectation value remains at baseline.")

        # AUTOMATISCHE SZENARIEN-ERKENNUNG
        if recognition_mode:
            print("\n🔍 [RECOGNITION] Analyzing multi-dimensional boundary metrics...")
            time.sleep(0.2)
            
            detected_scenario = "Scenario X (Hybrid Pathway)"
            if current_aeon == 0:
                if not photon_collapse and is_low_value:
                    detected_scenario = "Scenario 1 (The Primeval Topological Deflation Interface)"
                elif photon_collapse and is_infinity:
                    detected_scenario = "Scenario 0 (The Global CPT Crossover Baseline)"
                elif photon_collapse and not is_low_value:
                    detected_scenario = "Scenario 2 (Solitary/Isotropic Hierarchical Accretion)"
            else:
                if is_infinity:
                    detected_scenario = "Scenario 10 (Massless Conformal Cyclic Reset)" if num_black_holes == 0 else "Scenario 11 (Sterile Trap)"
                elif is_low_value:
                    detected_scenario = "Scenario 3b (Conformal Protection)" if num_black_holes == 1 else "Scenario 7 (Multi-Core Cluster)"
                else:
                    if num_black_holes == 1 and higgs_probability >= 0.5:
                        detected_scenario = "Scenario 5 (Solitary Anchor with Active Higgs Shockwave)"
                    elif num_black_holes >= 2 and higgs_probability >= 0.5:
                        detected_scenario = "Scenario 9 (Multi-Core Cluster with Radiative Perimeter Walls)"
                    elif num_black_holes >= 2 and higgs_probability < 0.5:
                        detected_scenario = "Scenario 6 (Multi-Core Cluster via Pure Relativistic Slingshot)"

            print(f"🎯 [MATCH] Classified Blueprint: {detected_scenario}")
            
            # Ausgabe des entkoppelten Cold Spots
            if cold_spot_triggered:
                print(f"❄️ [CMB COLD SPOT DETECTED] An anomalous 5-degree Cold Spot is verified!")
                print(f"                            Origin Matrix: {cold_spot_cause}")
            
            if is_inter_bubble:
                print(f"📚 [ADDENDUM 1b MATCH] Horizontal intersection active within Gen-ID: {aeon_generation_number}.")
            elif is_extremely_high and not mother_ccc_postponed:
                print("📚 [ADDENDUM 1a MATCH] Trans-Aeon Boundary Intersection active (Mother-to-Child coupling).")
            elif mother_ccc_postponed:
                print("📚 [ADDENDUM 1a CORRECTION] Reverse Metric Drainage active. CCC scaling suspended!")

        print(f"\n[EVOLUTION] Aeon {current_aeon} terminates via Event 3.")
        aeon_generation_number += 1
        current_aeon += 1
        observed_mass_baseline = int((observed_mass_baseline + 5000000) * 1.5)
        time.sleep(0.4)

    print("\n=====================================================================")
    print(" SANDBOX RUN COMPLETE: DYNAMIC PRECURSORS SECURED WITHOUT RE-LOCKING")
    print("=====================================================================\n")

if __name__ == "__main__":
    launch_ultimate_multiverse()
