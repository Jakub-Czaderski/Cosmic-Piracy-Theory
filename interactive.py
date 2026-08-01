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
    print("          COSMIC PIRACY MULTIVERSE STATE KERNEL - v11.3")
    print("          Mass-Dependent Scenario 1 Suppression & Invariant Guards")
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

    while current_aeon < total_aeons:
        
        # ===========================================================================
        # ISOLATED NODE FOR AEON 0 INITIALIZATION (STRICT ENGLISH STATE ENGINE)
        # ===========================================================================
        if current_aeon == 0:
            print("\n" + "="*75)
            print(f"ITERATION 0 (GEN-ID: {aeon_generation_number}) - INITIAL UR-GENESIS BOUNDARY LAYER")
            print("="*75)
            
            if cold_spot_active_from_previous:
                print("\n⏳ [GRAVITATIONAL LOCK] Reverse Metric Drainage active from Scenario 1 plasma backflow.")
                print("   The parent cosmos requires stabilization before Ur-Genesis can re-initialize.")
                while True:
                    drainage_input = input("   -> Enter finite stabilization displacement (in Gyr, e.g., 13.8): ")
                    try:
                        drainage_val = float(drainage_input)
                        if drainage_val <= 0:
                            print("      [ERROR] Value must be positive. Try again.")
                            continue
                        print(f"   [SUCCESS] Matrix stabilized at +{drainage_val} Gyr limit. Releasing lock.")
                        break
                    except ValueError:
                        print("      [ERROR] Invalid numerical value.")
                cold_spot_active_from_previous = False

            photon_input = input("-> Trigger early quantum-geometric Photon Collapse in Aeon 0? (y/n, Default=y): ")
            photon_collapse = False if photon_input.lower().strip() == 'n' else True

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

                if photon_collapse and is_low_value and numeric_value != 0.0:
                    print("\n[REJECTION] Core Accretion Lag: Primordial seeds require minimum operational timescales.\n")
                    continue
                break

            if photon_collapse and not is_infinity:
                higgs_input = input("-> Insert early instant Higgs vacuum decay for Aeon 0 initialization? (y/n, Default=y): ")
                higgs_probability_aeon0 = 1.0 if higgs_input.lower().strip() != 'n' else 0.0
            else:
                higgs_probability_aeon0 = 1.0 if (is_infinity and input("-> Insert intermediate Higgs vacuum decay during transition? (y/n, Default=n): ").lower().strip() == 'y') else 0.0

            if is_infinity or not photon_collapse:
                if is_infinity and photon_collapse:
                    print("[NOTICE] Future infinity boundary reached. All localized cores completely evaporated.")
                elif not photon_collapse:
                    print("[NOTICE] Pure massless radiation background locked. Core counts forced to 0.")
                umnc_aeon0, smnc_aeon0, imnc_aeon0, hmnc_aeon0 = 0, 0, 0, 0
            else:
                time_factor = numeric_value if numeric_value is not None else 13.8
                higgs_boost = 2.5 if higgs_probability_aeon0 >= 0.5 else 1.0
                max_aeon0_umnc = max(1, int(time_factor * 0.15 * higgs_boost))
                max_aeon0_smnc = max(2, int(time_factor * 0.35 * higgs_boost))
                max_aeon0_imnc = max(5, int(time_factor * 0.85 * higgs_boost))
                max_aeon0_hmnc = max(0, int((time_factor - 1.0) * 1.2 * higgs_boost)) if time_factor > 1.0 else 0
                
                print(f"\n[NUCLEATION] Primeval growth potential computed via timescale ({time_factor} Gyr):")
                try:
                    umnc_aeon0 = int(input(f"-> Enter active UMNC count (Max={max_aeon0_umnc}, Default=2): ") or 2)
                    smnc_aeon0 = int(input(f"-> Enter active SMNC count (Max={max_aeon0_smnc}, Default=4): ") or 4)
                    imnc_aeon0 = int(input(f"-> Enter active IMNC count (Max={max_aeon0_imnc}, Default=12): ") or 12)
                    hmnc_aeon0 = int(input(f"-> Enter active HMNC count (Max={max_aeon0_hmnc}, Default=0): ") or 0) if max_aeon0_hmnc > 0 else 0
                except ValueError:
                    umnc_aeon0, smnc_aeon0, imnc_aeon0, hmnc_aeon0 = 2, 4, 12, 0

            total_cores_aeon0 = umnc_aeon0 + smnc_aeon0 + imnc_aeon0 + hmnc_aeon0
            is_inter_bubble = False
            if not photon_collapse and is_low_value:
                is_inter_bubble = input("-> Does a parallel sibling bubble universe co-exist via vacuum perforation? (y/n, Default=n): ").lower().strip() == 'y'

            print(f"\n[TIMELINE] Target parameter locked at: {displacement_input}")
            print(f"[METRIC] Active grid processing total of {total_cores_aeon0} cores.")
            
            if photon_collapse and is_low_value:
                print("[ALERT] Micro-delay event matching active mass seeds. Scenario 1 triggered!")
                cold_spot_active_from_previous = True
            elif not photon_collapse and is_low_value:
                print("[NOTICE] Micro-delay timeline on an unseeded background. Sterile vacuum collapse.")

            if recognition_mode:
                print("\n[RECOGNITION] Evaluating Aeon 0 custom node matrix...")
                detected_scenario = "Scenario X (Hybrid Pathway)"
                if photon_collapse and is_low_value:
                    detected_scenario = "Scenario 1 (The Primeval Topological Deflation Interface)"
                elif not photon_collapse and is_low_value:
                    detected_scenario = "Scenario 10 (Massless Reset Baseline / Sterile Pocket)"
                elif photon_collapse and not is_low_value:
                    detected_scenario = "Scenario 0 (The Global CPT Crossover Baseline)"
                print(f"[MATCH] Classified Blueprint: {detected_scenario}")

            print("\n[EVOLUTION] Aeon 0 terminates via Conformal Crossover.")
            
            if photon_collapse and is_low_value:
                print("\n[RE-ROUTING] Conformal progression denied due to mass drain backflow. Re-executing Aeon 0...\n")
                current_aeon = 0  
            else:
                trigger_infinite_genesis_loop = (not photon_collapse and is_infinity and higgs_probability_aeon0 >= 0.5)
                if trigger_infinite_genesis_loop:
                    inherited_baryon_excess = True
                    current_aeon = 0
                else:
                    current_aeon = 1
                    observed_mass_baseline = int((observed_mass_baseline + 5000000) * 1.5)
                    if photon_collapse and is_low_value:
                        pathway_2_triggered_in_previous = True
                        inherited_umnc_count = umnc_aeon0 + 2
                        inherited_smnc_count = smnc_aeon0 + imnc_aeon0 + hmnc_aeon0
            
            aeon_generation_number += 1
            time.sleep(0.1)
            continue 
    # ===========================================================================
    # CONTINUOUS CASCADE LOOP FOR MULTI-GENERATIONAL ERAS (AEON 1+)
    # ===========================================================================
    while current_aeon < total_aeons:
        print("\n" + "="*75)
        print(f"ITERATION {current_aeon} (GEN-ID: {aeon_generation_number}) - THERMODYNAMIC MATRIX")
        print("="*75)
        
        if cold_spot_active_from_previous:
            print("\n[GRAVITATIONAL LOCK] Reverse Metric Drainage active from previous Scenario 1.")
            while True:
                drainage_input = input("   -> Enter finite stabilization displacement (in Gyr, e.g., 13.8): ")
                try:
                    drainage_val = float(drainage_input)
                    if drainage_val <= 0:
                        print("      [ERROR] Value must be positive. Try again.")
                        continue
                    print(f"   [SUCCESS] Boundary stabilized at +{drainage_val} Gyr limit. Releasing lock.")
                    break
                except ValueError:
                    print("      [ERROR] Invalid numerical value.")
            cold_spot_active_from_previous = False

        # 1. TIMELINE INPUT COLLECTED DIRECTLY AT POSITION 1
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

        # 2. TIME-GATED SEED EVALUATION WITH STABLY PRESERVED ANCESTRAL LOCKS
        if is_infinity:
            umnc_count, smnc_count, imnc_count, hmnc_count = 0, 0, 0, 0
            higgs_loop_input = input("-> Insert intermediate Higgs vacuum decay during transition? (y/n, Default=n): ")
            higgs_probability = 1.0 if higgs_loop_input.lower().strip() == 'y' else 0.0
            sfr_rate = 0.0
            pathway_2_triggered_in_previous = False
            relativistic_leap_active = False
        else:
            if pathway_2_triggered_in_previous and is_low_value:
                print(f"\n[INHERITANCE] Ancestral Pathway 2 active. Processing high-tensile shear mutation:")
                umnc_count = inherited_umnc_count
                smnc_count = inherited_smnc_count
                print(f"   >> Anchored Ancestral Stems: {umnc_count} UMNCs structurally locked.")
                print(f"   >> Conformal Compression: Sibling IMNCs/HMNCs forced into Supermassive matrix ({smnc_count} SMNCs).")
                print("   [NOTICE] Manual prompts disabled: Saturated runtime metrics permit zero new core genesis.")
                
                if numeric_value != 0.0 and (umnc_count + smnc_count >= 150) and current_aeon == 1:
                    print(f"\n[RELATIVISTIC SCHOCKWAVE] Extreme core density detected at micro-delay threshold!")
                    print("                          Cores are accelerated to 0.85 c via LQG slingshot.")
                    print("                          Lorentz time dilation factor gamma ~ 2.0 active.")
                    max_slingshot_cores = umnc_count + smnc_count
                    try:
                        slingshot_in = input(f"-> Enter number of active cores caught in the 0.85 c time leap (Max={max_slingshot_cores}, Default={max_slingshot_cores}): ")
                        active_slingshot_cores = int(slingshot_in) if slingshot_in.strip() else max_slingshot_cores
                        if active_slingshot_cores > max_slingshot_cores:
                            active_slingshot_cores = max_slingshot_cores
                    except ValueError:
                        active_slingshot_cores = max_slingshot_cores
                    
                    print(f"                          [LEAP CONTROL] {active_slingshot_cores} cores successfully project into Generation 3.")
                    inherited_umnc_count = min(umnc_count + 2, active_slingshot_cores)
                    inherited_smnc_count = max(0, active_slingshot_cores - inherited_umnc_count)
                    pathway_2_triggered_in_previous = True
                    relativistic_leap_active = True
                elif numeric_value == 0.0:
                    print("\n[TRUE SPACE-TIME RUPTURE] Instantaneous topological shearing executed at exactly 0 years.")
                    print("                          Cores remain spatially stationary. Zero Lorentz dilation triggered.")
                    print("                          [CAUSALITY] Standard sequential transition active into Iteration 2.")
                    inherited_umnc_count = umnc_count + 2
                    inherited_smnc_count = smnc_count
                    pathway_2_triggered_in_previous = True
                    relativistic_leap_active = False
                else:
                    if not is_low_value:
                        pathway_2_triggered_in_previous = False
                    relativistic_leap_active = False
            elif inherited_baryon_excess:
                print("\n[INHERITANCE] High-density baryon potential detected from Scenario 12 loop.")
                umnc_count, smnc_count = 2, 4
                inherited_baryon_excess = False
                relativistic_leap_active = False
            else:
                try:
                    umnc_count = int(input(f"-> Enter active UMNC count for Aeon {current_aeon} (Default=0): ") or 0)
                    smnc_count = int(input(f"-> Enter active SMNC count for Aeon {current_aeon} (Default=2): ") or 2)
                except ValueError:
                    umnc_count, smnc_count = 0, 2
                relativistic_leap_active = False

            try:
                higgs_input = input(f"-> Enter Higgs vacuum decay probability threshold (0.0 to 1.0, Default=0.85): ")
                higgs_probability = float(higgs_input) if higgs_input.strip() else 0.85
            except ValueError:
                higgs_probability = 0.85

            core_density_factor = (umnc_count * 2.0) + (smnc_count * 1.2)
            higgs_shock_boost = 3.0 if higgs_probability >= 0.5 else 1.0
            sfr_rate = round(max(0.1, (0.5 + (core_density_factor * 0.1)) * higgs_shock_boost), 2)
            print(f"[KINETICS] Computed Star Formation Rate: SFR = {sfr_rate}")
            # 5. TIME-GATED HOLE SUPPRESSION FOR MICRO-RUPTURES
            time_factor = numeric_value if numeric_value is not None else 13.8
            if is_low_value or time_factor == 0.0:
                if not relativistic_leap_active and time_factor != 0.0:
                    years_equivalent = int(time_factor * 1000000000)
                    print(f"[NOTICE] Timeline scale ({time_factor} Gyr / {years_equivalent:,} Years) is insufficient for stellar collapse.")
                    print("         New IMNC and HMNC formation is physically suppressed (Locked at 0).")
                imnc_count, hmnc_count = 0, 0
            else:
                if time_factor >= 500.0:
                    decay_magnitude = min(0.95, (time_factor / 10000.0))
                    print(f"\n[HAWKING DECAY] Enormous temporal displacement active ({time_factor} Gyr).")
                    print(f"                Cores are shrinking and evaporating (Magnitude: -{round(decay_magnitude*100, 1)}%).")
                    
                    shrunk_umnc = int(umnc_count * decay_magnitude)
                    umnc_count -= shrunk_umnc
                    smnc_count += shrunk_umnc
                    
                    shrunk_smnc = int(smnc_count * decay_magnitude)
                    smnc_count -= shrunk_smnc
                    imnc_count = max(0, int(12 * (1.0 - decay_magnitude)))
                    hmnc_count = 0
                else:
                    max_possible_imnc = max(1, int(time_factor * 8.5 * sfr_rate * higgs_shock_boost))
                    max_possible_hmnc = max(0, int((time_factor - 1.0) * 1.2 * sfr_rate * higgs_shock_boost)) if time_factor > 1.0 else 0
                    print(f"\n[DYNAMICS] Maximum bounds for newly generated cores: Max IMNC={max_possible_imnc} | Max HMNC={max_possible_hmnc}")
                    try:
                        imnc_count = min(max_possible_imnc, int(input(f"-> Enter active IMNC count (Max={max_possible_imnc}, Default=12): ") or 12))
                        hmnc_count = min(max_possible_hmnc, int(input(f"-> Enter active HMNC count (Max={max_possible_hmnc}, Default=0): ") or 0))
                    except ValueError:
                        imnc_count, hmnc_count = 12, 0

        # Compute total core network density post-decay execution
        total_active_cores = umnc_count + smnc_count + imnc_count + hmnc_count

        # Total Conformal Evaporation Guard
        if total_active_cores == 0 and not is_infinity:
            print("\n[CRITICAL THRESHOLD] Total Conformal Evaporation reached!")
            print("                     The metric has returned to a sterile dynamic vacuum state.")
            print("\nChoose subsequent execution pathway:")
            print("  1: Execute immediate Scenario 10 Conformal Reset")
            print("  2: Inject intermediate Higgs vacuum phase transition (Scenario 12 Loop)")
            while True:
                sterile_choice = input("-> Select pathway option (1 or 2): ").strip()
                if sterile_choice == "1":
                    higgs_probability, is_infinity = 0.0, True
                    break
                elif sterile_choice == "2":
                    higgs_probability, is_infinity = 1.0, True
                    break

        print(f"\n[TIMELINE] Target parameter successfully locked at: {displacement_input}")
        print(f"[METRIC] Active grid processing total of {total_active_cores} cores.")
        print(f"         [DISTRIBUTION] {umnc_count} UMNC | {smnc_count} SMNC | {imnc_count} IMNC | {hmnc_count} HMNC")

        # STANDARD PARALLEL BRANCH DETECTOR
        if is_low_value and total_active_cores >= 1 and not is_infinity and not relativistic_leap_active and time_factor != 0.0:
            print("\n[ALERT] High tensile shear stress verified. Pathway 2 triggered!")
            pathway_2_triggered_in_previous = True
            inherited_umnc_count = umnc_count + 2
            inherited_smnc_count = smnc_count + imnc_count + hmnc_count
            print(f"        [CAUSALITY] Inherited seeds locked for Generation {aeon_generation_number + 1}.")

        # AUTOMATED BLUEPRINT RECOGNITION MATRIX
        if recognition_mode:
            print("\n[RECOGNITION] Evaluating tracked multi-aeon metrics against blueprint matrix...")
            time.sleep(0.1)
            detected_scenario = "Scenario X (Hybrid Pathway)"
            if is_infinity:
                detected_scenario = "Scenario 12 (Sterile Loop)" if higgs_probability >= 0.5 else "Scenario 10 (Conformal Reset)"
            elif is_low_value or time_factor == 0.0:
                detected_scenario = "Scenario 3b (Conformal Protection)" if total_active_cores == 1 else "Scenario 7 (Multi-Core Cluster)"
            else:
                if total_active_cores == 1 and higgs_probability >= 0.5:
                    detected_scenario = "Scenario 5 (Solitary Anchor with Active Higgs Shockwave)"
                elif total_active_cores >= 2 and higgs_probability >= 0.5:
                    detected_scenario = "Scenario 9 (Multi-Core Cluster with Radiative Perimeter Walls)"
                elif total_active_cores >= 2 and higgs_probability < 0.5:
                    detected_scenario = "Scenario 6 (Multi-Core Cluster via Pure Relativistic Slingshot)"
            print(f"[MATCH] Classified Blueprint: {detected_scenario}")

        # INTERACTIVE EVEN-BRANCH CONTROLLER (CHRONOLOGY OVERRIDE)
        print("\n" + "-"*60)
        print(f"PROCESS CONTROL MENU FOR CURRENT MATRIX BOUNDARY (AEON {current_aeon})")
        print("-"*60)
        print("1: Add and follow consecutive event within this generation branch")
        print("2: Execute immediate Conformal Cyclic Reset (Linear forward progression)")
        
        while True:
            branch_choice = input("-> Select strategic next step (1 or 2): ").strip()
            if branch_choice == "1":
                print("\n[EVENT OVERRIDE] Staying within active generation layer.")
                print("                 Injecting dynamic subsequent perturbation...")
                pathway_2_triggered_in_previous = True
                inherited_umnc_count = umnc_count
                inherited_smnc_count = smnc_count + imnc_count + hmnc_count
                current_aeon = current_aeon 
                time_leap_override = True
                break
            elif branch_choice == "2":
                print("\n[CONFORMAL PROGRESSION] Executing smooth standard cyclic shift.")
                time_leap_override = False
                break
            else:
                print("[ERROR] Invalid selection. Enter 1 or 2.")

        # PROGRESSION AND RESET RE-ROUTING LAWS
        if is_infinity:
            if higgs_probability >= 0.5:
                print("\n[INFINITE LOOP] Conformal shift completed. Spectral baryon asymmetry injected! Reloading Aeon 0...\n")
                time.sleep(1.0)
                inherited_baryon_excess = True
                current_aeon = 0  
            else:
                print(f"\n[EVOLUTION] Aeon {current_aeon} terminates via smooth Scenario 10 transition.")
                current_aeon += 1
        else:
            if not time_leap_override:
                print(f"\n[EVOLUTION] Aeon {current_aeon} terminates via Conformal Crossover.")
                if relativistic_leap_active and current_aeon == 1:
                    print("\n[TIME LEAP] Selected core trajectories bypass Iteration 2 due to gamma expansion.")
                    print("            Forcing timeline continuum state directly to Iteration 3 matrix configuration.")
                    current_aeon = 3
                else:
                    current_aeon += 1
                observed_mass_baseline = int((observed_mass_baseline + 5000000) * 1.5)
            else:
                print(f"\n[INTEGRATION] Consecutive event layered into active Generation matrix.")
            
        aeon_generation_number += 1
        time.sleep(0.4)

    print("\n=====================================================================")
    print(" STATE KERNEL RUN COMPLETE: ALL SCENARIOS AND KAUSAL-PATHS VALIDATED")
    print("=====================================================================\n")

if __name__ == "__main__":
    launch_ultimate_multiverse()
