#!/usr/bin/env python3
import time
import math

def launch_ultimate_multiverse():
    print("=====================================================================")
    print("      ______   ______        _______  __    __   _______   ______ ")
    print("     /  ____| /  __  \\      |   ____||  |  |  | |   ____| /  ____|")
    print("    |  |     |  |  |  |     |  |__   |  |  |  | |  |__   |  |     ")
    print("    |  |     |  |  |  |     |   __|  |  |  |  | |   __|  |  |     ")
    print("    |  |____ |  `--'  |     |  |     |  `--'  | |  |____ |  |____ ")
    print("     \\______| \\______/      |__|      \\______/  |_______| \\______|")
    print("=====================================================================")
    print("          COSMIC PIRACY MULTIVERSE STATE ENGINE - v7.0")
    print("          Strict Causal Path Tracking & Invariant Boundary Guards")
    print("=====================================================================\n")

    mode_input = input("-> Enable automated Scenario Recognition mode (0-12 & Addenda)? (y/n, Default=y): ")
    recognition_mode = False if mode_input.lower().strip() == 'n' else True

    try:
        max_aeons = input("\n-> Enter maximum number of iterations/aeons (Default=4): ")
        total_aeons = int(max_aeons) if max_aeons.strip() else 4
    except ValueError:
        total_aeons = 4

    # Zustandsvariablen zur Vererbung der physikalischen Kausalität
    current_aeon = 0
    aeon_generation_number = 0
    observed_mass_baseline = 5000000
    
    pathway_2_triggered_in_previous = False
    pre_existing_cores_count = 0
    cold_spot_active_from_previous = False
    inherited_baryon_excess = False

    while current_aeon < total_aeons:
        print("\n" + "="*75)
        print(f"ITERATION {current_aeon} (GEN-ID: {aeon_generation_number}) - CAUSAL MATRIX ACTIVE")
        print("="*75)
        
        # 1. ERZWUNGENE SPEZIALABFRAGE FÜR COLD SPOT NACH SCENARIO 1
        if cold_spot_active_from_previous:
            print("\n⏳ [GRAVITATIONAL LOCK] Reverse Metric Drainage active from previous Scenario 1.")
            print("   You must configure the delayed finite timeline displacement parameter")
            print("   to stabilize the mother's suspended conformal boundary before proceeding.")
            while True:
                drainage_input = input("   -> Enter finite stabilization displacement (in Gyr, e.g., 13.8): ")
                try:
                    drainage_val = float(drainage_input)
                    if drainage_val <= 0:
                        print("      [ERROR] Value must be positive to overcome gravitational lock. Try again.")
                        continue
                    print(f"   [SUCCESS] Boundary stabilized at +{drainage_val} Gyr limit. Releasing lock.")
                    break
                except ValueError:
                    print("      [ERROR] Invalid numerical value. Try again.")
            cold_spot_active_from_previous = False

        # 2. ANZAHL DER SCHWARZEN LÖCHER (KERNE) FESTLEGEN ODER VERERBEN
        if pathway_2_triggered_in_previous:
            print(f"\n📦 [INHERITANCE] Pathway 2 was triggered in the preceding era.")
            print(f"   The number of non-singular cores is strictly pre-determined by ancestry.")
            num_black_holes = pre_existing_cores_count
            print(f"   [METRIC] Trapping locked at exactly {num_black_holes} core configurations.")
            pathway_2_triggered_in_previous = False
        elif inherited_baryon_excess:
            print("\n💥 [INHERITANCE] Massive matter excess from previous Scenario 12 Higgs decay!")
            print("   The primordial background is highly asymmetric. Seeding locked at 2 cores.")
            num_black_holes = 2
            inherited_baryon_excess = False
        elif current_aeon == 0:
            photon_input = input("-> Trigger early quantum-geometric Photon Collapse in Aeon 0? (y/n, Default=y): ")
            photon_collapse = False if photon_input.lower().strip() == 'n' else True
            num_black_holes = 2 if photon_collapse else 0
            if not photon_collapse:
                print("[NOTICE] Pure massless radiation background established for Aeon 0.")
        else:
            try:
                bh_input = input(f"-> Enter number of non-singular core configurations (Black Holes) for this Aeon (Default=2): ")
                num_black_holes = int(bh_input) if bh_input.strip() else 2
            except ValueError:
                num_black_holes = 2

        # 3. ZEITWERT-EINGABE MIT STRENGER VALIDIERUNG GEGEN UNMÖGLICHE SZENARIEN
        while True:
            displacement_input = input(f"-> Enter Timeline Displacement / event value for Aeon {current_aeon} (e.g., 13.8, infinity, 0.002): ")
            if not displacement_input.strip():
                displacement_input = "13.8"
                
            is_infinity = displacement_input.lower() == "infinity"
            try:
                numeric_value = float(displacement_input)
                is_low_value = numeric_value < 1.0 if not is_infinity else False
            except ValueError:
                is_low_value = False
                numeric_value = None

            # UNMÖGLICHE SZENARIEN SOFORT ABLEHNEN
            if num_black_holes == 0 and is_low_value and current_aeon > 0:
                print(f"\n[REJECTION] Impossible combination: A micro-delay rupture threshold (< 1.0 Gyr)")
                print("            requires localized core anomalies to generate conformal shear force.")
                print("            Command rejected. Try again with a value fitting description.\n")
                continue
                
            if num_black_holes == 0 and not is_infinity and current_aeon == 0 and not is_low_value:
                print(f"\n[REJECTION] Impossible combination: A massless background without a Photon Collapse")
                print("            cannot sustain an expanding, mass-bearing timeline without collapsing sterile.")
                print("            Command rejected. Try again with 'infinity' or a micro-delay threshold.\n")
                continue

            break

        # 4. KOEXISTIERENDE PARALLELE UNIVERSEN (ADDENDUM 1) ABFRAGEN
        is_inter_bubble = False
        if num_black_holes > 0 or current_aeon > 0:
            bubble_input = input("-> Does a parallel sibling bubble universe co-exist within this generation? (y/n, Default=n): ")
            is_inter_bubble = True if bubble_input.lower().strip() == 'y' else False
        print("\n" + "="*75)
        print(f"ITERATION {current_aeon} (GEN-ID: {aeon_generation_number}) - CAUSAL MATRIX ACTIVE")
        print("="*75)
        
        # 1. ERZWUNGENE SPEZIALABFRAGE FÜR COLD SPOT NACH SCENARIO 1
        if cold_spot_active_from_previous:
            print("\n⏳ [GRAVITATIONAL LOCK] Reverse Metric Drainage active from previous Scenario 1.")
            print("   You must configure the delayed finite timeline displacement parameter")
            print("   to stabilize the mother's suspended conformal boundary before proceeding.")
            while True:
                drainage_input = input("   -> Enter finite stabilization displacement (in Gyr, e.g., 13.8): ")
                try:
                    drainage_val = float(drainage_input)
                    if drainage_val <= 0:
                        print("      [ERROR] Value must be positive to overcome gravitational lock. Try again.")
                        continue
                    print(f"   [SUCCESS] Boundary stabilized at +{drainage_val} Gyr limit. Releasing lock.")
                    break
                except ValueError:
                    print("      [ERROR] Invalid numerical value. Try again.")
            cold_spot_active_from_previous = False

        # 2. ANZAHL DER SCHWARZEN LÖCHER (KERNE) FESTLEGEN ODER VERERBEN
        if pathway_2_triggered_in_previous:
            print(f"\n📦 [INHERITANCE] Pathway 2 was triggered in the preceding era.")
            print(f"   The number of non-singular cores is strictly pre-determined by ancestry.")
            num_black_holes = pre_existing_cores_count
            print(f"   [METRIC] Trapping locked at exactly {num_black_holes} core configurations.")
            pathway_2_triggered_in_previous = False
        elif inherited_baryon_excess:
            print("\n💥 [INHERITANCE] Massive matter excess from previous Scenario 12 Higgs decay!")
            print("   The primordial background is highly asymmetric. Seeding locked at 2 cores.")
            num_black_holes = 2
            inherited_baryon_excess = False
        elif current_aeon == 0:
            photon_input = input("-> Trigger early quantum-geometric Photon Collapse in Aeon 0? (y/n, Default=y): ")
            photon_collapse = False if photon_input.lower().strip() == 'n' else True
            num_black_holes = 2 if photon_collapse else 0
            if not photon_collapse:
                print("[NOTICE] Pure massless radiation background established for Aeon 0.")
        else:
            try:
                bh_input = input(f"-> Enter number of non-singular core configurations (Black Holes) for this Aeon (Default=2): ")
                num_black_holes = int(bh_input) if bh_input.strip() else 2
            except ValueError:
                num_black_holes = 2

        # 3. ZEITWERT-EINGABE MIT STRENGER VALIDIERUNG GEGEN UNMÖGLICHE SZENARIEN
        while True:
            displacement_input = input(f"-> Enter Timeline Displacement / event value for Aeon {current_aeon} (e.g., 13.8, infinity, 0.002): ")
            if not displacement_input.strip():
                displacement_input = "13.8"
                
            is_infinity = displacement_input.lower() == "infinity"
            try:
                numeric_value = float(displacement_input)
                is_low_value = numeric_value < 1.0 if not is_infinity else False
            except ValueError:
                is_low_value = False
                numeric_value = None

            # UNMÖGLICHE SZENARIEN SOFORT ABLEHNEN
            if num_black_holes == 0 and is_low_value and current_aeon > 0:
                print(f"\n[REJECTION] Impossible combination: A micro-delay rupture threshold (< 1.0 Gyr)")
                print("            requires localized core anomalies to generate conformal shear force.")
                print("            Command rejected. Try again with a value fitting description.\n")
                continue
                
            if num_black_holes == 0 and not is_infinity and current_aeon == 0 and not is_low_value:
                print(f"\n[REJECTION] Impossible combination: A massless background without a Photon Collapse")
                print("            cannot sustain an expanding, mass-bearing timeline without collapsing sterile.")
                print("            Command rejected. Try again with 'infinity' or a micro-delay threshold.\n")
                continue

            break

        # 4. KOEXISTIERENDE PARALLELE UNIVERSEN (ADDENDUM 1) ABFRAGEN
        is_inter_bubble = False
        if num_black_holes > 0 or current_aeon > 0:
            bubble_input = input("-> Does a parallel sibling bubble universe co-exist within this generation? (y/n, Default=n): ")
            is_inter_bubble = True if bubble_input.lower().strip() == 'y' else False
