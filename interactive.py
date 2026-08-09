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
            "scar_v1": False,
            "collision_v2": False,
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
            
            # --- INFINITY BYPASS GATE ---
            if t_input_str == "infinity":
                t_genesis = 150.0  # Asymptotic thermodynamic evaporation ceiling
                print("          [INFINITY] Vorspringen ans asymptotische Ende aller Tage...")
            else:
                t_genesis = float(t_input_str)
            
            seeding_epoch = min(10.0, t_genesis)
            umnc_spawned = int(0.005 * (seeding_epoch ** 1.1))
            smnc_spawned = int(0.65 * (seeding_epoch ** 2.0))
            imnc_spawned = int(18.5 * (seeding_epoch ** 2.0))
            
            n_umnc += umnc_spawned
            n_smnc += smnc_spawned
            n_imnc += imnc_spawned
            initial_object_count = n_umnc + n_hmnc + n_smnc + n_imnc
            if t_genesis >= 15.0:
                print(f"          [DISK-ACCRETION] Era depth ({t_genesis} Gyr) drives core growth...")
                
                shifted_to_smnc = 0
                if n_imnc > 0:
                    accretion_rate_t1 = min(0.85, t_genesis / 40.0)
                    shifted_to_smnc = int(n_imnc * accretion_rate_t1)
                    if shifted_to_smnc > 0:
                        n_imnc -= shifted_to_smnc
                        n_smnc += shifted_to_smnc
                        print(f"                            Accretion Tier 1: IMNC to SMNC.")
                
                shifted_to_hmnc = 0
                if n_smnc > 0:
                    accretion_rate_t2 = min(0.75, t_genesis / 50.0)
                    shifted_to_hmnc = int(n_smnc * accretion_rate_t2)
                    if shifted_to_hmnc > 0:
                        n_smnc -= shifted_to_hmnc
                        n_hmnc += shifted_to_hmnc
                        print(f"                            Accretion Tier 2: SMNC to HMNC.")

                upgraded_umnc = 0
                if n_hmnc > 0:
                    accretion_rate_t3 = min(0.65, t_genesis / 60.0)
                    upgraded_umnc = int(n_hmnc * accretion_rate_t3)
                    if upgraded_umnc > 0:
                        n_hmnc -= upgraded_umnc
                        n_umnc += upgraded_umnc
                        print(f"                            Accretion Tier 3: HMNC to UMNC.")
            
            imnc_evaporated = int(n_imnc * (1.0 - math.exp(-0.05 * t_genesis)))
            smnc_evaporated = int(n_smnc * (1.0 - math.exp(-0.01 * t_genesis)))
            
            n_imnc = max(0, n_imnc - imnc_evaporated)
            n_smnc = max(0, n_smnc - smnc_evaporated)
            
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
                print(f"            Multi-body kinematics fused and consumed {hmnc_fused * 2 + umnc_consumed} discrete horizons.")
            
            current_object_count = n_umnc + n_hmnc + n_smnc + n_imnc
            assert current_object_count <= initial_object_count, "PHYSICS CRASH: Unphysical core fission detected!"
            
            print("\n[SUCCESS] High-energy radiation fields collapsed stochastically.")
            print(f"          Current Pool: UMNC={n_umnc:,} | HMNC={n_hmnc:,} | SMNC={n_smnc:,} | IMNC={n_imnc:,}")

            print("\n[LQG] Evaluating Baseline Metric Shear Force...")
            active_umnc, active_hmnc, active_smnc, active_imnc = 0, 0, 0, 0
            total_active_horizons = n_umnc + n_hmnc + n_smnc + n_imnc
            
            if total_active_horizons > 0:
                print(f"        Available assets: {n_umnc} UMNC | {n_hmnc} HMNC | {n_smnc} SMNC | {n_imnc} IMNC cores.")
                print("        ---------------------------------------------------------------------")
                if n_umnc > 0:
                    active_umnc = int(input(f"        >> Enter active preparing UMNC anchors (0-{n_umnc}): "))
                    active_umnc = max(0, min(active_umnc, n_umnc))
                if n_hmnc > 0:
                    active_hmnc = int(input(f"        >> Enter active structural HMNC mergers (0-{n_hmnc}): "))
                    active_hmnc = max(0, min(active_hmnc, n_hmnc))
                if n_smnc > 0:
                    active_smnc = int(input(f"        >> Enter active slinging SMNC satellites (0-{n_smnc}): "))
                    active_smnc = max(0, min(active_smnc, n_smnc))
                if n_imnc > 0:
                    active_imnc = int(input(f"        >> Enter active peripheral IMNC shields (0-{n_imnc}): "))
                    active_imnc = max(0, min(active_imnc, n_imnc))
                
                baseline_shear = (active_umnc * 2.50) + (active_hmnc * 1.85) + (active_smnc * 1.25) + (active_imnc * 0.05)
            else:
                print("        [CRITICAL] Massless vacuum state reached. No active horizons exist.")
                baseline_shear = 0.0
            
            lqg_tensile_limit = 10.0
            print("        ---------------------------------------------------------------------")
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
                    pathway_2_allowed = True
                    genesis_reply_loop = False
                else:
                    pathway_2_allowed = False
                    
                    n_umnc = max(0, n_umnc - active_umnc)
                    n_smnc = max(0, n_smnc - active_smnc)
                    n_imnc = max(0, n_imnc - active_imnc)
                    n_hmnc = max(0, n_hmnc - active_hmnc)
                    total_remaining_mass = n_umnc + n_smnc + n_imnc + n_hmnc
                    
                    # --- VERSION 33.0: CONFORMAL MULTIVERSE RECYCLING ---
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
                                    "multiverse_counter": random.randint(1, 10),
                                    "replacement_shield": False
                                }
                            else:
                                distance_factor = abs(current_generation - parallel_timelines[slot]["generation"])
                                if distance_factor < 4:
                                    displacement_drift = random.uniform(0.90, 1.10)
                                    parallel_timelines[slot]["multiverse_counter"] += int(3 * displacement_drift)
                                    parallel_timelines[slot]["age"] += 5.0 * displacement_drift
                                else:
                                    # TOTAL TIMELINE DISPLACEMENT DECOUPLING:
                                    # The background clock can shift fluidly, stand completely still (0.0), 
                                    # or jump independently based on vacuum fluctuation resonance!
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
                        
                        n_umnc = active_umnc
                        n_smnc = active_smnc
                        n_imnc = active_imnc
                        n_hmnc = active_hmnc
                        
                        print(f"\n -> Coordination transfer completed. Entering Generation {current_generation} matrix.\n")
                        pathway_2_allowed = True
                        genesis_reply_loop = False
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
            pathway_2_allowed = False; genesis_reply_loop = False

    if pathway_2_allowed:
        print("\n[INPUT] Evaluate Rotating Kerr Horizon Geometry Bounds:")
        print("        [m] - Standard Matter Domain (Symmetric Baryon Average / +t)")
        print("        [a] - Antimatter Domain (CPT Chiral Inversion Enforced / -t)")
        print("        [s] - Stochastic Quantum Bifurcation (Probability-based roll)")
        chiral_choice = input("        Select Kerr Boundary Mode (m/a/S): ").strip().lower()
        
        if chiral_choice == 'a': cpt_chiral_inversion_active = True
        elif chiral_choice == 's':
            if random.random() > 0.5: cpt_chiral_inversion_active = True
    # --- ADVANCED ROUTING LOOP INTERFACE ---
    sandbox_active = True
    while sandbox_active:
        print("\n=====================================================================")
        print(" SIMULATION ROUTING MENUE - TIME AXIS EVOLUTION")
        print("=====================================================================")
        print(f" [CURRENT METRIC] Gen: {current_generation} | Core Assets: {n_umnc} UMNC | {n_hmnc} HMNC | {n_smnc} SMNC | {n_imnc} IMNC")
        print(f" [LOCAL MATRIX LOG] Master Multiverse Counter for this Spacetime: {active_manifold_multiverse_counter}")
        try:
            if addendum_1_scar_active: print(" [SIGNATURE] Permanent CMB Cold Spot Scar (Version A) verified in background.")
        except NameError:
            addendum_1_scar_active = False
            addendum_1_dynamic_collision = False
        print(" ---------------------------------------------------------------------")
        print(" [INPUT] Select Simulation Routing Mode:")
        print("         [m] - Manual Freedom (Reference Matrix Selection)")
        print("         [a] - Automatic Detection (Dynamic Runtime Context Matrix)")
        print("         [d] - DEVELOPER MODE (Absolute Control & Bound Overwrites)")
        mode_choice = input("         Select Mode (m/a/D): ").strip().lower()
        
        if mode_choice == 'd':
            dev_mode = True; auto_mode = False
        elif mode_choice == 'a':
            auto_mode = True; dev_mode = False
        else:
            auto_mode = False; dev_mode = False

        print("\n[INPUT] Enter target evolution timescale for this event:")
        t_input_str = input("        Delta t (in Gyr, e.g. 0.5 or infinity): ").strip().lower()
        
        # --- INFINITY RUNAWAY BYPASS ---
        if t_input_str == "infinity":
            t_input = 150.0
            print("          [INFINITY] Running asymptotic forward thermodynamic dilution...")
        else:
            t_input = float(t_input_str)

        # --- REFINED AUTOMATIC SCENARIO DETECTOR MATRIX ---
        user_choice = "4"
        if auto_mode:
            print("\n[SYS] Running automatic scenario detection matrix...")
            eval_total = n_umnc + n_hmnc + n_smnc + n_imnc
            accretion_drainage_active = addendum_1_scar_active or addendum_1_dynamic_collision or addendum_1_ccc_exchange_allowed
            
            if eval_total > 0 and accretion_drainage_active: user_choice = "8.5"
            elif eval_total > 0 and t_input < 1.0: user_choice = "7.2b"
            elif scenario_1_drainage_active and t_input < 1.0: user_choice = "1"
            elif eval_total >= 150 and t_input < 1.0: user_choice = "6"
            elif eval_total == 0 and t_input >= 50.0: user_choice = "12"
            else: user_choice = "4"
            print(f"        >> Auto-Detected Trajectory: Scenario {user_choice}")
        else:
            user_choice = input("        >> Enter target Scenario ID from manuscript (1-12): ").strip()

        print(f"\n[EVAL] Executing Matrix Evaluation for Scenario {user_choice}...")
        time.sleep(0.1)
        
        # Master Counter increases safely within the active localized spacetime frame
        active_manifold_multiverse_counter += int(2 * (t_input / 10.0))
        
        if user_choice == "8.5":
            print(" -> [RUNNING] Stable Horizon Shadow Non-Singular Transition Track active.")
            print(" >> Calculated Oasis Density (eta):    2.500000e-09")
            print(" >> CMB Cold Spot Centered Alignment:   False")
        elif user_choice == "7.2b":
            print(" -> [RUNNING] Multi-Core Cluster High-Tensile Repulsion Oasis active.")
            print(" >> Calculated Oasis Density (eta):    2.444449e-09")
            print(" >> CMB Cold Spot Centered Alignment:   False")
        else:
            print(f" -> [RUNNING] Scenario {user_choice} baseline evolution processed.")
            print(" >> Calculated Oasis Density (eta):    1.000000e-09")
            print(" >> CMB Cold Spot Centered Alignment:   True")

        # --- ISOLATED MENU: ADDENDUM 1 - VERSION A (STATIC TIMELINE SCAR) ---
        print("\n" + "-"*65)
        print(" [ADDENDUM 1 - VERSION A] PRIMORDIAL METRIC DRAINAGE INJECTOR")
        print("-"*65)
        toggle_scar = input(" >> Toggle permanent CMB Cold Spot drainage scar at this timestamp? (y/N): ").strip().lower()
        if toggle_scar == 'y':
            addendum_1_scar_active = True
            print(" [ADDENDUM 1 - VERSION A] Vacuum drainage scar successfully stamped into the background.")
        elif toggle_scar == 'w':
            addendum_1_scar_active = False
            print(" [ADDENDUM 1 - VERSION A] Scar retracted. Metric background normalized.")

        # --- ISOLATED MENU: ADDENDUM 1 - VERSION B (DYNAMIC MULTI-COLLISION TRACK) ---
        print("\n" + "-"*65)
        print(" [ADDENDUM 1 - VERSION B] MULTIVERSE COLLISION PROFILE ENGINE")
        print("-"*65)
        trigger_collisions = input(" >> Trigger trans-cosmic bubble universe boundary intersections now? (y/N): ").strip().lower()
        
        if trigger_collisions == 'y':
            addendum_1_dynamic_collision = True
            print("\n" + "="*65)
            print("[ADDENDUM 1 - VERSION B] RESOLVING MULTI-BODY INTERSECTION FIELDS")
            print("=" * 65)
            try:
                num_collisions = int(input(" >> Enter total number of intersecting bubble universes (e.g. 1 or 5): "))
                num_collisions = max(1, num_collisions)
                
                for i in range(num_collisions):
                    print(f"\n    --- Configuring Collision Node {i+1} of {num_collisions} ---")
                    t_collision = float(input(f"    >> Enter execution timeline for Collision {i+1} (in Gyr): "))
                    is_dense_env = input("    >> Is the local intersection domain a high-density plasma zone? (Y/n): ").strip().lower()
                    
                    if is_dense_env != 'n':
                        star_formation_multiplier = random.uniform(2.5, 5.0)
                        added_imnc = int(12 * t_collision * star_formation_multiplier)
                        added_smnc = int(2 * t_collision * (star_formation_multiplier / 2.0))
                        n_imnc += added_imnc; n_smnc += added_smnc
                        print(f"    [SHOCK-WAVE] Hydrodynamic compression amplified star formation frequency by {star_formation_multiplier:.2f}x!")
                    else:
                        print("    [DEFLATION] Energy leaked seamlessly. Metric boundary flattened without shockwaves.")
                print(" ---------------------------------------------------------------------")
                print(f" [SUCCESS] Multi-collision profile integrated. Pool updated safely.")
            except ValueError:
                print("    [SECURITY] Invalid parameters. Collision track bypassed.")
            print("="*65 + "\n")
        else:
            addendum_1_dynamic_collision = False

        # --- TRUTHFUL INTERACTIVE TIMELINE CROSSOVER JUMP ENGINE ---
        print("\n" + "-"*65)
        print(" [MULTIVERSE] TRANS-DIMENSIONAL COBWEB CROSSOVER DETECTED (FRAGERUNDE)")
        print("-"*65)
        print(" [INPUT] Do you want to abandon this active spacetime branch?")
        print("         [j] - Jump into a verified parallel bubble universe")
        print("         [n] - Remain on this coordinate lineage")
        jump_choice = input("         Select Choice (j/N): ").strip().lower()
        
        if jump_choice == 'j':
            print("\n=====================================================================")
            print("    MULTIVERSE MATRIX INDEX: 12 PARALLEL SPACETIMES RUNNING IN RAM     ")
            print("=====================================================================")
            for slot, data in parallel_timelines.items():
                # Displays truthful structural profiles based on physical background invariants
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
                    
                    # Swap the active runtime memory fields with the target workspace invariants
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
        action = input("        Select Action Control ([c]onsecutive event / [r]eset aeon / [q]uit): ").strip().lower()
        
        if action == 'r':
            current_generation += 1
            print(f"\n[RESET] Initiating conformal cyclic transition to Generation {current_generation}...")
            n_umnc = int(n_umnc * 0.15); n_hmnc = int(n_hmnc * 0.15); n_smnc = int(n_smnc * 0.15); n_imnc = int(n_imnc * 0.15)
            addendum_1_scar_active = False
            addendum_1_dynamic_collision = False
        elif action == 'q':
            print("\n[SHUTDOWN] Safely disconnecting Loop Quantum Gravity filaments. Offline.\n")
            sandbox_active = False
            genesis_reply_loop = False

if __name__ == "__main__":
    run_interactive_sandbox()
