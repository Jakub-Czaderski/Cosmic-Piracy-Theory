#!/usr/bin/env python3
import math
import time
import random
import sys

def execute_automated_logging(log_id, density, is_smooth, anomaly_score, descriptor):
    try:
        with open("causal_matrix_output.txt", "a") as f:
            f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] ID: {log_id} | "
                    f"Density: {density:.6e} | Smooth: {is_smooth} | "
                    f"Anomaly: {anomaly_score:.2f} | Info: {descriptor}\n")
    except IOError:
        pass

def evaluate_cluster_stability(active_umnc, active_smnc, active_imnc, n_hmnc, total_pnc_pool):
    print("\n[MONITOR] Running Multi-Body Vector Analysis...")
    mass_weights = {"umnc": 50.0, "hmnc": 25.0, "smnc": 10.0, "imnc": 0.5, "pnc": 0.01}
    lorentz_gamma = 1.9015  
    
    f_inward = (
        (active_umnc * mass_weights["umnc"]) +
        (n_hmnc * mass_weights["hmnc"]) +
        (active_smnc * mass_weights["smnc"] * lorentz_gamma) + 
        (active_imnc * mass_weights["imnc"]) +
        (total_pnc_pool * mass_weights["pnc"])
    )
    f_outward = (
        (active_smnc * mass_weights["smnc"] * (lorentz_gamma - 1.0) * 0.45) + 
        (active_imnc * mass_weights["imnc"] * 1.5) +                          
        (n_hmnc * mass_weights["hmnc"] * 0.25) +                        
        (active_umnc * mass_weights["umnc"] * 0.05)                           
    )
    
    if f_inward == 0.0:
        if f_outward > 0.0: return "Explosion"
        else: return "Massless"
            
    r_stabil = f_outward / f_inward
    print(f" -> Inward Gravitational Pull Vector: {f_inward:.2f}")
    print(f" -> Outward Relativistic Escape Vector: {f_outward:.2f}")
    print(f" -> Computed Dynamic Balance Ratio (R_stabil): {r_stabil:.4f}")
    
    if r_stabil < 0.28:
        print(" -> [TRAJECTORY]: COLLAPSE (Central consolidation)")
        return "Collapse"
    elif r_stabil > 0.65:
        print(" -> [TRAJECTORY]: EXPLOSION (Void structures)")
        return "Explosion"
    else:
        print(" -> [TRAJECTORY]: STABLE EQUILIBRIUM (Oasis formed)")
        return "Stable"
def run_interactive_sandbox():
    print("=====================================================================")
    print("   ______   ______   .___  ___.  __    ______     ______    __  ")
    print(r"  /  ____| /  __  \  |   \/   | |  |  /  ____|   /  __  \  |  |")
    print(r" |  |     |  |  |  | |  \  /  | |  | |  |       |  |  |  | |  |")
    print(r" |  |     |  |  |  | |  |\/|  | |  | |  |       |  |  |  | |  |")
    print(" |  |____ |  `--'  | |  |  |  | |  | |  |____   |  `--'  | |  | ")
    print(r"  \______| \______/  |__|  |__| |__|  \______|   \______/  |__|")
    print("=====================================================================")
    print("        COSMIC PIRACY SIMULATION - STATE ENGINE v33.2 (ASCII MATRIX)")
    print("        Background-Independent Quantum-Geometric Graph Evaluator")
    print("=====================================================================\n")
    
    # --- QUANTUM GEOMETRIC SIMULATION RESOLUTION MATRIX ---
    print("=====================================================================")
    print(" [RESOLUTION INTERFACE]: Configure Temporal Slicing Matrix")
    print("=====================================================================")
    print("  - Standard Matrix  : Constant 10-Year Steps across deep time")
    print("  - Big-bang Horizon  : Microscopic 1-Year Steps for the first 1000")
    print("                           years, then transitioning into 10-Year Steps.")
    print("---------------------------------------------------------------------")
    try:
        res_choice = input(" >> Select Temporal Resolution Node (1/2): ").strip()
    except ValueError:
        res_choice = "1"
    
    if res_choice == "2":
        res_profile = "Big-bang_focus"
        print("   [SUCCESS] Big-bang Focus locked. Enforcing 1-Year micro-increments for the birth phase.\n")
    else:
        res_profile = "standard_10y"
        print("   [SUCCESS] Standard Matrix locked. Slicing continuum into 10-Year steps.\n")
    time.sleep(0.4)

    current_generation = 0
    n_umnc, n_hmnc, n_smnc, n_imnc = 0, 0, 0, 0
    backup_umnc, backup_hmnc, backup_smnc, backup_imnc = 0, 0, 0, 0
    
    parallel_timelines = {}
    for slot in range(1, 13):
        parallel_timelines[slot] = {
            "umnc": 0, "hmnc": 0, "smnc": 10, "imnc": 253,
            "generation": 0, "age": 4.0,
            "scenario": "6 (Multi-Core Cluster Baseline)",
            "scar_v1": False, "collision_v2": False,
            "multiverse_counter": random.randint(5, 50),
            "is_empty_layer": False
        }
    active_manifold_multiverse_counter = 0
    assigned_scenario = "4"
    star_formation_mod = 1.0
    genesis_reply_loop = True
    while genesis_reply_loop:
        scenario_1_drainage_active = False
        addendum_1_scar_active = False
        addendum_1_dynamic_collision = False
        timeline_displacement_risk = False
        calculated_delay_gyr = 0.0

        if current_generation == 0:
            print("[INPUT] Initialize at Scenario 0 (Global CPT Crossover Node)?")
            genesis_reply = input("        Trigger Ur-Genesis Phase (Y/n): ").strip().lower()
            
            if genesis_reply != 'y' and genesis_reply != '':
                print("\n[CRITICAL RESET] Enforcing Conformal Cyclic Reset!")
                continue 

            print("\n[PHASE 0] AEON 0 - PRIMORDIAL SEEDING AND BOUNDARY GATES")
            print("---------------------------------------------------------------------")
        else:
            print("\n" + "="*65)
            print(f" [CONTINUUM] BOOTING CHILD SPACETIME MANIFOLD - GENERATION {current_generation}")
            print("="*65)
            print(f"    [PHASE {current_generation}] AEON {current_generation} - EVOLVING STRUCTURES & SEED KINETICS")
            print("---------------------------------------------------------------------")
            time.sleep(0.4)

        print(f"[INPUT] Enter target timescale for Aeon {current_generation} PNC growth phase:")
        t_input_str = input("        Delta t_0 (in Gyr, e.g. 4.0 or infinity): ").strip().lower()
        
        is_infinity_run = False
        if t_input_str == "infinity":
            t_genesis = 1e20  
            is_infinity_run = True
            print("          [INFINITY] Simulating continuous forward dilution until total vacuum...")
        else:
            try:
                t_genesis = float(t_input_str)
            except ValueError:
                t_genesis = 4.0
                print("          [INVALID] Defaulting to baseline timescale 4.0 Gyr.")

        try:
            print(f"\n[INPUT] Configure Multi-Bubble Generation Flux for Aeon {current_generation}:")
            agg_bubble_rate = float(input("        >> Enter creation aggressiveness (0.01 - 0.99): "))
            agg_bubble_rate = max(0.01, min(0.99, agg_bubble_rate))
        except ValueError:
            agg_bubble_rate = 0.25

        if current_generation == 0:
            star_formation_mod = 1.0 + (agg_bubble_rate * 0.5)
            conformal_saturation = math.tanh(t_genesis / 15.0)
            
            n_umnc = int(6.0 * conformal_saturation * star_formation_mod) + 2
            n_hmnc = 1  
            n_smnc = int(400.0 * conformal_saturation * (1.0 + math.log1p(t_genesis * 0.02)) * star_formation_mod) + 50
            n_imnc = int(1600.0 * conformal_saturation * (1.0 + math.log1p(t_genesis * 0.05)) * star_formation_mod) + 500
        else:
            print(f"          [STAR FORMATION ENGINE]: Active. Inherited Factor: {star_formation_mod:.3f}x")
            print(f"          [ANCHOR INJECTION]: Conformal layer running on imported anchors: HMNC={n_hmnc} | UMNC={n_umnc}")
            conformal_saturation = math.tanh(t_genesis / 15.0)
            
            base_umnc = 12.0 * conformal_saturation * star_formation_mod
            base_smnc = 650.0 * conformal_saturation * (1.0 + math.log1p(t_genesis * 0.04)) * star_formation_mod
            base_imnc = 2400.0 * conformal_saturation * (1.0 + math.log1p(t_genesis * 0.08)) * star_formation_mod
            
            if assigned_scenario == "9":
                umnc_spawned = int(base_umnc)
                smnc_spawned = int(base_smnc)
                imnc_spawned = int(base_imnc)
            elif assigned_scenario == "7.2b":
                tolerance_factor = random.uniform(0.85, 1.15)
                umnc_spawned = int(base_umnc * tolerance_factor)
                smnc_spawned = int(base_smnc * tolerance_factor)
                imnc_spawned = int(base_imnc * tolerance_factor)
            else:
                umnc_spawned = int(base_umnc)
                smnc_spawned = int(base_smnc)
                imnc_spawned = int(base_imnc)

            n_umnc += umnc_spawned
            n_smnc += smnc_spawned
            n_imnc += imnc_spawned

        backup_umnc = n_umnc
        backup_hmnc = n_hmnc
        backup_smnc = n_smnc
        backup_imnc = n_imnc

        # --- FIXED TEMPORAL SLICING RESOLUTION (NO HARDCODED LIMITS) ---
        initial_object_count = n_umnc + n_hmnc + n_smnc + n_imnc
        primordial_spacetimes = 0
        
        time_step_standard = 1e-8  # Continuous 10-Year Steps in Gyr
        time_step_micro = 1e-9     # Microscopic 1-Year Steps in Gyr

        if is_infinity_run:
            micro_cycles = 5000000 if res_profile == "Big-bang_focus" else 1000000
        else:
            if res_profile == "Big-bang_focus":
                remaining_time = max(0.0, t_genesis - 1e-6)
                micro_cycles = 1000 + int(remaining_time / time_step_standard)
            else:
                micro_cycles = max(100, int(t_genesis / time_step_standard))

        flux_efficiency = 1.0 / (1.0 + math.log1p(1.0 / agg_bubble_rate))
        print(f"          [COSMOLOGICAL EVOLUTION]: Processing {micro_cycles} dynamic matrix cycles...")
        
        actual_time_elapsed = 0.0

        for cycle in range(micro_cycles):
            # Strict vertical alignment of 12 spaces inside the active loop
            if res_profile == "Big-bang_focus" and actual_time_elapsed <= 1e-6:
                time_per_cycle = time_step_micro
            else:
                time_per_cycle = time_step_standard

            actual_time_elapsed += time_per_cycle
            
            # 1. Micro-Core Kinetic Transitions
            if n_imnc > 0:
                imnc_to_smnc = min(n_imnc, max(1, int(n_imnc * 0.05 * flux_efficiency)))
                n_imnc -= imnc_to_smnc
                n_smnc += imnc_to_smnc
            if n_smnc > 0:
                smnc_to_umnc = min(n_smnc, max(1, int(n_smnc * 0.02 * flux_efficiency)))
                n_smnc -= smnc_to_umnc
                n_umnc += smnc_to_umnc
            if n_umnc > 0 and (is_infinity_run or cycle > 500):
                umnc_to_hmnc = min(n_umnc, max(1, int(n_umnc * 0.005 * flux_efficiency)))
                n_umnc -= umnc_to_hmnc
                n_hmnc += umnc_to_hmnc

            # 2. Bubble Flux Probability & Seeding
            if n_imnc > 0 or n_smnc > 0 or n_umnc > 0 or n_hmnc > 0:
                pull_imnc = random.randint(0, max(1, int(n_imnc * agg_bubble_rate * 0.15))) if n_imnc > 0 else 0
                pull_smnc = random.randint(0, max(1, int(n_smnc * agg_bubble_rate * 0.25))) if n_smnc > 0 else 0
                pull_umnc = random.randint(0, max(1, int(n_umnc * agg_bubble_rate * 0.05))) if n_umnc > 0 else 0
                pull_hmnc = random.randint(0, max(1, int(n_hmnc * agg_bubble_rate * 0.01))) if n_hmnc > 0 else 0
                
                local_exposure = (pull_hmnc * (50.0**2)) + (pull_umnc * (25.0**2)) + (pull_smnc * (10.0**2)) + (pull_imnc * (0.5**2))
                ignition_prob = min(0.95, (local_exposure * 8.5e-4) * agg_bubble_rate)
                
                if random.random() <= ignition_prob:
                    primordial_spacetimes += 1
                    n_imnc = max(0, n_imnc - pull_imnc)
                    n_smnc = max(0, n_smnc - pull_smnc)
                    n_umnc = max(0, n_umnc - pull_umnc)
                    n_hmnc = max(0, n_hmnc - pull_hmnc)

            # 3. Precision Hawking Radiation decay per step
            r_imnc = 1.0 / ((1.0 + n_imnc * 0.05) ** 3.0) if n_imnc > 0 else 0
            r_smnc = 1.0 / ((50.0 + n_smnc * 1.0) ** 3.0) if n_smnc > 0 else 0
            r_umnc = 1.0 / ((1000.0 + n_umnc * 5.0) ** 3.0) if n_umnc > 0 else 0
            r_hmnc = 1.0 / ((1e8 + n_hmnc * 100.0) ** 3.0) if n_hmnc > 0 else 0
            
            n_imnc -= min(n_imnc, int(n_imnc * (1.0 - math.exp(-r_imnc * time_per_cycle))))
            n_smnc -= min(n_smnc, int(n_smnc * (1.0 - math.exp(-r_smnc * time_per_cycle))))
            n_umnc -= min(n_umnc, int(n_umnc * (1.0 - math.exp(-r_umnc * time_per_cycle))))
            n_hmnc -= min(n_hmnc, int(n_hmnc * (1.0 - math.exp(-r_hmnc * time_per_cycle))))

            # --- DYNAMIC BREAKPOINT GATER ---
            current_object_count = n_umnc + n_hmnc + n_smnc + n_imnc
            if cycle > 10 and current_object_count == 0:
                t_genesis = actual_time_elapsed
                print(f"          [DYNAMIC BREAK]: Total vacuum achieved at exact epoch: {t_genesis:.2e} Gyr.")
                break
        else:
            t_genesis = actual_time_elapsed


        # --- ABSOLUTE DISCONNECT LAYER ---
        if current_object_count == 0:
            active_manifold_multiverse_counter = primordial_spacetimes
            calculated_delay_gyr = float('inf')
            timeline_displacement_risk = True
            
            # Freeze state fields for Phase 4 display integrity
            n_umnc, n_hmnc, n_smnc, n_imnc = 0, 0, 0, 0
        else:
            active_manifold_multiverse_counter = primordial_spacetimes
            calculated_delay_gyr = 0.0
            timeline_displacement_risk = False

        # --- UI EXPLORER SYSTEM WITH COMPREHENSIVE REGISTRY ---
        all_available_scenarios = [
            "1 (Primeval Topological Deflation Interface)",
            "2 (Solitary Isotropic Hierarchical Accretion)",
            "3a (Sterile Gravitational Trap)",
            "3b (Chiral Antimatter Universe Cascade)",
            "4 (Decaying Parent Aeon Matrix)",
            "5 (Active Pathway 3 Higgs Shockwave)",
            "6 (Multi-Core Cluster Baseline)",
            "7.1 (Relativistic Slingshot Pocket)",
            "7.2a (Asymmetric Oasis-Galaxy Cluster)",
            "7.2b (Core Theft Slingshot Pocket)",
            "8.5 (Stable Shadow Track Drainage)",
            "9 (Radiative Perimeter Void Wall)"
        ]

        for slot in range(1, 13):
            data = parallel_timelines[slot]
            if slot <= active_manifold_multiverse_counter:
                data["chiral_inverted"] = random.choice([True, False])
                
                s_hmnc = random.randint(0, max(1, int(backup_hmnc * 0.5))) if backup_hmnc > 0 else 0
                s_umnc = random.randint(0, max(1, int(backup_umnc * 0.5))) if backup_umnc > 0 else 0
                s_smnc = random.randint(5, 50)
                s_imnc = random.randint(10, 200)
                
                has_modifier = random.choice([True, False])
                slot_sf_mod = random.uniform(2.5, 5.0) if has_modifier else 1.0
                mod_tag = f" | SF_Mod={slot_sf_mod:.2f}x" if has_modifier else " | SF_Mod=1.00x"
                
                selected_manifest = random.choice(all_available_scenarios)
                data["scenario"] = f"{selected_manifest} [HMNC={s_hmnc} | UMNC={s_umnc} | SMNC={s_smnc} | IMNC={s_imnc}{mod_tag}]"
                data["generation"] = current_generation
                data["age"] = t_genesis * random.uniform(0.8, 1.2)
                data["multiverse_counter"] = random.randint(100, int(active_manifold_multiverse_counter + 500))
                
                data["hmnc"] = s_hmnc
                data["umnc"] = s_umnc
                data["smnc"] = s_smnc
                data["imnc"] = s_imnc
                data["is_empty_layer"] = False
            else:
                data["scenario"] = "[EMPTY VACUUM LAYER]"
                data["chiral_inverted"] = False
                data["generation"] = 0
                data["age"] = 0.0
                data["multiverse_counter"] = 0
                data["hmnc"] = 0
                data["umnc"] = 0
                data["smnc"] = 0
                data["imnc"] = 0
                data["is_empty_layer"] = True

        print("\n[SUCCESS] Universal quantum-geometric fields processed stochastically.")
        print("\n" + "="*65)
        print("        ASTROPHYSICAL TIMELINE INTEGRITY STATUS DISPLAY        ")
        print("="*65)
        print(f" -> TOTAL ACTIVE CORES CONSTITUTED: HMNC={n_hmnc} | UMNC={n_umnc} | SMNC={n_smnc} | IMNC={n_imnc}")
        print(f" -> SPACETIMES CREATED BY THIS AEON: {active_manifold_multiverse_counter}")
        print("---------------------------------------------------------------------")

        # --- IMMEDIATE VACUUM COMMAND TRIGGER (WITH INTERNAL CONTROL LOOP) ---
        if current_object_count == 0:
            print("\n [WARNING]: TOTAL THERMODYNAMIC VACUUM DETECTED. ALL HORIZONS EVAPORATED.")
            print("            Conformal scale unanchored. Space-time closure forces immediate holonomic sequence.")
            
            vacuum_menu_active = True
            while vacuum_menu_active:
                print("\n" + "-"*65)
                print(" [MULTIVERSE] TRANS-DIMENSIONAL COBWEB CROSSOVER (VACUUM TRIGGER)")
                print("-"*65)
                print(" [INPUT] Choose active continuum trajectory command:")
                print("         [j] - Jump into a parallel universe (Stored in RAM)")
                print("         [r] - Trigger a conformal reset due to mass invariance")
                print("         [b] - Back to a certain point in time in this universe and continue")
                print("         [q] - Break the laws of physics, terminate the multiverse and exit existence. You can always come back and create a new one!")
                jump_choice = input("         Select Choice (j/r/b/Q): ").strip().lower()
                
                if jump_choice == 'j':
                    print("\n=====================================================================")
                    print("    MULTIVERSE MATRIX INDEX: 12 PARALLEL SPACETIMES STORED IN RAM     ")
                    print("=====================================================================")
                    for slot, data in parallel_timelines.items():
                        chiral_tag = "[A]" if data.get("chiral_inverted", False) else "[M]"
                        print(f" Slot {slot:02d} {chiral_tag} -> Manifest: {data.get('scenario', 'Unknown')}")
                        print(f"           Gen: {data.get('generation', 0)} | Age: {data.get('age', 0.0):.2e} Gyr")
                        print(" ---------------------------------------------------------------------")
                    try:
                        target_slot = int(input(" >> Select target Timeline Slot to jump into (1-12): "))
                        if target_slot in parallel_timelines:
                            if parallel_timelines[target_slot].get("is_empty_layer", False):
                                print(" [FAIL] Target slot coordinates are unallocated. Void layer unresolvable.\n")
                                continue
                                
                            print("\n[CROSSOVER] Slicing coordinates... Re-locking quantum loops...")
                            n_umnc = parallel_timelines[target_slot]["umnc"]
                            n_hmnc = parallel_timelines[target_slot]["hmnc"]
                            n_smnc = parallel_timelines[target_slot]["smnc"]
                            n_imnc = parallel_timelines[target_slot]["imnc"]
                            current_generation = parallel_timelines[target_slot]["generation"]
                            active_manifold_multiverse_counter = parallel_timelines[target_slot]["multiverse_counter"]
                            addendum_1_scar_active = parallel_timelines[target_slot]["scar_v1"]
                            addendum_1_dynamic_collision = parallel_timelines[target_slot]["collision_v2"]
                            print(f" -> [SUCCESS] Crossover locked. Welcome to Timeline Slot {target_slot:02d}.\n")
                            vacuum_menu_active = False
                            break
                    except ValueError:
                        print(" [SECURITY] Invalid coordinate selection.")
                        
                elif jump_choice == 'r':
                    current_generation += 1
                    assigned_scenario = "12" if random.random() < 0.5 else "10"
                    print(f"\n -> [SUCCESS] Massless reset initialized. Target Scenario Horizon: {assigned_scenario}\n")
                    n_umnc, n_hmnc, n_smnc, n_imnc = 0, 0, 0, 0
                    vacuum_menu_active = False
                    break

                elif jump_choice == 'b':
                    print("\n[TEMPORAL BOUNCE] Initiating localized timeline regression...")
                    try:
                        t_rollback = float(input("         >> Enter target epoch to bounce back to (Gyr): "))
                        if 0.0 <= t_rollback <= t_genesis:
                            t_genesis = t_rollback
                            
                            n_umnc = backup_umnc
                            n_hmnc = backup_hmnc
                            n_smnc = backup_smnc
                            n_imnc = backup_imnc
                            
                            micro_cycles = max(100, int(math.log1p(t_genesis) * 120.0)) if t_genesis > 1000.0 else max(1, int(t_genesis * 2))
                            print(f"          [RE-CALCULATING TIMELINE]: Processing {micro_cycles} cycles for {t_genesis:.4f} Gyr...")
                            
                            for cycle in range(micro_cycles):
                                if n_imnc > 0:
                                    imnc_to_smnc = min(n_imnc, max(1, int(n_imnc * 0.05 * flux_efficiency)))
                                    n_imnc -= imnc_to_smnc
                                    n_smnc += imnc_to_smnc
                                if n_smnc > 0:
                                    smnc_to_umnc = min(n_smnc, max(1, int(n_smnc * 0.02 * flux_efficiency)))
                                    n_smnc -= smnc_to_umnc
                                    n_umnc += smnc_to_umnc
                                if n_umnc > 0 and (t_genesis >= 120.0 or cycle > (micro_cycles * 0.4)):
                                    umnc_to_hmnc = min(n_umnc, max(1, int(n_umnc * 0.005 * flux_efficiency)))
                                    n_umnc -= umnc_to_hmnc
                                    n_hmnc += umnc_to_hmnc

                                if n_imnc > 0 or n_smnc > 0 or n_umnc > 0 or n_hmnc > 0:
                                    pull_imnc = random.randint(0, max(1, int(n_imnc * agg_bubble_rate * 0.15))) if n_imnc > 0 else 0
                                    pull_smnc = random.randint(0, max(1, int(n_smnc * agg_bubble_rate * 0.25))) if n_smnc > 0 else 0
                                    pull_umnc = random.randint(0, max(1, int(n_umnc * agg_bubble_rate * 0.05))) if n_umnc > 0 else 0
                                    pull_hmnc = random.randint(0, max(1, int(n_hmnc * agg_bubble_rate * 0.01))) if n_hmnc > 0 else 0
                                    
                                    local_exposure = (pull_hmnc * (50.0**2)) + (pull_umnc * (25.0**2)) + (pull_smnc * (10.0**2)) + (pull_imnc * (0.5**2))
                                    ignition_prob = min(0.95, (local_exposure * 8.5e-4) * agg_bubble_rate)
                                    
                                    if random.random() <= ignition_prob:
                                        primordial_spacetimes += 1
                                        n_imnc = max(0, n_imnc - pull_imnc)
                                        n_smnc = max(0, n_smnc - pull_smnc)
                                        n_umnc = max(0, n_umnc - pull_umnc)
                                        n_hmnc = max(0, n_hmnc - pull_hmnc)

                            r_imnc = 1.0 / ((1.0 + n_imnc * 0.05) ** 3.0) if n_imnc > 0 else 0
                            r_smnc = 1.0 / ((50.0 + n_smnc * 1.0) ** 3.0) if n_smnc > 0 else 0
                            r_umnc = 1.0 / ((1000.0 + n_umnc * 5.0) ** 3.0) if n_umnc > 0 else 0
                            r_hmnc = 1.0 / ((1e8 + n_hmnc * 100.0) ** 3.0) if n_hmnc > 0 else 0
                            
                            n_imnc -= min(n_imnc, int(n_imnc * (1.0 - math.exp(-r_imnc * t_genesis))))
                            n_smnc -= min(n_smnc, int(n_smnc * (1.0 - math.exp(-r_smnc * t_genesis))))
                            n_umnc -= min(n_umnc, int(n_umnc * (1.0 - math.exp(-r_umnc * t_genesis))))
                            n_hmnc -= min(n_hmnc, int(n_hmnc * (1.0 - math.exp(-r_hmnc * t_genesis))))

                            current_object_count = n_umnc + n_hmnc + n_smnc + n_imnc
                            active_manifold_multiverse_counter = primordial_spacetimes
                            print(f" -> [SUCCESS] Timeline recalculated. Regressed state: HMNC={n_hmnc} | UMNC={n_umnc}")
                            
                            if current_object_count > 0:
                                vacuum_menu_active = False
                                break
                            else:
                                print(" -> [NOTICE]: Recalculated state is still a total vacuum. Reloading menu options.")
                        else:
                            print(" [FAIL] Target coordinate outside the causal boundary of this aeon.")
                    except ValueError:
                        print(" [SECURITY] Invalid temporal configuration input.")
                        
                else:
                    print("\n[EXIT] An entire multiverse was erased from existence. Are you happy with yourself? Goodbye.\n")
                    sys.exit(0)
            
            if not vacuum_menu_active and current_object_count > 0:
                continue
        else:
            print("[INPUT] Configure active Horizon Assets for Evacuation:")
            try:
                active_umnc = min(n_umnc, int(input(f"        Active UMNC anchors (0-{n_umnc}): ") or n_umnc)) if n_umnc > 0 else 0
                active_hmnc = min(n_hmnc, int(input(f"        Active HMNC mergers (0-{n_hmnc}): ") or n_hmnc)) if n_hmnc > 0 else 0
                active_smnc = min(n_smnc, int(input(f"        Active SMNC satellites (0-{n_smnc}): ") or n_smnc)) if n_smnc > 0 else 0
                active_imnc = min(n_imnc, int(input(f"        Active IMNC shields (0-{n_imnc}): ") or n_imnc)) if n_imnc > 0 else 0
            except ValueError:
                print("        [INPUT ERROR] Core manual override failed. Keeping raw values.")
            print("\n" + "-"*50)
            print(" [SCENARIO 1 / ADDENDUM 1A] PRIMEVAL METRIC DRAINAGE INTERFACE")
            print("-"*50)
            drain_choice = input("        Trigger Scenario 1 Localized Metric Drainage? (y/N): ").strip().lower()
            scenario_1_drainage_active = True if drain_choice == 'y' else False
            addendum_1_scar_active = True if scenario_1_drainage_active else False

            print("\n" + "-"*50)
            print(" [PATHWAY 2] INDEPENDENT SPACETIME ISOLATION EVALUATOR (STERILE AEON 0)")
            print("-"*50)
            
            pathway_2_isolation_efficiency = (active_umnc + active_hmnc + active_smnc + active_imnc) / current_object_count
            core_mass_deficit_factor = math.exp(-0.06 * min(150.0, t_genesis))
            remaining_energy_density = (t_genesis ** 2.0) * core_mass_deficit_factor * (1.0 - pathway_2_isolation_efficiency)
            conformal_entropy_slippage = 0.25 * math.sin(min(150.0, t_genesis)) + 0.50
            
            remaining_hmnc = n_hmnc - active_hmnc
            remaining_umnc = n_umnc - active_umnc
            remaining_smnc = n_smnc - active_smnc
            remaining_imnc = n_imnc - active_imnc
            
            if pathway_2_isolation_efficiency >= 1.0:
                calculated_delay_gyr = 0.0
            else:
                hawking_time_factor = (remaining_hmnc * 1e60) + (remaining_umnc * 1e40) + (remaining_smnc * 1e20) + (remaining_imnc * 1e5)
                base_displacement = (min(150.0, t_genesis) * 0.15) + conformal_entropy_slippage
                calculated_delay_gyr = base_displacement * (1.0 - pathway_2_isolation_efficiency) * hawking_time_factor
            
            print(f" -> Pathway 2 Isolation Efficiency: {pathway_2_isolation_efficiency * 100.0:.2f}% Cores Isolated.")
            print(f" -> Available Residual Growth Energy Density: {remaining_energy_density:.4f}")
            print(f" -> Dynamic Timeline Displacement Result: {calculated_delay_gyr:.2e} Gyr")
            
            print("\n[COSMIC SYNCHRONIZATION]: Evaluating trans-cosmic impulse axis...")
            if calculated_delay_gyr == 0.0:
                print(" -> Status: Perfect core isolation. Quantum loops are synchronized.")
                print(" -> Conformal footprint occurs IMMEDIATELY (0.00 Gyr displacement).")
                impulse_reply = input(" >> Trigger immediate trans-cosmic impulse crossover? (Y/n): ").strip().lower()
            else:
                print(f" -> WARNING: Incomplete core isolation! Rest-mass forces 'Timeline Displacement'.")
                print(f" -> Conformal information sync delayed by: {calculated_delay_gyr:.2e} billion years (Gyr).")
                print("    (Per Addendum 1, the system remains in an asynchronous state until execution)")
                impulse_reply = input(f" >> Trigger holonomic impulse despite the calculated delay of {calculated_delay_gyr:.2e} Gyr? (Y/n): ").strip().lower()
                
            timeline_displacement_risk = True if (calculated_delay_gyr > 2.5 and impulse_reply != 'n') else False

            print("\n" + "-"*50)
            print(" [ADDENDUM 1 - VERSION B] MULTIVERSE COLLISION MONITOR")
            print("-"*50)
            coll_choice = input("        Engage Addendum 1 Version B Multi-Collision track? (y/N): ").strip().lower()
            addendum_1_dynamic_collision = True if coll_choice == 'y' else False
            
            collision_times = []
            omega_oaza = 1.0
            
            if addendum_1_dynamic_collision:
                print("\n=====================================================")
                print("[ADDENDUM 1 - VERSION B] COBWEB COLLISION DETECTOR")
                print("=====================================================")
                print(" -> THEORY NODE: Macro-Cosmological Boundary Intersections.")
                print("    Independently expanding sub-manifolds retain topological")
                print("    entanglement at their causal boundaries. Intersecting nodes")
                print("    induce localized stress, displacing baryonic densities")
                print("    to generate the CMB Cold Spot while transferring holonomic")
                print("    anomaly data to catalyze early-epoch star formation.")
                print("-----------------------------------------------------")
                b_mode = input("        Select Mode (m/S): ").strip().lower()
                num_collisions = 0

                if b_mode == 'm':
                    try:
                        num_collisions = int(input("        >> Enter total intersecting universes: "))
                        for i in range(num_collisions):
                            t_coll = float(input(f"           Enter time for Node {i+1} (Gyr): "))
                            collision_times.append((t_coll, 'manual'))
                    except ValueError: num_collisions = 0
                else:
                    global_density_pool = active_manifold_multiverse_counter
                    if global_density_pool > 0:
                        num_collisions = random.randint(1, max(3, int(math.log1p(global_density_pool) * 2.5)))
                        for _ in range(num_collisions):
                            collision_times.append((random.uniform(0.1, min(t_genesis, 1000.0)), 'auto'))
                        print(f"        [AUTO-FOAM] Anchored {num_collisions} independent intersections.")
                        
                if num_collisions > 0:
                    omega_oaza = 2.5
                    print("\n" + "-"*50)
                    print(" [ADDENDUM 1] HOLONOMIC ANOMALY STRUCTURE DATA TRANSFER")
                    print("-"*50)
                    for t_coll, density_flag in collision_times:
                        is_dense = 'n' if density_flag != 'manual' else input(f"        >> Is Node at t={t_coll:.1f} Gyr a high-density zone? (Y/n): ").strip().lower()
                        if is_dense != 'n':
                            sf_multiplier = random.uniform(2.5, 5.0)
                            star_formation_mod *= sf_multiplier

        print("---------------------------------------------------------------------")
        print(f" -> Conformal Compression Factor (Omega_Oaza): {omega_oaza:.2f}")
        print(f" -> Dynamic Trans-Cosmic Delay Vector: {calculated_delay_gyr:.2e} Gyr")
        print(f" -> Final Computed Star Formation Frequency Modifier: {star_formation_mod:.3f}x")

        if current_object_count > 0 and scenario_1_drainage_active:
            user_choice = "1"
        elif current_object_count > 0 and addendum_1_dynamic_collision and omega_oaza == 2.5:
            user_choice = "7.2b" if timeline_displacement_risk else "9"
        elif current_object_count > 0 and timeline_displacement_risk and not addendum_1_dynamic_collision:
            user_choice = "8.5"
        elif current_object_count >= 150 and t_genesis < 1.0: 
            user_choice = "6"
        elif current_object_count == 0 and t_genesis >= 50.0: 
            user_choice = "12"
        else: 
            user_choice = "4"
        
        print(f"        >> Verified Trajectory Phase: Scenario {user_choice} (Tolerance: {0.0}%)")
        assigned_scenario = user_choice
        active_manifold_multiverse_counter += int(2 * (min(150.0, t_genesis) / 10.0))

        for slot in range(1, 13):
            data = parallel_timelines[slot]
            if slot <= active_manifold_multiverse_counter:
                mass_mismatch = abs((n_umnc + n_smnc + n_hmnc) - (data.get("umnc", 0) + data.get("smnc", 0) + data.get("hmnc", 0)))
                data["chiral_inverted"] = True if mass_mismatch > 100 else False
                
                ignorance_threshold = random.uniform(0.1, 12.0)
                is_evolutionary_severed = True if (calculated_delay_gyr == float('inf') or calculated_delay_gyr > ignorance_threshold) else False
                
                if is_evolutionary_severed:
                    data["generation"] = data.get("generation", 0) + random.randint(1, 5)
                    delay_string = "INFINITE" if calculated_delay_gyr == float('inf') else f"+{calculated_delay_gyr:.2f}"
                    data["scenario"] = f"Scenario 8.5 [SEVERED BRANCH | Displaced {delay_string} Gyr]"
                    data["multiverse_counter"] = data.get("multiverse_counter", 0) + random.randint(10, 100)
                else:
                    data["generation"] = current_generation
                    data["multiverse_counter"] = int(active_manifold_multiverse_counter)
                    data["scenario"] = f"Scenario {user_choice} [Synchronized Layer]"

                data["age"] = float(t_genesis)
                data["imnc"] = int(n_imnc)
                data["smnc"] = int(n_smnc)
                data["umnc"] = int(n_umnc)
                data["hmnc"] = int(n_hmnc)
                data["scar_v1"] = addendum_1_scar_active
                data["collision_v2"] = addendum_1_dynamic_collision

        print("\n[SUCCESS] Universal quantum-geometric fields processed stochastically.")
        print("          RAM Multi-Manifold Index updated via isolation-displacement filtering.")

        print("\n" + "-"*65)
        print(" [MULTIVERSE] TRANS-DIMENSIONAL COBWEB CROSSOVER")
        print("-"*65)
        
        if current_generation == 0 and current_object_count > 0:
            print(" [CONTINUUM]: Active cores in Generation 0 verified. Rupture event guaranteed.")
            print("              Automating Conformal Reset to track the child aeon...")
            jump_choice = 'r'
            time.sleep(0.4)
        else:
            print(" [INPUT] Choose active continuum trajectory command:")
            print("         [j] - Jump into a parallel universe (Stored in RAM)")
            print("         [r] - Trigger a conformal reset due to mass invariance")
            print("         [b] - Back to a certain point in time in this universe and continue")
            print("         [q] - Break the laws of physics, terminate the multiverse and exit existence. You can always come back and create a new one!")
            jump_choice = input("         Select Choice (j/r/b/Q): ").strip().lower()
        
        if jump_choice == 'j':
            print("\n=====================================================================")
            print("    MULTIVERSE MATRIX INDEX: 12 PARALLEL SPACETIMES STORED IN RAM     ")
            print("=====================================================================")
            for slot, data in parallel_timelines.items():
                slot_chirality = data.get("chiral_inverted", False)
                chiral_tag = "[A]" if slot_chirality else "[M]"
                print(f" Slot {slot:02d} {chiral_tag} -> Manifest: {data.get('scenario', 'Unknown')}")
                print(f"           Gen: {data.get('generation', 0)} | Age: {data.get('age', 0.0):.2e} Gyr")
                print(" ---------------------------------------------------------------------")

            try:
                target_slot = int(input(" >> Select target Timeline Slot to jump into (1-12): "))
                if target_slot in parallel_timelines:
                    if parallel_timelines[target_slot].get("is_empty_layer", False):
                        print(" [FAIL] Target slot coordinates are unallocated. Void layer unresolvable.\n")
                        continue
                        
                    print("\n[CROSSOVER] Slicing coordinates... Re-locking quantum loops...")
                    time.sleep(0.3)
                    n_umnc = parallel_timelines[target_slot]["umnc"]
                    n_hmnc = parallel_timelines[target_slot]["hmnc"]
                    n_smnc = parallel_timelines[target_slot]["smnc"]
                    n_imnc = parallel_timelines[target_slot]["imnc"]
                    current_generation = parallel_timelines[target_slot]["generation"]
                    active_manifold_multiverse_counter = parallel_timelines[target_slot]["multiverse_counter"]
                    addendum_1_scar_active = parallel_timelines[target_slot]["scar_v1"]
                    addendum_1_dynamic_collision = parallel_timelines[target_slot]["collision_v2"]
                    print(f" -> [SUCCESS] Crossover locked. Welcome to Timeline Slot {target_slot:02d}.\n")
                    continue
            except ValueError:
                print(" [SECURITY] Invalid coordinate selection.")
        elif jump_choice == 'r':
            current_generation += 1
            print(f"\n" + "="*65)
            print(f" [UR-GENESIS] BIFURCATION MATRIX - TRANSITION TO GENERATION {current_generation}")
            print("="*65)
            print("        Capturing evacuated horizon assets for child-spacetime injection...")
            
            isolated_umnc = active_umnc
            isolated_hmnc = active_hmnc
            isolated_smnc = active_smnc
            isolated_imnc = active_imnc
            print(f"        -> Injecting invariant anchors: HMNC={isolated_hmnc} | UMNC={isolated_umnc}")
            
            print("\n[EVAL] Sampling stochastic overlap between LQG Tensile Limit and Higgs scalar onset...")
            time.sleep(0.4)
            
            remaining_massive_cores = n_hmnc + n_umnc
            higgs_roll = random.random()
            
            if remaining_massive_cores > 0 and calculated_delay_gyr < 1e10:
                higgs_roll = 0.95 
                print(f"           [CRITICAL]: Massive remnants ({remaining_massive_cores} cores) remain unevaporated at {calculated_delay_gyr:.2e} Gyr.")
                print("                       Conformal invariance broken. Quenching Pathway 3 shockwave.")
            
            if higgs_roll < 0.20:
                assigned_scenario = "9"
                print("           [STATUS]: Instantaneous Vacuum Drop (Higgs == LQG) triggered!")
            elif higgs_roll < 0.75:
                assigned_scenario = "7.2b"
                print("           [STATUS]: Delayed Transition (Higgs < LQG) registered.")
            else:
                assigned_scenario = "3a" if isolated_hmnc > 0 else "4"
                print(f"           [STATUS]: Suppressed Phase Transition (Higgs > LQG) invoked.")
                print(f"                     Trajectory bound to baseline configuration: Scenario {assigned_scenario}.")

            print(f"\n[RESET] Compressing and transferring rest-mass into Conformal Channel...")
            n_umnc = isolated_umnc
            n_hmnc = isolated_hmnc
            n_smnc = isolated_smnc
            n_imnc = isolated_imnc
            
            addendum_1_scar_active = False
            addendum_1_dynamic_collision = False
            print(f" -> [SUCCESS] Transition state primed. Advancing onto Conformal Layer.\n")
            time.sleep(0.4)
            continue

        elif jump_choice == 'b':
            print("\n[TEMPORAL BOUNCE] Initiating localized timeline regression...")
            try:
                t_rollback = float(input("         >> Enter target epoch to bounce back to (Gyr): "))
                if 0.0 <= t_rollback <= t_genesis:
                    t_genesis = t_rollback
                    
                    n_umnc = backup_umnc
                    n_hmnc = backup_hmnc
                    n_smnc = backup_smnc
                    n_imnc = backup_imnc
                    
                    micro_cycles = max(100, int(math.log1p(t_genesis) * 120.0)) if t_genesis > 1000.0 else max(1, int(t_genesis * 2))
                    
                    print(f"          [RE-CALCULATING TIMELINE]: Processing {micro_cycles} cycles for {t_genesis:.4f} Gyr...")
                    for cycle in range(micro_cycles):
                        if n_imnc > 0:
                            imnc_to_smnc = min(n_imnc, max(1, int(n_imnc * 0.05 * flux_efficiency)))
                            n_imnc -= imnc_to_smnc
                            n_smnc += imnc_to_smnc
                        if n_smnc > 0:
                            smnc_to_umnc = min(n_smnc, max(1, int(n_smnc * 0.02 * flux_efficiency)))
                            n_smnc -= smnc_to_umnc
                            n_umnc += smnc_to_umnc
                        if n_umnc > 0 and (t_genesis >= 120.0 or cycle > (micro_cycles * 0.4)):
                            umnc_to_hmnc = min(n_umnc, max(1, int(n_umnc * 0.005 * flux_efficiency)))
                            n_umnc -= umnc_to_hmnc
                            n_hmnc += umnc_to_hmnc

                        if n_imnc > 0 or n_smnc > 0 or n_umnc > 0 or n_hmnc > 0:
                            pull_imnc = random.randint(0, max(1, int(n_imnc * agg_bubble_rate * 0.15))) if n_imnc > 0 else 0
                            pull_smnc = random.randint(0, max(1, int(n_smnc * agg_bubble_rate * 0.25))) if n_smnc > 0 else 0
                            pull_umnc = random.randint(0, max(1, int(n_umnc * agg_bubble_rate * 0.05))) if n_umnc > 0 else 0
                            pull_hmnc = random.randint(0, max(1, int(n_hmnc * 0.01))) if n_hmnc > 0 else 0
                            
                            local_exposure = (pull_hmnc * (50.0**2)) + (pull_umnc * (25.0**2)) + (pull_smnc * (10.0**2)) + (pull_imnc * (0.5**2))
                            ignition_prob = min(0.95, (local_exposure * 8.5e-4) * agg_bubble_rate)
                            
                            if random.random() <= ignition_prob:
                                n_imnc = max(0, n_imnc - pull_imnc)
                                n_smnc = max(0, n_smnc - pull_smnc)
                                n_umnc = max(0, n_umnc - pull_umnc)
                                n_hmnc = max(0, n_hmnc - pull_hmnc)

                    current_object_count = n_umnc + n_hmnc + n_smnc + n_imnc
                    print(f" -> [SUCCESS] Timeline recalculated. Continuing with restored cores at {t_rollback:.4f} Gyr.\n")
                    continue
                else:
                    print(" [FAIL] Target coordinate outside the causal boundary of this aeon.")
            except ValueError:
                print(" [SECURITY] Invalid temporal configuration input.")

        elif jump_choice == 'q':
            print("\n[EXIT] An entire multiverse was erased from existence. You can always come back and create a new one! Goodbye.\n")
            sys.exit(0)
        else:
            print("\n[CONTINUE] Proceeding down current chronological lineage matrix...\n")

if __name__ == "__main__":
    run_interactive_sandbox()
