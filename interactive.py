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
    
    mass_weights = {
        "umnc": 50.0, "hmnc": 25.0, "smnc": 10.0,
        "imnc": 0.5,  "pnc":  0.01
    }
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
    
    # --- VERSION 33.0: 13-CHANNEL MULTIVERSE INITIALIZATION ---
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
        try:
            print("[INPUT] Enter target timescale for Aeon 0 PNC growth phase:")
            t_input_str = input("        Delta t_0 (in Gyr, e.g. 4.0 or infinity): ").strip().lower()
            
            if t_input_str == "infinity":
                t_genesis = 150.0  # Asymptotic thermodynamic ceiling
                print("          [INFINITY] Running forward thermodynamic dilution...")
            else:
                t_genesis = float(t_input_str)
            
            # --- FIXED v33.0: PURE PRIMORDIAL CORES FIELD SATURATION LAW ---
            # All artificial min/max caps are eliminated for absolute continuity.
            pnc_saturation_factor = math.exp(-0.06 * t_genesis)
            base_energy_density = (t_genesis ** 2.0) * pnc_saturation_factor
            
            # Core spawning follows pure non-linear exponential dynamics
            umnc_spawned = int(0.005 * (t_genesis ** 1.1) * pnc_saturation_factor)
            smnc_spawned = int(0.65 * base_energy_density)
            imnc_spawned = int(18.5 * base_energy_density)
                
            n_umnc += umnc_spawned
            n_smnc += smnc_spawned
            n_imnc += imnc_spawned
            initial_object_count = n_umnc + n_hmnc + n_smnc + n_imnc

            # --- AGGRESSIVENESS INITIALIZATION IN AEON 0 ---
            try:
                print("\n[INPUT] Configure Multi-Bubble Generation Flux:")
                agg_bubble_rate = float(input("        >> Enter creation aggressiveness (0.01 - 0.99): "))
                agg_bubble_rate = max(0.01, min(0.99, agg_bubble_rate))
            except ValueError:
                agg_bubble_rate = 0.25

            # --- FIXED v33.0: STOCHASTIC CLUSTER STABILITY & SHRINKAGE ---
            # Randomly spawns core clusters that gather to ignite bubble universes.
            # Loose ratios cannot hold together and shrink safely to prevent complete collapse!
            primordial_spacetimes = 0
            
            # Simulate structural micro-fluctuations over the time horizon
            micro_cycles = max(1, int(t_genesis * 2))
            for _ in range(micro_cycles):
                if n_imnc > 0 or n_smnc > 0:
                    # Gather a raw, random cluster of assets for an ignition attempt
                    pull_imnc = random.randint(0, max(1, int(n_imnc * agg_bubble_rate * 0.15)))
                    pull_smnc = random.randint(0, max(1, int(n_smnc * agg_bubble_rate * 0.25)))
                    
                    # Mass-Ratio Verification: Heavy cores must bind peripheral shields
                    # A loose 44:772 ratio triggers heavy centrifugal shedding
                    if pull_imnc > (pull_smnc * 8) and pull_smnc > 0:
                        # Cluster shrinks automatically to a sub-critical stable configuration
                        pull_imnc = int(pull_smnc * 4.5)
                        
                    # Calculate local horizon surface area exposed to quantum stress
                    local_exposure = (pull_smnc * (10.0**2.0)) + (pull_imnc * (0.5**2.0))
                    ignition_prob = min(0.85, (local_exposure * 8.5e-4) * agg_bubble_rate)
                    
                    if random.random() <= ignition_prob:
                        primordial_spacetimes += 1
                        # The escaping assets are physically extracted and dragged into the new branch!
                        n_imnc = max(0, n_imnc - pull_imnc)
                        n_smnc = max(0, n_smnc - pull_smnc)
                        
            active_manifold_multiverse_counter = max(1, primordial_spacetimes)
            initial_object_count = n_umnc + n_hmnc + n_smnc + n_imnc

            if t_genesis >= 15.0:
                print(f"          [DISK-ACCRETION] Pure era depth ({t_genesis} Gyr) drives core growth...")
                
                # Tier 1: IMNC to SMNC conversion scales naturally with time depth
                shifted_to_smnc = 0
                if n_imnc > 0:
                    accretion_rate_t1 = t_genesis / 40.0
                    shifted_to_smnc = int(n_imnc * accretion_rate_t1)
                    if shifted_to_smnc > 0:
                        n_imnc -= shifted_to_smnc
                        n_smnc += shifted_to_smnc
                        print(f"                            Accretion Tier 1: IMNC to SMNC resolved.")
                
                # Tier 2: SMNC to HMNC conversion
                shifted_to_hmnc = 0
                if n_smnc > 0:
                    accretion_rate_t2 = t_genesis / 50.0
                    shifted_to_hmnc = int(n_smnc * accretion_rate_t2)
                    if shifted_to_hmnc > 0:
                        n_smnc -= shifted_to_hmnc
                        n_hmnc += shifted_to_hmnc
                        print(f"                            Accretion Tier 2: SMNC to HMNC resolved.")

                # Tier 3: HMNC to UMNC conversion
                upgraded_umnc = 0
                if n_hmnc > 0:
                    accretion_rate_t3 = t_genesis / 60.0
                    upgraded_umnc = int(n_hmnc * accretion_rate_t3)
                    if upgraded_umnc > 0:
                        n_hmnc -= upgraded_umnc
                        n_umnc += upgraded_umnc
                        print(f"                            Accretion Tier 3: HMNC to UMNC resolved.")
            
            # Continuous evaporation without floor enforcement
            imnc_evaporated = int(n_imnc * (1.0 - math.exp(-0.05 * t_genesis)))
            smnc_evaporated = int(n_smnc * (1.0 - math.exp(-0.01 * t_genesis)))
            
            n_imnc -= imnc_evaporated
            n_smnc -= smnc_evaporated
            hmnc_fused = 0
            umnc_consumed = 0
            if t_genesis >= 25.0:
                print("            Processing regulated multi-body merger kinetics inside the cluster...")
                hmnc_fused = int(2.5e-4 * (n_smnc ** 1.5) * (t_genesis / 25.0))
                max_fused = int(n_smnc * 0.50 / 3)
                if hmnc_fused > max_fused: hmnc_fused = max_fused
                
                n_hmnc += hmnc_fused
                n_smnc -= (hmnc_fused * 3) 
                
                umnc_consumed = int(n_umnc * 0.05)
                n_umnc -= umnc_consumed
                n_hmnc += umnc_consumed
                print(f"            Multi-body kinetics fused and consumed {hmnc_fused * 2 + umnc_consumed} discrete horizons.")
            
            current_object_count = n_umnc + n_hmnc + n_smnc + n_imnc
            assert current_object_count <= initial_object_count, "PHYSICS CRASH: Unphysical core fission detected!"
            
            print("\n[SUCCESS] High-energy radiation fields collapsed stochastically.")

            # --- TRUTHFUL DISPLAY EXCLUSIVE FOR AEON 0 ---
            print("\n" + "="*65)
            print("        ASTROPHYSICAL TIMELINE INTEGRITY STATUS DISPLAY        ")
            print("="*65)
            print(f" -> TOTAL ACTIVE CORES CONSTITUTED: UMNC={n_umnc} | HMNC={n_hmnc} | SMNC={n_smnc} | IMNC={n_imnc}")
            print(f" -> SPACETIMES CREATED BY THIS AEON: {active_manifold_multiverse_counter}")
            print("---------------------------------------------------------------------")

            # --- DYNAMIC MANUAL VARIABLE ACTIVATION CHANNEL ---
            print("[INPUT] Configure active Horizon Assets for Evacuation:")
            active_umnc, active_hmnc, active_smnc, active_imnc = 0, 0, 0, 0
            if n_umnc > 0: active_umnc = min(n_umnc, int(input(f"        Active UMNC anchors (0-{n_umnc}): ")))
            if n_hmnc > 0: active_hmnc = min(n_hmnc, int(input(f"        Active HMNC mergers (0-{n_hmnc}): ")))
            if n_smnc > 0: active_smnc = min(n_smnc, int(input(f"        Active SMNC satellites (0-{n_smnc}): ")))
            if n_imnc > 0: active_imnc = min(n_imnc, int(input(f"        Active IMNC shields (0-{n_imnc}): ")))
            
            # --- BASELINE SHEAR CALCULATION ---
            baseline_shear = (active_umnc * 2.50) + (active_hmnc * 1.85) + (active_smnc * 1.25) + (active_imnc * 0.05)

            # --- METRIC MODIFIERS EVALUATION ---
            print("\n[INPUT] Configure Active Metric Modifiers for the New Manifold:")
            scen_1_choice = input("        Activate Scenario 1 Metric Drainage EXPLOSION? (y/N): ").strip().lower()
            scenario_1_drainage_active = True if scen_1_choice == 'y' else False
            
            star_formation_mod = 1.0 + (agg_bubble_rate * 0.5)
            if scenario_1_drainage_active:
                star_formation_mod *= 0.20
                print("          [EXPLOSION] Scenario 1 active: Star birth suppressed by -80%.")

            # --- ADDENDUM 1 VERSION A EVALUATOR ---
            addendum_1_scar_active = False
            total_remaining_mass = n_umnc + n_hmnc + n_smnc + n_imnc
            
            if scenario_1_drainage_active:
                print("        [CAUSAL] Drainage Explosion active. Instant Addendum 1A blocked.")
                addendum_1_scar_active = False
            else:
                if total_remaining_mass == 0:
                    print("        [CAUSAL] Massless vacuum reached. Instant trigger active.")
                    scar_choice = input("        Manifest Addendum 1 Version A CMB Scar instantly? (y/N): ").strip().lower()
                    if scar_choice == 'y':
                        addendum_1_scar_active = True
                        star_formation_mod *= 1.35
                else:
                    print("        [CAUSAL] Mass remnants exist. Calculating timeline displacement...")
                    active_foam_density = sum([d["multiverse_counter"] for d in parallel_timelines.values()])
                    foam_factor = max(1, active_foam_density)
                    
                    displacement_distortion = random.uniform(0.85, 1.35)
                    calculated_delay = (100.0 / (agg_bubble_rate * foam_factor)) * displacement_distortion
                    
                    print(f"        [COMPUTING] Delayed crystallization framework resolved.")
                    print(f"                    Calculated temporal displacement: {calculated_delay:.2f} Gyr.")
                    
                    scar_choice = input(f"        Trigger binary Addendum 1A event after {calculated_delay:.2f} Gyr delay? (y/N): ").strip().lower()
                    if scar_choice == 'y':
                        addendum_1_scar_active = True
                        star_formation_mod *= 1.15

            # --- FIXED v33.0: COMPLETE AUTOMATED HYPER-FOAM ADDENDUM 1B ENGINE ---
            print("\n" + "-"*50)
            print(" [ADDENDUM 1 - VERSION B] MULTIVERSE COLLISION MONITOR")
            print("-"*50)
            coll_choice = input("        Engage Addendum 1 Version B Multi-Collision track? (y/N): ").strip().lower()
            addendum_1_dynamic_collision = True if coll_choice == 'y' else False
            
            if addendum_1_dynamic_collision:
                print("\n" + "="*55)
                print("[ADDENDUM 1 - VERSION B] COBWEB COLLISION DETECTOR")
                print("=" * 55)
                print("        Select Intersection Detection Mode:")
                print("               [m] - Manual Configuration Node")
                print("               [s] - Stochastic Hyper-Foam (Fully Automated)")
                b_mode = input("        Select Mode (m/S): ").strip().lower()
                
                num_collisions = 0
                collision_times = []
                auto_dense_fluid_prob = 0.5  # Fallback probability
                
                if b_mode == 'm':
                    try:
                        num_collisions = int(input("        >> Enter total intersecting universes: "))
                        for i in range(num_collisions):
                            t_coll = float(input(f"           Enter time for Node {i+1} (Gyr): "))
                            collision_times.append((t_coll, 'manual'))
                    except ValueError:
                        num_collisions = 0
                else:
                    # Dynamically scales based on your 1321+ parallel spacetimes
                    global_density_pool = active_manifold_multiverse_counter
                    if global_density_pool > 0:
                        num_collisions = random.randint(1, max(3, int(math.log1p(global_density_pool) * 2.5)))
                        try:
                            print(f"\n        [FOAM-PROP] Active Multiverse Density: {global_density_pool} Spacetimes.")
                            global_sat = float(input("        >> Enter global plasma domain saturation fraction (0.01 - 0.99): "))
                            auto_dense_fluid_prob = max(0.01, min(0.99, global_sat))
                        except ValueError:
                            auto_dense_fluid_prob = 0.40
                            
                        for _ in range(num_collisions):
                            t_coll = random.uniform(0.1, t_input)
                            collision_times.append((t_coll, 'auto'))
                        print(f"        [AUTO-FOAM] Anchored {num_collisions} independent intersections.")
                    else:
                        print("        [AUTO-FOAM] Background foam metric sterile. No nodes anchored.")
                
                # --- EXECUTE COLLISION MATRIX LOOP WITH DENSITY DILUTION ---
                for t_coll, density_flag in collision_times:
                    if density_flag == 'manual':
                        is_dense = input(f"        >> Is Node at t={t_coll:.1f} Gyr a high-density zone? (Y/n): ").strip().lower()
                    else:
                        # --- EXPONENTIAL METRIC PLASMA DENSITY DILUTION ---
                        # Surrounding plasma dilutes heavily as global time axes expand.
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
                        print(f"           [SHOCK-FRONT] Collision at t={t_coll:.1f} Gyr compressed local fields by {sf_multiplier:.2f}x!")
                        print(f"                         Materialized +{added_imnc} IMNC and +{added_smnc} SMNC cores.")
                    else:
                        print(f"           [ALIGNMENT] Seamless holonomic information exchange at t={t_coll:.1f} Gyr.")
                        print(f"                       Metrics remain strictly decoupled. Local assets invariant.")

                print("---------------------------------------------------------------------")
                print(f" -> Final Computed Star Formation Frequency Modifier: {star_formation_mod:.3f}x")

            
            # --- FIXED v33.0: SEPARATED DISPLACEMENT FROM GLOBAL AGE ---
            print("\nConfigure New Daughter Universe Parameters:")
            try:
                # The user now explicitly defines a realistic long-term era depth
                new_age = float(input("    >> Enter initial operational Age for newborn universe (Gyr, e.g. 13.8): "))
                new_siblings = int(input("    >> Enter number of parallel sibling universes spawning in this grid: "))
            except ValueError:
                new_age = 13.8  # Default to a highly dense, mature baseline
                new_siblings = 0
                
            # The delayed crystallization factor is archived as a signature,
            # it NO LONGER overwrites the global t_genesis timescale!
            t_genesis = max(1.0, new_age)
            active_manifold_multiverse_counter += max(0, new_siblings)
            
            # Carry over your precisely selected evacuated fleet
            n_imnc = active_imnc
            n_smnc = active_smnc
            n_hmnc, n_umnc = 0, 0
            
            print(f"\n -> [SUCCESS] Daughter universe configured with your evacuated fleet!")
            print(f"              Current Pool: SMNC={n_smnc} | IMNC={n_imnc}")
            pathway_2_allowed = True; genesis_reply_loop = False; continue

            # --- EVALUATING COMBINED SHEAR FORCE AT HORIZON BOUNDARY ---
            lqg_tensile_limit = 10.0
            print("---------------------------------------------------------------------")
            print(f" -> Prepared Metric Baseline Shear (Hierarchical): {baseline_shear:.2f} / {lqg_tensile_limit:.2f}")
            print("")
            print("[TRIGGER] Simulating stochastic Planck-scale quantum fluctuation...")
            time.sleep(0.1)
            quantum_fluctuation_peak = random.uniform(1.5, 8.5)
            print(f" -> Generated Quantum Fluctuation Energy Peak: +{quantum_fluctuation_peak:.4f}")
            
            total_shear_force = baseline_shear + quantum_fluctuation_peak
            print(f" -> Total Combined Shear Force at Horizon Boundary: {total_shear_force:.2f}")
            
            if total_shear_force >= lqg_tensile_limit:
                print("[CRITICAL] Quantum fluctuation successfully breached the LQG tensile threshold!")
                print("[SUCCESS] Localized topological rupture verified (Pathway 2 Unleashed).")
                
                total_pnc_pool = n_imnc + n_smnc
                topology_fate = evaluate_cluster_stability(active_umnc, active_smnc, active_imnc, n_hmnc, total_pnc_pool)
                print("---------------------------------------------------------------------")
                
                is_developer = False
                try:
                    if dev_mode: is_developer = True
                except UnboundLocalError:
                    is_developer = False

                if topology_fate == "Stable" or is_developer:
                    if is_developer and topology_fate != "Stable":
                        print("[DEV-BYPASS] Administrative holonomy overwrite: Ignoring cluster instability.")
                    print("[CAUSAL-LOCK] Spacetime geometry stabilized. Processing coordinate transfer...")
                    pathway_2_allowed = True; genesis_reply_loop = False
                else:
                    pathway_2_allowed = False
                    n_umnc = max(0, n_umnc - active_umnc)
                    n_smnc = max(0, n_smnc - active_smnc)
                    n_imnc = max(0, n_imnc - active_imnc)
                    n_hmnc = max(0, n_hmnc - active_hmnc)
                    total_remaining_mass = n_umnc + n_smnc + n_imnc + n_hmnc
                    
                    # --- VERSION 33.0: CONFORMAL MULTIVERSE RECYCLING AT TODESPUNKT ---
                    if total_remaining_mass == 0 and not is_developer:
                        print("\n[AUTOMATIC RESET] Active spacetime is left completely massless.")
                        
                        replaced_count = random.randint(1, 5)
                        candidate_slots = [s for s in range(1, 13) if not parallel_timelines[s]["replacement_shield"]]
                        slots_to_replace = random.sample(candidate_slots, replaced_count)
                        
                        print(f"          [MULTIVERSE] Swapping {replaced_count} parallel slots with")
                        print(f"                       stochastic bubbles from active Generation {current_generation}...")
                        
                        for slot in range(1, 13):
                            if slot in slots_to_replace:
                                has_scar = random.choice([True, False])
                                has_collision = random.choice([True, False]) if not has_scar else False
                                
                                scen_id = "8.5" if (has_scar or has_collision) else "6 (Multi-Core Cluster Baseline)"
                                
                                parallel_timelines[slot] = {
                                    "umnc": 0, "hmnc": random.randint(0, 5), 
                                    "smnc": random.randint(10, 40), "imnc": random.randint(120, 290),
                                    "generation": current_generation, "age": random.uniform(1.0, 12.0),
                                    "scenario": scen_id, "scar_v1": has_scar, "collision_v2": has_collision,
                                    "multiverse_counter": random.randint(1, 10), "replacement_shield": False
                                }
                            else:
                                distance_factor = abs(current_generation - parallel_timelines[slot]["generation"])
                                if distance_factor < 4:
                                    displacement_drift = random.uniform(0.90, 1.10)
                                    parallel_timelines[slot]["multiverse_counter"] += int(3 * displacement_drift)
                                    parallel_timelines[slot]["age"] += 5.0 * displacement_drift
                                else:
                                    displacement_drift = random.choice([0.0, random.uniform(0.20, 1.80)])
                                    parallel_timelines[slot]["age"] += t_genesis * displacement_drift
                                    parallel_timelines[slot]["multiverse_counter"] += int(6 * displacement_drift)
                                
                                parallel_timelines[slot]["generation"] = current_generation
                        
                        coldspot_choice = input("\n        Manifest Addendum 1 CMB Cold Spot scar in the new universe? (Y/n): ").strip().lower()
                        if coldspot_choice != 'n':
                            print("\n[ADDENDUM 1 - VERSION A] Vacuum drainage scar injected directly into the matrix!")
                            addendum_1_scar_active = True 
                        else:
                            addendum_1_scar_active = False
                        
                        n_umnc, n_smnc, n_imnc, n_hmnc = active_umnc, active_smnc, active_imnc, active_hmnc
                        print(f"\n -> Coordination transfer completed. Entering Generation {current_generation} matrix.\n")
                        pathway_2_allowed = True; genesis_reply_loop = False
                    else:
                        current_generation += 1
                        print(f"\n[CRITICAL ERROR] Core instability without complete drainage. Forcing forward Gen flip to {current_generation}...")
                        n_umnc = int(n_umnc * 0.15); n_smnc = int(n_smnc * 0.15); n_imnc = int(n_imnc * 0.15); n_hmnc = int(n_hmnc * 0.15)
                        pathway_2_allowed = True; genesis_reply_loop = False
            else:
                print("[SUPPRESSED] Combined fluctuation amplitude insufficient to tear filaments.")
                print("[WARNING] Metric remains smoothly embedded. Pathway 2 blocked.")
                pathway_2_allowed = False
        except ValueError:
            print("[FAIL] Numerical validation aborted. Defaulting bounds.")
            pathway_2_allowed = False
            genesis_reply_loop = False

    if pathway_2_allowed:
        print("\n[INPUT] Evaluate Rotating Kerr Horizon Geometry Bounds:")
        print("        [m] - Standard Matter Domain (Symmetric Baryon Average / +t)")
        print("        [a] - Antimatter Domain (CPT Chiral Inversion Enforced / -t)")
        print("        [s] - Stochastic Quantum Bifurcation (Probability-based roll)")
        chiral_choice = input("        Select Kerr Boundary Mode (m/a/S): ").strip().lower()
        
        if chiral_choice == 'a':
            cpt_chiral_inversion_active = True
        elif chiral_choice == 's':
            if random.random() > 0.5:
                cpt_chiral_inversion_active = True

    sandbox_active = True
    while sandbox_active:
        print("\n" + "="*65)
        print(" SIMULATION ROUTING MENU - TIME EVOLUTION")
        print("="*65)
        print(f" [CURRENT METRIC] Gen: {current_generation}")
        print(f"   UMNC={n_umnc} | HMNC={n_hmnc} | "
              f"SMNC={n_smnc} | IMNC={n_imnc}")
        print(f" [LOCAL MATRIX LOG] Multiverse Counter: "
              f"{active_manifold_multiverse_counter}")
        try:
            if addendum_1_scar_active:
                print(" [SIGNATURE] Permanent CMB Cold Spot Scar"
                      " (Version A) verified in background.")
        except NameError:
            addendum_1_scar_active = False
            addendum_1_dynamic_collision = False
        print(" --------------------------------------------------")
        print(" [INPUT] Select Simulation Routing Mode:")
        print("         [m] - Manual Freedom (Reference Selection)")
        print("         [a] - Automatic Detection (Dynamic Context)")
        print("         [d] - DEVELOPER MODE (Absolute Control)")
        mode_choice = input("         Select Mode (m/a/D): ").strip().lower()
        
        if mode_choice == 'd':
            dev_mode = True; auto_mode = False
        elif mode_choice == 'a':
            auto_mode = True; dev_mode = False
        else:
            auto_mode = False; dev_mode = False

        print("\n[INPUT] Enter target evolution timescale:")
        t_input_str = input("        Delta t (Gyr, e.g. 0.5 or infinity): ").strip().lower()
        
        if t_input_str == "infinity":
            t_input = 150.0
            print("          [INFINITY] Running asymptotic dilution...")
        else:
            t_input = float(t_input_str)

        # --- IMMEDIATE MULTI-BUBBLE AGGRESSIVENESS CONFIG ---
        try:
            print("\n[INPUT] Configure Multi-Bubble Generation Flux:")
            agg_bubble_rate = float(input("        >> Enter creation aggressiveness (0.01 - 0.99): "))
            agg_bubble_rate = max(0.01, min(0.99, agg_bubble_rate))
        except ValueError:
            agg_bubble_rate = 0.25

        # --- EVALUATE EXPLOSIVE STAR FORMATION MODIFIER ---
        star_formation_mod = 1.0 + (agg_bubble_rate * 0.5)
        
        print("\n[INPUT] Configure Active Metric Modifiers:")
        scen_1_choice = input("        Activate Scenario 1 Metric Drainage EXPLOSION? (y/N): ").strip().lower()
        scenario_1_drainage_active = True if scen_1_choice == 'y' else False
        
        if scenario_1_drainage_active:
            star_formation_mod *= 0.20  # Detonation suppresses star birth (-80%)
            print("          [EXPLOSION] Scenario 1 active: Star birth suppressed by -80%.")

        # --- REFINED ADDENDUM 1 VERSION A TIMELINE DISPLACEMENT ---
        addendum_1_scar_active = False
        total_remaining_mass = n_umnc + n_hmnc + n_smnc + n_imnc
        
        if scenario_1_drainage_active:
            print("        [CAUSAL] Drainage Explosion active. Instant Addendum 1A blocked.")
            addendum_1_scar_active = False
        else:
            if total_remaining_mass == 0:
                print("        [CAUSAL] Massless vacuum reached. Immediate trigger engaged.")
                scar_choice = input("        Manifest Addendum 1 Version A CMB Scar instantly? (y/N): ").strip().lower()
                if scar_choice == 'y':
                    addendum_1_scar_active = True
                    star_formation_mod *= 1.35
            else:
                print("        [CAUSAL] Mass remnants exist. Calculating timeline displacement...")
                active_foam_density = sum([d["multiverse_counter"] for d in parallel_timelines.values()])
                foam_factor = max(1, active_foam_density)
                
                displacement_distortion = random.uniform(0.85, 1.35)
                calculated_delay = (100.0 / (agg_bubble_rate * foam_factor)) * displacement_distortion
                
                print(f"        [COMPUTING] Delayed crystallization framework resolved.")
                print(f"                    Calculated temporal displacement: {calculated_delay:.2f} Gyr.")
                
                scar_choice = input(f"        Trigger binary Addendum 1A event after {calculated_delay:.2f} Gyr delay? (y/N): ").strip().lower()
                if scar_choice == 'y':
                    addendum_1_scar_active = True
                    star_formation_mod *= 1.15

        # --- FIXED v33.0: COMPLETE CRASH-PROOF AUTOMATED HYPER-FOAM NODE ---
        print("\n" + "-"*50)
        print(" [ADDENDUM 1 - VERSION B] MULTIVERSE COLLISION MONITOR")
        print("-"*50)
        coll_choice = input("        Engage Addendum 1 Version B Multi-Collision track? (y/N): ").strip().lower()
        addendum_1_dynamic_collision = True if coll_choice == 'y' else False
        
        if addendum_1_dynamic_collision:
            print("\n" + "="*55)
            print("[ADDENDUM 1 - VERSION B] COBWEB COLLISION DETECTOR")
            print("=" * 55)
            print("        Select Intersection Detection Mode:")
            print("               [m] - Manual Configuration Node")
            print("               [s] - Stochastic Hyper-Foam (Fully Automated)")
            b_mode = input("        Select Mode (m/S): ").strip().lower()
            
            num_collisions = 0
            collision_times = []
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
                    try:
                        print(f"\n        [FOAM-PROP] Active Multiverse Density: {global_density_pool} Spacetimes.")
                        global_sat = float(input("        >> Enter global plasma domain saturation fraction (0.01 - 0.99): "))
                        auto_dense_fluid_prob = max(0.01, min(0.99, global_sat))
                    except ValueError:
                        auto_dense_fluid_prob = 0.40
                        
                    for _ in range(num_collisions):
                        t_coll = random.uniform(0.1, t_input)
                        collision_times.append((t_coll, 'auto'))
                    print(f"        [AUTO-FOAM] Anchored {num_collisions} independent intersections.")
                else:
                    print("        [AUTO-FOAM] Background foam metric sterile. No nodes anchored.")
            
            # --- EXECUTE COLLISION MATRIX LOOP WITH DENSITY DILUTION ---
            for t_coll, density_flag in collision_times:
                if density_flag == 'manual':
                    is_dense = input(f"        >> Is Node at t={t_coll:.1f} Gyr a high-density zone? (Y/n): ").strip().lower()
                else:
                    # Metric plasma density dilutes heavily over time axes expansion
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
                    print(f"           [SHOCK-FRONT] Collision at t={t_coll:.1f} Gyr compressed local fields by {sf_multiplier:.2f}x!")
                    print(f"                         Materialized +{added_imnc} IMNC and +{added_smnc} SMNC cores.")
                else:
                    print(f"           [ALIGNMENT] Seamless holonomic information exchange at t={t_coll:.1f} Gyr.")
                    print(f"                       Metrics remain strictly decoupled. Local assets invariant.")

            print("---------------------------------------------------------------------")
            print(f" -> Final Computed Star Formation Frequency Modifier: {star_formation_mod:.3f}x")

        # --- AUTOMATIC SCENARIO DETECTOR MATRIX ---
        accretion_drainage_active = (addendum_1_scar_active or 
                                     addendum_1_dynamic_collision or 
                                     addendum_1_ccc_exchange_allowed)
        
        if eval_total > 0 and accretion_drainage_active: user_choice = "8.5"
        elif eval_total > 0 and t_input < 1.0: user_choice = "7.2b"
        elif scenario_1_drainage_active and t_input < 1.0: user_choice = "1"
        elif eval_total >= 150 and t_input < 1.0: user_choice = "6"
        elif eval_total == 0 and t_input >= 50.0: user_choice = "12"
        else: user_choice = "4"
        
        print(f"        >> Verified Trajectory Phase: Scenario {user_choice}")
        print(f"\n[EVAL] Executing Evaluation for Scenario {user_choice}...")
        time.sleep(0.1)
        
        active_manifold_multiverse_counter += int(2 * (t_input / 10.0))

        # --- TRUTHFUL INTERACTIVE TIMELINE CROSSOVER JUMP ENGINE ---
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
                if data["scar_v1"]: addenda_desc = "Addendum 1 (Ver.A) Scar"
                elif data["collision_v2"]: addenda_desc = "Addendum 1 (Ver.B) Resonance"
                
                print(f" Slot {slot:02d} -> Baseline Manifest: Scenario {data['scenario']} | {addenda_desc}\n"
                      f"           Gen: {data['generation']} | Age: {data['age']:.1f} Gyr | Local Counter: {data['multiverse_counter']} \n"
                      f"           Pool: UMNC={data['umnc']} | HMNC={data['hmnc']} | SMNC={data['smnc']} | IMNC={data['imnc']}\n"
                      f" ---------------------------------------------------------------------")
            print("=====================================================================")
            try:
                target_slot = int(input(" >> Select target Timeline Slot to jump into (1-12): "))
                if target_slot in parallel_timelines:
                    print(f"\n[CROSSOVER] Slicing coordinates... Re-locking quantum loops...")
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
            n_umnc = int(n_umnc * 0.15); n_hmnc = int(n_hmnc * 0.15); n_smnc = int(n_smnc * 0.15); n_imnc = int(n_imnc * 0.15)
            addendum_1_scar_active = False
            addendum_1_dynamic_collision = False
        elif action == 'q':
            print("\n[SHUTDOWN] Safely disconnecting LQG filaments. Offline.\n")
            sandbox_active = False
            genesis_reply_loop = False

if __name__ == "__main__":
    run_interactive_sandbox()
