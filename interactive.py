#!/usr/bin/env python3
import math
import time
import sys
import numpy as np
from numba import njit

@njit
def run_jit_evolution(micro_cycles, is_big_bang_focus, flux_efficiency, agg_bubble_rate, t_genesis, is_infinity_run, n_imnc, n_smnc, n_umnc, n_hmnc, micro_window_years, time_step_micro, time_step_standard):
    actual_time_elapsed = 0.0
    # FIX: Start strictly from 0 for the current aeon calculation horizon
    primordial_spacetimes = np.int64(0)

    # Absolute upper bound for child universe seeding (Mass-Exclusivity Law)
    max_possible_universes = n_imnc + n_smnc + n_umnc + n_hmnc
    resolution_sensitivity = 1.45 if is_big_bang_focus else 1.00

    # Expand maximum loop security limits if infinity mode is active
    loop_limit = 20000000 if is_infinity_run else micro_cycles
    total_gw_energy_leak = 0.0

    for cycle in range(loop_limit):
        if is_big_bang_focus and cycle < micro_window_years:
            time_per_cycle = time_step_micro
        else:
            # Exponential time dilation for deep-time and infinity runs
            # Accelerates aging on the CPU as the manifold expands
            if is_infinity_run:
                time_per_cycle = time_step_standard * (1.0 + (actual_time_elapsed * 0.05))
            else:
                time_per_cycle = time_step_standard 

        actual_time_elapsed += time_per_cycle
        if actual_time_elapsed >= t_genesis:
            break
        
            if num_collisions > 0:
                omega_oaza = 2.5
                print("\n" + "-"*50)
                print(" [ADDENDUM 1] CONSERVED TOPOLOGICAL TUNNEL DATA TRANSFER")
                print("-"*50)
                
                total_collision_energy = 0.0
                for t_coll, density_flag in collision_times:
                    is_dense = 'n' if density_flag != 'manual' else input(f"        >> Is Node at t={t_coll:.1f} Gyr a high-density zone? (Y/n): ").strip().lower()
                    
                    ancestral_density_contribution = math.tanh(backup_hmnc * 0.5 + backup_umnc * 0.2)
                    quantum_saturation_boost = 1.0 + (ancestral_density_contribution * 1.5)
                    
                    transfer_factor = 3.75 if (is_dense == 'y') else 2.50
                    total_collision_energy += transfer_factor * (quantum_saturation_boost if density_flag == 'auto' else 1.0)
                
                # Thermal barrier saturation according to Eq. 25
                omega_oaza_saturation = 1.0 + (1.5 * math.tanh(total_collision_energy / 10.0))
                star_formation_mod *= omega_oaza_saturation

        # === 1. MACRO-CORE KINETIC TRANSITIONS (DENSITY-COUPLED MERGER MATRIX) ===
        # OPTIMIZATION: Reduce modulus branching frequency for mobile CPUs to maximize pipelining
        step_gate = 20000 if micro_cycles > 5000000 else 2000
        if (cycle % step_gate == 0):
            # Dynamic background density proxy (dilutes as total objects and spacetime expand)
            total_active_mass = n_imnc + n_smnc + n_umnc + n_hmnc
            if total_active_mass > 0:
                # Merger efficiency is proportional to the relative concentration of the source pool
                if n_imnc > 10:
                    imnc_to_smnc = np.int64(n_imnc * 0.01 * flux_efficiency * (n_imnc / max(1.0, float(total_active_mass))))
                    if imnc_to_smnc > 0:
                        n_imnc -= imnc_to_smnc
                        n_smnc += imnc_to_smnc
                        
                if n_smnc > 5:
                    smnc_to_umnc = np.int64(n_smnc * 0.005 * flux_efficiency * (n_smnc / max(1.0, float(total_active_mass))))
                    if smnc_to_umnc > 0:
                        n_smnc -= smnc_to_umnc
                        n_umnc += smnc_to_umnc
                        
                if n_umnc > 2:
                    umnc_to_hmnc = np.int64(n_umnc * 0.001 * flux_efficiency * (n_umnc / max(1.0, float(total_active_mass))))
                    if umnc_to_hmnc > 0:
                        n_umnc -= umnc_to_hmnc
                        n_hmnc += umnc_to_hmnc

        # --- UPDATE 2: HAMILTONIAN CONSTRAINT LOCKOUT (EQ 21) ---
        # Cleaned from arbitrary minimum wrappers
        if primordial_spacetimes > 0:
            lqg_elastic_recoil = math.tanh(primordial_spacetimes * 0.01)
            decay_step = np.int64(n_imnc * (lqg_elastic_recoil * 0.05))
            if n_imnc > decay_step:
                n_imnc -= decay_step
            else:
                n_imnc = np.int64(0)

        # 2. Bubble Flux Probability & Seeding via Collective Surface Area Stress
        if n_imnc > 0 or n_smnc > 0 or n_umnc > 0 or n_hmnc > 0:
            pull_imnc = np.int64(n_imnc * 0.05) if n_imnc > 0 else np.int64(0)
            pull_smnc = np.int64(n_smnc * 0.08) if n_smnc > 0 else np.int64(0)
            pull_umnc = np.int64(n_umnc * 0.02) if n_umnc > 0 else np.int64(0)
            pull_hmnc = np.int64(n_hmnc * 0.01) if n_hmnc > 0 else np.int64(0)
            
            characteristic_mass_exposure = (pull_hmnc * 2500.0) + (pull_umnc * 625.0) + (pull_smnc * 100.0) + (pull_imnc * 0.25)
            
            kappa_parameter = 1.5
            dimensionless_spin_proxy = 0.985 * resolution_sensitivity
            spin_enhancement_S = 1.0 + kappa_parameter * (dimensionless_spin_proxy ** 2)
            
            # Base physical shear stress of the cluster network (independent of agg)
            f_shear_base = characteristic_mass_exposure * spin_enhancement_S
            
            # MODULATION RULE: agg_bubble_rate * 10 = deviation in % (Max +/- 10% impact)
            agg_percentage_modulation = 1.0 + ((agg_bubble_rate - 0.5) * 0.20)
            f_shear_eff = f_shear_base * agg_percentage_modulation
            
            # FIX: We smooth the network expansion area logarithmically to prevent numerical freeze-out
            # This allows early-epoch dense scaling while preventing deep-time expansion from killing all ruptures
            network_expansion_damping = 1.0 + math.log1p(actual_time_elapsed * 1e3)
            a_eff = 4.0 * math.pi * (dimensionless_spin_proxy ** 2) * network_expansion_damping
            
            sigma_qg = 1e5 / (4.0 * math.pi * math.sqrt(3.0))
            
            if (f_shear_eff / a_eff) > sigma_qg:
                generated_nodes = max(np.int64(1), np.int64(math.log1p(f_shear_eff) * 0.5 * agg_percentage_modulation))
                
                # REPAIR: Decouple from strict instantaneous core counters to allow deep-time expansion remnants
                max_allowed_nodes = n_imnc + n_smnc + (n_umnc * 5) + (n_hmnc * 25)
                if primordial_spacetimes + generated_nodes <= max_allowed_nodes:
                    primordial_spacetimes += generated_nodes
                    omega_zamo = (2.0 * f_shear_eff * dimensionless_spin_proxy) / (1.0 + characteristic_mass_exposure)
                    total_gw_energy_leak += omega_zamo * generated_nodes * 1e-4
                    
                    n_imnc = max(np.int64(0), n_imnc - pull_imnc)
                    n_smnc = max(np.int64(0), n_smnc - pull_smnc)
                    n_umnc = max(np.int64(0), n_umnc - pull_umnc)
                    
                    stolen_hmnc = min(n_hmnc, np.int64(generated_nodes * 0.1))
                    n_hmnc = max(np.int64(0), n_hmnc - stolen_hmnc)

        # === 3. PRECISION AUTOMATED HAWKING DECAY (CONTINUOUS FIELD TRANSITION) ===
        r_imnc = 1.0 / ((1.0 + n_imnc * 0.05) ** 3.0) if n_imnc > 0 else 0
        r_smnc = 1.0 / ((50.0 + n_smnc * 1.0) ** 3.0) if n_smnc > 0 else 0
        r_umnc = 1.0 / ((1e5 + n_umnc * 5.0) ** 3.0) if n_umnc > 0 else 0
        r_hmnc = 1.0 / ((1e9 + n_hmnc * 100.0) ** 3.0) if n_hmnc > 0 else 0
        
        n_imnc -= min(n_imnc, np.int64(n_imnc * (1.0 - math.exp(-r_imnc * time_per_cycle * 0.01))))
        n_smnc -= min(n_smnc, np.int64(n_smnc * (1.0 - math.exp(-r_smnc * time_per_cycle * 0.01))))
        n_umnc -= min(n_umnc, np.int64(n_umnc * (1.0 - math.exp(-r_umnc * time_per_cycle * 0.001))))
        n_hmnc -= min(n_hmnc, np.int64(n_hmnc * (1.0 - math.exp(-r_hmnc * time_per_cycle * 0.0001))))

        current_object_count = n_umnc + n_hmnc + n_smnc + n_imnc
        
        # INFINITY & DEEP-TIME OPTIMIZATION: Early termination upon vacuum stabilization
        # This prevents mobile CPUs from grinding through millions of dead iterations
        if current_object_count == 0:
            return actual_time_elapsed, primordial_spacetimes, n_imnc, n_smnc, n_umnc, n_hmnc, current_object_count, total_gw_energy_leak
            
        if is_infinity_run and actual_time_elapsed > 50.0 and current_object_count < 10:
            return actual_time_elapsed, primordial_spacetimes, n_imnc, n_smnc, n_umnc, n_hmnc, current_object_count, total_gw_energy_leak

    current_object_count = n_umnc + n_hmnc + n_smnc + n_imnc
    return actual_time_elapsed, primordial_spacetimes, n_imnc, n_smnc, n_umnc, n_hmnc, current_object_count, total_gw_energy_leak

def execute_automated_logging(log_id, density, is_smooth, anomaly_score, descriptor):
    try:
        with open("causal_matrix_output.txt", "a") as f:
            f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] ID: {log_id} | "
                    f"Density: {density:.6e} | Smooth: {is_smooth} | "
                    f"Anomaly: {anomaly_score:.2f} | Info: {descriptor}\n")
    except IOError:
        pass

def evaluate_cluster_stabelity(active_umnc, active_smnc, active_imnc, n_hmnc, total_pnc_pool):
    print("\n[MONITOR] Running Multi-Body Vector Analysis...")
    mass_weights = {"umnc": 50.0, "hmnc": 25.0, "smnc": 10.0, "imnc": 0.5, "pnc": 0.01}
    lorentz_gamma = 1.9015  
    
    f_inward = (active_umnc * mass_weights["umnc"]) + (n_hmnc * mass_weights["hmnc"]) + (active_smnc * mass_weights["smnc"] * lorentz_gamma) + (active_imnc * mass_weights["imnc"]) + (total_pnc_pool * mass_weights["pnc"])
    f_outward = (active_smnc * mass_weights["smnc"] * (lorentz_gamma - 1.0) * 0.45) + (active_imnc * mass_weights["imnc"] * 1.5) + (n_hmnc * mass_weights["hmnc"] * 0.25) + (active_umnc * mass_weights["umnc"] * 0.05)                           
    
    if f_inward == 0.0:
        return "Explosion" if f_outward > 0.0 else "Massless"
            
    r_stabel = f_outward / f_inward
    print(f" -> Inward Gravitational Pull Vector: {f_inward:.2f}")
    print(f" -> Outward Relativistic Escape Vector: {f_outward:.2f}")
    print(f" -> Computed Dynamic Balance Ratio (R_stabel): {r_stabel:.4f}")
    
    if r_stabel < 0.28:
        print(" -> [TRAJECTORY]: COLLAPSE (Central consolidation)")
        return "Collapse"
    elif r_stabel > 0.65:
        print(" -> [TRAJECTORY]: EXPLOSION (Void structures)")
        return "Explosion"
    else:
        print(" -> [TRAJECTORY]: STABLE EQUILIBRIUM (Oasis formed)")
        return "Stable"

def run_interactive_sandbox():
    # === CENTRAL TEMPORAL RESOLUTION CONFIGURATION HEADER ===
    time_step_micro = 1e-9          # 1 micro-cycle = 1 Year (in Gyr)
    time_step_standard = 1e-7       # 1 standard-cycle = 100 Years (in Gyr)
    default_micro_count = 50000     # Default detail window size

    print("=====================================================================")
    print("   ______   ______   .___  ___.  __    ______     ______    __  ")
    print(r"  /  ____| /  __  \  |   \/   | |  |  /  ____|   /  __  \  |  |")
    print(r" |  |     |  |  |  | |  \  /  | |  | |  |       |  |  |  | |  |")
    print(r" |  |     |  |  |  | |  |\/|  | |  | |  |       |  |  |  | |  |")
    print(" |  |____ |  `--'  | |  |  |  | |  | |  |____   |  `--'  | |  | ")
    print(r"  \______| \______/  |__|  |__| |__|  \______|   \______/  |__|")
    print("=====================================================================")
    print("        COSMIC PIRACY SIMULATION - STATE ENGINE v34.0 (ASCII MATRIX)")
    print("        Background-Independent Quantum-Geometric Graph Evaluator")
    print("=====================================================================\n")
    
    # --- QUANTUM GEOMETRIC SIMULATION RESOLUTION MATRIX ---
    print("=====================================================================")
    print(" [RESOLUTION INTERFACE]: Configure Temporal Slicing Matrix")
    print("=====================================================================")
    print("  - Standard Matrix  (1): Deep-time macro steps via configuration header.")
    print("  - big_bang Horizon (2): High-resolution annual micro-cycles for the")
    print("                          early radiation era (dynamically configured).")
    print("---------------------------------------------------------------------")
    res_choice = input(" >> Select Temporal Resolution Node (1/2): ").strip()
    
    # Interactive custom overrides for the temporal step configuration
    try:
        # Clarified communication regarding hardware-adaptive macro slicing
        ts_std_input = input(f"    >> Set standard macro-step size in Gyr (Base Default: 1e-07, auto-scaled for Deep-Time): ").strip()
        if ts_std_input: time_step_standard = float(ts_std_input)
    except ValueError:
        pass

    if res_choice == "2":
        res_profile = "big_bang_focus"
        try:
            ts_mic_input = input(f"    >> Set micro-step size in Gyr (Default: {time_step_micro}): ").strip()
            if ts_mic_input: time_step_micro = float(ts_mic_input)
            
            user_micro_input = input(f"    >> Enter micro-cycle count in Years (Default: {default_micro_count}): ").strip()
            if user_micro_input: default_micro_count = int(user_micro_input)
        except ValueError:
            pass
        print()
    else:
        res_profile = "standard_10y"
        print("   [SUCCESS] Standard Matrix locked. Slicing continuum into macro steps.\n")
    time.sleep(0.4)

    current_generation = 0
    n_umnc, n_hmnc, n_smnc, n_imnc = 0, 0, 0, 0
    backup_umnc, backup_hmnc, backup_smnc, backup_imnc = 0, 0, 0, 0
    
    # --- DYNAMIC QUANTUM-GEOMETRIC RAM ALLOCATION (REPLACES HARDCODING) ---
    # We dynamically calculate the baseline saturation values following Eq. (7) and (28)
    initial_t_baseline = 4.0
    conformal_saturation_init = math.tanh(initial_t_baseline / 15.0)
    
    # Strictly aligned with the mass inflation benchmarks of Aeon 0
    base_smnc_init = int(40000.0 * conformal_saturation_init)
    base_imnc_init = int(1600000.0 * conformal_saturation_init)

    parallel_timelines = {}
    for slot in range(1, 13):
        # Scale each layer dynamically using the macro-multiverse progression factor
        slot_scale_factor = 1.0 + (slot * 0.05)
        
        parallel_timelines[slot] = {
            "umnc": int(2 * slot_scale_factor), 
            "hmnc": 1, 
            "smnc": int(base_smnc_init * slot_scale_factor), 
            "imnc": int(base_imnc_init * slot_scale_factor),
            "generation": 0, 
            "age": initial_t_baseline,
            "scenario": "6 (Multi-Core Cluster Baseline Framework)",
            "scar_v1": False, 
            "collision_v2": False,
            "multiverse_counter": int(42 * slot),
            "is_empty_layer": False,
            "chiral_inverted": (slot % 2 == 0), # Automatically enforces CPT antimatter symmetry
            "sf_mod": 1.00
        }
        
    active_manifold_multiverse_counter = 0
    assigned_scenario = "4"
    star_formation_mod = 1.0
    genesis_reply_loop = True

    while genesis_reply_loop:
        scenario_1_drainage_active = False
        addendum_1_scar_active = False
        addendum_1_dynamic_collision = False
        calculated_delay_gyr = 0.0

        if current_generation == 0:
            print("\n=====================================================================")
            print(" [COSMIC INITIALIZATION]: Universe and antiuniverse created from nothing.")
            print("=====================================================================")
            print("[INPUT] Initialize at Scenario 0 (Primordial Core Formation)?")
            
            raw_reply = input("        Trigger Ur-Genesis Phase (Y/n): ").strip()
            genesis_reply = raw_reply.lower()
            
            if "primordial black holes don't exist" in genesis_reply or "no primordial black holes" in genesis_reply:
                print("\n >> Congratulations! You don't exist!\n")
                sys.exit(0)
                
            elif "loop quantum gravity is false" in genesis_reply or "no lqg" in genesis_reply:
                print("\n >> Congratulations! You don't exist!\n")
                sys.exit(0)
                
            elif "cpt symmetry is broken" in genesis_reply or "no cpt" in genesis_reply:
                print("\n >> Congratulations! You don't exist!\n")
                sys.exit(0)
                
            elif "conformal cyclic cosmology is wrong" in genesis_reply or "no ccc" in genesis_reply:
                print("\n >> Congratulations! You don't exist!\n")
                sys.exit(0)
                
            elif "center for chaos containment is fake" in genesis_reply or "no center for chaos containment" in genesis_reply:
                print("\n >> Too much chaos everywhere! We need - ")
                print("    ...........................")
                print("    ...........................")
                print("    ...........................")
                print("    Maximum entropy achieved. No life ever again.\n")
                sys.exit(0)
                
            elif "cosmic piracy is a myth" in genesis_reply or "no piracy" in genesis_reply:
                print("\n >> Congratulations! You don't exist!\n")
                sys.exit(0)
                
            elif "string theory is true" in genesis_reply or "<3 strings" in genesis_reply:
                print("\n >> Congratulations! You don't exist!\n")
                sys.exit(0)
                
            elif "donkeys are stupid!" in genesis_reply or "donkeys are stupid" in genesis_reply:
                print("\n >> Congratulations! You don't exist!\n")
                sys.exit(0)
                
            elif "impossible ghost particles forever!" in genesis_reply or "<3 little ghost!" in genesis_reply or "<3 little ghost" in genesis_reply or "impossible ghost particles forever" in genesis_reply:
                print("\n >> WOW! This is my absolute favourite particle!")
                print("    ...........................")
                print("    ...........................")
                print("    :( System collapsed\n")
                sys.exit(0)

            elif genesis_reply == "":
                print("\n >> Alternatively, you can enter a CHEAT CODE!")
                time.sleep(2.0)
                continue

            elif genesis_reply == "?":
                print("Explanation:")
                print("\n >> Here you decide, wheather any PNCs will be created in this aeon. They are very important for life's creation.")
                time.sleep(2.0)
                continue

            elif "what did just happen?" in genesis_reply:
                print("\n Further explanation:")
                print("\n >> With no mass (aka PNCs), there was nothing to experience time, so a conformal reset followed. You may create a universe, or you just mash 'n' or any other letter except 'y' because you are bored.")
                time.sleep(2.0)
                continue

            if genesis_reply != 'y' and genesis_reply != '':
                print("\n [NOTICE]: NO MASS SEEDED. Conformal scale lost to infinite dilation.")
                print("           Enforcing immediate Conformal Cyclic Reset due to scale-invariance...")
                time.sleep(0.4)
                continue

            print("\n[PHASE 0] AEON 0 - PRIMORDIAL SEEDING AND BOUNDARY GATES")
            print("---------------------------------------------------------------------")
        else:
            print("\n" + "="*65)
            print(f" [CONTINUUM] BOOTING CHILD SPACETIME MANIFOLD - GENERATION {current_generation}")
            print("="*65)
            print(f"    [INHERITED HORIZON] Active Scenario: Scenario {assigned_scenario}")
            print(f"    [INHERITED ENGINE ] Current Star Formation Modifier: {star_formation_mod:.3f}x")
            print(f"    [INHERITED MASSES ] Injected Anchors: HMNC={n_hmnc} | UMNC={n_umnc} | SMNC={n_smnc} | IMNC={n_imnc}")
            print("---------------------------------------------------------------------")
            time.sleep(0.4)

        # --- DYNAMIC INTERFACE MODE NODE (FOR COLLISION/DEVELOPMENTTRACKING) ---
        if current_generation > 0:
            print("[INPUT] Select Interface Development Mode for the Child Aeon:")
            print("        [auto]   - Automated physics-tracking for boundary events")
            print("        [dev]    - Development override window for anomaly tuning")
            print("        [manual] - Step-by-step custom parameter injection")
            dev_mode_choice = input(" >> Mode Selection (auto/dev/manual): ").strip().lower()
            if dev_mode_choice not in ['auto', 'dev', 'manual']:
                dev_mode_choice = 'auto'
            print(f"   [SUCCESS] Interface Mode locked: [{dev_mode_choice.upper()}] Mode active.\n")
        else:
            dev_mode_choice = 'manual' # Aeon 0 defaults to manual startup

        # Every universe asks for its free tools independently of the mode
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

            print(f"\n[INPUT] Configure Multi-Bubble Generation Flux for Aeon {current_generation}:")
            try:
                agg_bubble_rate = float(input("        >> Enter creation aggressiveness (0.01 - 0.99): "))
            except ValueError:
                agg_bubble_rate = 0.25


        # --- PATHWAY 2 CAUSAL LAYER INITIALIZATION (ZERO HARDCODED BASES) ---
        if current_generation == 0:
            star_formation_mod = 1.0 + (agg_bubble_rate * 0.5)
            conformal_saturation = math.tanh(t_genesis / 15.0)
            
            # Primordial Ur-Genesis: Only heavy rotating anchors exist at the boundary node
            n_hmnc = 1  
            n_umnc = int(6.0 * conformal_saturation * star_formation_mod) + 2
            
            # Light cores do NOT exist yet; they must nucleate stochastically from the fields
            n_smnc = 0
            n_imnc = 0
        else:
            print(f"          [STAR FORMATION ENGINE]: Active. Inherited Factor: {star_formation_mod:.3f}x")
            print(f"          [PATHWAY 2 CORES]: Successfully transported via topological rupture.")
            
            # NO BASE VALUES ALLOWED: Core numbers are EXACTLY the assets isolated via Pathway 2
            n_hmnc = active_hmnc
            n_umnc = active_umnc
            n_smnc = active_smnc
            n_imnc = active_imnc

        # Synchronize snapshots for temporal rollbacks (Option b)
        backup_umnc = n_umnc
        backup_hmnc = n_hmnc
        backup_smnc = n_smnc
        backup_imnc = n_imnc

        initial_object_count = n_umnc + n_hmnc + n_smnc + n_imnc
        primordial_spacetimes = 0
        
        time_step_standard = 1e-7
        time_step_micro = 1e-9

        if is_infinity_run:
            micro_cycles = 1000000 if res_profile == "big_bang_focus" else 200000
            micro_window_years = default_micro_count
        else:
            if res_profile == "big_bang_focus":
                micro_window_years = default_micro_count
                micro_duration_gyr = micro_window_years * time_step_micro
                if t_genesis <= micro_duration_gyr:
                    micro_cycles = int(t_genesis / time_step_micro)
                    micro_window_years = micro_cycles
                else:
                    remaining_time_gyr = t_genesis - micro_duration_gyr
                    # OPTIMIZATION: Adaptive step scaling for Deep-Time (>10 Gyr)
                    # Compresses billions of dead macro-steps on mobile CPUs
                    if t_genesis > 10.0:
                        # Fine-tuned adaptive step scaling to balance cycle density and CPU load
                        adaptive_ts_std = time_step_standard * (t_genesis / 25.0)
                        standard_cycles = int(remaining_time_gyr / adaptive_ts_std)
                        time_step_standard = adaptive_ts_std
                    else:
                        standard_cycles = int(remaining_time_gyr / time_step_standard)
                    micro_cycles = micro_window_years + standard_cycles
            else:
                micro_window_years = 0
                micro_cycles = max(100, int(t_genesis / time_step_standard))

        flux_efficiency = 1.0 / (1.0 + math.log1p(1.0 / agg_bubble_rate))
        
        # --- PHYSICAL COUPLING: Star Formation factor dampening (Prevents Billiards overflow) ---
        # REPARATUR: Kontinuierliche Dämpfung basierend auf der maximalen LQG-Netzwerkspannung
        if star_formation_mod > 2.5:
            star_formation_mod = 2.5 + math.log1p(star_formation_mod - 2.5)
            
        print(f"          [STAR FORMATION ENGINE]: Active. Modulator locked at: {star_formation_mod:.3f}x")
        # Explicit hardware-tracking notification for Numba JIT compilation
        print(f"          [PATHWAY 2 CORES]: Processing {micro_cycles} hardware-optimized matrix cycles via JIT...")
        
        is_focus_bool = (res_profile == "big_bang_focus")
        
        # EXACTLY ONE REPAIRED JIT INVOCATION PASSING INHERITED CORES AND ALL 13 ARGUMENTS
        actual_relic_time, JIT_spacetimes, n_imnc, n_smnc, n_umnc, n_hmnc, current_object_count, total_emitted_gw_shrapnel = run_jit_evolution(
            micro_cycles, is_focus_bool, flux_efficiency, agg_bubble_rate, t_genesis, is_infinity_run, 
            n_imnc, n_smnc, n_umnc, n_hmnc, micro_window_years, time_step_micro, time_step_standard
        )

        # REPARATUR: Reset standard time step to prevent scaling bleeding into core logic
        time_step_standard = 1e-7

        active_manifold_multiverse_counter = int(JIT_spacetimes)

        if current_object_count == 0:
            calculated_delay_gyr = float('inf')
            n_umnc, n_hmnc, n_smnc, n_imnc = 0, 0, 0, 0
        else:
            # Re-implementation of mass-dependent delay tracking (Addendum 1A)
            remaining_heavy_mass = (n_hmnc * 2500.0) + (n_umnc * 625.0)
            if remaining_heavy_mass > 0:
                # Delay scales logarithmically with the frozen heavy remnant overhead
                calculated_delay_gyr = math.log1p(remaining_heavy_mass) * 1.85
            else:
                calculated_delay_gyr = 0.0

        # --- DETERMINISTIC UI EXPLORER SYSTEM WITH COMPREHENSIVE REGISTRY ---
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
                is_antimatter = (slot % 2 == 0)
                data["chiral_inverted"] = is_antimatter
                
                slot_fraction = slot / max(1, active_manifold_multiverse_counter)
                data["age"] = t_genesis * slot_fraction

                scenario_index = (slot + current_generation) % len(all_available_scenarios)
                selected_manifest = all_available_scenarios[scenario_index]

                if "7.1" in selected_manifest:
                    s_hmnc, s_umnc, s_smnc, s_imnc = 0, 0, 0, 0
                    data["age"] = 0.0
                    slot_sf_mod = 1.00
                    selected_manifest = "7.1 (Sterile Collapse Instabelity Node)"
                else:
                    slot_sf_mod = 1.0 + (math.tanh(slot_fraction * 2.0) * 4.0) if (slot % 3 == 0) else 1.00
                    
                    r_smnc_base = 1.0 / ((50.0 + backup_smnc * 1.0) ** 3.0) if backup_smnc > 0 else 0
                    r_imnc_base = 1.0 / ((1.0 + backup_imnc * 0.05) ** 3.0) if backup_imnc > 0 else 0
                    
                    base_sample_smnc = int(backup_smnc * math.exp(-r_smnc_base * data["age"])) if backup_smnc > 0 else 25000
                    base_sample_imnc = int(backup_imnc * math.exp(-r_imnc_base * data["age"])) if backup_imnc > 0 else 450000

                    if "7.2b" in selected_manifest or "7.1" in selected_manifest:
                        s_hmnc = int(backup_hmnc * 0.5) if backup_hmnc > 0 else 1
                        s_umnc = int(backup_umnc * 0.5) if backup_umnc > 0 else 2
                    else:
                        s_hmnc = 1 if (slot % 4 == 0) else 0
                        s_umnc = 2 if (slot % 5 == 0) else 1

                    if slot_sf_mod > 1.0:
                        s_smnc = max(1000, int(base_sample_smnc / (slot_sf_mod * 0.95)))
                        s_imnc = max(5000, int(base_sample_imnc / (slot_sf_mod * 1.15)))
                    else:
                        s_smnc = base_sample_smnc
                        s_imnc = base_sample_imnc

                mod_tag = f" | SF_Mod={slot_sf_mod:.2f}x" if slot_sf_mod > 1.0 else " | SF_Mod=1.00x"
                data["scenario"] = f"{selected_manifest} [HMNC={s_hmnc} | UMNC={s_umnc} | SMNC={s_smnc} | IMNC={s_imnc}{mod_tag}]"
                data["generation"] = current_generation
                data["multiverse_counter"] = int(active_manifold_multiverse_counter)
                data["sf_mod"] = slot_sf_mod
                
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
                data["sf_mod"] = 1.00
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

        # --- IMMEDIATE VACUUM COMMAND TRIGGER (DETERMINISTIC MAIN SYNC) ---
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
                jump_choice = input("         Select Choice (j/r/b/q): ").strip().lower()
                
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
                            star_formation_mod = parallel_timelines[target_slot]["sf_mod"]
                            print(f" -> [SUCCESS] Crossover locked. Welcome to Timeline Slot {target_slot:02d}.\n")
                            vacuum_menu_active = False
                            break
                    except ValueError:
                        print(" [SECURITY] Invalid coordinate selection.")
                        
                elif jump_choice == 'r':
                    current_generation += 1
                    assigned_scenario = "12" if (current_generation % 2 == 0) else "10"
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
                            
                            micro_cycles = max(100, int(math.log1p(t_genesis) * 120.0))
                            print(f"          [RE-CALCULATING TIMELINE]: Processing {micro_cycles} cycles for {t_genesis:.4f} Gyr...")
                            
                            is_focus_bool = (res_profile == "big_bang_focus")
                            t_genesis_out, primordial_spacetimes, n_imnc, n_smnc, n_umnc, n_hmnc, current_object_count, total_emitted_gw_shrapnel = run_jit_evolution(
                                micro_cycles_b, is_focus_bool, flux_efficiency, agg_bubble_rate, t_genesis, is_infinity_run, 
                                n_imnc, n_smnc, n_umnc, n_hmnc, micro_window_years, time_step_micro, time_step_standard
                            )

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
            print("---------------------------------------------------------------------")
            # Dynamic input prompts that accept 'Enter' to evacuate maximum available cores
            try:
                print(f" -> Available HMNC: {n_hmnc}")
                in_hmnc = input(f"    >> Enter HMNC quantity to evacuate (Default: {n_hmnc}): ").strip()
                active_hmnc = int(in_hmnc) if in_hmnc else n_hmnc
                
                print(f" -> Available UMNC: {n_umnc}")
                in_umnc = input(f"    >> Enter UMNC quantity to evacuate (Default: {n_umnc}): ").strip()
                active_umnc = int(in_umnc) if in_umnc else n_umnc
                
                print(f" -> Available SMNC: {n_smnc}")
                in_smnc = input(f"    >> Enter SMNC quantity to evacuate (Default: {n_smnc}): ").strip()
                active_smnc = int(in_smnc) if in_smnc else n_smnc
                
                print(f" -> Available IMNC: {n_imnc}")
                in_imnc = input(f"    >> Enter IMNC quantity to evacuate (Default: {n_imnc}): ").strip()
                active_imnc = int(in_imnc) if in_imnc else n_imnc
                
                # Boundary verification check against cheating physics
                active_hmnc = max(0, min(n_hmnc, active_hmnc))
                active_umnc = max(0, min(n_umnc, active_umnc))
                active_smnc = max(0, min(n_smnc, active_smnc))
                active_imnc = max(0, min(n_imnc, active_imnc))
                
            except ValueError:
                print("   [SECURITY] Invalid input detected. Defaulting to safe maximum core evacuation.")
                active_umnc = n_umnc
                active_hmnc = n_hmnc
                active_smnc = n_smnc
                active_imnc = n_imnc

            print("\n" + "-"*50)
            print(" [SCENARIO 1] PRIMEVAL METRIC DRAINAGE INTERFACE")
            print("-"*50)
            if dev_mode_choice == 'auto':
                # Scenario 1 is determined purely by the physical trajectory criteria later
                scenario_1_drainage_active = False 
                print("        [AUTO-PHYSICS]: Automated horizon tracking active for Scenario 1.")
            else:
                drain_choice = input("        Trigger Scenario 1 Localized Metric Drainage? (y/N): ").strip().lower()
                scenario_1_drainage_active = True if drain_choice == 'y' else False

            print("\n" + "-"*50)
            print(" [ADDENDUM 1 - VERSION A] PRIMEVAL COSMOLOGICAL SCAR TRACK")
            print("-"*50)
            if dev_mode_choice == 'auto':
                # addendum 1 version a triggers autonomously if specific shear thresholds were breached
                if active_manifold_multiverse_counter > 100:
                    addendum_1_scar_active = True
                    print("        [AUTO-PHYSICS]: High directional anisotropy. addendum 1 version a ENGAGED.")
                else:
                    addendum_1_scar_active = False
                    print("        [AUTO-PHYSICS]: Low topological stress. addendum 1 version a INACTIVE.")
                time.sleep(0.4)
            else:
                scar_choice = input("        Engage addendum 1 version a Cosmological Scar tracking? (y/N): ").strip().lower()
                addendum_1_scar_active = True if scar_choice == 'y' else False

            # If addendum 1 version a is active, it imprints the directional shift onto the engine
            if addendum_1_scar_active:
                star_formation_mod *= 1.45

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
            
            print(f" -> Pathway 2 Isolation Efficiency: {pathway_2_isolation_efficiency * 100.0:.2f}% Cores Isolated.")
            print(f" -> Available Residual Growth Energy Density: {remaining_energy_density:.4f}")
            print(" -> Status: Geometric boundary identification active.")
            print(" -> Conformal footprint occurs IMMEDIATELY (0.00e+00 Gyr displacement Vector).")

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
                    except ValueError: 
                        num_collisions = 0
                else:
                    # --- DETERMINISTIC HEISENBERG QUANTUM SMEARING MATRIX (ADDENDUM 1B) ---
                    ancestral_mass_pool = backup_hmnc + backup_umnc + (backup_smnc * 0.1)
                    if ancestral_mass_pool > 0 or active_manifold_multiverse_counter > 0:
                        num_collisions = max(1, int(math.log1p(ancestral_mass_pool + active_manifold_multiverse_counter) * 3.5))
                        for i in range(num_collisions):
                            t_coll = 0.1 + (i * (min(t_genesis, 1000.0) / max(1, num_collisions)))
                            collision_times.append((t_coll, 'auto'))
                        print(f"        [QUANTUM-SMEARING] Overlapped {num_collisions} synchronized intersection nodes.")
            if num_collisions > 0:
                omega_oaza = 2.5
                print("\n" + "-"*50)
                print(" [ADDENDUM 1] CONSERVED TOPOLOGICAL TUNNEL DATA TRANSFER")
                print("-"*50)
                
                total_collision_energy = 0.0
                for t_coll, density_flag in collision_times:
                    is_dense = 'n' if density_flag != 'manual' else input(f"        >> Is Node at t={t_coll:.1f} Gyr a high-density zone? (Y/n): ").strip().lower()
                    
                    ancestral_density_contribution = math.tanh(backup_hmnc * 0.5 + backup_umnc * 0.2)
                    quantum_saturation_boost = 1.0 + (ancestral_density_contribution * 1.5)
                    
                    transfer_factor = 3.75 if (is_dense == 'y') else 2.50
                    total_collision_energy += transfer_factor * (quantum_saturation_boost if density_flag == 'auto' else 1.0)
                
                # Thermal barrier saturation according to Eq. 25
                omega_oaza_saturation = 1.0 + (1.5 * math.tanh(total_collision_energy / 10.0))
                star_formation_mod *= omega_oaza_saturation

        print("---------------------------------------------------------------------")
        print(f" -> Conformal Compression Factor (Omega_Oaza): {omega_oaza:.2f}")
        print(f" -> Dynamic Trans-Cosmic Delay Vector: {calculated_delay_gyr:.2e} Gyr")
        print(f" -> Final Computed Star Formation Frequency Modifier: {star_formation_mod:.3f}x")

        # Cluster stability and balance calculation check
        evaluate_cluster_stabelity(active_umnc, active_smnc, active_imnc, n_hmnc, primordial_spacetimes)

        # === COMPLETE MULTIVERSE SCENARIO MATRIX ENGINE (STRICT LATEX COUPLING) ===
        # Formally resolving every single branching pathway and sub-case from Section 3.
        
        # Fundamental Initial State Proxies
        is_massless_vacuum = (current_object_count == 0)
        is_solitary_core = (backup_hmnc == 1 and backup_umnc <= 8 and backup_smnc == 0)
        is_multi_core_cluster = (backup_umnc > 8 or backup_smnc > 0 or backup_hmnc > 1)
        
        # Temporal & Density Framework Mapping (Case 1 vs Case 2)
        is_case_1_high_density = (t_genesis < 1000.0) and not is_infinity_run
        is_case_2_inf_diluted = (is_infinity_run or t_genesis >= 1000.0)

        # Main Architectural Decision Tree
        if not is_massless_vacuum:
            if scenario_1_drainage_active:
                # Scenario 1: Primeval Topological Deflation Blueprints (Section 3.1)
                user_choice = "1"
                
            elif is_solitary_core:
                if not addendum_1_dynamic_collision:
                    # Solitary core architectures without shockwaves (Section 3.2 & 3.4)
                    if is_case_1_high_density:
                        user_choice = "2"    # Solitary Isotropic Accretion
                    else:
                        user_choice = "4"    # Decaying Parent Aeon Collapse
                else:
                    # Event 1 coupled with dynamic field transitions (Section 3.3 & 3.5)
                    if is_case_1_high_density:
                        # Bifurcation inside Scenario 3 based on Higgs activation (Section 3.3)
                        # High expansion pressure (Omega_Oaza) triggers conformal protection
                        user_choice = "3b" if (omega_oaza >= 2.0) else "3a"
                    else:
                        user_choice = "5"    # Active Pathway 3 Higgs Shockwave
                        
            elif is_multi_core_cluster:
                if not addendum_1_dynamic_collision:
                    # Event 2 cluster metrics without subsequent transitions (Section 3.6 & 3.7.1)
                    if pathway_2_isolation_efficiency < 0.95:
                        user_choice = "8.5"  # Stable Shadow Track Drainage
                    else:
                        user_choice = "6"    # Multi-Core Cluster Baseline Framework
                else:
                    # Event 2 cluster with active multi-collision fields (Section 3.7, 3.8 & 3.9)
                    if is_case_1_high_density:
                        # Scenario 7 branching modes governed by stabilization efficiency (Section 3.7)
                        if pathway_2_isolation_efficiency < 0.30:
                            user_choice = "7.1"   # Sterile Collapse Instability Node
                        else:
                            # Selection between Solitary Anchor Mode and Multi-Core Cluster Mode
                            user_choice = "7.2a" if (n_hmnc == 1 and n_umnc < 10) else "7.2b"
                    else:
                        # Scenario 8 and 9 branching under Case 2 (Section 3.8 & 3.9)
                        if is_case_2_inf_diluted and not is_infinity_run:
                            # Subcase 1 (Solitary Anchor) vs Subcase 2 (Multi-Core Slingshot)
                            user_choice = "8 (Subcase 1)" if (n_umnc < 5) else "8 (Subcase 2)"
                        else:
                            # Radiative Void Walls driven by strict geometric limits
                            user_choice = "9" if (agg_bubble_rate <= 0.05) else "7.2b"
        else:
            # Absolute masslessness configurations under Event 3 (Section 3.10, 3.11 & 3.12)
            # Scenario 11 is mathematically blocked as stated in Section 3.11
            if agg_bubble_rate >= 0.50:
                user_choice = "12"  # Pure geometric phase transition of empty space
            else:
                user_choice = "10"  # Standard CCC radiation-restart with coded asymmetry

        print(f"        >> Verified Trajectory Phase: Scenario {user_choice} (Tolerance: 0.0%)")
        assigned_scenario = user_choice

        print("\n[SUCCESS] Universal quantum-geometric fields processed stochastically.")
        print("          RAM Multi-Manifold Index updated via isolation-displacement filtering.")

        print("\n" + "-"*65)
        print(" [MULTIVERSE] TRANS-DIMENSIONAL COBWEB CROSSOVER")
        print("-"*65)
        
        # Generation 0 bypass auto-forces reset tracker down down into the lineage
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
            jump_choice = input("         Select Choice (j/r/b/q): ").strip().lower()

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
                    print("\n[CROSSOVER] Slicing coordinates... Re-locking quantum loops...")
                    time.sleep(0.3)
                    n_umnc = parallel_timelines[target_slot]["umnc"]
                    n_hmnc = parallel_timelines[target_slot]["hmnc"]
                    n_smnc = parallel_timelines[target_slot]["smnc"]
                    n_imnc = parallel_timelines[target_slot]["imnc"]
                    current_generation = parallel_timelines[target_slot]["generation"]
                    active_manifold_multiverse_counter = parallel_timelines[target_slot]["multiverse_counter"]
                    star_formation_mod = parallel_timelines[target_slot]["sf_mod"]
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
            # Threshold check: Significant mass delay breaks standard CCC scale-invariance
            if remaining_massive_cores > 0 and calculated_delay_gyr > 0.05:
                print(f"           [CRITICAL]: Massive remnants ({remaining_massive_cores} cores) remain unevaporated. Delay: {calculated_delay_gyr:.4f} Gyr.")
                print("                       Conformal invariance broken. Quenching Pathway 3 shockwave.")
                assigned_scenario = "3a" if isolated_hmnc > 0 else "4"
            else:
                assigned_scenario = "9" if (current_generation % 2 == 0) else "7.2b"
            print(f"           [STATUS]: Trajectory bound to configuration: Scenario {assigned_scenario}.")

            print(f"\n[RESET] Compressing and transferring rest-mass into Conformal Channel...")
            n_umnc = isolated_umnc
            n_hmnc = isolated_hmnc
            n_smnc = isolated_smnc
            n_imnc = isolated_imnc
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
                    
                    micro_cycles = max(100, int(math.log1p(t_genesis) * 120.0))
                    print(f"          [RE-CALCULATING TIMELINE]: Processing {micro_cycles} cycles for {t_genesis:.4f} Gyr...")
                    
                    is_focus_bool = (res_profile == "big_bang_focus")
                    t_genesis_out, primordial_spacetimes, n_imnc, n_smnc, n_umnc, n_hmnc, current_object_count, total_emitted_gw_shrapnel = run_jit_evolution(
                        micro_cycles_b, is_focus_bool, flux_efficiency, agg_bubble_rate, t_genesis, is_infinity_run, 
                        n_imnc, n_smnc, n_umnc, n_hmnc, micro_window_years, time_step_micro, time_step_standard
                            )

                    
                    current_object_count = n_umnc + n_hmnc + n_smnc + n_imnc
                    print(f" -> [SUCCESS] Timeline recalculated. Continuing with restored cores at {t_rollback:.4f} Gyr.\n")
                    continue
            except ValueError:
                print(" [SECURITY] Invalid bounce configuration input.")
        else:
            print("\n[EXIT] An entire multiverse was erased from existence. Are you happy with yourself? Goodbye.\n")
            sys.exit(0)

if __name__ == "__main__":
    run_interactive_sandbox()
