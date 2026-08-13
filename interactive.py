#!/usr/bin/env python3
import math
import time
import random
import os
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
    print("        COSMIC PIRACY SIMULATION - STATE ENGINE v33.0 (ASCII MATRIX)")
    print("        Background-Independent Quantum-Geometric Graph Evaluator")
    print("=====================================================================\n")
    
    current_generation = 0
    n_umnc, n_hmnc, n_smnc, n_imnc = 0, 0, 0, 0
    pathway_2_allowed = False
    scenario_1_drainage_active = False
    addendum_1_scar_active = False
    addendum_1_dynamic_collision = False
    addendum_1_ccc_exchange_allowed = False
    cpt_chiral_inversion_active = False
    timeline_displacement_risk = False
    dev_mode = False
    auto_mode = False
    
    parallel_timelines = {}
    for slot in range(1, 13):
        parallel_timelines[slot] = {
            "umnc": 0, "hmnc": 0, "smnc": 10, "imnc": 253,
            "generation": 0, "age": 4.0,
            "scenario": "6 (Multi-Core Cluster Baseline)",
            "scar_v1": False, "collision_v2": False,
            "multiverse_counter": random.randint(5, 50),
            "replacement_shield": True if slot == 12 else False
        }
    active_manifold_multiverse_counter = 0
    genesis_reply_loop = True
    while genesis_reply_loop:
        print("[INPUT] Initialize at Scenario 0 (Global CPT Crossover Node)?")
        genesis_reply = input("        Trigger Ur-Genesis Phase (Y/n): ").strip().lower()
        
        if genesis_reply != 'y':
            print("\n[CRITICAL RESET] Enforcing Conformal Cyclic Reset!")
            print("                 -> Result: Instant metric scale loss.\n")
            time.sleep(0.4)
            n_umnc, n_hmnc, n_smnc, n_imnc = 0, 0, 0, 0
            continue 

        print("\n[PHASE 0] AEON 0 - PRIMORDIAL SEEDING AND BOUNDARY GATES")
        print("---------------------------------------------------------------------")
        print("[INPUT] Enter target timescale for Aeon 0 PNC growth phase:")
        t_input_str = input("        Delta t_0 (in Gyr, e.g. 4.0 or infinity): ").strip().lower()
        
        if t_input_str == "infinity":
            t_genesis = 150.0  
            print("          [INFINITY] Running forward thermodynamic dilution...")
        else:
            try:
                t_genesis = float(t_input_str)
            except ValueError:
                t_genesis = 4.0
                print("          [INVALID] Defaulting to baseline timescale 4.0 Gyr.")

        try:
            print("\n[INPUT] Configure Multi-Bubble Generation Flux:")
            agg_bubble_rate = float(input("        >> Enter creation aggressiveness (0.01 - 0.99): "))
            agg_bubble_rate = max(0.01, min(0.99, agg_bubble_rate))
        except ValueError:
            agg_bubble_rate = 0.25

        try:
            test_mod = star_formation_mod
        except NameError:
            star_formation_mod = 1.0 + (agg_bubble_rate * 0.5)

        # --- DYNAMIC BOUNDED SEEDING MATRIX (NO BASELINES) ---
        conformal_saturation = math.tanh(t_genesis / 15.0)
        umnc_spawned = int(6.0 * conformal_saturation * star_formation_mod)
        smnc_spawned = int(400.0 * conformal_saturation * (1.0 + math.log1p(t_genesis * 0.02)) * star_formation_mod)
        imnc_spawned = int(1600.0 * conformal_saturation * (1.0 + math.log1p(t_genesis * 0.05)) * star_formation_mod)
            
        n_umnc = umnc_spawned
        n_hmnc = 0
        n_smnc = smnc_spawned
        n_imnc = imnc_spawned
        initial_object_count = n_umnc + n_hmnc + n_smnc + n_imnc
        
        primordial_spacetimes = 0
        micro_cycles = max(100, int(math.log1p(t_genesis) * 120.0)) if t_genesis > 1000.0 else max(1, int(t_genesis * 2))
        flux_efficiency = 1.0 / (1.0 + math.log1p(1.0 / agg_bubble_rate))
        
        # --- SCALE-INVARIANCE GUARD ---
        scale_invariance_breach = False
        if t_genesis <= 0.0001:
            print("\n           [WARNING]: CRITICAL PHASE LIMIT REACHED! DETECTING EXTREME SCALE SLIPPAGE.")
            if initial_object_count > 0:
                print("                      Primordial PNC density prevents complete Conformal Scale Invariance Collapse.")
            else:
                scale_invariance_breach = True
                print("                      [METRIC EXITUS]: Scale Invariance Collapse uninhibited! System sterile.")
        print(f"          [COSMOLOGICAL EVOLUTION]: Processing {micro_cycles} epochal matrix cycles...")
        
        for cycle in range(micro_cycles):
            if scale_invariance_breach:
                break
                
            # 1. RIGID UPWARD MASS KINETICS (MASS CONSERVATION PRIOR TO EVACUATION)
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

            # 2. THE ORIGINAL MULTI-BUBBLE FLUX & PROBABILITY ENGINE
            if n_imnc > 0 or n_smnc > 0 or n_umnc > 0 or n_hmnc > 0:
                pull_imnc = random.randint(0, max(1, int(n_imnc * agg_bubble_rate * 0.15))) if n_imnc > 0 else 0
                pull_smnc = random.randint(0, max(1, int(n_smnc * agg_bubble_rate * 0.25))) if n_smnc > 0 else 0
                pull_umnc = random.randint(0, max(1, int(n_umnc * agg_bubble_rate * 0.05))) if n_umnc > 0 else 0
                pull_hmnc = random.randint(0, max(1, int(n_hmnc * agg_bubble_rate * 0.01))) if n_hmnc > 0 else 0
                
                local_exposure = (pull_hmnc * (50.0**2.0)) + (pull_umnc * (25.0**2.0)) + (pull_smnc * (10.0**2.0)) + (pull_imnc * (0.5**2.0))
                ignition_prob = min(0.95, (local_exposure * 8.5e-4) * agg_bubble_rate)
                
                # 3. SUCCESSFUL TRANSITION CONSUMES AND EVACUATES THE TRIGGER CORES
                if random.random() <= ignition_prob:
                    primordial_spacetimes += 1
                    n_imnc = max(0, n_imnc - pull_imnc)
                    n_smnc = max(0, n_smnc - pull_smnc)
                    n_umnc = max(0, n_umnc - pull_umnc)
                    n_hmnc = max(0, n_hmnc - pull_hmnc)

            # 4. DYNAMIC HAWKING RADIATION BALANCE CURVE FOR REMAINING CORES
            r_imnc = 1.0 / ((1.0 + n_imnc * 0.05) ** 3.0) if n_imnc > 0 else 0
            r_smnc = 1.0 / ((50.0 + n_smnc * 1.0) ** 3.0) if n_smnc > 0 else 0
            r_umnc = 1.0 / ((1000.0 + n_umnc * 5.0) ** 3.0) if n_umnc > 0 else 0
            r_hmnc = 1.0 / ((1e8 + n_hmnc * 100.0) ** 3.0) if n_hmnc > 0 else 0
            
            imnc_evap = min(n_imnc, int(n_imnc * (1.0 - math.exp(-r_imnc * (t_genesis / micro_cycles)))))
            smnc_evap = min(n_smnc, int(n_smnc * (1.0 - math.exp(-r_smnc * (t_genesis / micro_cycles)))))
            umnc_evap = min(n_umnc, int(n_umnc * (1.0 - math.exp(-r_umnc * (t_genesis / micro_cycles)))))
            hmnc_evap = min(n_hmnc, int(n_hmnc * (1.0 - math.exp(-r_hmnc * (t_genesis / micro_cycles)))))
            
            n_imnc -= imnc_evap
            n_smnc -= smnc_evap
            n_umnc -= umnc_evap
            n_hmnc -= hmnc_evap

        active_manifold_multiverse_counter = primordial_spacetimes
        current_object_count = n_umnc + n_hmnc + n_smnc + n_imnc
        print("\n[SUCCESS] Universal quantum-geometric fields processed stochastically.")
        print("\n" + "="*65)
        print("        ASTROPHYSICAL TIMELINE INTEGRITY STATUS DISPLAY        ")
        print("="*65)
        print(f" -> TOTAL ACTIVE CORES CONSTITUTED: HMNC={n_hmnc} | UMNC={n_umnc} | SMNC={n_smnc} | IMNC={n_imnc}")
        print(f" -> SPACETIMES CREATED BY THIS AEON: {active_manifold_multiverse_counter}")
        print("---------------------------------------------------------------------")
        # --- CRITICAL LOCKOUT: RE-ENFORCING INDEPENDENT ADDENDA 1 A & B ---
        if current_object_count == 0:
            print("\n [WARNING]: TOTAL THERMODYNAMIC VACUUM DETECTED. ALL HORIZONS EVAPORATED.")
            print("            Conformal scale unanchored. Space-time closure forces immediate holonomic sequence.")
            
            # Resetting tracking constants for the empty aeon checkpoint
            calculated_delay_gyr = float('inf')
            user_choice = "12"
            timeline_displacement_risk = True
            remaining_energy_density = 0.0
            pathway_2_isolation_efficiency = 0.0
            
            # --- PHASE 1 (VACUUM TRACK): ADDENDUM 1 VERSION A - PRIMEVAL METRIC DRAINAGE ---
            print("\n" + "-"*50)
            print(" [ADDENDUM 1 - VERSION A] PRIMEVAL METRIC DRAINAGE INTERFACE (VACUUM NODE)")
            print("-"*50)
            drain_choice = input("        Trigger Scenario 1 Localized Metric Drainage? (y/N): ").strip().lower()
            scenario_1_drainage_active = True if drain_choice == 'y' else False
            addendum_1_scar_active = True if scenario_1_drainage_active else False
            if addendum_1_scar_active:
                print("           [TOPOLOGICAL SEAM] Network rupture verified. Conical scar encoded into local metric.")

            # --- PHASE 3 (VACUUM TRACK): ADDENDUM 1 VERSION B - MULTIVERSE COLLISION MONITOR ---
            print("\n" + "-"*50)
            print(" [ADDENDUM 1 - VERSION B] MULTIVERSE COLLISION MONITOR (VACUUM NODE)")
            print("-"*50)
            coll_choice = input("        Engage Addendum 1 Version B Multi-Collision track? (y/N): ").strip().lower()
            addendum_1_dynamic_collision = True if coll_choice == 'y' else False
            
            collision_times = []
            star_formation_mod = 1.0 + (agg_bubble_rate * 0.5)
            omega_oaza = 1.0
            
            if addendum_1_dynamic_collision:
                print("\n=====================================================")
                print("[ADDENDUM 1 - VERSION B] COBWEB COLLISION DETECTOR")
                print("=====================================================")
                b_mode = input("        Select Intersection Detection Mode ([m]anual / [s]tochastic): ").strip().lower()
                num_collisions = 0
                auto_dense_fluid_prob = 0.5

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

        else:
            # --- REGULAR PATHWAY FOR ACTIVE MATRIX (CORES SURVIVED) ---
            print("[INPUT] Configure active Horizon Assets for Evacuation:")
            active_umnc, active_hmnc, active_smnc, active_imnc = 0, 0, 0, 0
            try:
                if n_umnc > 0: active_umnc = min(n_umnc, int(input(f"        Active UMNC anchors (0-{n_umnc}): ")))
                if n_hmnc > 0: active_hmnc = min(n_hmnc, int(input(f"        Active HMNC mergers (0-{n_hmnc}): ")))
                if n_smnc > 0: active_smnc = min(n_smnc, int(input(f"        Active SMNC satellites (0-{n_smnc}): ")))
                if n_imnc > 0: active_imnc = min(n_imnc, int(input(f"        Active IMNC shields (0-{n_imnc}): ")))
            except ValueError:
                print("        [INPUT ERROR] Core manual override failed. Keeping raw values.")

            # --- PHASE 1 (REGULAR): ADDENDUM 1 VERSION A - PRIMEVAL METRIC DRAINAGE ---
            print("\n" + "-"*50)
            print(" [SCENARIO 1 / ADDENDUM 1A] PRIMEVAL METRIC DRAINAGE INTERFACE")
            print("-"*50)
            drain_choice = input("        Trigger Scenario 1 Localized Metric Drainage? (y/N): ").strip().lower()
            scenario_1_drainage_active = True if drain_choice == 'y' else False
            addendum_1_scar_active = True if scenario_1_drainage_active else False

            # --- PHASE 2 (REGULAR): PATHWAY 2 INDEPENDENT SPACETIME ISOLATION EVALUATOR ---
            print("\n" + "-"*50)
            print(" [PATHWAY 2] INDEPENDENT SPACETIME ISOLATION EVALUATOR (STERILE AEON 0)")
            print("-"*50)
            
            pathway_2_isolation_efficiency = (active_umnc + active_hmnc + active_smnc + active_imnc) / current_object_count
            core_mass_deficit_factor = math.exp(-0.06 * min(150.0, t_genesis))
            remaining_energy_density = (t_genesis ** 2.0) * core_mass_deficit_factor * (1.0 - pathway_2_isolation_efficiency)
            
            conformal_entropy_slippage = 0.25 * math.sin(min(150.0, t_genesis)) + 0.50
            
            # --- PERFECT MASS COUPLING: OVERRIDING THE FLOATING LOWER BOUND ---
            base_displacement = (min(150.0, t_genesis) * 0.15) + conformal_entropy_slippage
            calculated_delay_gyr = base_displacement * (1.0 - pathway_2_isolation_efficiency)
            
            if calculated_delay_gyr < 0.0001:
                calculated_delay_gyr = 0.0
            
            print(f" -> Pathway 2 Isolation Efficiency: {pathway_2_isolation_efficiency * 100.0:.2f}% Cores Isolated.")
            print(f" -> Available Residual Growth Energy Density: {remaining_energy_density:.4f}")
            print(f" -> Dynamic Timeline Displacement Result: {calculated_delay_gyr:.2f} Gyr")
            
            print("\n[INPUT] Evaluate Calculated Trans-Cosmic Delay Impulse Axis?")
            
            # --- DYNAMIC INTERFACE PROMPT BASED ON TIMELINE DELAY SHIFT ---
            if calculated_delay_gyr == 0.0:
                print("        Execute instant holonomic information sync?")
                impulse_reply = input("        Trigger Instant Impulse Crossover? (Y/n): ").strip().lower()
            else:
                print(f"        Execute holonomic information sync after modified delay of {calculated_delay_gyr:.2f} Gyr?")
                impulse_reply = input("        Trigger Delayed Impulse Crossover? (Y/n): ").strip().lower()
                
            timeline_displacement_risk = True if (calculated_delay_gyr > 2.5 and impulse_reply != 'n') else False

            # --- PHASE 3 (REGULAR): ADDENDUM 1 VERSION B - MULTIVERSE COLLISION MONITOR ---
            print("\n" + "-"*50)
            print(" [ADDENDUM 1 - VERSION B] MULTIVERSE COLLISION MONITOR")
            print("-"*50)
            coll_choice = input("        Engage Addendum 1 Version B Multi-Collision track? (y/N): ").strip().lower()
            addendum_1_dynamic_collision = True if coll_choice == 'y' else False
            
            collision_times = []
            star_formation_mod = 1.0 + (agg_bubble_rate * 0.5)
            omega_oaza = 1.0
            
            if addendum_1_dynamic_collision:
                print("\n=====================================================")
                print("[ADDENDUM 1 - VERSION B] COBWEB COLLISION DETECTOR")
                print("=====================================================")
                # --- UX LEGEND FOR THE REGULAR COBWEB TRACK ---
                print("        Select Intersection Detection Mode:")
                print("               [m] - Manual Configuration Node")
                print("               [s] - Stochastic Hyper-Foam (Fully Automated)")
                b_mode = input("        Select Mode (m/S): ").strip().lower()
                num_collisions = 0
                auto_dense_fluid_prob = 0.5

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
            else:
                addendum_1_dynamic_collision = False

        # --- COMBINED METRIC TERMINATION AND STATUS DISPLAY ---
        print("---------------------------------------------------------------------")
        print(f" -> Conformal Compression Factor (Omega_Oaza): {omega_oaza:.2f}")
        print(f" -> Dynamic Trans-Cosmic Delay Vector: {calculated_delay_gyr if calculated_delay_gyr != float('inf') else 'INFINITE'} Gyr")
        print(f" -> Final Computed Star Formation Frequency Modifier: {star_formation_mod:.3f}x")

        # --- PHASE 4: TRAJECTORY PHASE ASSIGNMENT ---
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
        time.sleep(0.1)
        active_manifold_multiverse_counter += int(2 * (min(150.0, t_genesis) / 10.0))

        # --- UI EXPLORER TOOL: CPT CHIRALITY INVERSION & EVOLUTIONARY IGNORANCE INDEX ---
        for slot in range(1, 13):
            data = parallel_timelines[slot]
            ui_write_chance = 0.45 * flux_efficiency
            if timeline_displacement_risk:
                ui_write_chance *= 0.15
            if data.get("replacement_shield", False):
                ui_write_chance *= 0.50
                
            if random.random() <= ui_write_chance:
                # CPT Chirality Inversion Filter (Matter-Antimatter mismatch reflection at the Big Bang)
                mass_mismatch = abs((n_umnc + n_smnc + n_hmnc) - (data.get("umnc", 0) + data.get("smnc", 0) + data.get("hmnc", 0)))
                if mass_mismatch > 100:
                    data["chiral_inverted"] = True
                else:
                    data["chiral_inverted"] = False
                    
                ignorance_threshold = random.uniform(0.1, 12.0)
                is_evolutionary_severed = False
                current_delay = calculated_delay_gyr
                if current_delay == float('inf') or current_delay > ignorance_threshold:
                    is_evolutionary_severed = True
                    
                if is_evolutionary_severed:
                    data["generation"] = data.get("generation", 0) + random.randint(1, 5)
                    delay_string = "INFINITE" if current_delay == float('inf') else f"+{current_delay:.2f}"
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

        # --- TRANS-DIMENSIONAL COBWEB CROSSOVER DETECTED ---
        print("\n" + "-"*65)
        print(" [MULTIVERSE] TRANS-DIMENSIONAL COBWEB CROSSOVER DETECTED")
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
                addenda_desc = "Standard"
                if data.get("scar_v1"): 
                    addenda_desc = "Addendum 1 (Ver.A) Scar"
                elif data.get("collision_v2"): 
                    addenda_desc = "Addendum 1 (Ver.B) Resonance"
                
                slot_chirality = data.get("chiral_inverted", False)
                chiral_tag = "[A]" if slot_chirality else "[M]"
                
                print(f" Slot {slot:02d} {chiral_tag} -> Manifest: {data.get('scenario', 'Unknown')}")
                print(f"           Gen: {data.get('generation', 0)} | Age: {data.get('age', 0.0):.1f} Gyr | Local Counter: {data.get('multiverse_counter', 0)}")
                print(f"           Pool: UMNC={data.get('umnc', 0)} | HMNC={data.get('hmnc', 0)} | SMNC={data.get('smnc', 0)} | IMNC={data.get('imnc', 0)}")
                print(" ---------------------------------------------------------------------")

            print("=====================================================")
            try:
                target_slot = int(input(" >> Select target Timeline Slot to jump into (1-12): "))
                if target_slot in parallel_timelines:
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
                else:
                    print(" [FAIL] Target slot boundary unstable. Jump aborted.")
            except ValueError:
                print(" [SECURITY] Invalid coordinate selection.")
                
        elif jump_choice == 'r':
            current_generation += 1
            print(f"\n" + "="*65)
            print(f" [UR-GENESIS] BIFURCATION MATRIX - GENERATION {current_generation}")
            print("="*65)
            print("        Capturing evacuated horizon assets for child-spacetime injection...")
            
            isolated_umnc = locals().get('active_umnc', 0)
            isolated_hmnc = locals().get('active_hmnc', 0)
            isolated_smnc = locals().get('active_smnc', 0)
            isolated_imnc = locals().get('active_imnc', 0)
            
            print(f"        -> Injecting invariant anchors: HMNC={isolated_hmnc} | UMNC={isolated_umnc}")
            
            try:
                print("\n[INPUT] Configure child aeon timeline boundaries:")
                t_genesis_new = float(input(f"        >> Set target timescale for Generation {current_generation} phase (Gyr): "))
                t_genesis = max(0.0001, t_genesis_new)
            except ValueError:
                t_genesis = 4.0
                print("        [INVALID] Defaulting child timescale baseline to 4.0 Gyr.")
                
            print("\n[EVAL] Sampling stochastic overlap between LQG Tensile Limit and Higgs scalar onset...")
            time.sleep(0.2)
            
            higgs_roll = random.random()
            if hmnc_evap == 0 and umnc_evap == 0 and current_object_count > 0:
                higgs_roll = random.choice([0.1, 0.5])
                
            if higgs_roll < 0.20:
                # 1. Instantaneous Vacuum Drop (Higgs == LQG)
                assigned_scenario = "9"
                allowed_tolerance = 0.0
                print("           [STATUS]: Instantaneous Vacuum Drop (Higgs == LQG) triggered!")
                print("                     Immediate vacuum tunneling active. Precision tolerance: 0%.")
                star_formation_mod = 1.0
            elif higgs_roll < 0.75:
                # 2. Delayed Transition (Higgs < LQG)
                assigned_scenario = "7.2b"
                allowed_tolerance = 15.0
                print("           [STATUS]: Delayed Transition (Higgs < LQG) registered.")
                print("                     Fluid influx exposed to parent plasma fluctuations. Tolerance: +/-15%.")
                star_formation_mod = random.uniform(0.85, 1.15)
            else:
                # 3. Suppressed Phase Transition (Higgs > LQG)
                assigned_scenario = "3a" if random.random() < 0.5 else "4"
                allowed_tolerance = 0.0
                print("           [STATUS]: Suppressed Phase Transition (Higgs > LQG) invoked.")
                print("                     Pathway 3 shockwave quenched. Bound strictly to baseline parameters.")
                star_formation_mod = 1.0

            print(f"\n[RESET] Compressing and transferring rest-mass into Conformal Generation {current_generation}...")
            n_umnc = isolated_umnc + int((n_umnc * 0.15))
            n_hmnc = isolated_hmnc + int((n_hmnc * 0.15))
            n_smnc = isolated_smnc + int((n_smnc * 0.15))
            n_imnc = isolated_imnc + int((n_imnc * 0.15))
            
            addendum_1_scar_active = False
            addendum_1_dynamic_collision = False
            print(f" -> [SUCCESS] Child-spacetime initialized. Target Scenario Horizon: {assigned_scenario}\n")
            continue

        elif jump_choice == 'b':
            print("\n[TEMPORAL BOUNCE] Initiating localized timeline regression...")
            try:
                t_rollback = float(input("         >> Enter target epoch to bounce back to (Gyr): "))
                if 0.0 <= t_rollback <= t_genesis:
                    t_genesis = t_rollback
                    print(f" -> [SUCCESS] Coordinates shifted. Continuing from localized footprint at {t_rollback:.4f} Gyr.\n")
                    continue
                else:
                    print(" [FAIL] Target coordinate outside the causal boundary of this aeon.")
            except ValueError:
                print(" [SECURITY] Invalid temporal configuration input.")

        elif jump_choice == 'q':
            print("\n[SHUTDOWN] Safely disconnecting LQG filaments. Offline.\n")
            genesis_reply_loop = False
            break
            
        else:
            print("\n[CONTINUE] Proceeding down current chronological lineage matrix...\n")

if __name__ == "__main__":
    run_interactive_sandbox()
