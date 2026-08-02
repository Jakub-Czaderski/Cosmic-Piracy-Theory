#!/usr/bin/env python3
import math
import time
import random

def execute_automated_logging(assigned_scenario, eta_calc, spot_centered, deviation, details):
    log_filename = "causal_matrix_output.txt"
    try:
        with open(log_filename, "a") as log_file:
            log_file.write("=====================================================================\n")
            log_file.write(f" TIMESTAMP RECORD:  {time.strftime('%Y-%m-%d %H:%M:%S')} (SYSTEM LOG)\n")
            log_file.write("=====================================================================\n")
            log_file.write(f" -> Active Base Scenario:     Scenario {assigned_scenario}\n")
            log_file.write(f" -> Final Density Value (eta): {eta_calc:.6e}\n")
            log_file.write(f" -> Real-Time Drift Track:     {deviation:+.4f}%\n")
            log_file.write(f" -> Execution Parameters:      {details}\n")
            log_file.write("---------------------------------------------------------------------\n")
            log_file.write(" MULTI-AEON EVOLUTION LINE SECURED: PATH CONVERGES SUCCESSFULLY\n")
            log_file.write("=====================================================================\n\n")
    except IOError:
        print("[FAIL] File-Writer buffer blocked. Check folder write permissions.")

def run_interactive_sandbox():
    print("=====================================================================")
    print("   ______   ______   .___  ___.  __    ______     ______    __  ")
    print("  /  ____| /  __  \\  |   \\/   | |  |  /  ____|   /  __  \\  |  | ")
    print(" |  |     |  |  |  | |  \\  /  | |  | |  |       |  |  |  | |  | ")
    print(" |  |     |  |  |  | |  |\\/|  | |  | |  |       |  |  |  | |  | ")
    print(" |  |____ |  `--'  | |  |  |  | |  | |  |____   |  `--'  | |  | ")
    print("  \\______| \\______/  |__|  |__| |__|  \\______|   \\______/  |__| ")
    print("=====================================================================")
    print("        COSMIC PIRACY SIMULATION - STATE ENGINE v26.0 (MODULAR)")
    print("        Fully Flexible Scenario Matrix & Dynamic Addendum Modifiers")
    print("=====================================================================\n")
    
    current_generation = 0
    n_umnc, n_smnc, n_imnc, n_hmnc = 5, 120, 0, 0
    
    scenario_1_drainage_active = False
    addendum_1_collision_allowed = False
    addendum_1_ccc_exchange_allowed = False
    cpt_chiral_inversion_active = False
    timeline_displacement_risk = False

    print("[INPUT] Initialize at Scenario 0 (Global CPT Crossover Node)?")
    genesis_reply = input("        Trigger Ur-Genesis Phase (y/N): ").strip().lower()
    
    if genesis_reply == 'y':
        print("\n[PHASE 0] AEON 0 - PRIMORDIAL SEEDING AND BOUNDARY GATES")
        print("---------------------------------------------------------------------")
        try:
            print("[INPUT] Enter target timescale for Aeon 0 PNC growth phase:")
            t_genesis = float(input("        Delta t_0 (in Gyr, e.g. 0.2 or 1.5): "))
            n_smnc += int((2.5 * n_umnc + 0.8 * n_smnc) * t_genesis * 15)
            
            print("\n[LQG] Evaluating Baseline Metric Shear Force...")
            active_cores = int(input(f"        Enter active preparing UMNC cores (1-{n_umnc}): "))
            active_cores = max(1, min(active_cores, n_umnc))
            
            total_shear_force = (active_cores * 1.85) * random.uniform(1.2, 2.5)
            
            if total_shear_force >= 10.0:
                print("[SUCCESS] Localized topological rupture verified (Pathway 2 Active).")
                pathway_2_allowed = True
                
                print("\n[INPUT] Evaluate Rotating Kerr Horizon Geometry Bounds:")
                print("        [m] - Standard Materie-Domain (+t)")
                print("        [a] - Antimaterie-Domain (CPT Chiral Inversion Enforced / -t)")
                print("        [s] - Stochastic Quantum Bifurcation")
                kerr_choice = input("        Select Kerr Boundary Mode (m/a/S): ").strip().lower()
                
                if kerr_choice == 'a':
                    cpt_chiral_inversion_active = True
                    timeline_displacement_risk = True
                elif kerr_choice != 'm' and random.random() > 0.5:
                    cpt_chiral_inversion_active = True
                    timeline_displacement_risk = True
                    print("[SYS-GATE] Stochastic Roll triggered Chiral Inversion! Domain: Antimatter (-t).")
                
                print("\n[INPUT] Define Evolution Track Mode for Addendum 1 & Scenario 1:")
                print("        - Scenario 1 Metric Drainage (Delays/Blocks CCC Reset)")
                print("        [c] - Addendum 1 Macro-Collision Track (Physical boundary intersection)")
                print("        [e] - Addendum 1 Immediate CCC Information Exchange (Conformal invariants crossover)")
                track_choice = input("        Select Track (1/c/e): ").strip().lower()
                
                if track_choice == '1':
                    scenario_1_drainage_active = True
                elif track_choice == 'c':
                    addendum_1_collision_allowed = True
                elif track_choice == 'e':
                    addendum_1_ccc_exchange_allowed = True
            else:
                pathway_2_allowed = False
        except ValueError:
            pathway_2_allowed = False
    else:
        pathway_2_allowed = True

    print("\n[INPUT] Select Simulation Routing Mode:")
    print("        [m] - Manual Freedom (Reference Matrix Selection)")
    print("        [a] - Automatic Detection (Dynamic Runtime Context Matrix)")
    print("        [d] - DEVELOPER MODE (Absolute Control & Zero Bounds Override)")
    mode_choice = input("        Select Mode (m/a/D): ").strip().lower()
    
    dev_mode = (mode_choice == 'd')
    auto_mode = (mode_choice == 'a' and not dev_mode)

    if dev_mode:
        print("[SYS] DEVELOPER MODE ACTIVE: GATES MODULARIZED. ALL PHASES OPEN.")
        pathway_2_allowed = True
        scenario_1_drainage_active = True
        addendum_1_collision_allowed = True
        addendum_1_ccc_exchange_allowed = True
        cpt_chiral_inversion_active = True
        timeline_displacement_risk = True

    # Reine, unmodifizierte physikalische Szenarien-Matrix
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
        "8a":  {"name": "Multi-Core Symmetric Non-Disruptive Merging", "tolerance": 0.0, "target": 2.5e-9, "centered": True},
        "8b":  {"name": "Multi-Core Asymmetric Accretion Metric Tears", "tolerance": 15.0, "target": 2.5e-9, "centered": False},
        "9":   {"name": "Multi-Core Cluster Radiative Perimeter Void Walls", "tolerance": 0.0, "target": 2.5e-9, "centered": True},
        "10":  {"name": "Massless Conformal Cyclic Reset Sterile Pocket", "tolerance": 0.0, "target": 0.0, "centered": True},
        "12":  {"name": "Sterile Dynamic Vacuum Phase Infinite Reset Loop", "tolerance": 15.0, "target": 0.0, "centered": True}
    }
    running = True
    while running:
        total_cores = n_umnc + n_smnc + n_imnc + n_hmnc
        print(f"\n[STATE] ACTIVE TIMELINE MATRIX | GENERATION: {current_generation}")
        print(f" -> Active Core Population: {total_cores:,} Seeds")
        print(f"    >> UMNC (Anchors): {n_umnc} | SMNC (Satellite): {n_smnc}")
        print(f"    >> IMNC (Stellar): {n_imnc} | HMNC (Merger):    {n_hmnc}")
        print("---------------------------------------------------------------------")

        sfr_kinetic = max(0.1, (0.5 + (2.0 * n_umnc + 1.2 * n_smnc + 0.5 * n_imnc) * 0.1))
        eval_umnc, eval_smnc, eval_imnc, eval_hmnc = n_umnc, n_smnc, n_imnc, n_hmnc
        eval_total = total_cores

        try:
            print("[INPUT] Enter target evolution timescale for this event:")
            t_input = float(input("        Delta t (in Gyr, e.g. 0.5 or 13.8): "))

            if t_input >= 500.0 and not dev_mode:
                print(f"\n[SYS] Enforcing massive Hawking deflation...")
                n_umnc, n_smnc, n_imnc, n_hmnc = 0, 0, 0, 0
                continue

            if dev_mode or (not auto_mode):
                prompt_text = "        [DEV] Modify active core counts? (Y/n): " if dev_mode else "        Override active seeds? (y/N): "
                if input(prompt_text).strip().lower() in ['y', '']:
                    impact = input("        Select Impact ([t]emp/[p]erm): ").strip().lower()
                    eval_umnc = int(input("        >> Enter UMNC count: "))
                    eval_smnc = int(input("        >> Enter new SMNC count: "))
                    eval_imnc = int(input("        >> Enter new IMNC count: "))
                    eval_hmnc = int(input("        >> Enter new HMNC count: "))
                    if impact == 'p' and not (dev_mode and impact == 't'):
                        n_umnc, n_smnc, n_imnc, n_hmnc = eval_umnc, eval_smnc, eval_imnc, eval_hmnc
                    eval_total = eval_umnc + eval_smnc + eval_imnc + eval_hmnc

            # BASE SCENARIO ROUTING
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
            else:
                print("\n[INPUT] Enter target BASE scenario to execute from the reference matrix:")
                print("        Options: 2, 3a, 3b, 4, 5, 6, 7.1, 7.2a, 7.2b, 8a, 8b, 9, 10, 12")
                user_choice = input("        Select Base Scenario: ").strip()
                
                if not dev_mode:
                    if user_choice in ["10", "12"] and t_input < 100.0:
                        print("[BLOCKED] Early Event-3 scenarios blocked. Fallback to 9.")
                        user_choice = "9"
                if user_choice not in manuscript_scenarios and user_choice != "1":
                    user_choice = "9"

            # DYNAMISCHE APPLICATION VON ADDENDUM 1 ALS LAYER
            active_modifier = "None"
            active_tolerance = manuscript_scenarios[user_choice]["tolerance"] if user_choice != "1" else 15.0
            target_eta = manuscript_scenarios[user_choice]["target"] if user_choice != "1" else 0.0
            spot_centered = manuscript_scenarios[user_choice]["centered"] if user_choice != "1" else True

            if addendum_1_collision_allowed:
                # Unterscheidung des Modifikators rein nach Zeitskala (flexibel für alle Szenarien)
                if math.isclose(t_input, 13.8, rel_tol=1e-2):
                    active_modifier = "Addendum 1 (Delayed Hybrid)"
                    active_tolerance = 1.0  # Rigide 1% Grenze überschreibt das Szenario-Target!
                    spot_centered = True
                    print(f"\n[LAYER] Injecting {active_modifier} into Scenario {user_choice}!")
                    print("        Enforcing rigid statistical boundary tolerance of +/-1%.")
                elif t_input < 1.0 and eval_total >= 50:
                    active_modifier = "Addendum 1 (Same-Aeon Hybrid)"
                    active_tolerance = 15.0 # Schaltet stochastische Fluktuation frei
                    spot_centered = False
                    print(f"\n[LAYER] Injecting {active_modifier} into Scenario {user_choice}!")
                    print("        Forcing macro-cosmological lateral intersection. Spot de-centered.")

                # Das Materie-Mitnahme-Gatter arbeitet nun ebenfalls komplett flexibel
                if active_modifier != "None" and eval_umnc >= 1 and not dev_mode:
                    print(f"        [PROTOCOL] Mother core anchors ({eval_umnc} UMNC) present inside current manifold.")
                    if input("        Execute layer collision event? (Y/n): ").strip().lower() == 'n':
                        print("[SYS] Modifier bypassed. Running unperturbed base architecture.")
                        active_modifier = "None"
                        active_tolerance = manuscript_scenarios[user_choice]["tolerance"]
                        spot_centered = manuscript_scenarios[user_choice]["centered"]

            # FINAL BOUNDARY EVALUATION (Mit dynamisch injizierten Layern)
            print(f"\n[EVAL] Executing Evaluation for Scenario {user_choice} + Modifier [{active_modifier}]:")
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

            # PROCESS CONTROL INTERFACE
            print("\n" + "="*65)
            choice = input("        Select Action Control ([c]/[r]/[q]): ").strip().lower()

            if choice == 'c':
                print(f"\n[SYS] Slicing consecutive event path over {t_input} Gyr.")
                spawned_stars = int(sfr_kinetic * t_input * 1.5)
                n_imnc += int(spawned_stars * 0.70)
                n_smnc += int(spawned_stars * 0.25) + int(n_umnc * 0.05 * t_input)
                n_hmnc += int(n_smnc * 0.02 * t_input)
                n_smnc, n_imnc, n_hmnc = max(0, n_smnc), max(0, n_imnc), max(0, n_hmnc)
            elif choice == 'r':
                print("\n[RESET] Enforcing Conformal Cyclic Reset...")
                if scenario_1_drainage_active and not dev_mode:
                    print("[WARNING] Mass drainage delayed parent Hawking evaporation. Reset sterile.")
                elif addendum_1_ccc_exchange_allowed or dev_mode:
                    print("[ADDENDUM 1 - CROSSOVER] GW Spectra transferred safely via Conformal Crossover.")

                current_generation += 1
                n_umnc, n_smnc, n_imnc, n_hmnc = int(n_umnc * 0.15), int(n_smnc * 0.15), int(n_imnc * 0.15), int(n_hmnc * 0.15)
            elif choice == 'q':
                running = False
        except ValueError:
            running = False

if __name__ == "__main__":
    run_interactive_sandbox()
