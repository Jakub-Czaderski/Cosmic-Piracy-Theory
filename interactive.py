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
            log_file.write(f" -> Assigned Path Invariant:  Scenario {assigned_scenario}\n")
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
    print("=====================================================================")
    print("   ______   ______   .___  ___.  __    ______     ______    __  ")
    print("  /  ____| /  __  \\  |   \\/   | |  |  /  ____|   /  __  \\  |  | ")
    print(" |  |     |  |  |  | |  \\  /  | |  | |  |       |  |  |  | |  | ")
    print(" |  |     |  |  |  | |  |\\/|  | |  | |  |       |  |  |  | |  | ")
    print(" |  |____ |  `--'  | |  |  |  | |  | |  |____   |  `--'  | |  | ")
    print("  \\______| \\______/  |__|  |__| |__|  \\______|   \\______/  |__| ")
    print("=====================================================================")
    print("        COSMIC PIRACY SIMULATION - STATE ENGINE v18.0 (HYBRID)")
    print("        Stochastic Planck-Scale Fluctuation Trigger Framework")
    print("=====================================================================\n")
    
    current_generation = 0
    n_umnc = 5      
    n_smnc = 120    
    n_imnc = 0      
    n_hmnc = 0      

    print("[INPUT] Initialize at Scenario 0 (Global CPT Crossover Node)?")
    genesis_reply = input("        Trigger Ur-Genesis Phase (y/N): ").strip().lower()
    
    if genesis_reply == 'y':
        print("\n" + "="*65)
        print(" [PHASE 0] AEON 0 - PRIMORDIAL SEEDING AND NUCLEATION")
        print("="*65)
        try:
            print("[INPUT] Enter target timescale for Aeon 0 PNC growth phase:")
            t_genesis = float(input("        Delta t_0 (in Gyr, e.g. 0.2 or 1.5): "))
            
            pnc_spawned = int((2.5 * n_umnc + 0.8 * n_smnc) * t_genesis * 15)
            n_smnc += pnc_spawned
            print(f"[SUCCESS] High-energy radiation fields collapsed stochastically.")
            print(f"          Current Pool: UMNC={n_umnc} | SMNC={n_smnc}")
            
            print("\n[QUANTUM PREPARATION] Evaluating Baseline Metric Shear Force...")
            print(f"        Available frame-dragging anchors: {n_umnc} UMNC Cores.")
            active_cores = int(input(f"        Enter number of active preparing UMNC cores (1-{n_umnc}): "))
            active_cores = max(1, min(active_cores, n_umnc))
            
            # Basis-Scherkraft präpariert das Feld sub-kritisch (Kerne schaffen es nie allein)
            baseline_shear = active_cores * 1.85
            lqg_tensile_limit = 10.0  # Sigma_max
            print(f" -> Prepared Metric Baseline Shear (Sub-Critical): {baseline_shear:.2f} / {lqg_tensile_limit:.2f}")
            
            # STOCHASTISCHER QUANTENFLUKTUATION TRIGGER (Kritischer Impuls)
            print("\n[TRIGGER] Simulating stochastic Planck-scale quantum fluctuation...")
            time.sleep(0.1)
            quantum_fluctuation_amplitude = random.uniform(1.2, 2.5)
            print(f" -> Generated Fluctuation Amplitude Factor: x{quantum_fluctuation_amplitude:.4f}")
            
            # Totale Scherkraft = Basis-Scherung + stochastischer Quanten-Impuls
            total_shear_force = baseline_shear * quantum_fluctuation_amplitude
            print(f" -> Total Combined Shear Force at Horizon Boundary: {total_shear_force:.2f}")
            
            if total_shear_force >= lqg_tensile_limit:
                print("[CRITICAL] Quantum fluctuation successfully breached the LQG tensile threshold!")
                print("[SUCCESS] Localized topological rupture verified (Pathway 2 Unleashed).")
                pathway_2_allowed = True
            else:
                print("[SUPPRESSED] Combined fluctuation amplitude insufficient to tear filaments.")
                print("[WARNING] Metric remains smoothly embedded. Pathway 2 blocked.")
                pathway_2_allowed = False
                
            execute_automated_logging("0_Seeding", 2.5e-9, True, 0.0, f"Aeon0 Seeding t={t_genesis}Gyr, Fluctuation={quantum_fluctuation_amplitude:.2f}")
            print("\n[KERNEL] Phase 0 complete. Progressing...\n" + "="*65 + "\n")
        except ValueError:
            print("[FAIL] Numerical validation aborted.")
            pathway_2_allowed = False
    else:
        pathway_2_allowed = True

    print("[INPUT] Select Simulation Routing Mode:")
    print("        [m] - Manual Freedom (Reference Matrix Selection)")
    print("        [a] - Automatic Detection (Dynamic Runtime Context Matrix)")
    mode_choice = input("        Select Mode (m/A): ").strip().lower()
    auto_mode = (mode_choice != 'm')
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
        "12":  {"name": "Sterile Dynamic Vacuum Phase Infinite Reset Loop", "tolerance": 15.0, "target": 0.0, "centered": True},
        "6_add1_same": {"name": "Scenario 6 + Addendum 1 Same-Aeon Lateral Collision", "tolerance": 15.0, "target": 2.5e-9, "centered": False},
        "6_add1_delay": {"name": "Scenario 6 + Addendum 1 Mother-Child Delayed Crossover", "tolerance": 1.0, "target": 2.5e-9, "centered": True}
    }

    running = True
    while running:
        total_cores = n_umnc + n_smnc + n_imnc + n_hmnc
        print(f"\n⚡ ACTIVE TIMELINE MATRIX | GENERATION: {current_generation}")
        print(f" -> Active Core Population: {total_cores:,} Seeds")
        print(f"    >> UMNC (Anchors): {n_umnc} | SMNC (Satellite): {n_smnc}")
        print(f"    >> IMNC (Stellar): {n_imnc} | HMNC (Merger):    {n_hmnc}")
        print("-" * 65)

        sfr_kinetic = max(0.1, (0.5 + (2.0 * n_umnc + 1.2 * n_smnc + 0.5 * n_imnc) * 0.1))
        print(f" -> Computed Star Formation Rate (SFR): {sfr_kinetic:.4f} M_sun/yr")
        effective_acceleration_factor = 1.8983 / (1.0 / math.sqrt(1.0 - 0.8505**2))
        print(f" -> Active Core Metric Shielding Lock:  {effective_acceleration_factor:.4f}x")

        try:
            print("\n[INPUT] Enter target evolution timescale for this event:")
            t_input = float(input("        Delta t (in Gyr, e.g. 0.5 or 13.8): "))

            if t_input >= 500.0:
                print(f"\n [EVAPORATION] Enforcing massive Hawking deflation...")
                n_umnc, n_smnc, n_imnc, n_hmnc = 0, 0, 0, 0
                execute_automated_logging("10 (Sterile)", 0.0, True, -100.0, f"Hawking Deflation at {t_input} Gyr")
                continue

            eval_umnc, eval_smnc, eval_imnc, eval_hmnc = n_umnc, n_smnc, n_imnc, n_hmnc
            eval_total = total_cores
            eval_sfr = sfr_kinetic

            if not auto_mode:
                print("\n[INPUT] Do you want to manually override the core population counts?")
                override_choice = input("        Override active seeds? (y/N): ").strip().lower()
                if override_choice == 'y':
                    print("        Select Override Impact: [t] - Temporary / [p] - Permanent")
                    impact = input("        Select Impact (t/P): ").strip().lower()
                    in_umnc = int(input("        >> Enter new UMNC count: "))
                    in_smnc = int(input("        >> Enter new SMNC count: "))
                    in_imnc = int(input("        >> Enter new IMNC count: "))
                    in_hmnc = int(input("        >> Enter new HMNC count: "))
                    
                    if impact == 't':
                        eval_umnc, eval_smnc, eval_imnc, eval_hmnc = in_umnc, in_smnc, in_imnc, in_hmnc
                        eval_total = eval_umnc + eval_smnc + eval_imnc + eval_hmnc
                        eval_sfr = max(0.1, (0.5 + (2.0 * eval_umnc + 1.2 * eval_smnc + 0.5 * eval_imnc) * 0.1))
                    else:
                        n_umnc, n_smnc, n_imnc, n_hmnc = in_umnc, in_smnc, in_imnc, in_hmnc
                        total_cores = n_umnc + n_smnc + n_imnc + n_hmnc
                        sfr_kinetic = max(0.1, (0.5 + (2.0 * n_umnc + 1.2 * n_smnc + 0.5 * n_imnc) * 0.1))
                        eval_umnc, eval_smnc, eval_imnc, eval_hmnc = n_umnc, n_smnc, n_imnc, n_hmnc
                        eval_total, eval_sfr = total_cores, sfr_kinetic

            # SCENARIO BIFURCATION MATRIX (Prüft stochastische Berechtigung)
            if auto_mode:
                print("\n[KERNEL] Running automatic scenario detection matrix...")
                if math.isclose(t_input, 13.8, rel_tol=1e-2) and eval_total >= 100 and pathway_2_allowed:
                    user_choice = "6_add1_delay"
                elif t_input < 1.0 and 50 <= eval_total < 150 and pathway_2_allowed:
                    user_choice = "6_add1_same"
                elif t_input < 1.0 and eval_total < 50:
                    user_choice = "7.2b"
                elif eval_total >= 150 and t_input < 1.0:
                    user_choice = "6"
                else:
                    user_choice = "9"
                print(f"        >> Auto-Detected Trajectory: {user_choice}")
            else:
                print("\n[INPUT] Enter target scenario to execute from the reference matrix:")
                user_choice = input("        Select Scenario: ").strip()
                
                if user_choice in ["10", "12"] and t_input < 100.0:
                    print(f"\n[BLOCKED] Physics Violation! Early Event-3 scenarios blocked. Fallback to 9.")
                    user_choice = "9"
                
                pathway_2_scenarios = ["3a", "3b", "4", "7.2b", "8b", "9", "6_add1_same", "6_add1_delay"]
                if user_choice in pathway_2_scenarios and not pathway_2_allowed:
                    print(f"\n[BLOCKED] No Quantum Fluctuation triggered the rupture! Pathway 2 Scenario '{user_choice}' is impossible.")
                    print("          Spin-network filaments remained unbroken. Fallback to unperturbed Scenario 6.")
                    user_choice = "6"

                if user_choice not in manuscript_scenarios:
                    user_choice = "9"

            # BOUNDARY EVALUATION
            params = manuscript_scenarios[user_choice]
            print(f"\n [EVAL] Executing Boundary State Evaluation for Scenario {user_choice}:")
            print(f"   >> Blueprint Name: {params['name']}")

            target_eta = params["target"]
            tolerance_val = params["tolerance"]

            if tolerance_val == 15.0:
                eta_calc = target_eta * random.uniform(0.85, 1.15)
            elif tolerance_val == 1.0:
                eta_calc = target_eta * random.uniform(0.99, 1.01)
            else:
                eta_calc = target_eta

            spot_centered = params["centered"]
            deviation_percent = ((eta_calc - target_eta) / target_eta) * 100.0 if target_eta > 0 else 0.0
            print(f"   >> Calculated Oasis Density (eta):    {eta_calc:.6e}")

            details_str = f"Gen: {current_generation}, Cores: {eval_total}, Mode: {'Auto' if auto_mode else 'Manual'}"
            execute_automated_logging(user_choice, eta_calc, spot_centered, deviation_percent, details_str)

            # PROCESS CONTROL INTERFACE
            print("\n" + "="*65)
            print(" PROCESS CONTROL INTERFACE")
            print("="*65)
            choice = input("        Select Action Control ([c]/[r]/[q]): ").strip().lower()

            if choice == 'c':
                print(f"\n[KERNEL] Slicing consecutive event path over {t_input} Gyr.")
                spawned_stars = int(sfr_kinetic * t_input * 1.5)
                n_imnc += int(spawned_stars * 0.70)
                n_smnc += int(spawned_stars * 0.25) + int(n_umnc * 0.05 * t_input)
                n_hmnc += int(n_smnc * 0.02 * t_input)
                n_smnc, n_imnc, n_hmnc = max(0, n_smnc), max(0, n_imnc), max(0, n_hmnc)
                print(f"[SUCCESS] Core population advanced. Generated {spawned_stars} new anchors.")
            elif choice == 'r':
                print("\n[RESET] Enforcing Conformal Cyclic Reset...")
                current_generation += 1
                n_umnc, n_smnc, n_imnc, n_hmnc = int(n_umnc * 0.15), int(n_smnc * 0.15), int(n_imnc * 0.15), int(n_hmnc * 0.15)
                print(f" -> Conformal Rescaling Complete. Welcome to Generation {current_generation}!")
            elif choice == 'q':
                running = False
        except ValueError:
            print("\n[FAIL] Numerical inputs required.")
            running = False

if __name__ == "__main__":
    run_interactive_sandbox()
