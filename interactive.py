#!/usr/bin/env python3
import math
import time
import random
import os
import sys

def execute_automated_logging(log_id, density, is_smooth, anomaly_score, descriptor):
    """
    Saves runtime cosmological matrices, boundary footprints, 
    and invariant profiles safely into local audit fields.
    """
    try:
        with open("causal_matrix_output.txt", "a") as f:
            f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] ID: {log_id} | "
                    f"Density: {density:.6e} | Smooth: {is_smooth} | "
                    f"Anomaly: {anomaly_score:.2f} | Info: {descriptor}\n")
    except IOError:
        pass

def evaluate_cluster_stability(active_umnc, active_smnc, active_imnc, n_hmnc, total_pnc_pool):
    """
    SECTION 4.1 MONITOR: Relativistic Lorentz Mass Inflation Framework.
    Evaluates dual-vector interactions driving the decoupled manifold.
    Tracks whether external boundary conditions sustain an Oasis equilibrium.
    """
    print("\n[MONITOR] Running Refined Relativistic Multi-Body Vector Analysis...")
    
    mass_weights = {
        "umnc": 50.0,
        "hmnc": 25.0,
        "smnc": 10.0,
        "imnc": 0.5,
        "pnc":  0.01
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
        if f_outward > 0.0: 
            return "Explosion"
        else: 
            return "Massless"
            
    r_stabil = f_outward / f_inward
    print(f" -> Aggregate Inward Gravitational Pull Vector: {f_inward:.2f}")
    print(f" -> Aggregate Outward Relativistic Escape Vector: {f_outward:.2f}")
    print(f" -> Computed Dynamic Balance Ratio (R_stabil):  {r_stabil:.4f}")
    
    if r_stabil < 0.28:
        print(" -> [DOMINANT TRAJECTORY]: GRAVITATIONAL INFLUX (Central core consolidation)")
        return "Collapse"
    elif r_stabil > 0.65:
        print(" -> [DOMINANT TRAJECTORY]: ISOLATED EXPANSION (Dispersed void-wall structures)")
        return "Explosion"
    else:
        print(" -> [DOMINANT TRAJECTORY]: STABLE OASIS EQUILIBRIUM (JWST Oasis formed)")
        return "Stable"
def run_interactive_sandbox():
    """
    Main state engine executing multi-generational cosmological cascade models.
    Enforces dynamic timeline perturbations, overrides, and fluid fluctuations.
    """
    print("=====================================================================")
    print("   ______   ______   .___  ___.  __    ______     ______    __  ")
    print("  /  ____| /  __  \  |   \\/   | |  |  /  ____|   /  __  \\  |  | ")
    print(" |  |     |  |  |  | |  \\  /  | |  | |  |       |  |  |  | |  | ")
    print(" |  |     |  |  |  | |  |\\/|  | |  | |  |       |  |  |  | |  | ")
    print(" |  |____ |  `--'  | |  |  |  | |  | |  |____   |  `--'  | |  | ")
    print("  \\______| \\______/  |__|  |__| |__|  \\______|   \\______/  |__| ")
    print("=====================================================================")
    print("        COSMIC PIRACY SIMULATION - STATE ENGINE v32.0 (ASCII MATRIX)")
    print("        Background-Independent Quantum-Geometric Graph Evaluator")
    print("=====================================================================\n")
    
    current_generation = 0
    n_umnc = 0      
    n_hmnc = 0      
    n_smnc = 0      
    n_imnc = 0      
    
    pathway_2_allowed = False
    scenario_1_drainage_active = False
    addendum_1_collision_allowed = False
    addendum_1_ccc_exchange_allowed = False
    cpt_chiral_inversion_active = False
    timeline_displacement_risk = False
    dev_mode = False
    auto_mode = False
    
    genesis_reply_loop = True
    while genesis_reply_loop:
        print("[INPUT] Initialize at Scenario 0 (Global CPT Crossover Node)?")
        genesis_reply = input("        Trigger Ur-Genesis Phase (Y/n): ").strip().lower()
        
        if genesis_reply != 'y':
            print("\n[CRITICAL RESET] Enforcing Conformal Cyclic Reset for a massless vacuum!")
            print("                 No primordial condensation triggered. Rest-mass profile collapsed.")
            print("                 -> Result: Instant metric scale loss. Scenario 0 re-triggered.\n")
            time.sleep(0.4)
            n_umnc, n_hmnc, n_smnc, n_imnc = 0, 0, 0, 0
            continue 

        print("\n[PHASE 0] AEON 0 - PRIMORDIAL SEEDING AND BOUNDARY GATES")
        print("---------------------------------------------------------------------")
        try:
            print("[INPUT] Enter target timescale for Aeon 0 PNC growth phase:")
            t_genesis = float(input("        Delta t_0 (in Gyr, e.g. 4.0 or 60.0): "))
            
            # --- 1. PRIMORDIAL SEEDING LAW WITH DENSITY SATURATION ---
            # Fresh PNC generation from the vacuum field terminates as the metrics expand.
            pnc_saturation_factor = math.exp(-0.06 * t_genesis)
            base_energy_density = (t_genesis ** 2.0) * pnc_saturation_factor
            
            umnc_spawned = int(0.005 * (t_genesis ** 1.1) * pnc_saturation_factor)
            smnc_spawned = int(0.65 * base_energy_density)
            imnc_spawned = int(18.5 * base_energy_density)
            
            if t_genesis >= 40.0:
                umnc_spawned = int(umnc_spawned * 0.05)
                smnc_spawned = int(smnc_spawned * 0.05)
                imnc_spawned = int(imnc_spawned * 0.02)
                
            n_umnc += umnc_spawned
            n_smnc += smnc_spawned
            n_imnc += imnc_spawned
            initial_object_count = n_umnc + n_hmnc + n_smnc + n_imnc
            # --- 2. CONTINUOUS BOTTOM-UP RUNAWAY ACCRETION MATRIX ---
            # Cores swallow energy from disks. Mass transforms sequentially
            # through a real-time flow (IMNC -> SMNC -> HMNC -> UMNC).
            if t_genesis >= 15.0:
                print(f"          [DISK-ACCRETION] Prolonged era depth ({t_genesis} Gyr) drives core growth...")
                
                # Tier 1: Light IMNCs absorb local plasma fields and shift into SMNC satellites
                shifted_to_smnc = 0
                if n_imnc > 0:
                    accretion_rate_t1 = min(0.85, t_genesis / 40.0)
                    shifted_to_smnc = int(n_imnc * accretion_rate_t1)
                    if shifted_to_smnc > 0:
                        n_imnc -= shifted_to_smnc
                        n_smnc += shifted_to_smnc
                        print(f"                            Accretion Tier 1: Matured {shifted_to_smnc} IMNCs to SMNC.")
                
                # Tier 2: Existing and newly arrived SMNCs undergo runaway accretion into HMNC mergers
                shifted_to_hmnc = 0
                if n_smnc > 0:
                    accretion_rate_t2 = min(0.75, t_genesis / 50.0)
                    shifted_to_hmnc = int(n_smnc * accretion_rate_t2)
                    if shifted_to_hmnc > 0:
                        n_smnc -= shifted_to_hmnc
                        n_hmnc += shifted_to_hmnc
                        print(f"                            Accretion Tier 2: Matured {shifted_to_hmnc} SMNCs to HMNC.")

                # Tier 3: Hypermassive HMNCs experience ultimate saturation into UMNC anchors
                upgraded_umnc = 0
                if n_hmnc > 0:
                    accretion_rate_t3 = min(0.65, t_genesis / 60.0)
                    upgraded_umnc = int(n_hmnc * accretion_rate_t3)
                    if upgraded_umnc > 0:
                        n_hmnc -= upgraded_umnc
                        n_umnc += upgraded_umnc
                        print(f"                            Accretion Tier 3: Matured {upgraded_umnc} HMNCs to UMNC anchors.")
            
            # --- 3. EXPONENTIAL HAWKING EVAPORATION TERMINATION ---
            # Unprotected light cores leak mass into radiation over mature epochs
            imnc_evaporated = int(n_imnc * (1.0 - math.exp(-0.05 * t_genesis)))
            smnc_evaporated = int(n_smnc * (1.0 - math.exp(-0.01 * t_genesis)))
            
            n_imnc = max(0, n_imnc - imnc_evaporated)
            n_smnc = max(0, n_smnc - smnc_evaporated)
            
            # --- 4. CENTRIFUGAL CLUSTER FUSION KINETICS (REDUCES NET OBJECT COUNT) ---
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
            
            # --- 5. STRICT NON-FISSION SAFETY GUARD ---
            current_object_count = n_umnc + n_hmnc + n_smnc + n_imnc
            assert current_object_count <= initial_object_count, "PHYSICS CRASH: Unphysical core fission detected!"
            
            print("\n[SUCCESS] High-energy radiation fields collapsed stochastically.")
            print(f"          Current Pool: UMNC={n_umnc:,} | HMNC={n_hmnc:,} | SMNC={n_smnc:,} | IMNC={n_imnc:,}")
            
            # --- 6. FOUR-CHANNEL METRIC SHEAR FORCE EVALUATION ---
            print("\n[LQG] Evaluating Baseline Metric Shear Force...")
            active_umnc = 0
            active_hmnc = 0
            active_smnc = 0
            active_imnc = 0
            
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
            # --- EVALUATING HIERARCHICAL METRIC SHEAR ---
            print("\n[LQG] Evaluating Baseline Metric Shear Force...")
            active_umnc = 0
            active_hmnc = 0
            active_smnc = 0
            active_imnc = 0
            
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
            
            print("\n[TRIGGER] Simulating stochastic Planck-scale quantum fluctuation...")
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
                    
                    if total_remaining_mass == 0 and not is_developer:
                        print("\n[AUTOMATIC RESET] Total asset extraction! Aeon 0 is left completely massless.")
                        print("                  Conformal metric scale loss forces an instant global CCC Reset of Aeon 0!")
                        print("[INPUT] Do you want this violent energy drainage to manifest a permanent CMB Cold Spot anomaly inside the newly decoupled pocket?")
                        coldspot_choice = input("        Manifest Addendum 1 CMB Cold Spot scar in the new universe? (Y/n): ").strip().lower()
                        
                        if coldspot_choice != 'n':
                            print("\n[ADDENDUM 1 - VERSION A] Vacuum drainage scar injected directly into the newborn metric matrix!")
                            addendum_1_scar_active = True 
                        else:
                            print("\n[SMOOTH RESET] Scar bypassed. Metric drainage potential expanded into isotropic background fields.")
                            addendum_1_scar_active = False
                        
                        n_umnc = active_umnc
                        n_smnc = active_smnc
                        n_imnc = active_imnc
                        n_hmnc = active_hmnc
                        
                        print(f"\n -> Coordination transfer completed. Forwarding {n_umnc + n_hmnc + n_smnc + n_imnc} cores to timeline matrix.\n")
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
        
        if chiral_choice == 'a':
            cpt_chiral_inversion_active = True
        elif chiral_choice == 's':
            if random.random() > 0.5: cpt_chiral_inversion_active = True
    # --- ADVANCED ROUTING LOOP INTERFACE ---
    sandbox_active = True
    while sandbox_active:
        print("\n=====================================================================")
        print(" SIMULATION ROUTING MENUE - TIME AXIS EVOLUTION")
        print("=====================================================================")
        print(f" [CURRENT METRIC] Gen: {current_generation} | Core Assets: {n_umnc} UMNC | {n_hmnc} HMNC | {n_smnc} SMNC | {n_imnc} IMNC")
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
        t_input = float(input("        Delta t (in Gyr, e.g. 0.5 or 13.8): "))

        # --- REFINED AUTOMATIC SCENARIO DETECTOR MATRIX ---
        user_choice = "4"
        if auto_mode:
            print("\n[SYS] Running automatic scenario detection matrix...")
            eval_total = n_umnc + n_hmnc + n_smnc + n_imnc
            accretion_drainage_active = addendum_1_scar_active or addendum_1_dynamic_collision or addendum_1_ccc_exchange_allowed
            
            if eval_total > 0 and accretion_drainage_active:
                user_choice = "8.5"
            elif eval_total > 0 and t_input < 1.0:
                user_choice = "7.2b"
            elif scenario_1_drainage_active and t_input < 1.0:
                user_choice = "1"
            elif eval_total >= 150 and t_input < 1.0:
                user_choice = "6"
            elif eval_total == 0 and t_input >= 50.0:
                user_choice = "12"
            else:
                user_choice = "4"
            print(f"        >> Auto-Detected Trajectory: Scenario {user_choice}")
        else:
            user_choice = input("        >> Enter target Scenario ID from manuscript (1-12): ").strip()

        print(f"\n[EVAL] Executing Matrix Evaluation for Scenario {user_choice}...")
        time.sleep(0.1)
        
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
        try:
            print(f" Current Status: Scar Active = {addendum_1_scar_active}")
        except NameError:
            addendum_1_scar_active = False
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
            print("="*65)
            try:
                num_collisions = int(input(" >> Enter total number of intersecting bubble universes (e.g. 1 or 5): "))
                num_collisions = max(1, num_collisions)
                
                for i in range(num_collisions):
                    print(f"\n    --- Configuring Collision Node {i+1} of {num_collisions} ---")
                    t_collision = float(input(f"    >> Enter execution timeline for Collision {i+1} (in Gyr): "))
                    is_dense_env = input("    >> Is the local intersection domain a high-density plasma zone? (Y/n): ").strip().lower()
                    
                    print(f"    [COMPUTING] Resolving intermetric seam friction at t={t_collision} Gyr...")
                    time.sleep(0.1)
                    
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

        print("=====================================================================")
        print(" PROCESS CONTROL INTERFACE")
        print("=====================================================================")
        action = input("        Select Action Control ([c]onsecutive event / [r]eset aeon / [q]uit): ").strip().lower()
        
        if action == 'r':
            current_generation += 1
            print(f"\n[RESET] Initiating conformal cyclic transition to Generation {current_generation}...")
            n_umnc = int(n_umnc * 0.15); n_hmnc = int(n_hmnc * 0.15); n_smnc = int(n_smnc * 0.15); n_imnc = int(n_imnc * 0.15)
            addendum_1_scar_active = False
            addendum_1_dynamic_collision = False
        elif action == 'q':
            print("\n[SHUTDOWN] Safely disconnecting Loop Quantum Gravity filaments. Offline.\n")
            sandbox_active = False; genesis_reply_loop = False
