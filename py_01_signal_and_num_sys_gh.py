#!/usr/bin/env python3
"""
Chapter 1: Introduction to Signals and Number Systems
Demonstrates basic number system conversions and digital vs analog concepts
"""

def decimal_to_binary(n):
    """Convert decimal to binary"""
    if n == 0:
        return "0"
    binary = ""
    num = abs(int(n))
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    return binary

def binary_to_decimal(binary_str):
    """Convert binary string to decimal"""
    return int(binary_str, 2)

def simulate_digital_signal(duration=10):
    """Simulate a simple digital signal (square wave)"""
    import time
    print("\nSimulating Digital Signal (0V = 0, 5V = 1):")
    print("Time(s) | Voltage | Bit")
    print("-" * 30)
    
    for i in range(duration):
        bit = i % 2  # Alternating 0 and 1
        voltage = "5V" if bit else "0V"
        print(f"  {i}     |  {voltage}  |  {bit}")

def main():
    print("=" * 60)
    print("CHAPTER 1: Signals and Number Systems")
    print("=" * 60)
    
    # Example 1: Decimal to Binary conversion
    print("\n--- Example 1: Decimal to Binary Conversion ---")
    decimal_num = 45
    binary_result = decimal_to_binary(decimal_num)
    print(f"Decimal: {decimal_num}")
    print(f"Binary:  {binary_result}")
    print(f"Verification: {binary_to_decimal(binary_result)} (back to decimal)")
    
    # Example 2: Binary to Decimal conversion
    print("\n--- Example 2: Binary to Decimal Conversion ---")
    binary_num = "110101"
    decimal_result = binary_to_decimal(binary_num)
    print(f"Binary:  {binary_num}")
    print(f"Decimal: {decimal_result}")
    
    # Example 3: Digital Signal Simulation
    print("\n--- Example 3: Digital Signal Simulation ---")
    simulate_digital_signal(8)
    
    print("\n" + "=" * 60)
    print("Key Concepts:")
    print("- Digital signals have discrete values (0 or 1)")
    print("- Binary is base-2 representation")
    print("- 1 bit = one binary digit, 8 bits = 1 byte")
    print("=" * 60)

if __name__ == "__main__":
    main()
