#!/usr/bin/env python3
import math
import time
import random

def execute_automated_logging(assigned_scenario, eta_calc, spot_centered, deviation, details):
    """
    Handles permanent track logging into a local text database.
    Strictly uses ASCII decorators for terminal and server environment compatibility.
    """
    log_filename = "causal_matrix_output.txt"
    try:
        with open(log_filename, "a") as log_file:
            log_file.write("=====================================================================\n")
            log_file.write(f" TIMESTAMP RECORD:  {time.strftime('%Y-%m-%d %H:%M:%S')} (SYSTEM LOG)\n")
            log_file.write("=====================================================================\n")
            log_file.write(f" -> Active Base Scenario:     Scenario {assigned_scenario}\n")
            log_file.write(f" -> Final Density Value (eta): {eta_calc:.6e}\n")
            log_file.write(f" -> CMB Scar Center Profile:  {spot_centered}\n")
            log_file.write(f" -> Real-Time Drift Track:     {deviation:+.4f}%\n")
            log_file.write(f" -> Execution Parameters:      {details}\n")
            log_file.write("---------------------------------------------------------------------\n")
            log_file.write(" MULTI-AEON EVOLUTION LINE SECURED: PATH CONVERGES SUCCESSFULLY\n")
            log_file.write("=====================================================================\n\n")
    except IOError:
        print("[FAIL] File-Writer buffer blocked. Check folder write permissions.")

def run_interactive_sandbox():
    """
    Main state engine executing multi-generational cosmological cascade models.
    Enforces dynamic timeline perturbations, overrides, and fluid fluctuations.
    """
    print("=====================================================================")
    print("   ______   ______   .___  ___.  __    ______     ______    __  ")
    print("  /  ____| /  __  \\  |   \\/   | |  |  /  ____|   /  __  \\  |  | ")
    print(" |  |     |  |  |  | |  \\  /  | |  | |  |       |  |  |  | |  | ")
    print(" |  |     |  |  |  | |  |\\/|  | |  | |  |       |  |  |  | |  | ")
    print(" |  |____ |  `--'  | |  |  |  | |  | |  |____   |  `--'  | |  | ")
    print("  \\______| \\______/  |__|  |__| |__|  \\______|   \\______/  |__| ")
    print("=====================================================================")
    print("        COSMIC PIRACY SIMULATION - STATE ENGINE v26.2 (UNRESTRICTED)")
    print("        ASCII Core Layout & Stochastic Additive Quantum Peak Online")
    print("=====================================================================\n")
    
    # Astrophysical initialization: No stars or mergers exist in the initial infant phase
    current_generation = 0
    n_umnc = 5      # Inherited primordial anchor seeds
    n_smnc = 120    # Inherited primordial satellite seeds
    n_imnc = 0      # Dynamic stellar collapse cores (generated over time via SFR)
    n_hmnc = 0      # Hypermassive merger anchors (generated via consecutive slicing)
    
    # Boundary gate flags initialized for Aeon 0 routing
    pathway_2_allowed = False
    scenario_1_drainage_active = False
    addendum_1_collision_allowed = False
    addendum_1_ccc_exchange_allowed = False
    cpt_chiral_inversion_active = False
    timeline_displacement_risk = False

    # 1. SCENARIO 0 INITIALIZATION PROFILE
    print("[INPUT] Initialize at Scenario 0 (Global CPT Crossover Node)?")
    genesis_reply = input("        Trigger Ur-Genesis Phase (y/N): ").strip().lower()
    
    if genesis_reply == 'y':
        print("\n[PHASE 0] AEON 0 - PRIMORDIAL SEEDING AND BOUNDARY GATES")
        print("---------------------------------------------------------------------")
        try:
            print("[INPUT] Enter target timescale for Aeon 0 PNC growth phase:")
            t_genesis = float(input("        Delta t_0 (in Gyr, e.g. 0.2 or 1.5): "))
            
            # Seed propagation during the early unperturbed nucleation era
            pnc_spawned = int((2.5 * n_umnc + 0.8 * n_smnc) * t_genesis * 15)
            n_smnc += pnc_spawned
            print("[SUCCESS] High-energy radiation fields collapsed stochastically.")
            print(f"          Current Pool: UMNC={n_umnc} | SMNC={n_smnc}")
            
            print("\n[LQG] Evaluating Baseline Metric Shear Force...")
            active_umnc = int(input(f"        Enter active preparing UMNC cores (1-{n_umnc}): "))
            active_umnc = max(1, min(active_umnc, n_umnc))
            
            # Baseline shear prepared by the cores (sub-critical on its own)
            baseline_shear = active_umnc * 1.85
            lqg_tensile_limit = 10.0  # Invariant structural threshold (Sigma_max)
            print(f" -> Prepared Metric Baseline Shear (Sub-Critical): {baseline_shear:.2f} / {lqg_tensile_limit:.2f}")
            
            # STOCHASTIC PEAK TRIGGER: The quantum fluctuation provides the definitive high-energy boost
            print("\n[TRIGGER] Simulating stochastic Planck-scale quantum fluctuation...")
            time.sleep(0.1)
            
            # A highly energetic fluctuation roll injects a massive additive energy spike to breach the 10.0 limit
            quantum_fluctuation_peak = random.uniform(1.5, 8.5)
            print(f" -> Generated Quantum Fluctuation Energy Peak: +{quantum_fluctuation_peak:.4f}")
            
            # Total combined force is the baseline preparation plus the sudden quantum peak
            total_shear_force = baseline_shear + quantum_fluctuation_peak
            print(f" -> Total Combined Shear Force at Horizon Boundary: {total_shear_force:.2f}")
            
            if total_shear_force >= lqg_tensile_limit:
                print("[CRITICAL] Quantum fluctuation successfully breached the LQG tensile threshold!")
                print("[SUCCESS] Localized topological rupture verified (Pathway 2 Unleashed).")
                pathway_2_allowed = True
                
                # Three-tier chiral bifurcation gate (Section 3.2 mapping)
                print("\n[INPUT] Evaluate Rotating Kerr Horizon Geometry Bounds:")
                print("        [m] - Standard Materie Domain (Symmetric Baryon Average / +t)")
                print("        [a] - Antimaterie Domain (CPT Chiral Inversion Enforced / -t)")
                print("        [s] - Stochastic Quantum Bifurcation (Probability-based roll)")
                kerr_choice = input("        Select Kerr Boundary Mode (m/a/S): ").strip().lower()
                
                if kerr_choice == 'a':
                    cpt_chiral_inversion_active = True
                    timeline_displacement_risk = True
                elif kerr_choice != 'm' and random.random() > 0.5:
                    cpt_chiral_inversion_active = True
                    timeline_displacement_risk = True
                    print("[SYS-GATE] Stochastic roll triggered Ergosphere Chiral Inversion! (-t)")
                
                # Topological track mapping for ancestral metric interactions
                print("\n[INPUT] Define Evolution Track Mode for Addendum 1 & Scenario 1:")
                print("        - Scenario 1 Metric Drainage (Absorbs mass into parent aeon -> Blocks immediate Reset)")
                print("        [c] - Addendum 1 Macro-Collision Track (Physical boundary intersection later in time)")
                print("        [e] - Addendum 1 Immediate CCC Information Exchange (Conformal invariants crossover)")
                track_choice = input("        Select Track (1/c/e): ").strip().lower()
                
                if track_choice == '1':
                    scenario_1_drainage_active = True
                    print("[SYS-GATE] Mass injected into old universe. Parent Hawking evaporation delayed.")
                elif track_choice == 'c':
                    addendum_1_collision_allowed = True
                    print("[SYS-GATE] Kinematic boundary intersection primed for later epoch evaluations.")
                elif track_choice == 'e':
                    addendum_1_ccc_exchange_allowed = True
                    print("[SYS-GATE] Invariant tensor perturbations aligned across the crossover.")
            else:
                print("[SUPPRESSED] Combined fluctuation amplitude insufficient to tear filaments.")
                print("[WARNING] Metric remains smoothly embedded. Pathway 2 blocked.")
                pathway_2_allowed = False
                
            execute_automated_logging("0_Seeding", 2.5e-9, True, 0.0, f"Aeon0 Seeding t={t_genesis}")
            print("\n[KERNEL] Phase 0 complete. Progressing...\n" + "="*65 + "\n")
        except ValueError:
            print("[FAIL] Numerical validation aborted. Defaulting bounds.")
            pathway_2_allowed = False
    else:
        pathway_2_allowed = True
    # 2. RUNTIME SIMULATION ENVIRONMENT CONFIGURATION
    print("[INPUT] Select Simulation Routing Mode:")
    print("        [m] - Manual Freedom (Reference Matrix Selection)")
    print("        [a] - Automatic Detection (Dynamic Runtime Context Matrix)")
    print("        [d] - DEVELOPER MODE (Absolute Control & Zero Bounds Override Overrides)")
    mode_choice = input("        Select Mode (m/a/D): ").strip().lower()
    
    dev_mode = (mode_choice == 'd')
    auto_mode = (mode_choice == 'a' and not dev_mode)

    # Developer override triggers: Administrative detachment from physics bounds
    if dev_mode:
        print("[SYS] DEVELOPER MODE ACTIVE: ALL GATES OPEN. CONSTRAINT BYPASSERS UNLIMITED.")
        pathway_2_allowed = True
        scenario_1_drainage_active = True
        addendum_1_collision_allowed = True
        addendum_1_ccc_exchange_allowed = True
        cpt_chiral_inversion_active = True
        timeline_displacement_risk = True

    # Standalone unperturbed evolutionary scenarios defined in the manuscript
    manuscript_scenarios = {
        "2":   {"name": "Solitary Isotropic Hierarchical Accretion", "tolerance": 15.0, "target": 1.0e-9, "centered": True},
        "3a":  {"name": "Direct Conformal Protection Branch", "tolerance": 0.0, "target": 2.5e-9, "centered": True},
        "3b":  {"name": "Advanced Conformal Protection Antimatter Domain", "tolerance": 15.0, "target": 2.5e-9, "centered": False},
        "4":   {"name": "Decaying Parent Aeon Slow Accretion Matrix", "tolerance": 15.0, "target": 1.0e-9, "centered": False},
        "5":   {"name": "Solitary Anchor Matrix with Active Shockwave", "tolerance": 0.0, "target": 2.5e-9, "centered": True},
        "6":   {"name": "Multi-Core Cluster Baseline Kinematics", "tolerance": 0.0, "target": 2.5e-9, "centered": True},
        "7.1": {"name": "Multi-Core Initial Oasis Density Core Theft", "tolerance": 15.0, "target": 2.5e-9, "centered": False},
        "7.2a":{"name": "Multi-Core Transitional Relativistic Slingshot Pockets", "tolerance": 15.0, "target": 2.444449e-09, "centered": False},
        "7.2b":{"name": "Multi-Core Cluster High-Tensile Repulsion Oasis", "tolerance": 15.0, "target": 2.444449e-09, "centered": False},
        "9":   {"name": "Multi-Core Cluster Radiative Perimeter Void Walls", "tolerance": 0.0, "target": 2.5e-9, "centered": True},
        "10":  {"name": "Massless Conformal Cyclic Reset Sterile Pocket", "tolerance": 0.0, "target": 0.0, "centered": True},
        "12":  {"name": "Sterile Dynamic Vacuum Phase Infinite Reset Loop", "tolerance": 15.0, "target": 0.0, "centered": True}
    }

    # 3. INTERACTIVE SIMULATION RUNTIME LOOP
    running = True
    while running:
        total_cores = n_umnc + n_smnc + n_imnc + n_hmnc
        print(f"\n[STATE] ACTIVE TIMELINE MATRIX | GENERATION: {current_generation}")
        print(f" -> Active Core Population: {total_cores:,} Seeds")
        print(f"    >> UMNC (Anchors): {n_umnc} | SMNC (Satellite): {n_smnc}")
        print(f"    >> IMNC (Stellar): {n_imnc} | HMNC (Merger):    {n_hmnc}")
        if cpt_chiral_inversion_active:
            print(" -> Metric Vector Domain: ANTIMATTER METRIC METRIC ACTIVE (-t)")
        else:
            print(" -> Metric Vector Domain: STANDARD MATERIE METRIC ACTIVE (+t)")
        print("---------------------------------------------------------------------")

        # Dynamic star formation kinetics scaling directly with current core counts
        sfr_kinetic = max(0.1, (0.5 + (2.0 * n_umnc + 1.2 * n_smnc + 0.5 * n_imnc) * 0.1))
        print(f" -> Computed Star Formation Rate (SFR): {sfr_kinetic:.4f} M_sun/yr")
        
        # Lorentz metrics computed for the semi-classical 0.85c escape limits
        effective_acceleration_factor = 1.8983 / (1.0 / math.sqrt(1.0 - 0.8505**2))
        print(f" -> Active Core Metric Shielding Lock:  {effective_acceleration_factor:.4f}x")

        try:
            print("\n[INPUT] Enter target evolution timescale for this event:")
            t_input = float(input("        Delta t (in Gyr, e.g. 0.5 or 13.8): "))

            # Enforce absolute timeline collapse across hyper-mature eras if dev mode is inactive
            if t_input >= 500.0 and not dev_mode:
                print(f"\n[SYS] Timescale triggers total Hawking evaporation. Clearing active metrics...")
                n_umnc, n_smnc, n_imnc, n_hmnc = 0, 0, 0, 0
                continue

            # Allocation copies created to shield core state data during evaluation
            eval_umnc, eval_smnc, eval_imnc, eval_hmnc = n_umnc, n_smnc, n_imnc, n_hmnc
            eval_total = total_cores

            # UNRESTRICTED ASSET OVERRIDES (Always open in Dev, optional in manual)
            if dev_mode or (not auto_mode):
                prompt_text = "        [DEV] Modify active core counts? (Y/n): " if dev_mode else "        Override active seeds? (y/N): "
                if input(prompt_text).strip().lower() in ['y', '']:
                    impact = input("        Select Override Scope ([t]emp run setup / [p]ermanent global line): ").strip().lower()
                    eval_umnc = int(input("        >> Enter UMNC count: "))
                    eval_smnc = int(input("        >> Enter SMNC count: "))
                    eval_imnc = int(input("        >> Enter IMNC count: "))
                    eval_hmnc = int(input("        >> Enter HMNC count: "))
                    
                    if impact == 'p' and not (dev_mode and impact == 't'):
                        # Apply permanent baseline shifts to the universal chronology
                        n_umnc, n_smnc, n_imnc, n_hmnc = eval_umnc, eval_smnc, eval_imnc, eval_hmnc
                        sfr_kinetic = max(0.1, (0.5 + (2.0 * n_umnc + 1.2 * n_smnc + 0.5 * n_imnc) * 0.1))
                    eval_total = eval_umnc + eval_smnc + eval_imnc + eval_hmnc
            # 4. CONTEXT BIFURCATION & ROUTING ENGINE
            if auto_mode:
                print("\n[SYS] Running automatic scenario detection matrix...")
                if scenario_1_drainage_active and t_input < 1.0:
                    user_choice = "1"
                elif eval_total < 50:
                    user_choice = "7.2b"
                elif eval_total >= 150 and t_input < 1.0:
                    user_choice = "6"
                else:
                    user_choice = "9"
                print(f"        >> Auto-Detected Trajectory: {user_choice}")
            else:
                print("\n[INPUT] Enter target BASE scenario to execute from the reference matrix:")
                print("        Options: 2, 3a, 3b, 4, 5, 6, 7.1, 7.2a, 7.2b, 9, 10, 12")
                user_choice = input("        Select Base Scenario: ").strip()
                
                # Administrative block bypass guards active under Dev mode
                if not dev_mode:
                    if user_choice == "1" and not scenario_1_drainage_active:
                        print("[BLOCKED] Vacuum drainage gates absent in Phase 0! Fallback to 9.")
                        user_choice = "9"
                    if user_choice in ["10", "12"] and t_input < 100.0:
                        print("[BLOCKED] Early Event-3 scenarios restricted. Fallback to 9.")
                        user_choice = "9"
                if user_choice not in manuscript_scenarios and user_choice != "1":
                    user_choice = "9"

            # 5. DYNAMIC MODIFIER INJECTION TRACKER (MODULAR ADDENDUM LAYER)
            active_modifier = "None"
            active_tolerance = manuscript_scenarios[user_choice]["tolerance"] if user_choice != "1" else 15.0
            target_eta = manuscript_scenarios[user_choice]["target"] if user_choice != "1" else 0.0
            spot_centered = manuscript_scenarios[user_choice]["centered"] if user_choice != "1" else True

            if addendum_1_collision_allowed:
                # Topographical profiling: Enforce spatial centering based on chronological history
                if math.isclose(t_input, 13.8, rel_tol=1e-2):
                    active_modifier = "Addendum 1 (Delayed Hybrid)"
                    active_tolerance = 1.0  
                    spot_centered = True    # Ancestral link fixes causal feedback directly at the center
                    print(f"\n[LAYER] Injecting {active_modifier} into Scenario {user_choice}!")
                    print("        Enforcing centered trans-cosmic link with +/-1% tolerance boundaries.")
                elif t_input < 1.0 and eval_total >= 50:
                    active_modifier = "Addendum 1 (Same-Aeon Hybrid)"
                    active_tolerance = 15.0 
                    spot_centered = False   # Lateral stochastic collision forces a de-centered Cold Spot profile
                    print(f"\n[LAYER] Injecting {active_modifier} into Scenario {user_choice}!")
                    print("        Enforcing de-centered lateral macro-collision bounds.")

                # Unrestricted manual control bypass for the Binary Gate of Section 4.4
                if active_modifier != "None" and eval_umnc >= 1 and not dev_mode:
                    print(f"        [PROTOCOL] Mother core anchors ({eval_umnc} UMNC) present inside current manifold.")
                    if input("        Execute layered collision event? (Y/n): ").strip().lower() == 'n':
                        print("[SYS] Modifier bypassed. Restoring unperturbed base architecture.")
                        active_modifier = "None"
                        active_tolerance = manuscript_scenarios[user_choice]["tolerance"]
                        spot_centered = manuscript_scenarios[user_choice]["centered"]

            # 6. TIMELINE DISPLACEMENT BOUND EVALUATION
            high_energy_chiral_cascades = ["3b", "5", "7.2b", "9"]
            if user_choice in high_energy_chiral_cascades and timeline_displacement_risk:
                print("\n[CAUSAL CRITICAL] TIMELINE DISPLACEMENT INITIATED!")
                print("                  Mass-free boundary condition lost scale-invariance.")
                # Compute chronological phase shift vector between asymmetric (+t) and (-t) regions
                chronological_phase_shift = (t_input * eval_umnc * 3.14159) / 100.0
                print(f"                  -> Computed Chronological Phase Shift: {chronological_phase_shift:.4f} rad")
                if dev_mode:
                    print("                  [DEV-BYPASS] Holonomy entanglement overwrites synchronization errors.")
                else:
                    print("                  [SUCCESS] Subsection 4.3 Quantum Entanglement anchors the causal link.")
                    print("                            CPT-conserving macro-equilibrium successfully stabilized.")
            # Compute fluid fluctuations and target density tracks
            print(f"\n[EVAL] Executing Matrix Evaluation for Scenario {user_choice} + Modifier [{active_modifier}]:")
            if active_tolerance == 15.0:
                eta_calc = target_eta * random.uniform(0.85, 1.15)
            elif active_tolerance == 1.0:
                eta_calc = target_eta * random.uniform(0.99, 1.01)
            else:
                eta_calc = target_eta

            deviation_percent = ((eta_calc - target_eta) / target_eta) * 100.0 if target_eta > 0 else 0.0
            print(f"   >> Calculated Oasis Density (eta):    {eta_calc:.6e}")
            print(f"   >> CMB Cold Spot Centered Alignment:   {spot_centered}")

            execute_automated_logging(user_choice, eta_calc, spot_centered, deviation_percent, f"Modifier: {active_modifier}")

            # 7. METRIC TIMELINE PROGRESSION AND PROCESS CONTROL INTERFACE
            print("\n" + "="*65)
            print(" PROCESS CONTROL INTERFACE")
            print("="*65)
            choice = input("        Select Action Control ([c]onsecutive event / [r]eset aeon / [q]uit): ").strip().lower()

            if choice == 'c':
                print(f"\n[SYS] Slicing consecutive event path over {t_input} Gyr.")
                
                # CONTINUOUS HAWKING RADIATION THERMAL EVAPORATION (hierarchical mass leakage)
                print("[HAWKING-RADIATION] Processing active mass evaporation leakage...")
                n_imnc_evap = int(n_imnc * (1.0 - math.exp(-0.05 * t_input)))   # Fast stellar core decay
                n_smnc_evap = int(n_smnc * (1.0 - math.exp(-0.01 * t_input)))   # Moderate satellite decay
                n_hmnc_evap = int(n_hmnc * (1.0 - math.exp(-0.001 * t_input)))  # Highly resilient merger decay
                n_umnc_evap = int(n_umnc * (1.0 - math.exp(-0.0001 * t_input))) # Saturated metric anchor stability
                
                if (n_imnc_evap + n_smnc_evap) > 0:
                    print(f"                    Thermal Evaporation: -{n_imnc_evap} IMNC, -{n_smnc_evap} SMNC seeds.")
                
                n_imnc = max(0, n_imnc - n_imnc_evap)
                n_smnc = max(0, n_smnc - n_smnc_evap)
                n_hmnc = max(0, n_hmnc - n_hmnc_evap)
                n_umnc = max(0, n_umnc - n_umnc_evap)

                # ACCELERATED STAR AND MERGER CORE NUCLEATION (SFR metrics)
                spawned_stars = int(sfr_kinetic * t_input * 1.5)
                n_imnc += int(spawned_stars * 0.70)
                n_smnc += int(spawned_stars * 0.25) + int(n_umnc * 0.05 * t_input)
                n_hmnc += int(n_smnc * 0.02 * t_input)
                
                n_smnc, n_imnc, n_hmnc = max(0, n_smnc), max(0, n_imnc), max(0, n_hmnc)
                print(f"[SUCCESS] Core population advanced. Generated {spawned_stars} fresh anchors.")
                
            elif choice == 'r':
                print("\n[RESET] Enforcing Conformal Cyclic Reset across the 3-surface horizon...")
                time.sleep(0.1)
                
                # Structural reset check: Evaluates if mass drainage delayed Hawking deflation
                if scenario_1_drainage_active and not dev_mode:
                    print("[WARNING] Massive mass drainage from Scenario 1 is still trapped in the parent metric.")
                    print("          Parent Hawking evaporation is heavily delayed. Instant CCC exchange FAILED.")
                    print("          -> Result: Crossover surface is sterile. No tensor remnants preserved.")
                elif addendum_1_ccc_exchange_allowed or dev_mode:
                    print("[ADDENDUM 1 - CONFORMAL CROSSOVER] Transferring tensor invariants via Gravitational Wave Spectra!")
                    print("          -> Success: Residual masses converted into smooth geometric perturbations.")
                else:
                    print("[SYS] Standard cyclic transition complete. No non-local tensor anomalies stored.")

                # Conformal Mass Evaporation Filter: 15% of structures survive as ancestral remnants
                current_generation += 1
                n_umnc = int(n_umnc * 0.15)
                n_smnc = int(n_smnc * 0.15)
                n_imnc = int(n_imnc * 0.15)
                n_hmnc = int(n_hmnc * 0.15)
                print(f" -> Conformal Rescaling Complete. Welcome to Generation {current_generation}!")
                
            elif choice == 'q':
                print("\n[SHUTDOWN] Safely disconnecting loop quantum gravity filaments. Exiting kernel...")
                running = False
            else:
                print("\n[SYS] Control command unassigned. Maintaining active timeline matrix.")
        except ValueError:
            print("\n[FAIL] Numerical evaluation requires valid physical entries.")
            running = False

    print("\n=====================================================================")
    print(" MULTI-AEON SIMULATION RUN COMPLETE: MATRIX OUTPUT PERMANENTLY LOCKED")
    print("=====================================================================\n")

if __name__ == "__main__":
    run_interactive_sandbox()
