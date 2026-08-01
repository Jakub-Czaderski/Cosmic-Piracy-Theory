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
    print("          COSMIC PIRACY MULTIVERSE STATE ENGINE - v9.2")
    print("          Massless Infinity Limits & Precise Time-First Symmetries")
    print("=====================================================================\n")

    mode_input = input("-> Enable automated Scenario Recognition mode (0-12 & Addenda)? (y/n, Default=y): ")
    recognition_mode = False if mode_input.lower().strip() == 'n' else True

    try:
        max_aeons = input("\n-> Enter maximum number of iterations/aeons (Default=4): ")
        total_aeons = int(max_aeons) if max_aeons.strip() else 4
    except ValueError:
        total_aeons = 4

    current_aeon = 0
    aeon_generation_number = 0
    observed_mass_baseline = 5000000
    
    pathway_2_triggered_in_previous = False
    cold_spot_active_from_previous = False
    inherited_baryon_excess = False
    
    inherited_umnc_count = 0
    inherited_smnc_count = 0

    # ===========================================================================
    # ISOLATED EXPERIMENTAL NODE FOR AEON 0 (TIME-FIRST CRITERIA)
    # ===========================================================================
    print("\n" + "="*75)
    print("ITERATION 0 (GEN-ID: 0) - INITIAL UR-GENESIS BOUNDARY LAYER")
    print("="*75)
    
    photon_input = input("-> Trigger early quantum-geometric Photon Collapse in Aeon 0? (y/n, Default=y): ")
    photon_collapse = False if photon_input.lower().strip() == 'n' else True

    # 1. TIME EVOLUTION INPUT COLLECTED FIRST
    while True:
        example_aeon0 = "e.g., 13.8, infinity" if photon_collapse else "e.g., infinity, 0.002"
        displacement_input = input(f"-> Enter Timeline Displacement value for Aeon 0 ({example_aeon0}): ")
        if not displacement_input.strip():
            displacement_input = "13.8"
            
        is_infinity = displacement_input.lower() == "infinity"
        try:
            numeric_value = float(displacement_input)
            is_low_value = numeric_value < 1.0 if not is_infinity else False
        except ValueError:
            is_low_value = False
            numeric_value = None

        if photon_collapse and is_low_value:
            print("\n[REJECTION] Core Accretion Lag: Primordial seeds require a minimum operational")
            print("            timescale (> 1.0 Gyr) to expand metric horizons and accumulate spin.")
            print("            Re-enter value matching physical accretion predictions.\n")
            continue
        if not photon_collapse and not is_infinity and not is_low_value:
            print("\n[REJECTION] Sterile Horizon: Empty fields without a geometric Photon Collapse")
            print("            cannot sustain prolonged expanding mass-metrics. Choose 'infinity' or '0.002'.\n")
            continue
        break

    # 2. DYNAMIC NUCLEATION BASED ENTIRELY ON SELECTED DISPLACEMENT
    if is_infinity or not photon_collapse:
        if is_infinity:
            print("[NOTICE] Future infinity boundary reached. All localized cores completely evaporated.")
        else:
            print("[NOTICE] Massless radiation background locked. Core counts forced to 0.")
        umnc_aeon0, smnc_aeon0, imnc_aeon0, hmnc_aeon0 = 0, 0, 0, 0
        higgs_probability_aeon0 = 1.0 if (is_infinity and input("-> Insert intermediate Higgs vacuum decay during this infinite transition? (y/n, Default=n): ").lower().strip() == 'y') else 0.0
    else:
        higgs_input = input("-> Insert early instant Higgs vacuum decay for Aeon 0 initialization? (y/n, Default=y): ")
        higgs_probability_aeon0 = 1.0 if higgs_input.lower().strip() != 'n' else 0.0
        umnc_aeon0 = 2
        smnc_aeon0 = 4
        time_factor = numeric_value if numeric_value else 13.8
        imnc_aeon0 = max(1, int(time_factor * 0.86))
        hmnc_aeon0 = 0
        print(f"[NUCLEATION] Primeval seeding verified via timescale ({time_factor} Gyr):")
        print(f"             >> {umnc_aeon0} UMNCs | {smnc_aeon0} SMNCs | {imnc_aeon0} IMNCs detected.")

    is_inter_bubble = False
    if not photon_collapse and is_low_value:
        bubble_input = input("-> Does a parallel sibling bubble universe co-exist via vacuum perforation? (y/n, Default=n): ")
        is_inter_bubble = True if bubble_input.lower().strip() == 'y' else False

    print(f"\n[TIMELINE] Target parameter locked at: {displacement_input}")
    if not photon_collapse and is_low_value:
        print("[ALERT] Micro-delay event matching unseeded radiation. Scenario 1 triggered!")
        cold_spot_active_from_previous = True

    if recognition_mode:
        print("\n[RECOGNITION] Evaluating Aeon 0 custom node matrix...")
        detected_scenario = "Scenario X (Hybrid Pathway)"
        if not photon_collapse and is_low_value:
            detected_scenario = "Scenario 1 (The Primeval Topological Deflation Interface)"
        elif photon_collapse and is_infinity:
            detected_scenario = "Scenario 0 (The Global CPT Crossover Baseline)"
        elif photon_collapse and not is_low_value:
            detected_scenario = "Scenario 2 (Solitary/Isotropic Hierarchical Accretion)"
        elif not photon_collapse and is_infinity:
            detected_scenario = "Scenario 12 (Sterile Reset Loop)" if higgs_probability_aeon0 >= 0.5 else "Scenario 10 (Initial Conformal Baseline)"
        print(f"[MATCH] Classified Blueprint: {detected_scenario}")

    print("\n[EVOLUTION] Aeon 0 terminates via Conformal Crossover.")
    
    trigger_infinite_genesis_loop = (not photon_collapse and is_infinity and higgs_probability_aeon0 >= 0.5)
    if trigger_infinite_genesis_loop:
        print("\n[INFINITE LOOP] Sterile vacuum reset completed. Aeon 0 loop hard locked.\n")
        inherited_baryon_excess = True
        current_aeon = 0
    else:
        current_aeon = 1
        observed_mass_baseline = int((observed_mass_baseline + 5000000) * 1.5)
        if is_low_value and photon_collapse:
            pathway_2_triggered_in_previous = True
            inherited_umnc_count = umnc_aeon0
            inherited_smnc_count = smnc_aeon0
    
    aeon_generation_number += 1
    time.sleep(0.4)
    # ===========================================================================
    # CONTINUOUS CASCADE LOOP FOR MULTI-GENERATIONAL ERAS (AEON 1+)
    # ===========================================================================
    while current_aeon < total_aeons:
        print("\n" + "="*75)
        print(f"ITERATION {current_aeon} (GEN-ID: {aeon_generation_number}) - MASS CLASSIFICATION MATRIX")
        print("="*75)
        
        # 1. SCENARIO 1 REVERSE METRIC DRAINAGE BOUNDARY LOCK
        if cold_spot_active_from_previous:
            print("\n[GRAVITATIONAL LOCK] Reverse Metric Drainage active from previous Scenario 1.")
            print("   The parent universe requires finite timelines to stabilize expansion parameters.")
            while True:
                drainage_input = input("   -> Enter finite stabilization displacement (in Gyr, e.g., 13.8): ")
                try:
                    drainage_val = float(drainage_input)
                    if drainage_val <= 0:
                        print("      [ERROR] Value must be positive to overcome gravitational lock. Try again.")
                        continue
                    print(f"   [SUCCESS] Boundary stabilized at +{drainage_val} Gyr limit. Releasing lock.")
                    break
                except ValueError:
                    print("      [ERROR] Invalid numerical value. Try again.")
            cold_spot_active_from_previous = False

        # 2. TIMELINE INPUT COLLECTED FIRST (THE STRATEGIC CONTROLLER FOR AEON 1+)
        while True:
            displacement_input = input(f"-> Enter Timeline Displacement value for Aeon {current_aeon} (e.g., 13.8, infinity, 0.002): ")
            if not displacement_input.strip():
                displacement_input = "13.8"
                
            is_infinity = displacement_input.lower() == "infinity"
            try:
                numeric_value = float(displacement_input)
                is_low_value = numeric_value < 1.0 if not is_infinity else False
            except ValueError:
                is_low_value = False
                numeric_value = None
            break

        # 3. SEED MATRIX EVALUATION: CONDITIONAL ON CHOSEN DISPLACEMENT BOUNDARY
        if is_infinity:
            print("[NOTICE] Future infinity boundary selected. All active core structures completely evaporated.")
            umnc_count, smnc_count = 0, 0
        else:
            if pathway_2_triggered_in_previous:
                print(f"\n[INHERITANCE] Ancestral Pathway 2 detected. Importing structural remnants:")
                umnc_count = inherited_umnc_count
                smnc_count = inherited_smnc_count
                print(f"   >> Anchored Ancestral Stems: {umnc_count} UMNCs, {smnc_count} SMNCs tracked.")
                pathway_2_triggered_in_previous = False
            elif inherited_baryon_excess:
                print("\n[INHERITANCE] High-density baryon potential detected from Scenario 12 loop decay.")
                umnc_count, smnc_count = 2, 4
                inherited_baryon_excess = False
            else:
                # Normal manual seed prompt for intermediate mass-bearing timelines
                try:
                    umnc_in = input(f"-> Enter active UMNC count for Aeon {current_aeon} (Default=0): ")
                    umnc_count = int(umnc_in) if umnc_in.strip() else 0
                    smnc_in = input(f"-> Enter active SMNC count for Aeon {current_aeon} (Default=2): ")
                    smnc_count = int(smnc_in) if smnc_in.strip() else 2
                except ValueError:
                    umnc_count, smnc_count = 0, 2

            # REJECTION GUARD AGAINST MASSLESS INSTANT RUPTURES
            if umnc_count == 0 and smnc_count == 0 and is_low_value:
                print(f"\n[REJECTION] Impossible Boundary: A micro-delay rupture threshold (< 1.0 Gyr)")
                print("            requires pre-existing metric anomalies to apply conformal shear stress.")
                print("            Resetting configuration layer. Re-evaluate metrics.\n")
                continue

        # 4. CROSS-OVER SIBLING BUBBLE ANCHORING FILTER
        is_inter_bubble = False
        if is_low_value and (umnc_count > 0 or smnc_count > 0) and not is_infinity:
            bubble_input = input("-> Does a parallel sibling bubble universe co-exist within this generation? (y/n, Default=n): ")
            is_inter_bubble = True if bubble_input.lower().strip() == 'y' else False

        # 5. HIGGS TRANSITION PROFILE
        if is_infinity:
            sfr_rate = 0.0
            higgs_loop_input = input("-> Insert intermediate Higgs vacuum decay during transition? (y/n, Default=n): ")
            higgs_probability = 1.0 if higgs_loop_input.lower().strip() == 'y' else 0.0
        else:
            try:
                sfr_input = input("-> Enter Star Formation Rate / acceleration modifier (0.1 to 5.0, Default=1.0): ")
                sfr_rate = float(sfr_input) if sfr_input.strip() else 1.0
                
                higgs_input = input("-> Enter Higgs vacuum decay probability threshold (0.0 to 1.0, Default=0.85): ")
                higgs_probability = float(higgs_input) if higgs_input.strip() else 0.85
            except ValueError:
                sfr_rate = 1.0
                higgs_probability = 0.85
        # 6. DYNAMIC CORE ACCRETION AND CLASS SPECIFICATION (IMNC & HMNC LAWS)
        if is_infinity:
            imnc_count, hmnc_count = 0, 0
            max_possible_imnc = 0
            max_possible_hmnc = 0
        else:
            time_factor = numeric_value if numeric_value else 13.8
            higgs_boost = 2.5 if higgs_probability >= 0.5 else 1.0
            
            # Calculate absolute maximum limits based on chronological age and SFR acceleration
            max_possible_imnc = max(1, int(time_factor * 8.5 * sfr_rate * higgs_boost))
            max_possible_hmnc = max(0, int((time_factor - 1.0) * 1.2 * sfr_rate * higgs_boost)) if time_factor > 1.0 else 0

            print(f"\n[DYNAMICS] Local conditions compute maximum bounds for stellar-process cores:")
            print(f"           >> Upper limit for IMNCs (Intermediate Mass): {max_possible_imnc:,}")
            print(f"           >> Upper limit for HMNCs (Hypermassive):     {max_possible_hmnc:,}")

            try:
                imnc_in = input(f"-> Enter active IMNC count (Max={max_possible_imnc}, Default=12): ")
                imnc_count = int(imnc_in) if imnc_in.strip() else 12
                if imnc_count > max_possible_imnc:
                    print(f"           [NOTICE] Capping IMNC count at physical upper bound limit ({max_possible_imnc}).")
                    imnc_count = max_possible_imnc
            except ValueError:
                imnc_count = 12

            try:
                if max_possible_hmnc > 0:
                    hmnc_in = input(f"-> Enter active HMNC count (Max={max_possible_hmnc}, Default=1): ")
                    hmnc_count = int(hmnc_in) if hmnc_in.strip() else 1
                    if hmnc_count > max_possible_hmnc:
                        print(f"           [NOTICE] Capping HMNC count at physical upper bound limit ({max_possible_hmnc}).")
                        hmnc_count = max_possible_hmnc
                else:
                    print("           [NOTICE] Timeline too short for HMNC generation. Locked at 0.")
                    hmnc_count = 0
            except ValueError:
                hmnc_count = 0

        # Compute total core network density for metric verification
        total_active_cores = umnc_count + smnc_count + imnc_count + hmnc_count

        print(f"\n[TIMELINE] Target parameter successfully locked at: {displacement_input}")
        print(f"[METRIC] Active grid processing total of {total_active_cores} cores.")
        print(f"         [DISTRIBUTION] {umnc_count} UMNC | {smnc_count} SMNC | {imnc_count} IMNC | {hmnc_count} HMNC")

        # PARALLEL BRANCH DETECTOR FOR NEXT GENERATION
        if is_low_value and total_active_cores >= 1 and not is_infinity:
            print("\n[ALERT] High tensile shear stress verified. Pathway 2 triggered!")
            pathway_2_triggered_in_previous = True
            inherited_umnc_count = umnc_count + 2 if umnc_count > 0 else 2
            inherited_smnc_count = smnc_count + imnc_count
            print(f"        [CAUSALITY] Inherited seeds locked for Generation {aeon_generation_number + 1}.")

        if higgs_probability >= 0.5 and not is_infinity:
            print("[PATHWAY 3] Higgs conformal phase transition ignited. Radiative shockwave expanding.")

        # AUTOMATED BLUEPRINT RECOGNITION MATRIX (SCENARIOS 3 TO 12 MAPPING)
        if recognition_mode:
            print("\n[RECOGNITION] Evaluating tracked multi-aeon metrics against blueprint matrix...")
            time.sleep(0.1)
            
            detected_scenario = "Scenario X (Hybrid Pathway)"
            if is_infinity:
                if higgs_probability >= 0.5:
                    detected_scenario = "Scenario 12 (Sterile Dynamic Vacuum Phase / Infinite Reset Loop)"
                else:
                    detected_scenario = "Scenario 10 (Massless Conformal Cyclic Reset)"
            elif is_low_value:
                detected_scenario = "Scenario 3b (Conformal Protection)" if total_active_cores == 1 else "Scenario 7 (Multi-Core Cluster)"
            else:
                if total_active_cores == 1 and higgs_probability >= 0.5:
                    detected_scenario = "Scenario 5 (Solitary Anchor with Active Higgs Shockwave)"
                elif total_active_cores >= 2 and higgs_probability >= 0.5:
                    detected_scenario = "Scenario 9 (Multi-Core Cluster with Radiative Perimeter Walls)"
                elif total_active_cores >= 2 and higgs_probability < 0.5:
                    detected_scenario = "Scenario 6 (Multi-Core Cluster via Pure Relativistic Slingshot)"

            print(f"[MATCH] Classified Blueprint: {detected_scenario}")
            
            if is_inter_bubble:
                print(f"[CMB COLD SPOT DETECTED] An anomalous 5-degree Cold Spot is verified!")
                print("                            Origin Matrix: Addendum 1b horizontal collision between sibling domains.")
                print(f"[ADDENDUM 1b MATCH] Sibling bubble collision verified within Gen-ID: {aeon_generation_number}.")

        # PROGRESSION AND RESET CORRECTION MATRIX
        if is_infinity:
            print(f"\n[EVOLUTION] Aeon {current_aeon} terminates via Scenario 10.")
            if higgs_probability >= 0.5:
                print("\n[INFINITE LOOP] Conformal shift completed. Spectral baryon asymmetry injected!")
                print("                   The subsequent era inherits a permanent matter excess baseline.")
                print("                   Aeon 0 repeats exactly with high-density seeds! Reloading metric...\n")
                time.sleep(1.0)
                inherited_baryon_excess = True
                current_aeon = 0  
            else:
                current_aeon += 1
        else:
            print(f"\n[EVOLUTION] Aeon {current_aeon} terminates via Conformal Crossover.")
            current_aeon += 1
            observed_mass_baseline = int((observed_mass_baseline + 5000000) * 1.5)
            
        aeon_generation_number += 1
        time.sleep(0.4)

    print("\n=====================================================================")
    print(" STATE ENGINE RUN COMPLETE: ALL SCENARIOS AND KAUSAL-PATHS VALIDATED")
    print("=====================================================================\n")

if __name__ == "__main__":
    launch_ultimate_multiverse()
