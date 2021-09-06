import os
import sys
import random


def main():
    s11, s12, s13, s14, s15, s16 = input("Enter your numbers: ").split(",")
    s11 = int(s11)
    s12 = int(s12)
    s13 = int(s13)
    s14 = int(s14)
    s15 = int(s15)
    s16 = int(s16)
    s21, s22, s23, s24, s25, s26 = input("Enter your numbers: ").split(",")
    s21 = int(s21)
    s22 = int(s22)
    s23 = int(s23)
    s24 = int(s24)
    s25 = int(s25)
    s26 = int(s26)
    s31, s32, s33, s34, s35, s36 = input("Enter your numbers: ").split(",")
    s31 = int(s31)
    s32 = int(s32)
    s33 = int(s33)
    s34 = int(s34)
    s35 = int(s35)
    s36 = int(s36)
    s41, s42, s43, s44, s45, s46 = input("Enter your numbers: ").split(",")
    s41 = int(s41)
    s42 = int(s42)
    s43 = int(s43)
    s44 = int(s44)
    s45 = int(s45)
    s46 = int(s46)
    s51, s52, s53, s54, s55, s56 = input("Enter your numbers: ").split(",")
    s51 = int(s51)
    s52 = int(s52)
    s53 = int(s53)
    s54 = int(s54)
    s55 = int(s55)
    s56 = int(s56)
    s61, s62, s63, s64, s65, s66 = input("Enter your numbers: ").split(",")
    s61 = int(s61)
    s62 = int(s62)
    s63 = int(s63)
    s64 = int(s64)
    s65 = int(s65)
    s66 = int(s66)
    s71, s72, s73, s74, s75, s76 = input("Enter your numbers: ").split(",")
    s71 = int(s71)
    s72 = int(s72)
    s73 = int(s73)
    s74 = int(s74)
    s75 = int(s75)
    s76 = int(s76)
    winning_numbers = set(random.choices(range(1, 59), k=6))
    t1 = [s11, s12, s13, s14, s15, s16]
    t2 = [s21, s22, s23, s24, s25, s26]
    t3 = [s31, s32, s33, s34, s35, s36]
    t4 = [s41, s42, s43, s44, s45, s46]
    t5 = [s51, s52, s53, s54, s55, s56]
    t6 = [s61, s62, s63, s64, s65, s66]
    t7 = [s71, s72, s73, s74, s75, s76]
    f1 = set(t1)
    f2 = f1.intersection(winning_numbers)
    print(f2)
    g1 = set(t2)
    g2 = g1.intersection(winning_numbers)
    print(g2)
    h1 = set(t3)
    h2 = h1.intersection(winning_numbers)
    print(h2)
    i1 = set(t4)
    i2 = i1.intersection(winning_numbers)
    print(i2)
    j1 = set(t5)
    j2 = j1.intersection(winning_numbers)
    print(j2)
    k1 = set(t6)
    k2 = k1.intersection(winning_numbers)
    print(k2)
    l1 = set(t7)
    l2 = l1.intersection(winning_numbers)
    print(l2)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())

