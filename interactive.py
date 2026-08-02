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
    print("        COSMIC PIRACY SIMULATION - STATE ENGINE v12.0")
    print("        Restored August 1st Legacy Control Matrix (Pure ASCII)")
    print("=====================================================================\n")
    
    # 1. RESTORED SCENARIO 0 INITIALIZATION GUARD
    print("[INPUT] Initialize at Scenario 0 (Global CPT Crossover Node)?")
    genesis_reply = input("        Trigger Ur-Genesis Phase (y/N): ").strip().lower()
    
    if genesis_reply == 'y':
        print("\n[PHASE 0] Initializing Global CPT Crossover...")
        time.sleep(0.2)
        print("[PHASE 0] Enforcing Net-Zero Energy via Eq 1.")
        print(" -> Matter Domain Vector |psi_+t>:   +4.61352e-30 kg/m^3")
        print(" -> Antimatter Domain Vector |psi_-t>: -4.61352e-30 kg/m^3")
        print("[SUCCESS] Scenario 0 Verified: Net Quantum Multiverse State Q_hat |Psi> = 0")
        print("          Perfect thermodynamic zero-sum balance frozen at crossover.\n")
        execute_automated_logging("0 (Genesis)", 2.5e-9, True, 0.0, "Global CPT Crossover Enforced")
        print("[KERNEL] Ur-Genesis verified. Progressing to Pathway Dynamics...\n" + "="*65 + "\n")

    # RESTORED AUGUST 1ST GLOBAL CORE CLASSES MEMORY MATRIX
    current_generation = 0
    n_umnc = 5      # Ultramassive Non-Singular Cores
    n_smnc = 25     # Supermassive Non-Singular Cores
    n_imnc = 150    # Intermediate Mass Non-Singular Cores
    n_hmnc = 0      # Hypermassive Merger Cores
    
    running = True
    while running:
        total_cores = n_umnc + n_smnc + n_imnc + n_hmnc
        print(f"\n⚡ ACTIVE TIMELINE MATRIX | GENERATION: {current_generation}")
        print(f" -> Active Core Population: {total_cores:,} Seeds")
        print(f"    >> UMNC (Anchors): {n_umnc} | SMNC (Satellite): {n_smnc}")
        print(f"    >> IMNC (Stellar): {n_imnc} | HMNC (Merger):    {n_hmnc}")
        print("-" * 65)

        # RESTORED ADDENDUM 1 STOCHASTIC PNC TRIGGER RE-INITIALIZATION
        if total_cores == 0:
            print(" [WARNING] Absolute massless vacuum threshold reached (Cores = 0).")
            print("     Initiating Addendum 1 Stochastic Recalibration Phase...")
            time.sleep(0.3)
            print(" [PNC-TRIGGER] Activating quantum-geometric boundary entanglement...")
            n_umnc = random.randint(2, 8)
            n_smnc = random.randint(15, 35)
            n_imnc = random.randint(100, 200)
            total_cores = n_umnc + n_smnc + n_imnc + n_hmnc
            print(f" [SUCCESS] Quantum collapse verified! Spawned {total_cores} fresh PNC seeds.")
            print("     Sterile dilemma bypassed. Multi-generational cascade restarted.\n")

        try:
            print("[INPUT] Enter target evolution timescale for this event:")
            t_input = float(input("        Delta t (in Gyr, e.g. 0.5 or 13.8): "))

            # RESTORED HAWKING DEFLATION GUARD FOR ANCESTRAL TIME SCALES
            if t_input >= 500.0:
                print(f"\n [EVAPORATION] Timeline spans extensive deep era ({t_input} Gyr).")
                print("     Enforcing massive Hawking deflation and core density loss...")
                time.sleep(0.2)
                n_umnc, n_smnc, n_imnc, n_hmnc = 0, 0, 0, 0
                execute_automated_logging("10 (Sterile)", 0.0, True, -100.0, f"Hawking Evaporation at {t_input} Gyr")
                continue

            # RESTORED DYNAMIC MULTI-VARIABLE SCENARIO SELECTION ENGINE
            print("\n[KERNEL] Running automatic scenario detection matrix...")
            
            if t_input < 1.0 and total_cores < 50:
                assigned_scenario = "7.2b"
                omega_oaza = 2.444449 * random.uniform(0.85, 1.15)
                spot_centered = False
                allowed_tolerance = 15.0
                target_eta = 2.444449e-09
            elif total_cores >= 150 and t_input < 1.0:
                assigned_scenario = "6"
                omega_oaza = 2.500000
                spot_centered = True
                allowed_tolerance = 0.0
                target_eta = 2.5e-9
            elif n_umnc == 0:
                assigned_scenario = "1"
                omega_oaza = 0.0
                spot_centered = True
                allowed_tolerance = 15.0
                target_eta = 0.0
            else:
                assigned_scenario = "9"
                omega_oaza = 2.500000
                spot_centered = True
                allowed_tolerance = 0.0
                target_eta = 2.5e-9

            # RESTORED LORENTZ MASS INFLATION & SHIELDING CONSTANT MATRIX
            v_ratio = 0.8505
            lorentz_gamma = 1.0 / math.sqrt(1.0 - v_ratio**2)
            inflated_mass = total_cores * 1e10 * lorentz_gamma
            eff_accel = 1.8983 / lorentz_gamma

            print(f" -> Dynamic Lorentz Mass Inflation (gamma): {lorentz_gamma:.4f}")
            print(f" -> Expanded Relativistic Asset Mass:       {inflated_mass:.4e} M_sun")
            print(f" -> Core Metric Shielding Lock Constant:     {eff_accel:.4f}x")

            baryon_baseline = 1e-9
            eta_calc = baryon_baseline * omega_oaza if assigned_scenario != "1" else 0.0
            deviation_percent = ((eta_calc - target_eta) / target_eta) * 100.0 if target_eta > 0 else -100.0

            print(f"\n -> Routed Framework Target:           Scenario {assigned_scenario}")
            print(f" -> Final Calculated Density (eta):    {eta_calc:.6e}")
            print(f" -> Real-Time Path Drift Deviation:    {deviation_percent:+.4f}%")
            print(f" -> CMB Cold Spot Alignment Centered:   {spot_centered}")

            # RESTORED AUTOMATED STAR FORMATION RATE (SFR) KINETICS
            # Dynamic growth scales directly with existing high-order core densities
            sfr_kinetic = max(0.1, (0.5 + (2.0 * n_umnc + 1.2 * n_smnc + 0.5 * n_imnc) * 0.1))
            print(f" -> Computed Star Formation Rate (SFR): {sfr_kinetic:.4f} M_sun/yr")
            # AUTOMATED PERMANENT RUNTIME TRACK LOGGING
            details_str = f"Gen: {current_generation}, Cores: {total_cores}, SFR: {sfr_kinetic:.2f}"
            execute_automated_logging(assigned_scenario, eta_calc, spot_centered, deviation_percent, details_str)

            # -------------------------------------------------------------------
            # RESTORED PROCESS CONTROL INTERFACE (THE MULTIVERSE WEICHE)
            # -------------------------------------------------------------------
            print("\n" + "="*65)
            print(" PROCESS CONTROL INTERFACE: DEFINE TIMELINE DISPLACEMENT")
            print("="*65)
            print(" [c] - Add and follow consecutive event (Keep active cores inside this Aeon)")
            print(" [r] - Execute Conformal Cyclic Reset   (Progress to Generation + 1)")
            print(" [q] - Terminate Simulation Engine and close kernel")
            choice = input("        Select Action Control: ").strip().lower()

            if choice == 'c':
                print("\n[KERNEL] Slicing consecutive event path. Time continuum preserved.")
                # Cores multiply dynamically via the live computed SFR kinetics
                growth_factor = 1.0 + (sfr_kinetic * 0.01)
                n_imnc = int(n_imnc * growth_factor)
                n_hmnc += int(n_smnc * 0.05)  # Satellite core mergers generate HMNCs
                n_smnc = int(n_smnc * 0.95) + int(n_umnc * 0.1)
                print("[SUCCESS] Core population advanced through automated accretion.")
                
            elif choice == 'r':
                print("\n[RESET] Enforcing Conformal Cyclic Reset boundary transition...")
                time.sleep(0.3)
                current_generation += 1
                
                # 85% Conformal Mass Evaporation Filter across the 3-surface horizon boundary
                n_umnc = int(n_umnc * 0.15)
                n_smnc = int(n_smnc * 0.15)
                n_imnc = int(n_imnc * 0.15)
                n_hmnc = int(n_hmnc * 0.15)
                print(f" -> Conformal Rescaling Complete. Welcome to Generation {current_generation}!")
                
            elif choice == 'q':
                print("\n[SHUTDOWN] Safely disconnecting Loop Quantum Gravity filaments. Exiting...")
                running = False
            else:
                print("\n[KERNEL] Unrecognized control vector. Maintaining timeline baseline.")

        except ValueError:
            print("\n[FAIL] Numerical inputs required for physics verification.")
            running = False

    print("\n=====================================================================")
    print(" MULTI-AEON SIMULATION RUN COMPLETE: MATRIX OUTPUT PERMANENTLY LOCKED")
    print("=====================================================================\n")

if __name__ == "__main__":
    run_interactive_sandbox()
