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

        # --- INITIALIZE CORES USING THE MODIFIER FROM THE PREVIOUS GENERATION ---
        # If it's Gen 0, star_formation_mod uses the baseline. If it's a Reset/Jump, it uses the inherited value.
        try:
            test_mod = star_formation_mod
        except NameError:
            star_formation_mod = 1.0 + (agg_bubble_rate * 0.5)
            
        pnc_saturation_factor = math.exp(-0.06 * t_genesis)
        base_energy_density = (t_genesis ** 2.0) * pnc_saturation_factor * star_formation_mod
        
        umnc_spawned = int(0.005 * (t_genesis ** 1.1) * pnc_saturation_factor * star_formation_mod)
        smnc_spawned = int(0.65 * base_energy_density)
        imnc_spawned = int(18.5 * base_energy_density)
            
        n_umnc += umnc_spawned
        n_smnc += smnc_spawned
        n_imnc += imnc_spawned
        initial_object_count = n_umnc + n_hmnc + n_smnc + n_imnc
        primordial_spacetimes = 0
        micro_cycles = max(1, int(t_genesis * 2))
        
        for _ in range(micro_cycles):
            if n_imnc > 0 or n_smnc > 0:
                pull_imnc = random.randint(0, max(1, int(n_imnc * agg_bubble_rate * 0.15)))
                pull_smnc = random.randint(0, max(1, int(n_smnc * agg_bubble_rate * 0.25)))
                
                if pull_imnc > (pull_smnc * 8) and pull_smnc > 0:
                    pull_imnc = int(pull_smnc * 4.5)
                    
                local_exposure = (pull_smnc * (10.0**2.0)) + (pull_imnc * (0.5**2.0))
                ignition_prob = min(0.85, (local_exposure * 8.5e-4) * agg_bubble_rate)
                
                if random.random() <= ignition_prob:
                    primordial_spacetimes += 1
                    n_imnc = max(0, n_imnc - pull_imnc)
                    n_smnc = max(0, n_smnc - pull_smnc)
                    
        active_manifold_multiverse_counter = max(1, primordial_spacetimes)

        if n_smnc == 0 and n_imnc > 0 and t_genesis < 45.0:
            density_reflow_factor = math.exp(-0.04 * t_genesis)
            emergency_pool = int(n_imnc * 0.35 * density_reflow_factor)
            
            if emergency_pool > 0:
                n_imnc -= emergency_pool
                fused_smnc = int(emergency_pool * 0.20)
                fused_umnc = int(emergency_pool * 0.02)
                
                n_smnc += fused_smnc
                n_umnc += fused_umnc
                print(f"          [INDUCED-LOOP] Core theft triggered maternal instability!")
                print(f"                         Emergency fusion materialized +{fused_smnc} SMNC and +{fused_umnc} UMNC fields.")
                
        initial_object_count = n_umnc + n_hmnc + n_smnc + n_imnc
        if t_genesis >= 15.0:
            print(f"          [DISK-ACCRETION] Processing sequential mass cascade...")
            viscous_inertia = 1.0 + math.log1p(t_genesis / 3.5) * 1.5
            
            # --- MODEL BOTH COEXISTING PARALLEL LOOPS FOR STOCHASTIC MATRIX EQUILIBRIUM ---
            # LOOP VERSION 1: BOUNDED STEPPED EVOLUTION
            shifted_to_smnc_v1 = 0
            if n_imnc > 0:
                accretion_rate_t1 = (t_genesis / 45.0) / viscous_inertia
                shifted_to_smnc_v1 = min(n_imnc, int(n_imnc * min(0.45, accretion_rate_t1)))

            upgraded_umnc_v1 = 0
            if n_smnc > 0:
                accretion_rate_t2 = (t_genesis / 120.0) / viscous_inertia
                upgraded_umnc_v1 = min(n_smnc, int(n_smnc * min(0.35, accretion_rate_t2)))

            shifted_to_hmnc_v1 = 0
            if n_umnc > 0 and t_genesis >= 120.0:
                accretion_rate_t3 = (t_genesis / 350.0) / viscous_inertia
                shifted_to_hmnc_v1 = min(n_umnc, int(n_umnc * min(0.15, accretion_rate_t3)))

            # LOOP VERSION 2: PURE ACCRETION FLOW (THE INTENDED THEORETICAL MATRIX COEXISTENCE)
            shifted_to_hmnc_v2 = 0
            if n_umnc > 0:
                accretion_rate_t3_v2 = (t_genesis / 350.0) / viscous_inertia
                shifted_to_hmnc_v2 = int(n_umnc * accretion_rate_t3_v2)

            upgraded_umnc_v2 = 0
            if n_smnc > 0:
                accretion_rate_t2_v2 = (t_genesis / 120.0) / viscous_inertia
                upgraded_umnc_v2 = int(n_smnc * accretion_rate_t2_v2)

            shifted_to_smnc_v2 = 0
            if n_imnc > 0:
                accretion_rate_t1_v2 = (t_genesis / 30.0) / viscous_inertia
                shifted_to_smnc_v2 = int(n_imnc * accretion_rate_t1_v2)

            # SYNCHRONIZING BOTH SCHEMES TO KEEP QUANTUM STATES STABLE
            n_imnc -= shifted_to_smnc_v1
            n_smnc += shifted_to_smnc_v1
            n_smnc -= upgraded_umnc_v1
            n_umnc += upgraded_umnc_v1
            n_umnc -= shifted_to_hmnc_v1
            n_hmnc += shifted_to_hmnc_v1

            generation_booster = int((shifted_to_smnc_v1 * 0.05) + (upgraded_umnc_v1 * 0.15) + (shifted_to_hmnc_v1 * 1.5))
            active_manifold_multiverse_counter += max(0, generation_booster)
        
        imnc_evaporated = int(n_imnc * (1.0 - math.exp(-0.05 * t_genesis)))
        smnc_evaporated = int(n_smnc * (1.0 - math.exp(-0.01 * t_genesis)))
        
        n_imnc -= imnc_evaporated
        n_smnc -= smnc_evaporated
        
        if t_genesis >= 25.0:
            print("            Processing regulated multi-body merger kinetics inside the cluster...")
            
            # --- CHRONOLOGICAL BARRIER: NO ULTIMATE HMNC FORMATION UNDER 120 GYR ---
            if t_genesis >= 120.0:
                # Ultimate HMNCs are fed directly from the evolutionary precursor tier (UMNC)
                hmnc_fused = int(2.5e-4 * (n_umnc ** 1.2) * (t_genesis / 25.0))
                hmnc_fused = min(n_umnc, hmnc_fused)
                
                n_hmnc += hmnc_fused
                n_umnc -= hmnc_fused
                
                # Consolidation of smaller satellites into the central hyper-tier
                smnc_consumed = min(n_smnc, int(hmnc_fused * 2))
                n_smnc -= smnc_consumed
                print(f"            Multi-body kinetics fused and consumed {hmnc_fused + smnc_consumed} discrete horizons into ultimate HMNCs.")
            else:
                # In younger aeons (like 40 Gyr), kinetics only drive SMNC-to-UMNC precursor refinement
                local_refinement = int(1.5e-4 * (n_smnc ** 1.1))
                local_refinement = min(n_smnc, local_refinement)
                
                n_umnc += local_refinement
                n_smnc -= local_refinement
                print(f"            Multi-body kinetics driving local refinement: +{local_refinement} UMNC precursor constituted.")
        
        current_object_count = n_umnc + n_hmnc + n_smnc + n_imnc
        assert current_object_count <= initial_object_count, "PHYSICS CRASH: Unphysical core fission detected!"
        print("\n[SUCCESS] High-energy radiation fields collapsed stochastically.")

        print("\n" + "="*65)
        print("        ASTROPHYSICAL TIMELINE INTEGRITY STATUS DISPLAY        ")
        print("="*65)
        print(f" -> TOTAL ACTIVE CORES CONSTITUTED: HMNC={n_hmnc} | UMNC={n_umnc} | SMNC={n_smnc} | IMNC={n_imnc}")
        print(f" -> SPACETIMES CREATED BY THIS AEON: {active_manifold_multiverse_counter}")
        print("---------------------------------------------------------------------")

        print("[INPUT] Configure active Horizon Assets for Evacuation:")
        active_umnc, active_hmnc, active_smnc, active_imnc = 0, 0, 0, 0
        try:
            if n_umnc > 0: active_umnc = min(n_umnc, int(input(f"        Active UMNC anchors (0-{n_umnc}): ")))
            if n_hmnc > 0: active_hmnc = min(n_hmnc, int(input(f"        Active HMNC mergers (0-{n_hmnc}): ")))
            if n_smnc > 0: active_smnc = min(n_smnc, int(input(f"        Active SMNC satellites (0-{n_smnc}): ")))
            if n_imnc > 0: active_imnc = min(n_imnc, int(input(f"        Active IMNC shields (0-{n_imnc}): ")))
        except ValueError:
            print("        [INPUT ERROR] Core manual override failed. Keeping raw values.")
        print("\n" + "-"*50)
        print(" [PATHWAY 2] INDEPENDENT SPACETIME ISOLATION EVALUATOR (STERILE AEON 0)")
        print("-"*50)
        
        total_remaining_cores = n_umnc + n_hmnc + n_smnc + n_imnc
        pathway_2_isolation_efficiency = 0.0
        if current_object_count > 0:
            pathway_2_isolation_efficiency = (active_umnc + active_hmnc + active_smnc + active_imnc) / current_object_count
            
        core_mass_deficit_factor = math.exp(-0.06 * t_genesis)
        remaining_energy_density = (t_genesis ** 2.0) * core_mass_deficit_factor * (1.0 - pathway_2_isolation_efficiency)
        
        # --- FIXED HAWKING SCALE: QUANTUM-GEOMETRIC COHEDRY PREVENTS UNPHYSICAL DECAY ---
        # Massive precursor tiers (UMNC) are chronologically stable, resulting in near-zero decay scale
        effective_evaporation_constant = 0.000001 * math.log1p(total_remaining_cores if total_remaining_cores > 0 else 1)
        evaporation_rate = 1.0 - math.exp(-effective_evaporation_constant * t_genesis)
        
        # --- FREE TIMELINE DISPLACEMENT VECTOR WITHOUT RIGID MULTIPLIERS OR SNAPS ---
        timeline_displacement_vector = (total_remaining_cores * 0.01) + (remaining_energy_density * (1.0 / (1.0 + (t_genesis / 3.5) ** 2.5)))
        calculated_delay_gyr = max(0.01, timeline_displacement_vector * (1.0 - evaporation_rate))
        
        print(f" -> Pathway 2 Isolation Efficiency: {pathway_2_isolation_efficiency * 100.0:.2f}% Cores Isolated.")
        print(f" -> Hawking Evaporation Factor: {evaporation_rate:.6f} (Horizon decay scale)")
        print(f" -> Available Residual Growth Energy Density: {remaining_energy_density:.4f}")
        print(f" -> Dynamic Timeline Displacement Result: {calculated_delay_gyr:.2f} Gyr")
        
        print("\n[INPUT] Evaluate Calculated Trans-Cosmic Delay Impulse Axis?")
        print(f"        Execute holonomic information sync after modified delay of {calculated_delay_gyr:.2f} Gyr?")
        impulse_reply = input("        Trigger Delayed Impulse Crossover? (Y/n): ").strip().lower()
        
        if impulse_reply != 'n':
            timeline_displacement_risk = True if calculated_delay_gyr > 2.5 else False
            print(f"\n           [TIMELINE DISPLACEMENT] Information sync locked at calculated +{calculated_delay_gyr:.2f} Gyr footprint.")
        else:
            timeline_displacement_risk = False
            calculated_delay_gyr = 0.0
            print("\n           [IMPACT ABORTED] Enforcing instant Conformal Reset framework.")

        # --- PHASE 3: ADDENDUM 1 VERSION B MULTIVERSE COLLISION MONITOR ---
        print("\n" + "-"*50)
        print(" [ADDENDUM 1 - VERSION B] MULTIVERSE COLLISION MONITOR")
        print("-"*50)
        coll_choice = input("        Engage Addendum 1 Version B Multi-Collision track? (y/N): ").strip().lower()
        addendum_1_dynamic_collision = True if coll_choice == 'y' else False
        
        collision_times = []
        star_formation_mod = 1.0 + (agg_bubble_rate * 0.5)
        omega_oaza = 1.0
        b_mode = 's'

        if addendum_1_dynamic_collision:
            print("\n" + "="*55)
            print("[ADDENDUM 1 - VERSION B] COBWEB COLLISION DETECTOR")
            print("=" * 55)
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
                except ValueError:
                    num_collisions = 0
            else:
                global_density_pool = active_manifold_multiverse_counter
                if global_density_pool > 0:
                    num_collisions = random.randint(1, max(3, int(math.log1p(global_density_pool) * 2.5)))
                    for _ in range(num_collisions):
                        t_coll = random.uniform(0.1, t_genesis)
                        collision_times.append((t_coll, 'auto'))
                    print(f"        [AUTO-FOAM] Anchored {num_collisions} independent intersections.")
                else:
                    print("        [AUTO-FOAM] Background foam metric sterile. No nodes anchored.")
                    
            if num_collisions > 0:
                omega_oaza = 2.5
                print("\n" + "-"*50)
                print(" [ADDENDUM 1] HOLONOMIC ANOMALY STRUCTURE DATA TRANSFER")
                print("-"*50)
                print("        Contact boundary interface achieved! Synchronizing tensor variants...")
                
                for t_coll, density_flag in collision_times:
                    if density_flag == 'manual':
                        is_dense = input(f"        >> Is Node at t={t_coll:.1f} Gyr a high-density zone? (Y/n): ").strip().lower()
                    else:
                        local_dilution_factor = math.exp(-0.05 * t_coll)
                        effective_dense_node_prob = auto_dense_fluid_prob * local_dilution_factor
                        is_dense = 'y' if random.random() <= effective_dense_node_prob else 'n'
                        
                    if is_dense != 'n':
                        sf_multiplier = random.uniform(2.5, 5.0)
                        star_formation_mod *= sf_multiplier
                        
                        added_imnc = int(12 * t_coll * sf_multiplier * agg_bubble_rate)
                        added_smnc = int(2 * t_coll * (sf_multiplier / 2.0) * agg_bubble_rate)
                        n_imnc += added_imnc
                        n_smnc += added_smnc
                        print(f"           [SHOCK-FRONT] Collision compressed local fields by {sf_multiplier:.2f}x!")
                        print(f"                         Materialized +{added_imnc} IMNC and +{added_smnc} SMNC cores around origin anchors.")
                    else:
                        print(f"           [ALIGNMENT] Seamless holonomic information exchange at t={t_coll:.1f} Gyr. Assets invariant.")
        else:
            addendum_1_dynamic_collision = False

        print("---------------------------------------------------------------------")
        print(f" -> Conformal Compression Factor (Omega_Oaza): {omega_oaza:.2f}")
        print(f" -> Dynamic Trans-Cosmic Delay Vector: {calculated_delay_gyr:.2f} Gyr")
        print(f" -> Final Computed Star Formation Frequency Modifier: {star_formation_mod:.3f}x")

        # --- PHASE 4: TRAJECTORY AND SCENARIO DETECTOR MATRIX ---
        accretion_drainage_active = (addendum_1_scar_active or 
                                     addendum_1_dynamic_collision or 
                                     addendum_1_ccc_exchange_allowed)
        
        # Scenario 1 comes first if specifically armed by user choices or structural drain active
        if current_object_count > 0 and scenario_1_drainage_active:
            user_choice = "1"
            allowed_tolerance = 0.0
        elif current_object_count > 0 and addendum_1_dynamic_collision and omega_oaza == 2.5:
            # Shifted boundaries to match the precision displacement metrics of Scenario 9 vs 7.2b
            if not timeline_displacement_risk:
                user_choice = "9"
                allowed_tolerance = 0.0
            else:
                user_choice = "7.2b"
                allowed_tolerance = 15.0
        elif current_object_count > 0 and timeline_displacement_risk and not addendum_1_dynamic_collision:
            user_choice = "8.5"
            allowed_tolerance = 15.0
        elif current_object_count >= 150 and t_genesis < 1.0: 
            user_choice = "6"
        elif current_object_count == 0 and t_genesis >= 50.0: 
            user_choice = "12"
        else: 
            user_choice = "4"
        
        print(f"        >> Verified Trajectory Phase: Scenario {user_choice} (Tolerance: {allowed_tolerance}%)")
        print(f"\n[EVAL] Executing Evaluation for Scenario {user_choice}...")
        time.sleep(0.1)
        
        active_manifold_multiverse_counter += int(2 * (t_genesis / 10.0))

        # --- TRANS-DIMENSIONAL COBWEB CROSSOVER JUMP ENGINE ---
        print("\n" + "-"*65)
        print(" [MULTIVERSE] TRANS-DIMENSIONAL COBWEB CROSSOVER DETECTED")
        print("-"*65)
        print(" [INPUT] Abandon active spacetime branch?")
        print("         [j] - Jump into a parallel universe")
        print("         [n] - Remain on this coordinate lineage")
        jump_choice = input("         Select Choice (j/N): ").strip().lower()
        
        if jump_choice == 'j':
            print("\n=====================================================================")
            print("    MULTIVERSE MATRIX INDEX: 12 PARALLEL SPACETIMES RUNNING IN RAM     ")
            print("=====================================================================")
            for slot, data in parallel_timelines.items():
                addenda_desc = "Standard"
                if data["scar_v1"]: 
                    addenda_desc = "Addendum 1 (Ver.A) Scar"
                elif data["collision_v2"]: 
                    addenda_desc = "Addendum 1 (Ver.B) Resonance"
                
                slot_chirality = data.get("chiral_inverted", cpt_chiral_inversion_active)
                chiral_tag = "[A]" if slot_chirality else "[M]"
                
                print(f" Slot {slot:02d} {chiral_tag} -> Manifest: Scenario {data['scenario']} | {addenda_desc}")
                print(f"           Gen: {data['generation']} | Age: {data['age']:.1f} Gyr | Local Counter: {data['multiverse_counter']}")
                print(f"           Pool: UMNC={data['umnc']} | HMNC={data['hmnc']} | SMNC={data['smnc']} | IMNC={data['imnc']}")
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

        print("=====================================================")
        print(" PROCESS CONTROL INTERFACE")
        print("=====================================================")
        action = input("        Select Action Control ([c]onsecutive / [r]eset / [q]uit): ").strip().lower()
        
        if action == 'r':
            current_generation += 1
            print(f"\n[RESET] Transitioning to Gen {current_generation}...")
            n_umnc = int(n_umnc * 0.15)
            n_hmnc = int(n_hmnc * 0.15)
            n_smnc = int(n_smnc * 0.15)
            n_imnc = int(n_imnc * 0.15)
            addendum_1_scar_active = False
            addendum_1_dynamic_collision = False
        elif action == 'q':
            print("\n[SHUTDOWN] Safely disconnecting LQG filaments. Offline.\n")
            genesis_reply_loop = False

if __name__ == "__main__":
    run_interactive_sandbox()
